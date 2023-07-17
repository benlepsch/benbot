# paprika.py
# auto sends paprika when theres a paprika
from discord.ext import commands
from random import randint

class Paprika(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.paprika_gifs = [
            'https://tenor.com/view/paprika-movie-anime-atsuko-chiba-satoshi-kon-gif-14134517',
            'https://tenor.com/view/paprika-gif-5430367',
            'https://tenor.com/view/paprika-gif-25394130',
            'https://tenor.com/view/paprika-paprika-anime-gif-10413276',
            'https://media.tenor.com/wxaaQuEOXQAAAAAC/anime-burger.gif'
        ]
        self.user = 873414777064542268

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.user:
            return

        if 'paprika' in message.content:
            await message.channel.send(self.paprika_gifs[randint(0, len(self.paprika_gifs)-1)])
        
        if message.content.startswith('..online'):
            await message.channel.send('pin bot online')
            
        if message.content.startswith('..riddle'):
            await message.channel.send('I end with ' + ' '.join(message.content.split(' ')[1:])[1:] + ' and start with ' + message.content.split(' ')[1][0] + '. What am I?')

        if randint(0, 12000) == 128:
            await message.channel.send('please kill me')
        
async def setup(bot: commands.Bot):
  """ Sets up the cog

     Parameters
     -----------
     bot: commands.Bot
        The main cog runners commands.Bot object
  """
  await bot.add_cog(Paprika(bot))
  print("[Paprika]: Loaded")