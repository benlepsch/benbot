import discord, asyncio, requests
from token_folder import token

class Echo(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

        # this works but discord limits the amount of times you can change pfp
        # pfp = open('original_pfp.png','rb')
        # byte = pfp.read()
        # pfp.close()
        # await echo.user.edit(password=None,avatar=byte)

        game = discord.Game('VALORANT')
        await echo.change_presence(status=discord.Status.online, activity=game)
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        

        # "echo" imitates a person on the server, copying their role, nickname, and status

        # first unecho if it was already copying someone
        if message.content.startswith('echo'):
            for role in message.author.guild.me.roles:
               if role.name != 'not spam bot' and role.name != '@everyone':
                   await role.edit(name='BenBot', colour=discord.Colour(5).lighter_grey(), hoist=False)
                   await message.author.guild.me.edit(nick='BenBot')

            # get the member it's copying from the message
            copying = message.content.split()[1]
            copying = int(copying[3:len(copying)-1])
            guild = message.author.guild
            me = guild.me
            copying = guild.get_member(copying)
            
            # change nickname
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

            if not tr == None:
                # edit the "benbot" role in the server to be the name/colour of the person im echoing
                for role in me.roles:
                    if role.name != 'not spam bot' and role.name != '@everyone':
                        await role.edit(name=tr.name, colour=tr.colour)
                        await role.edit(hoist=True)
                        break
            
            # next
            # GET PROFILE PICTURE
            # this is insane
            # this also doesnt work

            # url = copying.avatar_url
            # with open('profile.jpg', 'wb') as handle:
            #     response = requests.get(url, stream=True)

            #     if not response.ok:
            #         print(response)

            #     for block in response.iter_content(1024):
            #         if not block:
            #             break

            #         handle.write(block)
            # pic = open('profile.jpg','rb')
            # b = pic.read()
            # pic.close()
            # await echo.user.edit(password=None, avatar=pic)

        if message.content.startswith('unecho'):
           for role in message.author.guild.me.roles:
               if role.name != 'not spam bot' and role.name != '@everyone':
                    await role.edit(name='BenBot', colour=discord.Colour(5).lighter_grey(), hoist=False)
                    await message.author.guild.me.edit(nick='BenBot')
                    pfp = open('original_pfp.png','rb')
                    byte = pfp.read()
                    pfp.close()

                    try:
                        await echo.user.edit(password=None,avatar=byte)
                    except:
                        await message.channel.send('cant chagne profile pic right now :(')


            

echo = Echo()
echo.run(token)