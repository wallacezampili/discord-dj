from Classes.Player import Player
from discord import Interaction, FFmpegPCMAudio
from discord.ext.commands import Bot, Context
import yt_dlp





async def try_to_connect_voice(interaction: Interaction, player: Player):
    voice = interaction.user.voice
    print(interaction.user.voice)
    
    if voice and interaction.guild.voice_client == None:
        vc = await voice.channel.connect()
        player.add_channel(vc, interaction.guild.id)
        return True
    
    elif voice and interaction.guild.voice_client != None: 
        await interaction.guild.voice_client.disconnect()
        vc = await voice.channel.connect()
        player.add_channel(vc, interaction.guild.id)
        return True
    else:
       await interaction.response.send_message("You are not connected to a voice channel.")
       return False
    
async def sync(bot: Bot, ctx: Context):
    await bot.tree.sync()
    await ctx.send("Commands synced!")

async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello there!")

# async def con(interaction: Interaction):
#     voice = interaction.user.voice
#     if voice:
#         vc = await voice.channel.connect()  # <-- ESSA LINHA FAZ TODA A DIFERENÇA
#         await interaction.response.send_message(f"Connected to {voice.channel.name}")
#     else:
#         await interaction.response.send_message("You are not connected to a voice channel.")


async def play(interaction: Interaction, url: str, player: Player):
    
    import pathlib

    path = pathlib.Path("./a2.webm")
    if not path.exists():
        raise ValueError("Uh oh!!")

    is_in_voice_channel = await try_to_connect_voice(interaction, player)
    
    if not is_in_voice_channel:
        return

    voice_channel = player.get_channel(interaction.guild.id)


    url = "https://rr2---sn-pouxgoxm5-bpbl.googlevideo.com/videoplayback?expire=1765569769&ei=iSA8adfXMpmPobIP2bWRmQg&ip=201.33.185.86&id=o-AJoC2oiWxvD5FmXKOjNMickpSux7qJw4E0A8Z0xhqseO&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=0&met=1765548169%2C&mh=zV&mm=31%2C29&mn=sn-pouxgoxm5-bpbl%2Csn-gpv7kn76&ms=au%2Crdu&mv=m&mvi=2&pl=24&rms=au%2Cau&initcwndbps=1616250&bui=AYUSA3B78vc10NCko-jOpg0mkoYXZNA1d0WXq6nWPQGwBXHBNupv3mtHmR9RleVO6RIZOgyB5DMO8g9Z&spc=wH4QqwsRyzO4&vprv=1&svpuc=1&mime=audio%2Fwebm&rqh=1&gir=yes&clen=191186&dur=10.021&lmt=1741510597012606&mt=1765543507&fvip=5&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=6208224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhAI3y06SjF-kvGdoCLnZbBEuWcqrNDraY_MzHYCSj8XrpAiEA2o5JAtwKdhhAhjZD4zK0WaPjuLTH5DJK36p353GyfXk%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRAIgGTrSzQzgM1ZFf7Hb59N1BfDgbIiSY4qO9MoX6ZwZ8DECIHO26iM7EnTgkNqC9r9W6jUZ8IlKW3D9Ub7iKjpAIxZS"
    #url = data['url']
    ffmpeg_options = {'options':'-vn', 'executable': 'ffmpeg'}
    audio_source = FFmpegPCMAudio(url, **ffmpeg_options)
    
    await interaction.response.send_message(f"Playing: {url}")

    voice_channel.play(audio_source)

    #await interaction.response.send_message(f"Playing: {url}")




    