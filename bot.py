import discord, asyncio, urllib.request
from token_folder import token

class SwagBot(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        game = discord.Game('ballin\'')
        await swagger.change_presence(status=discord.Status.online, activity=game)

     
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

swagger = SwagBot()
swagger.run(token)
