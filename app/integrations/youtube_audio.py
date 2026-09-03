import os
import tempfile
from typing import Any, cast
import yt_dlp


class YouTubeAudioDownloader:
    def download(self, video_id: str) -> str:
        temp_dir = tempfile.mkdtemp()

        output_template = os.path.join(
            temp_dir,
            f"{video_id}.%(ext)s",
        )

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "noplaylist": True,
        }

        url = f"https://www.youtube.com/watch?v={video_id}"

        with yt_dlp.YoutubeDL(cast(Any, ydl_opts)) as ydl:
            info = ydl.extract_info(
                url,
                download=True,
            )

            downloaded_file = ydl.prepare_filename(info)

        return downloaded_file
