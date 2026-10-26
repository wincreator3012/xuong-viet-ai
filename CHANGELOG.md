# Nhật ký thay đổi của bản vẽ

Trợ lý AI đọc tệp này khi người dùng nói "cập nhật xưởng": từ phiên bản ghi trong `XUONG.json` của xưởng tới bản mới nhất, để kể bằng lời thường điều gì mới và điều gì sẽ đổi. Mỗi mục ghi: phiên bản (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng. Mục mới ở trên cùng.

## 2026.10.26

Bản vẽ đầu tiên: Xưởng viết AI chuyển sang mô hình bản vẽ dựng xưởng riêng, như các xưởng web, phim, thiết kế cùng tác giả.

- **Dựng xưởng riêng trên máy người dùng** (`AGENTS.md`, `DUNG-XUONG.md`, `BAN-DUNG.json`, `tools/ban-dung.py`): trợ lý chép phần năng lực đúng từng byte, viết phần riêng từ `mau-xuong/`.
- **Kho tư liệu nguyên bản** (`khuon/kho-tu-lieu/`): sáu ngăn theo hình thái chất liệu, hướng dẫn đưa tư liệu vào, mục lục ghi nội dung, loại chất liệu, nguồn và ngày, mức riêng tư, đã dùng ở bài nào. Công cụ `tools/kho.py` rà và tìm trong kho, chỉ đọc.
- **Thư mục bài** (`khuon/bai-viet/`, `tools/bai-moi.py`): mỗi bài một thư mục gồm chất liệu, bản nháp, ghi chú bàn giao, sổ nguồn, bản chốt.
- **Giọng văn của người dùng** (`phong-cach/GIONG-VAN.mau.md`, `bai-hoc-giong.mau.md`, `ho-so-nguoi-viet.mau.md`): một tệp thay cho mục "Cấu hình cá nhân" rải ở từng skill.
- **Skill mới `viet-thiet-lap`**: tạo kho, phỏng vấn giọng văn, dẫn đưa tư liệu đầu tiên vào kho và xếp kho, đóng gói skill riêng, giới thiệu xưởng; có chế độ nhẹ cho khung chat.
- **Bốn skill viết nối với kho và thư mục bài**: `viet-nguyen-ban` (mục II-b), `tap-viet` (mục III), `kiem-chung`, `factual-review`.
- **Đóng gói skill** (`tools/dong-goi-skill.py`): gói riêng mang tiền tố `xuong-viet-`, khối "Đã thiết lập" và bản chụp giọng văn, không mang tư liệu; gói chung cho đường nhẹ ở `dong-goi/`. Mô tả trong gói `.zip` rút còn dưới 200 ký tự theo giới hạn tải skill lên Claude.
- **Công cụ kiểm** `tools/cai-dat.py`, `tools/kiem-sach.py`, `tools/kiem-tai-lieu.py`.
- **Sắp lại repo**: `skills-nguon/` thành `skills/`, `cong-cu/` thành `tools/`, `BAI-HOC.md` thành `docs/BAI-HOC.md`; thêm `HUONG-DAN.md`, `GHI-CONG.md`, `LICENSE-TAI-LIEU.md`.

Việc trong xưởng đã dựng: không có (bản đầu tiên).
