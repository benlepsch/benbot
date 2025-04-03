# timer.py
# gives time delta from the time the command is run to the time specified in the command
# writing this because asher's bot sucks
from discord.ext import commands
import datetime as dt
from time import time

class Timer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # self.default_tz = 
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        
        if message.content.startswith('..tt'):
            # format should be something like
            # ..tt 4:30pm


            time_now = dt.datetime.fromtimestamp(time()) #, dt.timezone.utc)


async def setup(bot: commands.Bot):
  """ Sets up the cog

     Parameters
     -----------
     bot: commands.Bot
        The main cog runners commands.Bot object
  """
  await bot.add_cog(Timer(bot))
  print("[Timer]: Loaded")