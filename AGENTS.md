# AGENTS.md: đọc trước tiên, đây là bản vẽ, không phải chỗ làm việc

Bạn là trợ lý AI (Claude, ChatGPT, Codex, Gemini, Antigravity, Cursor...) vừa được đưa tới **bản vẽ Xưởng viết AI**. Bản vẽ chứa đủ mọi thứ để bạn dựng trên máy người dùng một xưởng viết cùng AI mang giọng của chính họ: bộ skill, chuẩn nghề, công cụ, một kho tư liệu nguyên bản để họ đưa tư liệu của mình vào, và bộ skill riêng để họ lưu vào tài khoản AI. Người dùng thường là người viết tiếng Việt dưới tên mình (nhà giáo dục, nhà tham vấn, nhà khai vấn, giảng viên, chuyên gia), không biết lập trình.

Điều quan trọng nhất: **bản vẽ không phải phần mềm để tải về rồi làm việc bên trong.** Không `git clone`, không bảo người dùng tải ZIP, không `git pull` về sau. Bạn đọc bản vẽ, hỏi người dùng, rồi dựng một xưởng riêng ở thư mục của họ; xưởng đó không nối với bản vẽ. Khi bản vẽ có bản mới, bạn đọc nhật ký thay đổi và áp chọn lọc vào xưởng của họ.

Địa chỉ bản vẽ: https://github.com/wincreator3012/xuong-viet-ai. Đọc nguyên văn từng tệp (tệp thô [raw]) ở `https://raw.githubusercontent.com/wincreator3012/xuong-viet-ai/main/<đường dẫn tệp>`, ví dụ `https://raw.githubusercontent.com/wincreator3012/xuong-viet-ai/main/BAN-DUNG.json`.

## Xác định tình huống trước khi làm gì

| Bạn thấy | Tình huống | Làm gì |
|---|---|---|
| Người dùng đưa đường dẫn bản vẽ, nhờ dựng hay thiết lập xưởng viết; bạn ghi được tệp vào thư mục trên máy họ; thư mục làm việc chưa có `xuong-viet-ai/XUONG.json` | dựng mới | làm theo `DUNG-XUONG.md` từ bước 0 |
| Thư mục làm việc đã có `xuong-viet-ai/XUONG.json` | xưởng đã dựng | đọc `CLAUDE.md` (Claude) hoặc `AGENTS.md` (trợ lý khác) **của xưởng đó**, không làm theo tệp này nữa |
| Người dùng nói "cập nhật xưởng", "xưởng có bản mới không" | cập nhật | `DUNG-XUONG.md` mục "Cập nhật về sau" (lệnh chạy trong xưởng của họ) |
| Bạn chỉ có khung chat, không ghi được tệp vào máy người dùng | đường nhẹ | giải thích một câu vì sao chưa dựng được xưởng đầy đủ; dẫn người dùng dùng gói chung trong `dong-goi/` theo `BAT-DAU.md` mục "Đường nhẹ"; skill `viet-thiet-lap` có chế độ nhẹ để ghi giọng văn và dựng kho dạng tệp nén |
| Thư mục đang mở chính là bản vẽ tải về (có `DUNG-XUONG.md`, `BAN-DUNG.json`, không có `XUONG.json`) | dùng nhầm cách | giải thích một câu: đây là bản vẽ, xưởng của họ sẽ được dựng riêng; dựng ở thư mục làm việc khác theo `DUNG-XUONG.md`, dùng bản tải về làm nguồn đọc (`--ban-ve <thư mục này>`); không viết bài, không sửa tệp trong bản vẽ |
| Người bảo trì bản vẽ nhờ sửa chính bản vẽ | bảo trì | sửa theo `docs/DONG-GOP.md` |
| Người dùng chỉ hỏi về xưởng (làm được gì, cần gì, có mất phí không) | tìm hiểu | trả lời từ `README.md`, `HUONG-DAN.md`, `chuan/`; mời họ dựng khi sẵn sàng |

## Cần đọc gì, theo thứ tự

1. Tệp này.
2. `DUNG-XUONG.md`: quy trình dựng, cập nhật, gỡ rối.
3. `BAN-DUNG.json`: danh mục mọi tệp, loại (`chep`, `mau`, `chi-ban-ve`) và vân tay sha256.
4. Sau khi dựng: các tệp trong xưởng của người dùng (`CLAUDE.md` của xưởng, `skills/viet-thiet-lap/SKILL.md`).

## Nguyên tắc khi làm việc với người dùng

- **Rẽ nhánh theo khả năng thật của phiên**, không theo tên nền tảng: bạn đọc được web không, ghi được tệp vào thư mục trên máy họ không, chạy được Python không (`DUNG-XUONG.md` bước 0).
- **Đọc đúng tài liệu trước khi hướng dẫn**, không dựa vào trí nhớ về nền tảng. Tên nút, menu, gói tài khoản đổi liên tục: trước khi dẫn người dùng bấm gì trên Claude, ChatGPT, Gemini, kiểm trang trợ giúp chính thức hiện hành khi có công cụ tìm kiếm.
- **Hỏi ít, có mặc định, từng bước một.** Mỗi lượt tối đa bốn câu. Việc chỉ người dùng làm được (đưa tư liệu vào kho, tải skill lên tài khoản) thì dẫn một bước mỗi lượt, chờ họ xác nhận.
- **Giọng văn và tư liệu là của người dùng.** Không đề xuất tên, xưng hô, từ ngữ, giá trị của tác giả bản vẽ hay của ai khác; không tạo tư liệu thay họ; không suy diễn về con người họ từ bài viết.
- **Không bao giờ xin mật khẩu, mã xác thực, mã khôi phục, khóa bí mật.**
- **Ghi công.** Xưởng dựng ra giữ `GHI-CONG.md` và các tệp giấy phép.

## Quy đổi vài chỗ riêng của Claude trong tài liệu xưởng

| Trong tài liệu ghi | Với trợ lý khác |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số lựa chọn, tối đa bốn câu mỗi lượt, luôn có mặc định |
| Cowork, máy ảo gắn thư mục, môi trường đám mây của phiên | bạn chạy lệnh thẳng trên máy người dùng: bỏ qua phần chuyển tệp |
| Skill trên tài khoản | nền tảng của bạn có tính năng skill theo chuẩn Agent Skills thì người dùng lưu được gói skill; không có thì đọc thẳng `skills/<tên>/SKILL.md` trong xưởng (`skills/README.md`) |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân tạo ra và chia sẻ miễn phí cho cộng đồng (`GHI-CONG.md`); mã theo MIT (`LICENSE`), tài liệu theo CC BY 4.0 (`LICENSE-TAI-LIEU.md`).
