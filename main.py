import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog




intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
"""
my_files = ["music_cog.py", "help_cog.py"]
async def load_extensions():
    for file in my_files:
        await bot.load_extension(f"cogs.{file[:-3]}")"""


#start the bot with our token
bot.run("TOKEN")