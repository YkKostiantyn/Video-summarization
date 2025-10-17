import os
import yt_dlp
import subprocess
from utils.file_utils import remove_file

def downl_extract_audio(url, filename = "audio.wav"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.dirname(current_dir)
    out_dir = os.path.join(package_dir, "uploads")

    temp_video = os.path.join(out_dir, "temp_video.mp4")
    out_audio = os.path.join(out_dir, filename)

    ydl_opts = {
        'format' : 'bestaudio/best',
        'outtmpl' : temp_video
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    subprocess.run([
        "ffmpeg",  "-y", "-i", temp_video, "-vn", "-acodec", "pcm_s16le", out_audio
    ])

    remove_file(temp_video)

    return out_audio