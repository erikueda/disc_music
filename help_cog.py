import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
comandos gerais:
!help, /h - Ajuda
!p <link> ou <nome da musica>- encontra a música no youtube e a reproduz em seu canal atual. Retomará a reprodução da música atual se ela estiver pausada
!q - mostra fila atual
!skip - pula a musica atual
!clear - para a musica e limpa a fila
!leave - chuta o bot do canal atual
!pause - pausa a musica
!resume - despausa a musica
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help",aliases=["h"], help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
