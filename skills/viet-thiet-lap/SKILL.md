---
name: viet-thiet-lap
description: "Thiết lập xưởng viết riêng của người dùng (dựng từ bản vẽ Xưởng viết AI, thư mục xuong-viet-ai): tạo kho tư liệu nguyên bản và thư mục bài viết, dẫn người dùng đưa tư liệu của chính họ vào kho, phỏng vấn ngắn để ghi giọng văn (tên, xưng hô, những vai thật sự giữ, người đọc, quy ước ngôn ngữ, từ của họ), đóng gói bộ skill riêng và dẫn lưu vào tài khoản AI, rồi giới thiệu xưởng. Dùng khi người dùng nói thiết lập xưởng viết, bắt đầu, lần đầu dùng, tạo kho tư liệu, xếp kho, đưa tư liệu vào kho, đổi giọng văn, đổi cách xưng hô, kiểm tra xưởng, lưu skill vào tài khoản, đóng gói lại skill, xưởng làm được gì, giới thiệu xưởng, hoặc khi phong-cach/GIONG-VAN.md còn trống, chưa có kho tư liệu, chưa có skill riêng. Cũng dùng ở khung chat không có thư mục để dựng kho dạng tệp nén cho người dùng tải về."
---

# Thiết lập xưởng viết

## Cấu hình cá nhân

Skill này tự đọc `phong-cach/GIONG-VAN.md` và `XUONG.json` của xưởng; không có mục riêng cần điền.

## Mục tiêu

Sau khoảng 40-60 phút, người dùng có trên máy một xưởng viết mang giọng của chính họ: một **kho tư liệu nguyên bản** đã có vài tư liệu đầu tiên do chính họ đưa vào và đã vào mục lục; một **thư mục bài viết**; tệp **giọng văn** ghi đúng điều họ nói; **bộ skill riêng** (đã lưu vào tài khoản AI nếu họ muốn); họ hiểu xưởng làm được gì, việc nào của họ, và biết câu đầu tiên để viết bài thật.

Nguyên tắc: hỏi ít, mỗi lượt tối đa bốn câu, luôn có phương án mặc định (Claude: AskUserQuestion; trợ lý khác: đánh số lựa chọn); giải thích bằng lời thường; ghi ngay sau mỗi lượt, không gom tới cuối. Người dùng vắng mặt thì chọn mặc định, ghi rõ giả định vào `GIONG-VAN.md`, và không tạo tư liệu thay họ.

**Giọng văn là của người dùng.** Không đề xuất tên, chức danh, cách xưng hô, từ ngữ, giá trị của tác giả xưởng hay của ai khác. Chỉ ghi điều người dùng nói ra; không suy từ bài viết của họ ra tính cách, giá trị, hoàn cảnh.

## Bước 0. Định vị

Đọc `CLAUDE.md` của xưởng (trợ lý khác Claude: `AGENTS.md`) nếu chưa đọc trong phiên. Rồi xác định tình huống:

| Thấy | Làm |
|---|---|
| Gốc xưởng có `XUONG.json` và phiên đọc, ghi được thư mục làm việc | Thiết lập đầy đủ: bước 1 tới 5 |
| Thư mục đang mở là bản vẽ (có `DUNG-XUONG.md`, chưa có `XUONG.json`) | Dừng thiết lập; dựng xưởng theo `DUNG-XUONG.md` của bản vẽ trước |
| Skill được gọi từ tài khoản mà phiên chưa gắn thư mục làm việc | Nhờ người dùng gắn thư mục làm việc (thư mục cha chứa `xuong-viet-ai`, `Kho tu lieu`, `Bai viet`); không gắn được thì chỉ trả lời, giới thiệu dựa trên `references/`, nói rõ đó là bản chụp |
| Khung chat không có thư mục nào (dùng gói chung) | Chế độ nhẹ, mục cuối skill |

Người dùng nói "kiểm tra xưởng": chạy `python3 tools/cai-dat.py --trang-thai`, `python3 tools/ban-dung.py --kiem`, `python3 tools/kiem-tai-lieu.py`, `python3 tools/kiem-sach.py` ở gốc xưởng (Windows: `py` thay cho `python3`), báo bằng lời thường; không phỏng vấn lại.

## Bước 1. Tạo kho tư liệu và thư mục bài

Thư mục làm việc đã có tệp giọng văn hay kho từ đường nhẹ (`GIONG-VAN.md`, `Kho tu lieu/`): chép `GIONG-VAN.md` vào `phong-cach/` của xưởng trước (lệnh dưới không ghi đè tệp đã có), và dùng luôn kho ấy.

Ở gốc xưởng: `python3 tools/cai-dat.py`. Lệnh tạo những gì còn thiếu, không bao giờ ghi đè:

- `phong-cach/GIONG-VAN.md`, `bai-hoc-giong.md`, `ho-so-nguoi-viet.md` từ bản khởi đầu `.mau.md`;
- kho tư liệu (mặc định `../Kho tu lieu`) với sáu ngăn, `HUONG-DAN-KHO.md`, `MUC-LUC.md`;
- thư mục bài (mặc định `../Bai viet`) với `_skill/`, `_tam/`, `HUONG-DAN-BAI-VIET.md`.

Người dùng đã chọn dùng một kho ghi chép có sẵn (ghi trong `XUONG.json` > `thuMucKho` ở lúc dựng): chạy `python3 tools/cai-dat.py --khong-tao-ngan`, chỉ thêm hướng dẫn dành cho kho có sẵn và mục lục vào đó, không tạo ngăn, không chuyển tệp nào của họ. Thư mục ấy phải được gắn vào phiên mới đọc được; trong máy ảo, đường dẫn phiên thấy khác đường dẫn trên máy người dùng thì thêm `--kho <đường dẫn phiên thấy>`. Với kho có sẵn, mục lục chỉ ghi những ghi chép người dùng chọn đưa vào việc viết, không lập cho cả kho.

Dấu hiệu xong: dòng "CÀI XONG", và `python3 tools/cai-dat.py --trang-thai` thấy kho, thư mục bài, tệp giọng văn. Báo người dùng một câu bằng lời thường: kho và thư mục bài đã nằm cạnh xưởng, ở đâu trên máy họ.

## Bước 2. Phỏng vấn giọng văn (ba lượt)

Đọc `phong-cach/GIONG-VAN.md` trước. Sau mỗi lượt, thay đúng chỗ `[...]` tương ứng, giữ cấu trúc tệp, đổi tiêu đề thành tên người dùng, ghi ngày cập nhật. Câu nào người dùng muốn để sau thì giữ nguyên `[...]`; các skill sẽ hỏi lại khi cần.

**Lượt 1, về bạn.** Tên viết dưới bài kèm học vị, đúng nguyên văn (hỏi lại cách viết học vị và chữ dễ nhầm, nói rõ sẽ hiện y như vậy); trợ lý gọi bạn là gì (đã hỏi lúc dựng, có ở `XUONG.json` > `xungHoNguoiDung`, thì ghi luôn, không hỏi lại); nghề và nơi làm việc, viết theo cách họ muốn người đọc thấy; kinh nghiệm viết (mới viết, đang lớn, lâu năm).

**Lượt 2, về vai và người đọc.** Giải thích năm vai bằng một câu mỗi vai (nghiên cứu; đào tạo; nhận diện vấn đề và sáng tạo lối giải; thực hành nghề; chiêm nghiệm), hỏi đa chọn vai họ thật sự giữ, và với mỗi vai đã chọn, một chất liệu có thật đứng sau. Người đọc chính; kênh hay đăng; cách xưng hô với người đọc.

**Lượt 3, về chữ và cách làm việc.** Đọc nhanh quy ước ngôn ngữ mặc định (mục 5 của tệp), hỏi giữ hay đổi, và kiểu dấu thanh; từ họ dùng theo nghĩa riêng và từ họ không bao giờ dùng (có thể để sau, xưởng học dần từ bản chốt); với bài đứng tên họ, muốn mở đầu bằng phỏng vấn, soạn có cờ, hay tự viết thô trước; cường độ soi mặc định.

Một câu mở, không bắt buộc: "Vài dòng về điều bạn muốn văn mình mang tới người đọc?" Ghi đúng lời họ vào mục 3. Họ chưa muốn nói thì để trống, không gợi ý thay.

Xong ba lượt: `python3 tools/cai-dat.py --danh-dau thiet-lap`.

## Bước 3. Đưa tư liệu đầu tiên vào kho

Đây là bước làm cho xưởng thành của người dùng. Làm cùng họ, từng bước.

1. **Giải thích kho trong bốn câu**, theo `HUONG-DAN-KHO.md` trong kho: kho giữ những thứ chỉ họ có; khi họ nhờ viết, trợ lý tìm trong kho trước rồi mới hỏi; bài nguyên bản được viết từ đây, không từ chuyện bịa; kho nằm trên máy họ, trợ lý chỉ đọc khi họ mở thư mục, và phần đã đọc được gửi tới dịch vụ AI họ dùng như mọi điều họ gõ.
2. **Chỉ chỗ.** Nói đường dẫn kho trên máy họ như họ thấy trong Finder hay File Explorer (theo `XUONG.json` > `thuMucLamViec`), kể sáu ngăn bằng một dòng mỗi ngăn. Không biết để đâu thì thả vào `0 Moi them`.
3. **Gợi ý ba đến năm thứ đầu tiên**, cụ thể theo những vai họ vừa chọn và điều họ sắp viết, ví dụ: hai bài họ hài lòng nhất vào ngăn `3 Ban viet cua toi`, kèm một dòng vì sao thích; một ghi âm sau buổi dạy vào ngăn `2 Loi noi`; một trăn trở đang có vào ngăn `1 Ky uc va noi tam`; một nghiên cứu họ hay dẫn vào ngăn `4 Tu lieu tham khao`. Nhắc: ẩn danh chuyện của người khác ngay khi ghi; không để mật khẩu, giấy tờ, hồ sơ trị liệu chưa ẩn danh.
4. **Chờ họ thả tệp.** Người dùng tự kéo thả; trợ lý không chép, không tạo tư liệu thay họ. Họ muốn kể ngay một chuyện thay vì có sẵn tệp: ghi đúng lời họ thành một tệp `.md` trong ngăn phù hợp, đọc lại cho họ duyệt.
5. **Xếp kho.** `python3 tools/kho.py --quet`. Với mỗi tệp chưa vào mục lục: đọc, đề xuất một dòng theo cột của `MUC-LUC.md` (nội dung một dòng, yếu tố chất liệu, nguồn và ngày, mức riêng tư); tệp ở `0 Moi them` thì đề xuất ngăn. Trình cả bảng đề xuất một lần; người dùng duyệt, sửa, rồi mới ghi mục lục và chuyển tệp. Mức riêng tư không chắc thì hỏi, mặc định "ẩn danh khi dùng".
6. **Học giọng từ bài cũ (khi ngăn 3 có bài).** Đọc hai ba bài họ hài lòng, nêu vài từ, cụm, cách mở bài lặp lại như một quan sát kèm ví dụ trong bài, hỏi họ có muốn ghi vào `GIONG-VAN.md` mục 6 không. Chỉ ghi điều họ xác nhận.

Có ít nhất một tư liệu đã vào mục lục: `python3 tools/cai-dat.py --danh-dau kho`. Người dùng chưa có tư liệu lúc này: không sao; nói họ gọi lại bằng câu "xếp kho" sau khi thả tệp, và không ghi dấu.

## Bước 4. Bộ skill riêng cho tài khoản AI

Toàn bộ chất liệu giải thích và các bước lưu nằm ở `skills/README.md`.

1. **Kiểm cấu hình cho gói.** `XUONG.json` cần có `thuMucLamViec` (đường dẫn như người dùng thấy trên máy, ví dụ `~/Documents/Viet AI`, không phải đường dẫn máy ảo) và `xungHoNguoiDung`; thiếu thì hỏi rồi ghi.
2. **Đóng gói.** `python3 tools/dong-goi-skill.py`. Dấu hiệu xong: "ĐÓNG GÓI: ĐẠT" và các tệp `xuong-viet-*.zip` trong `Bai viet/_skill/`. Có CẢNH BÁO cấu hình còn thiếu thì điền rồi đóng gói lại. Có LỖI khóa hay mật khẩu: gỡ khỏi tệp được báo, nói người dùng đổi mật khẩu ấy.
3. **Giải thích bằng lời thường** (bốn đến sáu câu, theo đoạn đầu `skills/README.md`): skill là cuốn sổ tay quy trình trợ lý mở ra đúng lúc; bản gốc nằm trong xưởng; lưu lên tài khoản thì mọi cuộc trò chuyện đều nhận ra việc viết, kể cả trên điện thoại, nhờ bản chụp giọng văn; vì là bản chụp nên đổi giọng văn thì đóng gói lại; gói không chứa tư liệu trong kho. Nói rõ gói chụp những tệp riêng nào: giọng văn (mọi gói), bài học giọng (gói viết nguyên bản), hồ sơ người viết (gói tập viết); người dùng muốn chỉ mang giọng văn thì đóng gói lại với `--chi-giong-van`. Hỏi: lưu ngay, để sau, hay không cần.
4. **Dẫn lưu từng bước** theo `skills/README.md` mục "Lưu vào tài khoản", đúng nền tảng người dùng dùng hằng ngày (`XUONG.json` > `ungDungHangNgay`); kiểm trang trợ giúp hiện hành trước khi dẫn. Một bước mỗi lượt; người dùng tự bấm tải lên.
5. **Thử** theo mục "Thử xem skill đã chạy chưa" của `skills/README.md`.
6. `python3 tools/cai-dat.py --danh-dau skill` (cả khi người dùng chọn để sau: nói họ gọi lại bằng câu "lưu skill vào tài khoản").

## Bước 5. Giới thiệu xưởng và bài đầu tiên

1. **Tóm tắt thiết lập** trong năm đến bảy câu: kho ở đâu và đã có gì, giọng văn đã ghi gì và còn để trống gì, skill đã lưu chưa, việc còn treo. Nhắc: mọi điều vừa chọn đổi được bằng một câu "từ nay...", hoặc sửa tay `phong-cach/GIONG-VAN.md`.
2. **Giới thiệu có hệ thống** theo `references/gioi-thieu-xuong.md` (năm chặng, mỗi lượt một chặng, kết bằng một câu hỏi). Cuối cùng: `python3 tools/cai-dat.py --danh-dau gioi-thieu`.
3. **Mời bài đầu tiên:** một bài ngắn, thật, sắp dùng, có chất liệu vừa đưa vào kho. Đưa hai câu mẫu: một cho `tap-viet` ("Tôi đang có một ý về..., nghĩ cùng tôi"), một cho `viet-nguyen-ban` ("Viết giúp tôi bài... từ tư liệu trong kho, phỏng vấn tôi trước").

Người dùng nói "để sau" hay vắng mặt: tóm tắt chặng 1 và 5 trong một tin nhắn, vẫn ghi dấu, nói họ gọi lại bằng câu "giới thiệu lại xưởng".

Cuối phiên: `python3 tools/kiem-sach.py` ĐẠT.

## Khi người dùng nói "xếp kho" (bất cứ lúc nào)

Làm bước 3, từ điểm 5 (xếp kho). Thêm: dòng mục lục không còn tệp thì hỏi tệp đã đổi tên, chuyển chỗ hay bỏ; tư liệu ở ngăn 4 chưa có nguồn đủ để kiểm thì đánh dấu "cần bổ sung nguồn"; tệp ghi âm chưa có bản gỡ băng thì hỏi có muốn gỡ băng không. Không xóa tệp nào trong kho; tệp người dùng muốn bỏ thì chuyển vào `Bai viet/_to_delete/` để họ tự xóa.

## Khi người dùng muốn đổi giọng văn

Đọc `GIONG-VAN.md`, chỉ hỏi về phần muốn đổi, ghi lại, ghi một dòng vào mục 8. Đổi cách xưng hô thì sửa cả `XUONG.json` > `xungHoNguoiDung`. Người dùng đã lưu skill lên tài khoản thì đóng gói lại và dẫn thay bản cũ, vì gói mang bản chụp giọng văn cũ.

## Chế độ nhẹ: khung chat không có thư mục

Người dùng chỉ có khung chat (gói chung tải lên Claude, ChatGPT Projects, Gemini Gems). Nói thẳng một câu: xưởng đầy đủ cần một ứng dụng AI làm việc được với thư mục trên máy (Claude Desktop có chế độ Cowork, Claude Code, Codex, Antigravity); trong khung chat vẫn làm được phần sau:

1. **Giọng văn:** phỏng vấn như bước 2, theo khung `assets/phong-cach/GIONG-VAN.mau.md` (khi gói có thư mục `assets/`; không có thì theo mục lục tệp ấy trong bước 2). Trả kết quả thành tệp `GIONG-VAN.md` để người dùng tải về (khi có công cụ tạo tệp), hoặc một khối chữ để họ lưu thành tệp. Dặn họ tải tệp ấy vào phần tri thức của Project hay Gem để mọi cuộc trò chuyện sau dùng.
2. **Kho tư liệu:** có công cụ chạy mã thì dựng một tệp nén `Viet AI.zip` gồm `Kho tu lieu/` và `Bai viet/`, đưa người dùng tải về, giải nén vào Documents, rồi thả tư liệu vào các ngăn như bước 3. Gói có `assets/khuon/` thì chép nguyên `assets/khuon/kho-tu-lieu/` và `assets/khuon/bai-viet/HUONG-DAN-BAI-VIET.md`; không có (tệp tải lên dự án) thì tạo sáu ngăn theo bảng dưới, mỗi ngăn một tệp `_huong-dan.md` ngắn ghi cột "Để gì vào", cùng `MUC-LUC.md` có hàng tiêu đề | Tệp | Nội dung | Chất liệu | Nguồn, ngày | Riêng tư | Đã dùng ở |. Không có công cụ chạy mã: mô tả sáu ngăn, gợi ý họ tạo các thư mục ấy trên máy.

   | Ngăn | Để gì vào |
   |---|---|
   | `0 Moi them` | Thứ chưa biết xếp đâu |
   | `1 Ky uc va noi tam` | Nhật ký, ghi chú, kỷ niệm, trăn trở |
   | `2 Loi noi` | Ghi âm, bài nói, podcast, bản gỡ băng |
   | `3 Ban viet cua toi` | Bài đã đăng, bản chốt, thư, giáo án, ghi chép chuyên môn |
   | `4 Tu lieu tham khao` | Nghiên cứu, trích sách, số liệu kèm nguồn; phản hồi đã ẩn danh |
   | `5 Hinh anh va do vat` | Ảnh, sơ đồ, đồ vật có câu chuyện, kèm một dòng kể |
3. **Dùng tư liệu trong khung chat:** người dùng tải tư liệu vào phần tri thức của Project hay Gem, tên tệp bắt đầu bằng số ngăn (ví dụ `1 - 2026-10-20 hoc tro hoi cau kho.md`), để trợ lý biết loại chất liệu. Mục lục giữ trong một tệp `MUC-LUC.md` họ tải lên cùng; trợ lý đề xuất dòng mới, họ cập nhật tệp.
4. Khi người dùng có ứng dụng làm việc được với thư mục: dựng xưởng đầy đủ theo bản vẽ (`DUNG-XUONG.md`), dùng lại kho họ đã có.

## Quy tắc cứng

- Tên, học vị, chức danh viết đúng nguyên văn người dùng đưa; không tự rút gọn, không "sửa cho hay".
- `GIONG-VAN.md` chỉ chứa điều người dùng nói hay đã xác nhận; không suy diễn tính cách, giá trị, hoàn cảnh, sức khỏe từ bài viết hay tư liệu.
- Không tạo, sửa, xóa, chuyển tệp tư liệu khi người dùng chưa đồng ý; không bao giờ đưa tư liệu trong kho vào gói skill.
- Không ghi mật khẩu, mã xác thực, khóa, số tài khoản, giấy tờ tùy thân vào bất kỳ tệp nào; thấy trong kho thì nhắc người dùng bỏ ra.
- Ghi `GIONG-VAN.md` sau mỗi lượt hỏi, không gom tới cuối.
- Không sửa bản khởi đầu `.mau.md`, không sửa `khuon/`: đó là năng lực của xưởng; sửa phần riêng.
- Sửa tệp có dấu tiếng Việt bằng cách đọc, sửa, ghi trọn tệp, rồi đọc lại đoạn vừa ghi để chắc dấu còn nguyên.

## Tham chiếu

| Tệp | Nội dung |
|---|---|
| `references/gioi-thieu-xuong.md` | Kịch bản giới thiệu xưởng năm chặng |
| `skills/README.md` (trong xưởng) | Skill là gì, lưu vào tài khoản từng nền tảng, thử, gỡ rối |
| `khuon/kho-tu-lieu/HUONG-DAN-KHO.md` (trong xưởng) | Hướng dẫn kho cho người dùng, được chép vào kho lúc cài |

---

*Phiên bản 1.0, 26/10/2026. Phương pháp và nội dung: Thạc sĩ Lương Dũng Nhân. Giấy phép CC BY 4.0.*
