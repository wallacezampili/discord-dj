import yt_dlp

ydl_opts = {
        'format': 'bestaudio/best',
    }

dp = yt_dlp.YoutubeDL(ydl_opts)
data = dp.extract_info("https://www.youtube.com/watch?v=1ewdQFdVHY8", download=True)

with open("a.json", mode="w") as f:
    import json
    json.dump(data, f, indent=4)

print(data['url'])

