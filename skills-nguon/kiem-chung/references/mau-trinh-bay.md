# Mẫu trình bày kết quả kiểm chứng

Các mẫu dưới đây là điểm xuất phát đã dùng thật, không phải khuôn bắt buộc. Đổi theo người nhận và theo quy ước của nhà xuất bản.

## 1. Sổ nguồn (dùng khi soạn và khi rà)

Mỗi nguồn một dòng. Sổ sống suốt dự án; khi chính văn đổi, sổ đổi theo.

| Mệnh đề trong bài | Nguồn (APA 7, DOI) | Nguồn nói gì (trích ngắn nguyên văn) | Mức diễn giải | Trạng thái kiểm | Ngày kiểm |
|---|---|---|---|---|---|
| "Thở ra dài hơn hít vào làm tăng hoạt động phó giao cảm" | Laborde và cộng sự (2021), https://doi.org/... | "..." | Diễn giải gần | Kiểm qua tóm tắt gốc | 14/10/2026 |

- Mức diễn giải: nguyên văn / diễn giải gần / suy rộng của tác giả.
- Trạng thái kiểm: kiểm trên toàn văn / kiểm qua tóm tắt gốc / kiểm qua nguồn thứ cấp (ghi nguồn nào) / chưa kiểm được. Nguồn đã tra đủ mà không có thì ghi "đã xác định không tồn tại" ở cột ghi chú.
- Nguồn chỉ dùng để kiểm (không nhắc trong chính văn): ghi thêm "chỉ làm căn cứ kiểm chứng".

## 2. Một mục gửi ban biên tập

```
## Rà soát (R07). [Tên lỗi viết như mô tả văn bản, không quy lỗi người]

**Trang:** 72-73
**Vị trí:** Bài 2. [Tên bài]; Thông tin thêm, câu 2

**Văn bản đang dàn:**

[Chép nguyên văn từ bản dàn, kể cả lỗi chính tả, để tìm được bằng chức năng Tìm.]

**Đề xuất sửa:**

[Văn bản dán được ngay. Chỉ dẫn dàn trang, nếu có, đặt trong ngoặc vuông ở dòng riêng.]

**Căn cứ kiểm chứng:**

- [Đã đọc gì: tóm tắt hay toàn văn, trang nào.] [Trích ngắn câu then chốt của nguồn.] [Vì sao câu cũ lệch.]

**Nguồn:**

- [APA 7 đầy đủ, có DOI.]
```

Lỗi nhỏ đưa vào bảng một dòng mỗi lỗi:

| # | Trang | Vị trí | Lỗi | Văn bản đang dàn | Đề xuất sửa | Lý do, căn cứ |
|---|---|---|---|---|---|---|

Lỗi lặp nhiều nơi gom thành quy tắc chung: nêu quy tắc, số chỗ đếm trên bản dàn hiện hành, danh sách vị trí, cách sửa bằng Tìm và Thay thế, và ngoại lệ (tên sách đã xuất bản, trích nguyên văn).

## 3. File riêng cho tác giả

```
# VIỆC TÁC GIẢ CẦN CHỐT

*Tài liệu nội bộ, không gửi ban biên tập. Tác giả ghi ý kiến sau dấu "=>"; mục để trống nghĩa là đồng ý phương án đang dùng.*

| # | Chỗ trong sách | Đang thấy gì | Phương án đang dùng trong file gửi biên tập | Ý kiến của tác giả |
|---|---|---|---|---|
| 1 | Chương 1, tr. 18 | Sách ghi 21%, bản tổng kết khảo sát ghi 22% | Chưa sửa | => |
```

Chia ba nhóm: quyết định nội dung lớn; chi tiết đời tác giả do người khác thêm hoặc đổi; số liệu và nguồn chỉ tác giả đối chiếu được. Thêm một mục "Những điểm tôi đã tự quyết trong file (để tác giả biết)" để tác giả thấy mọi lựa chọn không hiển nhiên.

Khi tác giả trả lời xong, đưa quyết định vào file đề xuất ngay, và giữ nguyên các dòng "=>" của tác giả trong file này làm hồ sơ. Dòng "=>" nào tác giả viết thẳng vào file gửi biên tập thì viết lại thành câu hoàn chỉnh trước khi xuất bản.

## 4. Phụ lục các mục đã xử lý

Ở vòng sau, mục mà biên tập đã sửa xong chuyển sang một bảng riêng: mã mục, trang, nội dung, tình trạng (đã sửa đúng đề xuất / đã sửa theo cách khác, chính xác / không còn áp dụng), ghi chú. Bảng này giúp hai bên thấy tiến độ và ghi nhận phần việc của biên tập.

## 5. Phần máy làm được

- So nguyên văn: mọi đoạn "văn bản đang dàn" phải tìm thấy trong văn bản trích từ file dàn trang (sau khi gộp khoảng trắng). Công cụ: `cong-cu/doi-chieu-nguyen-van.py` trong repo xuong-viet-ai.
- Đếm theo quy tắc chung: dấu gạch dài, kiểu dấu thanh, thuật ngữ cần đổi, đếm lại trên đúng bản dàn đang xét.
- Mã mục trùng, mã mục bị nhảy, chỗ trỏ chéo "xem B198" trỏ đúng mục.
- Cụm báo số bị rơi: hai khoảng trắng sau "hơn", "khoảng", "gần".

Máy không kiểm được nghĩa. Một câu khớp nguyên văn bản dàn vẫn có thể nói sai điều nguồn nói.
