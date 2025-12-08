from discord import Interaction, FFmpegPCMAudio
from discord.ext.commands import Bot, Context


def get_ytb_info(url: str):
    import yt_dlp

    ydl_opts = {
        'format': 'bestaudio/best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info




async def sync(bot: Bot, ctx: Context):
    await bot.tree.sync()
    await ctx.send("Commands synced!")

async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello there!")

async def con(interaction: Interaction):
    voice = interaction.user.voice
    if voice:
        vc = await voice.channel.connect()  # <-- ESSA LINHA FAZ TODA A DIFERENÇA
        await interaction.response.send_message(f"Connected to {voice.channel.name}")
    else:
        await interaction.response.send_message("You are not connected to a voice channel.")


async def play(interaction: Interaction, url: str):
    voice_channel = interaction.guild.voice_client

    if voice_channel is None:
        return await interaction.response.send_message("Bot is not connected to a voice channel.")
    
    info = get_ytb_info(url)["url"]
    audio_source = FFmpegPCMAudio(info, executable="ffmpeg")
    interaction.guild.voice_client.play(audio_source)
    await interaction.response.send_message(f"Playing: {url}")




    