# DỰNG XƯỞNG: quy trình cho trợ lý AI dựng xưởng viết riêng từ bản vẽ

Tài liệu này viết cho trợ lý AI. Người dùng đưa bạn đường dẫn bản vẽ Xưởng viết AI và nhờ "dựng xưởng viết cho tôi". Bạn đọc bản vẽ rồi dựng trên máy họ một xưởng riêng: phần năng lực giống hệt bản vẽ; phần giọng văn, kho tư liệu và bộ skill là của chính họ. Người dùng chỉ trả lời vài lượt câu hỏi, tự tay đưa tư liệu của mình vào kho, và tự tay lưu skill vào tài khoản AI. Toàn bộ mất khoảng 40-60 phút, phần máy chạy chỉ vài phút.

Đọc `AGENTS.md` trước nếu chưa đọc. Mỗi bước dưới đây có ba phần: làm gì, dấu hiệu đã xong, nếu không thấy dấu hiệu đó thì làm gì.

## Ba điều không làm

1. **Không biến bản vẽ thành chỗ làm việc.** Không `git clone`, không bảo người dùng tải ZIP về rồi mở, không viết bài bên trong bản vẽ. Người dùng đã lỡ tải về: dùng bản đó làm nguồn đọc (`--ban-ve <thư mục bản tải về>`), dựng xưởng ở chỗ khác, cuối cùng hỏi họ có muốn bỏ bản tải về không (chuyển vào thùng rác là việc của họ).
2. **Không viết lại "theo ý hiểu" các tệp năng lực.** Skill, chuẩn, công cụ, khuôn, bản khởi đầu `.mau.md` (loại `chep` trong `BAN-DUNG.json`) phải trùng khớp từng byte với bản vẽ, kiểm bằng vân tay sha256. Gõ lại bằng tay gần như luôn lệch vài ký tự. Cá nhân hóa nằm ở phần riêng và ở bộ skill đóng gói, không nằm ở tệp năng lực.
3. **Không chép phần riêng của bất kỳ ai, và không tạo tư liệu thay người dùng.** Bản vẽ chỉ có bản khởi đầu và hướng dẫn; tên, xưng hô, giọng văn đều hỏi từ người dùng; tư liệu trong kho do chính họ đưa vào hoặc kể ra.

## Kết quả cần có

```
<thư mục làm việc, mặc định Documents/Viet AI>/
├── xuong-viet-ai/   xưởng riêng: năng lực (chép đúng bản vẽ) + phần riêng (phong-cach/, XUONG.json, CLAUDE.md,
│                    AGENTS.md); không có .git, không nối với bản vẽ
├── Kho tu lieu/     kho tư liệu nguyên bản: sáu ngăn, HUONG-DAN-KHO.md, MUC-LUC.md, và tư liệu đầu tiên của người dùng
└── Bai viet/        mỗi bài một thư mục; _skill/ chứa gói skill riêng; _tam/ việc tạm
```

Giữ đúng tên `xuong-viet-ai` cho thư mục xưởng: skill và công cụ gọi thư mục xưởng là "xưởng" hay "gốc xưởng".

## Bước 0: kiểm năng lực của phiên

| Cần | Để làm gì | Không có thì |
|---|---|---|
| Đọc được bản vẽ trực tuyến (công cụ đọc web, hoặc lệnh có mạng tới `raw.githubusercontent.com`) | đọc `BAN-DUNG.json` và tệp thô | nhờ người dùng kiểm mạng; tối thiểu phải đọc được `BAN-DUNG.json` và `tools/ban-dung.py` |
| Ghi tệp vào một thư mục trên máy người dùng | dựng xưởng, tạo kho | không dựng được xưởng: nói thẳng, gợi ý ứng dụng làm việc được với thư mục (`BAT-DAU.md` bước 1), hoặc dùng đường nhẹ (gói chung trong `dong-goi/`, skill `viet-thiet-lap` chế độ nhẹ) |
| Chạy lệnh Python 3.9 trở lên | đọc thô, kiểm, cài, đóng gói skill | hướng dẫn cài Python (`BAT-DAU.md`, mục "Nếu máy chưa có Python") rồi mới đi tiếp |

Rẽ nhánh theo nơi bạn chạy lệnh:

| Phiên | Cách làm |
|---|---|
| Claude Cowork (máy ảo gắn thư mục người dùng, cộng môi trường đám mây của phiên) | Thử `ban-dung.py --doc-tho` trong máy ảo trước. Máy ảo báo lỗi mạng: dựng phần năng lực ở môi trường đám mây, trong thư mục mà công cụ chuyển tệp nhận (thường là thư mục đầu ra của phiên, ví dụ `/mnt/user-data/outputs/xuong-viet-ai/`), `--kiem --chi-nang-luc` ĐẠT ở đó, rồi chuyển cả cây, kể cả `BAN-DUNG.json`, vào thư mục người dùng bằng công cụ chuyển tệp (giữ đúng đường dẫn, tối đa 50 tệp mỗi lần), chạy lại `--kiem --chi-nang-luc` trong máy ảo |
| Claude Code, Codex (kể cả chế độ Codex trong ChatGPT desktop), Antigravity, Cursor (chạy lệnh thẳng trên máy người dùng) | chạy mọi lệnh tại chỗ |
| Chỉ có khung chat, không ghi được tệp | không dựng được xưởng; giải thích một câu vì sao; giới thiệu đường nhẹ trong `BAT-DAU.md` |

Dấu hiệu xong: bạn biết mình đi nhánh nào, và `python3 --version` (Windows: `py --version`) chạy được ở nơi sẽ dựng, báo 3.9 trở lên.

## Bước 1: hỏi người dùng một lượt

Nói trước một câu: bạn sẽ dựng xưởng trên máy họ trong vài phút, rồi cùng họ tạo kho tư liệu và ghi giọng văn. Hỏi tối đa bốn câu, câu nào cũng có mặc định:

1. **Thư mục làm việc**: mặc định tạo `Viet AI` trong Documents (Tài liệu). Người dùng đã có `Viet AI` từ đường nhẹ (có `GIONG-VAN.md`, `Kho tu lieu/`) thì dùng luôn thư mục ấy; bước 5 giữ lại những gì đã có. Thư mục phải được gắn vào phiên (Cowork: nút thêm thư mục; ứng dụng khác: mở thư mục). Nói một câu: kho tư liệu sẽ nằm ở đây; đặt trong iCloud, Google Drive, Dropbox hay OneDrive thì kho cũng được đồng bộ lên dịch vụ ấy.
2. **Trợ lý gọi bạn là gì**: "bạn", "anh", "chị", "thầy", "cô", hay tên riêng.
3. **Ứng dụng AI bạn dùng hằng ngày**: Claude (ứng dụng, Cowork, Claude Code), ChatGPT, Gemini, hay khác. Câu trả lời quyết định bước lưu skill.
4. **Bạn đang giữ ghi chép, tư liệu ở đâu**: chưa có gì (mặc định: tạo kho mới); rải rác trong máy (tạo kho mới, sau đó họ chép dần vào); hay đã có một kho ghi chép riêng như một thư mục Obsidian (hỏi có muốn dùng luôn thư mục ấy làm kho không: có thì ghi đường dẫn vào `thuMucKho` ở bước 4 và nhắc họ gắn thư mục ấy vào phiên khi viết).

Dấu hiệu xong: thư mục làm việc đã gắn vào phiên và bạn đọc, ghi được trong đó. Không thấy: dừng, hướng dẫn người dùng gắn thư mục theo `BAT-DAU.md` bước 2.

## Bước 2: đọc danh mục, viết công cụ dựng

1. Đọc `BAN-DUNG.json` của bản vẽ ở `https://raw.githubusercontent.com/wincreator3012/xuong-viet-ai/main/BAN-DUNG.json`: phiên bản, danh sách tệp, loại từng tệp (`chep`, `mau`, `chi-ban-ve`). Địa chỉ đọc thô của mọi tệp: khóa `nguonTho` cộng đường dẫn tệp (khoảng trắng mã hóa thành `%20`).
2. Tạo `<thư mục làm việc>/xuong-viet-ai/tools/`, rồi ghi `tools/ban-dung.py` đúng nguyên văn tệp thô `<nguonTho>tools/ban-dung.py`: có lệnh và mạng thì dùng lệnh đọc tệp thô (ví dụ `curl -fsSL <nguonTho>tools/ban-dung.py -o tools/ban-dung.py`); không có thì đọc bằng công cụ đọc web và ghi bằng công cụ ghi tệp, không sửa một ký tự. Người dùng đã có bản tải về của bản vẽ và gắn nó vào phiên: chép `tools/ban-dung.py` từ bản đó.
3. So vân tay, chạy ở gốc xưởng: `python3 -c "import hashlib;print(hashlib.sha256(open('tools/ban-dung.py','rb').read()).hexdigest())"` phải bằng giá trị `sha256` của dòng `tools/ban-dung.py` trong `BAN-DUNG.json`.

Dấu hiệu xong: hai chuỗi vân tay khớp. Không khớp: ghi lại bằng đường đọc thô; công cụ đọc web tóm tắt hay định dạng lại nội dung thì không dùng được cho bước này.

## Bước 3: ghi phần năng lực

Ở gốc xưởng: `python3 tools/ban-dung.py --doc-tho`. Công cụ đọc thô từng tệp loại `chep`, kiểm vân tay rồi mới ghi, in một dòng cho mỗi tệp, và lưu `BAN-DUNG.json` của lần dựng vào xưởng. Báo tiến độ bằng lời thường ("đang chép skill và công cụ vào xưởng của bạn").

Dấu hiệu xong: dòng cuối "ĐỌC THÔ: ghi ... tệp, ... 0 lỗi", và `python3 tools/ban-dung.py --kiem --chi-nang-luc` ĐẠT. Lệnh `--kiem` đầy đủ lúc này còn KHÔNG ĐẠT vì thiếu ba tệp điểm vào: bước 4 lo.

Nếu không thấy: lỗi mạng thì theo nhánh Cowork ở bước 0, hoặc người dùng đã có bản tải về thì `--ban-ve <thư mục bản tải về>`; lỗi vân tay thì xem mục gỡ rối.

## Bước 4: viết phần riêng của xưởng

Ba tệp loại `mau` (đọc từ `mau-xuong/` của bản vẽ, ghi vào gốc xưởng):

- `XUONG.json` từ `mau-xuong/XUONG.mau.json`: điền `phienBan` (của `BAN-DUNG.json`), `ngayDung`, `ngayCapNhat`, `troLyDung`, `thuMucLamViec` (đường dẫn như người dùng thấy trong Finder hay File Explorer, ví dụ `~/Documents/Viet AI`, không phải đường dẫn máy ảo), `xungHoNguoiDung`, `ungDungHangNgay`; `thuMucKho` giữ `../Kho tu lieu` trừ khi người dùng chọn dùng kho ghi chép có sẵn ở bước 1; bỏ khóa `_huong-dan`.
- `CLAUDE.md` và `AGENTS.md` từ `mau-xuong/`: chép nguyên nội dung mẫu. Sau bước thiết lập có thể thêm một dòng đầu nói đây là xưởng của ai; không đổi quy tắc cứng.

Dấu hiệu xong: `python3 tools/ban-dung.py --kiem` ĐẠT và `python3 tools/kiem-tai-lieu.py` ĐẠT. Không thấy: đọc dòng báo lỗi, viết bù tệp còn thiếu.

## Bước 5: tạo kho tư liệu, ghi giọng văn, đưa tư liệu đầu tiên vào kho

Từ đây làm việc trong xưởng vừa dựng. Làm bước 1 tới 3 của `skills/viet-thiet-lap/SKILL.md`:

1. `python3 tools/cai-dat.py`: tạo `Kho tu lieu/` (sáu ngăn, hướng dẫn, mục lục), `Bai viet/` (kèm `_skill/`, `_tam/`), và tệp giọng văn từ bản khởi đầu.
2. Phỏng vấn ba lượt về giọng văn, ghi vào `phong-cach/GIONG-VAN.md` sau mỗi lượt.
3. Giải thích kho, chỉ chỗ trên máy họ, gợi ý ba đến năm tư liệu đầu tiên, chờ họ tự thả tệp vào, rồi "xếp kho" cùng họ (`python3 tools/kho.py --quet`, đề xuất dòng mục lục, họ duyệt rồi mới ghi).

Dấu hiệu xong: `python3 tools/cai-dat.py --trang-thai` báo giọng văn "đã thiết lập" và kho có ít nhất một tư liệu đã vào mục lục. Người dùng chưa có tư liệu lúc này: ghi rõ trong tin nhắn cuối, hẹn họ nói "xếp kho" sau khi thả tệp; không tạo tư liệu thay họ.

## Bước 6: bộ skill riêng cho tài khoản AI

Là bước 4 của `skills/viet-thiet-lap/SKILL.md`: `python3 tools/dong-goi-skill.py` tạo các gói `xuong-viet-*.zip` trong `Bai viet/_skill/`, mỗi gói mang khối "Đã thiết lập" và bản chụp giọng văn của người dùng (gói viết nguyên bản thêm bài học giọng, gói tập viết thêm hồ sơ người viết; `--chi-giong-van` để chỉ mang giọng văn), không mang tư liệu nào trong kho. Giải thích skill bằng lời thường, dẫn họ lưu vào tài khoản từng bước theo `skills/README.md`, rồi thử một câu.

Dấu hiệu xong: "ĐÓNG GÓI: ĐẠT", các tệp `.zip` trong `Bai viet/_skill/`, và `--trang-thai` báo bước skill riêng đã xong (người dùng lưu ngay hay hẹn sau đều được).

## Bước 7: giới thiệu xưởng và bàn giao

Là bước 5 của `skills/viet-thiet-lap/SKILL.md`. Kết bằng: xưởng, kho, thư mục bài nằm ở đâu; các gói skill đã lưu chưa; câu đầu tiên để viết bài thật; câu "cập nhật xưởng" cho về sau.

Dấu hiệu xong: `--trang-thai` báo "Giới thiệu xưởng: đã", `python3 tools/ban-dung.py --kiem` ĐẠT, `python3 tools/kiem-sach.py` ĐẠT.

## Cập nhật về sau

Người dùng nói "cập nhật xưởng", "có bản mới không", hoặc bạn thấy `phienBan` trong `XUONG.json` cũ hơn bản vẽ:

1. `python3 tools/ban-dung.py --so-ban-ve`: liệt kê tệp mới, tệp bản vẽ đã đổi, tệp người dùng đã sửa trong xưởng, tệp bản vẽ đã bỏ.
2. Đọc `CHANGELOG.md` của bản vẽ từ phiên bản trong `XUONG.json` tới bản mới. Kể cho người dùng bằng lời thường: điều gì mới, điều gì sẽ đổi trong xưởng. Kho tư liệu, bài viết và giọng văn của họ không bị đụng tới.
3. Người dùng đồng ý: `python3 tools/ban-dung.py --doc-tho`. Tệp người dùng đã chủ ý sửa được giữ nguyên và báo ra; cùng họ quyết giữ bản của họ, lấy bản mới (`--ghi-de --chi <đường dẫn>`), hay trộn tay.
4. Tệp bản vẽ đã bỏ: hỏi người dùng; cần bỏ thì chuyển vào `Bai viet/_to_delete/`, không tự xóa.
5. Mẫu điểm vào đổi (`mau-xuong/`): đọc bản mới, trộn phần mới vào `CLAUDE.md`, `AGENTS.md` của xưởng, giữ phần riêng; khóa mới của `XUONG.mau.json` thì thêm vào `XUONG.json`, không đổi giá trị đã có.
6. Bản khởi đầu `.mau.md` đổi: so với tệp riêng của người dùng, thêm mục mới mà không đổi điều họ đã ghi. Khuôn kho đổi: `python3 tools/cai-dat.py` chỉ thêm tệp hướng dẫn còn thiếu, không đụng tư liệu.
7. Skill đổi: `python3 tools/dong-goi-skill.py`, hướng dẫn người dùng thay bản trên tài khoản (`skills/README.md`, mục thay bản cũ).
8. Kiểm: `python3 tools/ban-dung.py --kiem`, `python3 tools/kiem-tai-lieu.py`, `python3 tools/kiem-sach.py`; ghi `phienBan`, `ngayCapNhat` mới vào `XUONG.json`.

## Gỡ rối

| Thấy | Thường do | Làm gì |
|---|---|---|
| `--doc-tho` báo lỗi mạng, 403, hết thời gian | nơi chạy lệnh bị chặn mạng tới `raw.githubusercontent.com` | chạy ở nơi có mạng (Cowork: môi trường đám mây) rồi chuyển tệp; hoặc nhờ người dùng mở quyền mạng cho ứng dụng |
| "vân tay không khớp bản vẽ" | bản vẽ vừa cập nhật giữa lúc đọc danh mục và lúc đọc tệp | chờ vài phút, chạy lại `--doc-tho` (chỉ đọc tệp còn thiếu); vẫn lệch thì mở issue trên GitHub của bản vẽ |
| `--kiem` báo THIẾU sau khi chuyển tệp từ môi trường đám mây | chuyển thiếu một đợt, sai đường dẫn, hay tên thư mục có khoảng trắng bị đổi | chuyển nốt đúng đường dẫn, chạy lại `--kiem` |
| Công cụ báo "DỪNG: thư mục này là bản vẽ" | đang chạy lệnh trong bản vẽ tải về | dựng xưởng ở thư mục khác |
| Người dùng gắn nhầm thư mục `xuong-viet-ai` thay vì thư mục làm việc | `Kho tu lieu/`, `Bai viet/` phải nằm cạnh xưởng | nhờ gắn thư mục làm việc (thư mục cha) |
| Kho là một thư mục ghi chép có sẵn nằm ngoài thư mục làm việc, công cụ báo không thấy kho | thư mục ấy chưa gắn vào phiên, hoặc đường dẫn trong `XUONG.json` là đường dẫn trên máy người dùng mà phiên chạy trong máy ảo | gắn thêm thư mục ấy vào phiên; trong Cowork, đường dẫn máy ảo khác đường dẫn trên máy: dùng `--kho <đường dẫn máy ảo>` cho lệnh đang chạy |
| Windows báo không có `python3` | Windows dùng lệnh `py` | thay `python3` bằng `py` |
| Tải gói skill lên tài khoản bị từ chối | mô tả quá dài, trùng tên, hoặc tài khoản chưa bật tính năng | `skills/README.md` mục gỡ rối |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân tạo ra và chia sẻ miễn phí (`GHI-CONG.md`); mã theo MIT, tài liệu theo CC BY 4.0.
