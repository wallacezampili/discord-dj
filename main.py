import discord
import interactions
from discord import Intents
from discord.ext import commands
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=Intents.all())

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



@bot.event
async def on_soundboard_sound_finish(sound):
    print(f'Sound {sound.name} has finished playing.')

# Command to sync application commands
@bot.command()
async def sync(ctx: discord.ext.commands.Context):
    await interactions.sync(bot, ctx)

# Hi
@bot.tree.command(name="hello", description="Says hello!")
async def hello(interaction):
    await interactions.hello(interaction)

@bot.tree.command(name="voice", description="Check voice channel connection")
async def voice(interaction):
    await interactions.con(interaction)

@bot.tree.command(name="play", description="play a song")
async def play(interaction, url: str):
    await interactions.play(interaction, url)

if __name__ == '__main__':
    bot.run(TOKEN)
