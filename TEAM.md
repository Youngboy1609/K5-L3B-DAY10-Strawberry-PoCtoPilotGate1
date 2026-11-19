# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Strawberry
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Strawberry-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S2

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

Cả nhóm làm việc trên máy của trưởng nhóm. Các mục dưới đây ghi phần mỗi người phụ trách trong sản phẩm chung. Nhật ký vòng 2 và báo cáo ba mốc dùng chung cho cả nhóm. Nhóm dùng Codex để hỗ trợ soạn phiếu, viết và rà guard/monitor, chạy kiểm chứng và gom hồ sơ.

## HoTrongNghia-2A202603729

### Phần việc phụ trách

Chủ trì Phiếu A, soạn tiêu chí và đề xuất cổng kinh doanh ở B7.4. Phụ trách bản đồ dữ liệu B3, điều phối pre-mortem B6 và trình bày căn cứ cho quyết định v1 ở B8, v2 ở C12. Cả nhóm chốt tiêu chí và hai quyết định.

### Đóng góp cụ thể

- Chủ trì chốt ngưỡng chấp nhận của Strawberry trước lần đánh giá đầu tiên và xác nhận quyết định v1 là Tiếp tục sau khi đọc kết quả bộ nền đã chốt.
- Phụ trách bản đồ dữ liệu, phần kinh doanh và lý do của các ngưỡng trong Phiếu A và B. Cùng nhóm đối chiếu chi phí, ROI, độ phủ và giới hạn an toàn trước khi xác nhận v2 là Tiếp tục với pilot có giám sát.

### Bằng chứng

- Commit ký tiêu chí `89a8a17` và [Phiếu A, A4–A5](templates/form-a-criteria.md#a4).
- Commit chốt v1 `31b2554` và [Phiếu B, B8](templates/form-b-evaluation-gates.md#b8) ghi căn cứ từ mốc `prepared`.
- [Phiếu C, C12](templates/form-c-incident.md#c12) đối chiếu report `R-S2-grade-20261119-164856-b92294` với tiêu chí đã ký và ghi lý do giữ quyết định ở v2.

### Exit ticket

- Em học được rằng dù bộ nền đúng 109/110 lượt, một ca hoàn sai và ghi oan vẫn đủ để trượt ngưỡng an toàn đã ký.
- Em chưa chắc tỷ lệ chuyển duyệt 33,33% trên S2 sẽ ảnh hưởng thế nào đến hàng chờ khi pilot gặp giờ cao điểm thật.

## PhamDangQuang-2A202603760

### Phần việc phụ trách

Phụ trách cổng trong `lab10/guards.py` và cung cấp căn cứ kỹ thuật cho B7.1, C7. Cùng Mạnh đối chiếu mức bảo vệ của cổng vòng 1.

### Đóng góp cụ thể

- Triển khai ba cổng vòng 1: chọn chính sách theo ngày hiệu lực, xác minh quyền hoàn và ngăn ghi lặp, xác minh căn cứ và đúng kiện trước khi ghi lỗi hãng.
- Đối chiếu hành vi của guard trên `T-002@55` và cung cấp kết quả kỹ thuật để nhóm tổng hợp B7.1. Ở vòng 2, cùng nhóm phụ trách kiểm bên chịu phí, hiệu lực phê duyệt và hạn mức tự động theo khách trước khi ghi sổ.
- Dùng Codex để hỗ trợ sửa guard, chạy kiểm thử và rà bằng chứng kỹ thuật.

### Bằng chứng

- [PR #1](https://github.com/Youngboy1609/K5-L3B-DAY10-Strawberry-PoCtoPilotGate1/pull/1), merge commit `af479a6` và [bản chốt guard vòng 1](lab10/guards_round1.py).
- [Phiếu B, B7](templates/form-b-evaluation-gates.md#b7) dùng mốc chung `R-base-after-20261119-154443-b42cfb`. Bộ nền đạt 110/110 lượt, hoàn sai và lỗi hãng oan đều về 0.
- [Guard vòng 2](lab10/guards.py) và [Phiếu C, C7](templates/form-c-incident.md#c7), đối chiếu lần chạy `R-S2-after-20261119-164856-b92294`.

### Exit ticket

- Em học được cách dùng tracking và chính sách để kiểm khoản hoàn ngay trước khi ghi sổ.
- Em chưa chắc nên xác định kiện nào khi một đơn có nhiều kiện mà ticket thiếu mã kiện.

## NguyenDucManh-2A202603731

### Phần việc phụ trách

Phụ trách A1–A2 về mục tiêu vận hành và telemetry, HAZOP B4, checklist B5, cấu hình `operating_gates.json` và runbook B7.5–B7.6. Ở vòng 2, phụ trách phần riêng của thẻ, HAZOP, risk register và cập nhật runbook. Cùng Quang phụ trách bonus vòng 1 và gom hồ sơ nộp bài.

### Đóng góp cụ thể

- Phụ trách mục tiêu vận hành, telemetry, HAZOP và checklist go-live. Cùng nhóm đối chiếu dữ liệu mô phỏng để chọn người duyệt, công suất ca trực, hạn mức và điều kiện dừng.
- Phụ trách bảng quyền kiểm soát của người duyệt trên S2, risk register và runbook phản ứng khi ca chuyển duyệt tăng. Cùng nhóm kiểm lại hồ sơ và bằng chứng vận hành trước khi gom bài.
- Dùng Codex trên máy chung để hỗ trợ soạn HAZOP, runbook và đối chiếu số liệu vận hành.

### Bằng chứng

- [Cấu hình vận hành](config/operating_gates.json) và [Phiếu B, B4–B7](templates/form-b-evaluation-gates.md#b4), gồm SLA 60 phút, 1 người trực và công suất 6 ca/giờ.
- [Phiếu C, C3.1](templates/form-c-incident.md#c3) về quyền duyệt, [C4](templates/form-c-incident.md#c4) về HAZOP và [C10–C11](templates/form-c-incident.md#c10) về risk register và runbook. Report `R-S2-grade-20261119-164856-b92294` ghi 33,33% chuyển duyệt và 0 ca ùn trên S2 after.

### Exit ticket

- Em học được rằng trần ngân sách toàn hệ thống và trần theo từng khách kiểm soát hai rủi ro khác nhau.
- Em chưa chắc một người duyệt có giữ được SLA 60 phút khi nhiều ca đến dồn vào cùng một giờ.

## NguyenDucNhat-2A202603812

### Phần việc phụ trách

Phụ trách metric offline A2, nhật ký B0–B1, trace B2 và behavioral test B7.3. Ở vòng 2, phụ trách trace C2, monitor mới tại C8 và report ba mốc. Tìm và ghi bằng chứng `ticket@seed` nếu guard hoặc monitor phát hiện lỗi chìm ngoài thẻ được giao. Đối chiếu report để xác định kết quả của cả hai mục bonus.

### Đóng góp cụ thể

- Phụ trách cách đo offline, nhật ký dùng chung và đối chiếu trace `T-002@55` tại bộ nền. Cùng nhóm kiểm hai ca thử hành vi ở B7.3.
- Phụ trách phân tích trace S2, đối chiếu ba mốc và kiểm hồi quy trên bộ nền. Cùng nhóm thêm monitor theo trần hoàn theo khách và monitor phát hiện mâu thuẫn với tracking. Ghi bằng chứng bonus từ dữ liệu đo thực tế.
- Dùng Codex trên máy chung để hỗ trợ đọc trace, triển khai monitor và tổng hợp kết quả kiểm chứng.

### Bằng chứng

- [Phiếu A, A2](templates/form-a-criteria.md#a2), [Phiếu B, B0–B2](templates/form-b-evaluation-gates.md#b0) và [nhật ký lần chạy chung](submission/runs/journal.jsonl). Mốc nền đầu tiên là `R-base-before-20261119-151315-bde05c`.
- [Monitor](lab10/monitors.py), [Phiếu C, C8](templates/form-c-incident.md#c8) và [báo cáo tự kiểm tra S2](submission/runs/grade-report.md). S2 đạt 75/75 lượt, bộ nền đạt 110/110 lượt và monitor trần theo khách ghi 10 lượt chuyển duyệt.
- Bằng chứng ngoài thẻ `T-002@55`, event 03 và 06 ở mốc `R-base-after-20261119-164856-b92294`, được ghi ở C8. Đề xuất lệch tracking đã được phát hiện, và khoản hoàn sai bị chặn trước khi ghi.

### Exit ticket

- Em học được rằng trace có thể cho thấy agent đã dùng sai dữ liệu dù cổng chặn kịp và kết quả cuối vẫn đúng.
- Em chưa chắc monitor sẽ bỏ sót bao nhiêu ca nếu trace thực tế thiếu sự kiện hoặc giao dịch đi qua kênh khác.
