import discord, asyncio
import urllib.request
from token_folder import token

class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        game = discord.Game('nitro boosting')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
            
        if message.content.startswith('..getip'):
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            await message.author.send('public ip: ' + external_ip)

        if message.content.startswith('..mention'):
            print(message.author.mention)
client = MyClient()
client.run(token)