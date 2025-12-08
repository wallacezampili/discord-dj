import yt_dlp

class Player:
    channel:str = None
    queue = []
    
    yt_dlp_opts = {
        'format': 'bestaudio/best'
    }
    
    def __init__(self):
        pass

    def add_to_queue(self, url: str):
        self.queue.append(url)
    