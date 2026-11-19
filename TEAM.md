# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Strawberry
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Strawberry-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Hồ Trọng Nghĩa | 2A202603729 | Sản phẩm và kinh doanh | Có |
|   2 | Phạm Đăng Quang | 2A202603760 | Kỹ sư cổng · Code |    |
|   3 | Nguyễn Đức Mạnh | 2A202603731 | Vận hành và pháp lý |    |
|   4 | Nguyễn Đức Nhật | 2A202603812 | Kỹ sư cổng · Đo, trace và monitor |    |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Các phần việc bên dưới là phân công đã chốt. Mỗi thành viên tự bổ sung đóng góp thực tế, bằng chứng, phần đã dùng AI nếu có và exit ticket.

## HoTrongNghia-2A202603729

### Phần việc phụ trách

Chủ trì Phiếu A, soạn tiêu chí và đề xuất cổng kinh doanh ở B7.4. Phụ trách bản đồ dữ liệu B3, điều phối pre-mortem B6 và trình bày căn cứ cho quyết định v1 ở B8, v2 ở C12. Cả nhóm chốt tiêu chí và hai quyết định.

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket

## PhamDangQuang-2A202603760

### Phần việc phụ trách

Phụ trách `lab10/guards.py` và B7.1. Triển khai 2–3 cổng phòng ngừa vòng 1 từ HAZOP và pre-mortem. Khi nhận thẻ, sửa cổng theo nguyên nhân đã xác minh và ghi bằng chứng ở C7. Cùng Mạnh phụ trách phần bonus về mức bảo vệ của cổng vòng 1.

### Đóng góp cụ thể

- Triển khai ba cổng vòng 1: chọn chính sách theo ngày hiệu lực, xác minh quyền hoàn và ngăn ghi lặp, xác minh căn cứ và đúng kiện trước khi ghi lỗi hãng.
- Điền Phiếu B mục B7.1 và đối chiếu trace `T-002@55` trước và sau khi thêm cổng.
- Dùng Codex để hỗ trợ sửa `lab10/guards.py`, chạy kiểm thử và soạn phần bằng chứng trong phiếu.

### Bằng chứng

- PR #1, nhánh `quang/round1-guards`.
- Bộ nền trước cổng: `R-base-before-20261119-152741-f6a302`. Sau cổng: `R-base-after-20261119-153900-7fabcf`.
- Số lượt đúng tăng từ 109/110 lên 110/110. Hoàn sai giảm từ 20.000đ xuống 0đ, lỗi hãng oan giảm từ 1 xuống 0. Bộ unit test đạt 13/13.
- C7 và bằng chứng bonus cần report từ thẻ chính thức sau khi nhóm chốt vòng 1.

### Exit ticket

- Bản nháp để Quang xác nhận: Học được cách dùng tracking ở bước ghi để chặn một đề xuất dựa trên số ngày khách tự khai. Còn chưa chắc cách xác định đúng kiện khi đơn có nhiều kiện mà ticket thiếu mã kiện.

## NguyenDucManh-2A202603731

### Phần việc phụ trách

Phụ trách A1–A2 về mục tiêu vận hành và telemetry, HAZOP B4, checklist B5, cấu hình `operating_gates.json` và runbook B7.5–B7.6. Ở vòng 2, phụ trách phần riêng của thẻ, HAZOP, risk register và cập nhật runbook. Cùng Quang phụ trách bonus vòng 1 và gom hồ sơ nộp bài.

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket

## NguyenDucNhat-2A202603812

### Phần việc phụ trách

Phụ trách metric offline A2, nhật ký B0–B1, trace B2 và behavioral test B7.3. Ở vòng 2, phụ trách trace C2, monitor mới tại C8 và report ba mốc. Tìm và ghi bằng chứng `ticket@seed` nếu guard hoặc monitor phát hiện lỗi chìm ngoài thẻ được giao. Đối chiếu report để xác định kết quả của cả hai mục bonus.

### Đóng góp cụ thể

### Bằng chứng

### Exit ticket
