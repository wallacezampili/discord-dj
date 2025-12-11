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
    
    elif voice and interaction.guild.voice_client != None: 
        await interaction.guild.voice_client.disconnect()
        vc = await voice.channel.connect()
        player.add_channel(vc, interaction.guild.id)
    else:
        interaction.response.send_message("You are not connected to a voice channel.")
    
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
    
    await try_to_connect_voice(interaction, player)
    
    voice_channel = player.get_channel(interaction.guild.id)


    
    #url = data['url']
    ffmpeg_options = {'options':'-vn', 'executable': 'ffmpeg'}
    audio_source = FFmpegPCMAudio("../a.webm", **ffmpeg_options)
    
    await interaction.response.send_message(f"Playing: {url}")

    voice_channel.play(audio_source)

    # await interaction.response.send_message(f"Playing: {url}")




    