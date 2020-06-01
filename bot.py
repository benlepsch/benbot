import discord, asyncio
from token_folder import token

class SwagBot(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        # for talking :)
        # i checked none of these are already defined
        self.selected_server = None
        self.channels = []
        self.selected_channel = None

        f = open('selected.txt')
        data = f.read().split('\n')
        print(data)
        g = data[0]
        c = data[1]

        for guild in self.guilds:
            if guild.name == g:
                self.selected_server = guild
                for channel in guild.channels:
                    if type(channel) is discord.TextChannel and channel.name == c:
                        self.selected_channel = channel
                        break
                break

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
                print('bruh u gotsta select a guild first')
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
                print('cnat select by name if u dont select da server')
            else:
                cname = inp[15:]
                for channel in self.selected_server.channels:
                    if channel.name == cname:
                        self.selected_channel = channel
                
                if not self.selected_channel:
                    print('couldnt find channel wit dat name')
                else:
                    print('selected channel {}'.format(self.selected_channel))


        if inp[0:3] == 'msg':
            if not self.selected_channel:
                print('idiot u dont have channel select')
            else:
                sending = inp[4:]
                if len(sending) > 2000:
                    print('idiot cant send over 2k characters')
                else:
                    await self.selected_channel.send(sending)
        
        await self.getInput()

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return


swagger = SwagBot()
swagger.run(token)
