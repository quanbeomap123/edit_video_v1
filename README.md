# CapcutEdit-v1

Skill cho trợ lý lập trình AI dựng video short talking head bằng workflow file/code, với project CapCut có thể chỉnh sửa tiếp. Được thiết kế từ một quy trình dựng thực tế và các vòng feedback về typography, pace, SFX và đóng gói project.

**Đây là hướng dẫn vận hành kèm công cụ kiểm tra, không phải plugin hay ứng dụng dựng video tự động.** Skill không cài CapCut, không điều khiển chuột/phím, không cung cấp API chính thức của CapCut và không bảo đảm mọi phiên bản draft đều tương thích.

## Skill làm gì?

- Cắt vấp, nói lặp và khoảng nghỉ; giữ nguyên ý nghĩa lời nói.
- Một video dùng một project CapCut; các bản sửa nằm trong nhiều timeline khi đang làm.
- Ưu tiên phụ đề native để sửa được nội dung/font trong CapCut. Motion phức tạp có thể là clip alpha riêng từng scene, giữ source để sửa và render lại scene đó.
- Bố cục chữ theo khuôn mặt, gesture và asset; bold sans kết hợp serif mảnh có chọn lọc; highlight và motion theo vai trò câu nói.
- Giữ picture, voice, asset, caption, motion và SFX riêng track.
- Kiểm tra media trên timeline **và media bin**; nhận biết đường dẫn tương đối/placeholder CapCut.
- Khi đã chốt final, lập kế hoạch dọn bản cũ/cache, bảo vệ media đang dùng và kho asset tái sử dụng.

Style mặc định: 9:16, 1080×1920/30 fps, nền grid tối chuyển động nhẹ, không glassmorphism, không glow nặng. Có thể thay đổi bằng brief mới.

## Cài vào Codex

1. Clone repo hoặc tải **Code → Download ZIP** rồi giải nén.
2. Chép **thư mục `capcutedit-v1` bên trong repo** vào `~/.codex/skills/`. Trên Windows là `%USERPROFILE%\.codex\skills\capcutedit-v1`.
3. Skill có thể được nhận ở lượt tiếp theo; nếu chưa xuất hiện, mở chat mới hoặc khởi động lại ứng dụng.

Ví dụ dùng PowerShell, chạy từ thư mục muốn tải repo:

```powershell
git clone https://github.com/quanbeomap123/edit_video_v1.git
$skillRoot = Join-Path $env:USERPROFILE '.codex\skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
if (Test-Path -LiteralPath (Join-Path $skillRoot 'capcutedit-v1')) {
    throw 'Skill đã tồn tại; sao lưu hoặc đối chiếu bản cũ trước khi cập nhật.'
}
Copy-Item -LiteralPath '.\edit_video_v1\capcutedit-v1' -Destination $skillRoot -Recurse
```

Gọi trong chat:

```text
$capcutedit-v1 Dựng các footage trong [đường dẫn], theo thứ tự 1–6.
Hook dùng [asset] trong 3 giây. Phụ đề thường dùng text native CapCut.
Tạo mẫu style 10 giây để tôi duyệt trước khi làm toàn bộ.
```

Feedback theo đoạn:

```text
$capcutedit-v1 Sửa scene 00:28–00:30: tăng keyword 20%, giảm SFX.
Giữ thời lượng, chỉ render lại scene motion này và replace trên timeline hiện tại.
```

## Yêu cầu và giới hạn

- Trợ lý có quyền đọc/ghi file và chạy lệnh; native draft phải là JSON đọc được. Agent cần kiểm tra schema thực tế trước khi sửa.
- CapCut Desktop, footage và asset do người dùng chuẩn bị. Windows là môi trường tham chiếu đã dùng; macOS chưa được kiểm thử trong repo này.
- Python 3.9+ cho validator. FFmpeg, công cụ transcribe và runtime motion cần được cài riêng nếu công việc yêu cầu; không được bundle ở đây.
- HyperFrames, Remotion và Typography là lựa chọn bổ trợ, không phải dependency được tự động cài. Không dùng dịch vụ có phí nếu chưa được cho phép.
- Với thay đổi metadata, có thể cần lưu và đóng CapCut để tránh ứng dụng ghi đè dữ liệu từ bộ nhớ.
- Các scene alpha chỉ sửa như media clip trong CapCut; muốn đổi chữ cần chỉnh source và render lại scene. Muốn MP4 mới hoàn chỉnh vẫn cần xuất lại timeline.
- Không có footage, ảnh meme, nhạc, SFX, font thương mại, thông tin tài khoản hay dữ liệu project cá nhân trong gói này. Tạo kho `assets/` riêng và lưu nguồn/license.

## Kiểm tra project

```powershell
python capcutedit-v1/scripts/validate_project.py "PATH_TO_CAPCUT_PROJECT"
python capcutedit-v1/scripts/validate_project.py "PATH_TO_CAPCUT_PROJECT" --report validation.json
```

Validator **chỉ đọc draft**, không tự sửa hoặc xóa file. Nó kiểm tra path media, media bin, material ID, timeline ID và root/active mirrors. Mã thoát 0 không đồng nghĩa CapCut đã playback/export đúng; codec, motion, hình ảnh và âm thanh cần kiểm tra riêng. URL media bên ngoài được ghi là chưa xác minh.

Chạy regression checks của validator:

```powershell
python -m unittest discover -s tests -v
```

## Bên trong repo

```text
capcutedit-v1/
  SKILL.md
  agents/openai.yaml
  references/
    capcut-project.md
    design-and-sound.md
    delivery-and-cleanup.md
  scripts/validate_project.py
tests/test_validate_project.py
```

Đọc `SKILL.md` trước; agent chỉ nạp tài liệu chi tiết khi cần để tiết kiệm context/token. Cleanup là quy trình có kiểm tra tham chiếu và kế hoạch cụ thể, không có lệnh xóa tự động đi kèm.

## License

MIT cho code và hướng dẫn trong repo; xem [LICENSE](LICENSE). License này không cấp quyền với footage, âm thanh, font hoặc các ứng dụng bên ngoài.
