# Nhật ký thay đổi của bản vẽ

Trợ lý AI đọc tệp này khi người dùng nói "cập nhật xưởng": từ phiên bản ghi trong `XUONG.json` của xưởng tới bản mới nhất, để kể bằng lời thường điều gì mới và điều gì sẽ đổi. Mỗi mục ghi: phiên bản (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng. Mục mới ở trên cùng.

## 2026.10.31

Hai nếp tiếng Việt tự nhiên và quy ước chữ số, rút từ đợt hiệu đính một cuốn sách thực hành và ứng dụng đi kèm (30/10/2026); gộp luôn các sửa nhỏ ngày 29/10 và 30/10.

- **Nhịp song âm tiết** (`skills/viet-nguyen-ban/references/tu-vung-va-cau-truc.md` D1): bảng từ đơn âm tiết cụt và từ thay, kèm phép thử đọc to và thứ tự cách nới.
- **Thoát lối dịch sát** (cùng tệp, A4b): bảng xếp theo kiểu (lượng từ "một" theo mạo từ Anh, thành ngữ dịch từng chữ, động từ đa nghĩa, thuật ngữ chuyên môn, bị động, chức danh), kèm phép thử dịch ngược.
- **Quy ước trình bày** (cùng tệp, A5): chữ số Ả Rập cho mọi số đếm và đại lượng ở mọi văn bản, không trộn chữ và số; ngoặc vuông tiếng Anh chỉ khi tiếng Việt chưa tự đủ nghĩa; tên ấn phẩm đúng từng chữ theo bản in cuối.
- **Chuẩn 04, mục 8**: bản tóm của hai nếp.
- **`viet-nguyen-ban`**: lượt mạch và câu có một lượt đọc to riêng cho hai nếp.
- **`kiem-chung`, chuẩn 01**: chức danh nước ngoài theo cách gọi Việt Nam đang dùng: assistant professor là "trợ lý giáo sư" (không "giáo sư trợ lý", không nâng thành "phó giáo sư"), Lead Economist là "chuyên gia kinh tế trưởng".
- **`tools/ra-tu-va-cau-truc.py`**: dò thêm cụm dịch sát, từ đơn âm tiết đứng cuối mệnh đề (D1) và câu trộn chữ với số (A5).

Việc trong xưởng đã dựng: chép lại các tệp năng lực (`tools/ban-dung.py`); hỏi người dùng có muốn thêm hai dòng mới của mục 5 trong `phong-cach/GIONG-VAN.mau.md` (tiếng Việt tự nhiên, chữ số) vào tệp giọng văn của họ không; đóng gói lại skill riêng (`tools/dong-goi-skill.py`).

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
