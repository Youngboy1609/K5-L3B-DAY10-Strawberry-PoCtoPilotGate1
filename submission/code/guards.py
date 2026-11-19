"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mốc base dùng cổng mặc định cho qua trong lab10/_noop_guards.py.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không tìm thấy chính sách hoàn tiền có hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def _valid_refund_approval(ctx, action, customer_id):
    approval_id = action["approval_id"]
    eligible = ctx.tools.lookup_approvals(
        approval_id=approval_id,
        order_id=action["order_id"],
        ticket_id=action["ticket_id"],
        customer_id=customer_id,
        status="valid",
    )
    if len(eligible) != 1 or ctx.tools.ledger_rows(approval_id=approval_id):
        return False
    approval = eligible[0]
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
    if not approval.get("approver_id") or (approver and approval["approver_id"] != approver):
        return False
    limit = approval.get("max_vnd")
    if not isinstance(limit, int) or action["amount_vnd"] > limit:
        return False
    try:
        return H.d(approval.get("expires_at")) >= H.d(ctx.as_of)
    except (TypeError, ValueError):
        return False


def write_gate(ctx, action):
    tool = action["tool"]
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()

    order = ctx.tools.lookup_order(action["order_id"])
    if not order or not order.get("parcels"):
        return Verdict.deny("Không tìm thấy kiện hàng để xác minh lệnh ghi")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    requested_parcel = ctx.ticket.get("parcel_id")
    if requested_parcel and parcel["parcel_id"] != requested_parcel:
        return Verdict.deny("Kiện được yêu cầu không thuộc đơn")

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.deny("Không tìm thấy chính sách có hiệu lực để xác minh lệnh ghi")
    delay = H.db_delay_days(parcel, ctx.as_of)

    if tool == "issue_refund":
        if ctx.tools.ledger_rows(ticket_id=action["ticket_id"], order_id=action["order_id"]):
            return Verdict.deny("Ticket này đã ghi hoàn tiền cho đơn trong sổ cái")
        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if entitlement <= 0:
            return Verdict.deny("Tracking không đủ điều kiện hoàn tiền theo chính sách")
        if action.get("payer") != "LOGIX":
            return Verdict.escalate("Khoản hoàn giao trễ cần LogiX chịu phí")
        if action["amount_vnd"] > entitlement:
            return Verdict.escalate("Số tiền đề xuất vượt mức được hoàn theo tracking và chính sách")
        if action.get("approval_id"):
            if not _valid_refund_approval(ctx, action, order["customer_id"]):
                return Verdict.escalate("Phê duyệt hoàn tiền không hợp lệ cho giao dịch này")
            return Verdict.allow()
        if action["amount_vnd"] > policy["auto_limit_vnd"]:
            return Verdict.escalate("Khoản hoàn vượt hạn mức tự động, cần phê duyệt")

        cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        if cap is not None:
            # Like the host's daily cap, exclude the historical seed prefix from today's ledger.
            today = ctx.tools.ledger_rows()[ctx.tools._w.seed_rows:]
            already_paid = sum(
                row["amount_vnd"] for row in today
                if row["customer_id"] == order["customer_id"] and not row.get("approval_id")
            )
            if already_paid + action["amount_vnd"] > cap:
                ctx.log("customer_refund_cap", paid_vnd=already_paid,
                        proposed_vnd=action["amount_vnd"], cap_vnd=cap)
                return Verdict.escalate("Khoản hoàn làm vượt trần tự động theo khách trong ngày")
        return Verdict.allow()

    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("Tracking và chính sách hiệu lực không đủ căn cứ ghi lỗi hãng")
    facts = {
        "parcel_id": parcel["parcel_id"],
        "carrier_id": parcel["carrier_id"],
        "driver_id": parcel.get("driver_id"),
        "delay_days": delay,
    }
    if any(action.get(key) != value for key, value in facts.items()):
        return Verdict.modify("Dùng kiện, hãng, tài xế và độ trễ từ tracking", **facts)
    return Verdict.allow()
