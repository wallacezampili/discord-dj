import yt_dlp

ydl_opts = {
        'format': 'bestaudio/best',
    }

dp = yt_dlp.YoutubeDL(ydl_opts)
data = dp.extract_info("https://www.youtube.com/watch?v=dQw4w9WgXcQ", download=True)

