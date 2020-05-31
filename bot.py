import discord, asyncio, urllib.request
from token_folder import token

class SwagBot(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        game = discord.Game('VALORANT')
        await swagger.change_presence(status=discord.Status.online, activity=game)

        # for talking :)
        # i checked none of these are already defined
        self.selected_server = None
        self.channels = []
        self.selected_channel = None
        #print(self.guilds)

        await self.getInput()

    async def getInput(self):
        inp = input('> ')

        if inp == 'show guilds':
            for g in self.guilds:
                print(g.name)
        
        if inp[0:12] == 'select guild':
            pass

        if inp == 'show channels':
            if self.selected_server == None:
                print('bruh u gotsta select a guild first')
            else:
                pass
        
        if inp[0:14] == 'select channel':
            pass

        if inp[0:3] == 'msg':
            if self.selected_channel == None:
                print('idiot u dont have channel select')
            else:
                pass
        
        await self.getInput()

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return


swagger = SwagBot()
swagger.run(token)
