import yt_dlp

def validate_url(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {'valid': True, 'duration': info.get('duration', 0)}
    except Exception as e:
        return {'valid': False, 'error': str(e)}