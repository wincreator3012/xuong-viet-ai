# Gói skill chung cho đường nhẹ

Thư mục này chứa các skill của xưởng ở dạng chung, chưa mang giọng văn của ai, cho người chỉ dùng khung chat. Muốn có xưởng đầy đủ (kho tư liệu trên máy, bộ skill mang giọng của bạn), dựng xưởng theo [`BAT-DAU.md`](../BAT-DAU.md).

| Bạn dùng | Lấy |
|---|---|
| Claude, có Skills | Các tệp `.zip` ở đây: `viet-thiet-lap.zip`, `tap-viet.zip`, `viet-nguyen-ban.zip`, `kiem-chung.zip`, `factual-review.zip`. Tải lên nguyên tệp, không giải nén |
| ChatGPT Projects, Gemini Gems, Claude Projects | Các tệp `.md` trong `tep-cho-du-an/`, kèm đoạn chỉ dẫn mẫu trong `BAT-DAU.md` |

Trong `tep-cho-du-an/`, tệp `ten-skill.md` là phần chính của skill; tệp `ten-skill--ten-tep.md` là tệp tham chiếu `references/ten-tep.md` của skill ấy.

Các gói được dựng từ `skills/` bằng `python3 tools/dong-goi-skill.py --chung`; đừng sửa tay ở đây.
