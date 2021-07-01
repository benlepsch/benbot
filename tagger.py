import discord, asyncio
from token_folder import token

'''
    I have two discord accounts, one for my computer, one for my phone
    this is so that i can use my phone camera while in call
    but if someone only tags one of them, i might not see it
    so im making this bot to help with that

    in addition, if i dm benbot on desktop acct, it'll forward to phone
    and vice versa
'''

class TagClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        self.tag_one = '<@!262637906865291264>'
        self.tag_two = '<@!490706151176929294>'

        self.id_one = '262637906865291264'
        self.id_two = '490706151176929294'

        self.guild_name = 'sexy babeys'
        for guild in self.guilds:
            if guild.name == self.guild_name:
                self.sexy_babeys = guild

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if self.tag_one in message.content and not self.tag_two in message.content:
            await message.channel.send(self.tag_two + ' ^')
        
        if self.tag_two in message.content and not self.tag_one in message.content:
            await message.channel.send(self.tag_one + ' ^')
        
        # i use message.author.send(msg)

        if isinstance(message.channel, discord.DMChannel):

            mauth_id = ''.join([i for i in list(message.author.mention) if i.isdigit()])

            if mauth_id == self.id_one:
                # send message content to tag two acct
                # how do i get the tag two user?
                sending = await self.sexy_babeys.fetch_member(self.id_two)
                await sending.send(message.content) 

            if mauth_id == self.id_two:
                # send to tag one acct
                sending = await self.sexy_babeys.fetch_member(self.id_one)
                await sending.send(message.content) 

client = TagClient()
client.run(token)