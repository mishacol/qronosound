import yt_dlp
import os

def fetch_audio(url, format):
    try:
        ydl_opts = {
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format,
                'preferredquality': '192',
            }],
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return {
                'status': 'success',
                'title': info.get('title'),
                'file_path': f"downloads/{info['title']}.{format}"
            }
    except Exception as e:
        return {'status': 'error', 'error': str(e)}