import discord, asyncio
from token_folder import token

class Echo(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        game = discord.Game('VALORANT')
        await echo.change_presence(status=discord.Status.online, activity=game)
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        

        # "echo" imitates a person on the server, copying their role, nickname, and status
        if message.content.startswith('echo'):
            for role in message.author.guild.me.roles:
               if role.name != 'not spam bot' and role.name != '@everyone':
                   await role.edit(name='BenBot', colour=discord.Colour(5).lighter_grey(), hoist=False)
                   await message.author.guild.me.edit(nick='BenBot')

            copying = message.content.split()[1]
            copying = int(copying[3:len(copying)-1]) # id of person tagged in the command
            guild = message.author.guild
            me = guild.me

            copying = guild.get_member(copying)
            await me.edit(nick=copying.display_name)
            
            # get every role that the person i'm copying has that is visible in the sidebar and sort them to determine which to copy
            hoists = []
            for role in copying.roles:
                if role.hoist:
                    hoists.append(role)
            
            top = 0
            tr = None
            for role in hoists:
                if role.position > top:
                    top = role.position
                    tr = role

            # edit the "benbot" role in the server to be the name/colour of the person im echoing
            for role in me.roles:
                if role.name != 'not spam bot' and role.name != '@everyone':
                    await role.edit(name=tr.name, colour=tr.colour)
                    await role.edit(hoist=True)
                    break

        if message.content.startswith('unecho'):
           for role in message.author.guild.me.roles:
               if role.name != 'not spam bot' and role.name != '@everyone':
                   await role.edit(name='BenBot', colour=discord.Colour(5).lighter_grey(), hoist=False)
                   await message.author.guild.me.edit(nick='BenBot')


            

echo = Echo()
echo.run(token)