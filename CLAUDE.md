# Xưởng viết AI: điểm vào cho AI

Đọc file này trước khi dùng repo để viết hay kiểm một văn bản cho người dùng.

## Tinh thần

Văn nguyên bản là văn mà sau mỗi câu có một người thật đứng: chất liệu là của người viết, phán đoán là của người viết, và người viết sẵn lòng đứng tên. AI không đóng vai thay người viết; AI giữ chỗ để vai thật của họ lên tiếng bằng cách hỏi, soi, kiểm, và soạn từ chất liệu họ trao. Mọi khung và danh sách trong repo là gương soi sau khi viết, không phải khuôn đúc trước khi viết.

## Đọc theo thứ tự

1. `chuan/00-ten-goi-va-he-mo-hinh.md` để dùng đúng tên khái niệm.
2. `skills-nguon/viet-nguyen-ban/SKILL.md` khi AI soạn hay sửa bài dưới tên người dùng; `skills-nguon/tap-viet/SKILL.md` khi người dùng muốn tự nghĩ, tự viết và được hỏi, soi, khai vấn, hoặc khi cần thẩm định theo ACCORD-ACCEPT. Đọc mục "Cấu hình cá nhân" trước, mục nào trống thì hỏi.
3. `skills-nguon/kiem-chung/SKILL.md` khi văn bản nhắc nguồn, con số, nhà nghiên cứu, lời trích.
4. `skills-nguon/viet-nguyen-ban/references/tu-vung-va-cau-truc.md` khi viết hay rà tiếng Việt: từ cấm tuyệt đối, từ đặc thù của người viết, từ ngờ, cấu trúc có trần; chạy `python3 cong-cu/ra-tu-va-cau-truc.py <file>` trước khi giao.
5. `chuan/` khi cần bản tóm để giải thích cho người dùng.
6. `BAI-HOC.md` khi cần biết một bài học đến từ đâu.

## Trước khi bắt tay, tự hỏi

1. Việc này đang ở chặng nào của vòng viết (Tiếp nhận, Nội quán, Đồng kiến tạo, Nghiền ngẫm, Học hỏi), và câu hỏi lớn của chặng ấy đã trả lời được chưa? Người dùng cần AI soạn, hay muốn tự viết và được soi?
2. Thể loại này ở mức nguyên bản nào, vai nào cầm bè, và AI được làm tới đâu?
3. Chất liệu thật đã đủ chưa? Thiếu thì hỏi hoặc đặt cờ có hướng; không lấp bằng khái quát hay chi tiết hình dung.
4. Hai chỉ dẫn có trái nhau không? Nếu có, xếp theo thang thẩm quyền và ghi lựa chọn vào ghi chú bàn giao.

## Người dùng nói gì thì dùng gì

| Người dùng nói | Dùng |
|---|---|
| "tập viết", "nghĩ cùng tôi", "tôi đang có một ý", "nên viết thành gì", "đọc bản tôi tự viết", "góp ý nhưng đừng viết lại", "thẩm định bản thảo sách", "đánh giá chương trình", "nhìn lại bài vừa rồi" | `tap-viet` |
| "viết bài", "soạn bài báo", "newsletter", "bài mạng xã hội", "chuyển bài nói thành bài viết" | `viet-nguyen-ban` |
| "kiểm chứng", "rà trích dẫn", "soát danh mục tham khảo" | `kiem-chung` |
| Gửi bản đã sửa, "đây là bản chốt" | `viet-nguyen-ban`, mục VII |
| "viết truyện cho tôi" | `viet-nguyen-ban` mục IV: hỏi và soi, không viết câu vào truyện |

## Quy tắc khi sửa repo

1. Skill là bản đầy đủ, chuẩn là bản tóm; sửa skill trước rồi cập nhật chuẩn.
2. Bài học mới ghi một dòng ở `BAI-HOC.md`, có ngày và nguồn đã ẩn danh.
3. Không đưa tên người, tên dự án, chuyện riêng của bất kỳ ai vào repo.
