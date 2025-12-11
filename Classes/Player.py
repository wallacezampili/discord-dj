from discord import VoiceClient

class Player:
    voice_channels = {}
    queue = []

    yt_dlp_opts = {
        'format': 'bestaudio/best'
    }
    
    def __init__(self):
        pass

    def add_to_queue(self, url: str):
        self.queue.append(url)
    
    def add_channel(self, vc: VoiceClient, guild_id: int):
        self.voice_channels[guild_id] = vc
    

    def get_channel(self, guild_id: int) -> VoiceClient | None:

        if(guild_id in self.voice_channels):
            return self.voice_channels[guild_id]
        else: 
            print("SOBROU NADA PARA O BETA!")
            return None