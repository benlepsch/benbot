import discord, asyncio
from token_folder import token

'''
    I have two discord accounts, one for my computer, one for my phone
    this is so that i can use my phone camera while in call
    but if someone only tags one of them, i might not see it
    so im making this bot to help with that
'''

class TagClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        self.tag_one = '<@!262637906865291264>'
        self.tag_two = '<@!490706151176929294>'

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if self.tag_one in message.content and not self.tag_two in message.content:
            await message.channel.send(self.tag_two + ' ^')
        
        if self.tag_two in message.content and not self.tag_one in message.content:
            await message.channel.send(self.tag_one + ' ^')

client = TagClient()
client.run(token)