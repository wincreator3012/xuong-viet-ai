# Đóng góp và bảo trì bản vẽ

Tài liệu cho người bảo trì bản vẽ (tác giả và người được mời đóng góp), và cho trợ lý AI khi được nhờ sửa chính bản vẽ.

## Nguyên tắc

1. Skill là bản đầy đủ, chuẩn là bản tóm: sửa skill trước, rồi cập nhật chuẩn trong `chuan/`.
2. Không đưa tên người, tên dự án, chuyện riêng của bất kỳ ai vào bản vẽ. Ví dụ dùng ca ghép có ghi rõ, hoặc ca giả định gọi rõ là giả định.
3. Phần riêng của người dùng chỉ có bản khởi đầu `.mau.md` ở bản vẽ; không bao giờ có `XUONG.json` hay tệp giọng văn đã điền.
4. Văn bản theo quy ước nền: không dùng dấu gạch dài, không viết hoa chữ đầu mỗi từ trong tiêu đề, ngoặc tròn cho chú thích, ngoặc vuông cho thuật ngữ gốc, kiểu dấu thanh cũ (`python3 tools/chuan-hoa-dau-thanh.py --write <tệp>`), rà từ và cấu trúc (`python3 tools/ra-tu-va-cau-truc.py <tệp>`).
5. Bài học mới ghi một dòng ở `docs/BAI-HOC.md`, có ngày và nguồn đã ẩn danh.

## Sau mỗi lần sửa

1. `python3 tools/kiem-tai-lieu.py` ĐẠT.
2. Sửa skill: `python3 tools/dong-goi-skill.py --chung` để dựng lại `dong-goi/`.
3. Thêm một mục vào đầu `CHANGELOG.md`: phiên bản mới (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng.
4. `python3 tools/ban-dung.py --lap` để lập lại `BAN-DUNG.json` (phiên bản lấy từ mục đầu `CHANGELOG.md`).
5. `python3 tools/kiem-sach.py` ĐẠT.
6. Thử dựng một xưởng từ bản vẽ trên máy vào một thư mục tạm: chép `tools/ban-dung.py` vào `<tạm>/xuong-viet-ai/tools/`, chạy `--doc-tho --ban-ve <bản vẽ>`, viết phần riêng từ `mau-xuong/`, rồi `--kiem`, `tools/cai-dat.py`, `tools/dong-goi-skill.py`.

## Loại tệp trong `BAN-DUNG.json`

- `chep`: năng lực, chép đúng từng byte vào xưởng.
- `mau`: tệp trong `mau-xuong/`, trợ lý điền rồi ghi thành tệp điểm vào của xưởng.
- `chi-ban-ve`: chỉ ở bản vẽ (README, BAT-DAU, AGENTS, CLAUDE, GEMINI, DUNG-XUONG, CHANGELOG, `dong-goi/`, tệp này).

Muốn đổi nhóm của một tệp: sửa `CHI_BAN_VE` hoặc `MAU` trong `tools/ban-dung.py`.
