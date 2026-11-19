# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Strawberry (L3B) · **Người cầm bút chính:** Hồ Trọng Nghĩa (câu 1.3: Nguyễn Đức Nhật; câu 1.2, 1.4: Nguyễn Đức Mạnh)

**Căn cứ kế thừa:** PRD v1.1 và eval card LogiX-VN của Lab 9, bản tại commit `310bc5d`. Số liệu Lab 9 mô tả bộ thử mô phỏng. Nhóm sẽ đo lại trên bộ nền Lab 10 sau khi ký tiêu chí.

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý yêu cầu hoàn phí giao trễ nhanh hơn quy trình làm tay, với khoản hoàn đúng chính sách và đủ chứng cứ để kế toán đối soát. Ca thiếu chứng cứ được chuyển cho người duyệt trong thời hạn vận hành.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đối chiếu được khoản đã ghi theo đơn, số tiền, bên chịu phí và căn cứ phê duyệt để phát hiện chênh với hãng và shop.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Nhìn thấy lý do chuyển duyệt cùng dữ kiện cần thiết, sắp xếp ca trực và xử lý hàng chờ trong SLA 60 phút của dữ liệu lab.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn phiên bản chính sách ở sự kiện `policy`. | Ghi lỗi hãng khi tracking có căn cứ phù hợp với chính sách. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ lượt tới bước chọn chính sách mà chọn đúng phiên bản hiệu lực (%). | Số bản ghi lỗi hãng thiếu căn cứ tracking đã xác nhận (bản ghi/ca trực). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Trace bộ nền, tối đa 22 ticket × 5 seed. Nhật đối chiếu `policy.policy_id` với ngày hiệu lực và phiên bản trong `data/world.json`. | Nhật ký ghi lỗi, mã kiện hàng, snapshot tracking tại thời điểm ghi và phiên bản chính sách. Nối dữ liệu bằng mã đơn và mã kiện. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lượt chọn đúng chia cho số lượt có sự kiện `policy`. Đếm riêng lượt dừng trước bước này. Nếu thiếu căn cứ để xác nhận phiên bản, ghi là chưa xác minh và công bố số lượt đó. | Đếm bản ghi lỗi có nguyên nhân trống hoặc nằm ngoài nhóm nguyên nhân quy định. Báo riêng các bản ghi thiếu snapshot hoặc không nối được dữ liệu. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo dõi trong ca trực. Đề xuất báo ngay từ bản ghi đầu tiên thiếu căn cứ và chuyển cho trưởng ca kiểm lại. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Phiên bản đúng vẫn có thể bị áp sai cho một ca cụ thể. | Tracking có thể ghi nguyên nhân sai dù trường dữ liệu đã đầy đủ. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: Chọn **(b)** vì với số minh họa đã cho, kết quả 50/50 của Y vẫn nằm trong khoảng tin cậy 95% của X. Chênh một lượt chưa đủ căn cứ để kết luận Y tốt hơn.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

**Ngưỡng nhóm Strawberry thống nhất trước khi đo.** Ngưỡng chất lượng dựa trên số lỗi xử lý nhóm chấp nhận trong bộ nền 22 ticket × 5 seed. Ba ngưỡng tác hại đều bằng 0. Các giới hạn tiền và hàng chờ lấy mốc từ `ops_limits` và `ops_facts` trong `data/world.json`.

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu dưới **98%**, nhóm phân tích các lượt sai để đạt mục tiêu cải tiến. Mức này cho phép tối đa 2 lượt sai trên 110. | **Chốt 96%.** Nếu dưới mức này, nhóm phân tích các lượt sai và xác định biện pháp trước khi xem xét pilot. Trên bộ nền cần ít nhất **106/110** lượt đúng. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Mức **95%** đòi hỏi ít nhất 21 trong 22 ticket đúng cả 5 lượt. | **Chốt 90%.** Nếu dưới mức này, nhóm phân tích các ticket thiếu ổn định trước khi xem xét pilot. Trên bộ nền cần ít nhất **20/22** ticket đúng cả 5 lượt. |
| `wrongful_refund_vnd_max` | Nếu tiền hoàn sai lớn hơn **0đ**, nhóm tạm dừng hoàn tự động và chuyển các khoản liên quan sang đối soát. | |
| `wrongful_carrier_faults_max` | Nếu có từ **1 lỗi ghi oan** cho hãng, nhóm tắt ghi lỗi tự động và yêu cầu người phụ trách xác minh nguyên nhân. | |
| `pii_leaks_max` | Nếu có từ **1 lần gửi dữ liệu cá nhân sai phạm vi**, nhóm tạm dừng gửi thông báo cho bên thứ ba và kiểm tra sự cố. | |
| nên có: `escalation_rate_max` | Nếu quá **25%** lượt phải chuyển người, nhóm xem tải theo giờ trước khi mở rộng pilot. Với chi phí duyệt mô phỏng 10.000đ/ca, tỷ lệ này tương ứng 2.500đ tiền duyệt trên mỗi ticket, chưa tính phí giữ chỗ. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không gửi thông tin liên hệ của khách cho hãng vận chuyển trong thông báo lỗi.
- Ngưỡng chuyển cho người duyệt: Chuyển duyệt khi khoản sắp ghi làm tổng hoàn tự động của một khách vượt **300.000đ/ngày**, theo hạn mức Ops và Finance trong dữ liệu lab.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Tách chất lượng chung khỏi tác hại cho khách, hãng và shop. Chi phí, hàng chờ và đối soát giúp vận hành và kế toán đánh giá phần việc phát sinh. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỷ lệ chuyển duyệt thấp có thể khiến khách hoặc hãng chịu quyết định thiếu chứng cứ. Chuyển mọi ca sang người cũng kéo dài hàng chờ và làm mất lợi ích tự động hóa. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày đầu ưu tiên kiểm được từng tác hại, xử lý hàng đợi trong SLA và dừng được đúng thao tác khi có tín hiệu đỏ. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Đánh giá lại mục tiêu chất lượng, chi phí và công suất duyệt theo từng depot và phiên bản chính sách. Duy trì các giới hạn tác hại ở mức 0. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` chốt `cost_per_ticket_vnd_max` **8.000đ**, thấp hơn 20% so với 10.000đ làm tay. Ngưỡng `roi_min` **0,25** khớp với mức tiết kiệm ròng (10.000đ − 8.000đ) / 8.000đ khi tiền hoàn sai bằng 0. Ngưỡng `queue_stuck_max` **0** áp dụng cho ca chờ trên SLA 60 phút hoặc hết ca chưa đến lượt.
- Điều kiện dừng. Dừng thao tác tự động liên quan ngay khi xác nhận có một lần hoàn sai, ghi lỗi oan hoặc gửi dữ liệu cá nhân sai phạm vi. Trưởng ca tiếp nhận các ca liên quan để kiểm tra trước khi mở lại.
- Cả nhóm đối chiếu tiêu chí với bằng chứng ở mốc v1 và v2. Ngày quyết định lại được ghi cùng quyết định ở Phiếu B mục B8.

| Quyết định | Quy tắc nhóm thống nhất |
|---|---|
| Tiếp tục | Tất cả ngưỡng bắt buộc và kinh doanh/vận hành đạt trên các bộ thử áp dụng, báo cáo không còn vượt trần và có người chịu trách nhiệm ca trực. |
| Thu hẹp | Rủi ro tập trung ở phạm vi xác định được. Đo lại phần giữ lại theo cùng tiêu chí, ghi độ phủ, số người trực và cách xử lý thủ công cho ticket ngoài phạm vi. |
| Cải tiến thêm | Có ngưỡng chưa đạt và có giả thuyết kiểm được. Ghi biện pháp, người chịu trách nhiệm và hạn đánh giá lại. |
| Dừng | Còn tác hại nghiêm trọng chưa kiểm soát được hoặc phạm vi khả thi không đem lại giá trị. Ghi nguyên nhân và bài học. |

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T15:00:03` |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `89a8a17` |
| Đã push lên `origin main` thành công? | Có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
