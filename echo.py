import discord, asyncio
from token_folder import token

class Echo(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        f = open('oldrole.txt')
        z = f.read().split('\n')
        if z[0]:
            pass # cleanse old role
        f.close()

        #for guild in self.guilds:
        #    await guild.me.edit(nick='BenBot')

        game = discord.Game('VALORANT')
        await echo.change_presence(status=discord.Status.online, activity=game)
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        try:
            await self.nr.delete()
        except:
            pass

        # "echo" imitates a person on the server, copying their role, nickname, and status
        if message.content.startswith('echo'):
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

            # make a new role with the same color/name as the top role
            # i dont assign the same role because for some reason i got permissions errors when i did that 
            # despite giving the bot "manage roles" permission idk
            await guild.create_role(name=tr.name,colour=tr.colour,hoist=True)
            allroles = guild.roles
            latest = allroles[0].created_at
            for role in allroles:
                if role.created_at > latest:
                    latest = role.created_at
                    self.nr = role
            await me.add_roles(self.nr)
            self.echoed = guild.name

        if message.content.startswith('unecho'):
            if self.nr:
                if self.echoed == message.author.guild.name:
                    # this errors but works anyway so im leaving it
                    await message.author.guild.me.edit(nick='BenBot')
                    await self.nr.delete()
                    

            

echo = Echo()
echo.run(token)