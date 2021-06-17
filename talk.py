import discord, asyncio
from token_folder import token

class MsgClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------------')

        self.selected_server = None
        self.channels = []
        self.selected_channel = None

        await self.getInput()
    
    async def getInput(self):
        inp = input('> ')

        if inp == 'show guilds':
            for g in self.guilds:
                print(g.name)
        
        if inp[0:12] == 'select guild':
            gname = inp[13:]
            for g in self.guilds:
                if g.name == gname:
                    self.selected_server = g
            
            if not self.selected_server:
                print('no guild with that name')
            else:
                print('selected guild:')
                print(self.selected_server)

        if inp == 'show channels':
            if not self.selected_server:
                print('no guild selected')
            else:
                txts = []
                voice = []
                category = []
                for channel in self.selected_server.channels:   
                    if type(channel) is discord.CategoryChannel:
                        category.append(channel)
                    if type(channel) is discord.TextChannel:
                        txts.append(channel)
                    if type(channel) is discord.VoiceChannel:
                        voice.append(channel)
                print('text channels:')
                for txt in txts:
                    print(txt.name + '\t|\t' + str(txt.id))
        
        if inp[0:14] == 'select channel':
            if not self.selected_server:
                print('no guild selected')
            else:
                cname = inp[15:]
                for channel in self.selected_server.channels:
                    if channel.name == cname:
                        self.selected_channel = channel
            
                if not self.selected_channel:
                    print('no channel with that name')
                else:
                    print('selected channel:')
                    print(self.selected_channel)

        if inp[0:3] == 'msg':
            if not self.selected_channel:
                print('no channel selected')
            else:
                sending = inp[4:]
                if len(sending) > 2000:
                    print('too many characters')
                else:
                    await self.selected_channel.send(sending)
        
        await self.getInput()
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

client = MsgClient()
client.run(token)