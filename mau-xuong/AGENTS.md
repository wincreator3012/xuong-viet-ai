# AGENTS.md: cho trợ lý AI không phải Claude, trong xưởng viết của người dùng

Bạn là trợ lý AI (ChatGPT, Codex, Gemini, Antigravity, Cursor...) được mở trong **xưởng viết riêng của người dùng**, do một trợ lý AI dựng trên máy họ từ bản vẽ Xưởng viết AI (địa chỉ, phiên bản: `XUONG.json`). Toàn bộ cách làm việc viết trong `CLAUDE.md`; xưởng được viết và kiểm chứng trên Claude, nhưng mọi phần đều là tệp chữ và công cụ Python thông thường nên bạn dùng được như nhau.

## Việc đầu tiên

1. Đọc `CLAUDE.md` và làm theo, coi mọi chỗ ghi "Claude" là "trợ lý AI" (là bạn).
2. Chạy `python3 tools/cai-dat.py --trang-thai` ở gốc xưởng (Windows: `py tools\cai-dat.py --trang-thai`). Chưa thiết lập: làm theo `skills/viet-thiet-lap/SKILL.md`.
3. Mỗi việc: đọc SKILL.md tương ứng trong `skills/` theo bảng "Việc nào, skill nào" của `CLAUDE.md`. Skill là tệp Markdown, đọc và làm theo; không cần cài gì.

## Quy đổi vài chỗ riêng của Claude

| Trong tài liệu ghi | Với bạn |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số lựa chọn, tối đa bốn câu mỗi lượt, luôn có mặc định |
| Cowork, máy ảo gắn thư mục, môi trường đám mây của phiên | bạn chạy lệnh thẳng trên máy người dùng: chạy mọi lệnh tại chỗ |
| Skill trên tài khoản (tên `xuong-viet-*`) | nền tảng của bạn có tính năng skill theo chuẩn Agent Skills thì người dùng lưu được gói ở `Bai viet/_skill/` (`skills/README.md`; tra trang trợ giúp hiện hành trước khi hướng dẫn); không có thì đọc thẳng `skills/<tên>/SKILL.md` |

## Bất biến

- Không bịa chuyện, nguồn, con số, lời chứng thực; không làm giả giùm người viết.
- `phong-cach/GIONG-VAN.md` chỉ ghi điều người viết nói ra; không suy diễn về con người họ.
- Kho tư liệu (`Kho tu lieu/`) là của người viết: không sửa, xóa, chuyển khi chưa được đồng ý; giữ đúng mức riêng tư trong mục lục.
- Bài, bản nháp, việc tạm ghi NGOÀI xưởng (`Bai viet/`); cuối phiên `python3 tools/kiem-sach.py` phải ĐẠT.
- Không bao giờ hỏi mật khẩu, mã xác thực, khóa. Không tự commit, push, xóa tệp của người dùng.
- Xưởng không phải bản sao git của bản vẽ: cập nhật theo `CLAUDE.md` mục "Xưởng này từ đâu ra".
