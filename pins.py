import discord, asyncio
from token_folder import token

class PinClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

        game = discord.Game('League of Legends')
        await client.change_presence(status=discord.Status.online, activity=game)
        
        self.pinning_channel_id = 855127902416273468
        self.guild_name = 'sexy babeys'

        for g in self.guilds:
            if g.name == self.guild_name:
                self.pinning_guild = g
                break
        

        for c in self.pinning_guild.channels:
            if c.id == self.pinning_channel_id:
                self.pinning_channel = c
                break

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('..online'):
            await message.channel.send('pin bot online')
        
        if message.content.startswith('..riddle'):
            await message.channel.send('I end with ' + message.content[1:] + ' and start with ' + message.content[0] + '. What am I?')

        if message.content.startswith('..pin'):
            # fetch message from id
            m_id = message.content.split()[1]
            msg = await message.channel.fetch_message(m_id)

            # grab attachments
            attachments = []
            a_type = 'none'
            if len(msg.attachments) == 1:
                attachments.append(msg.attachments[0])
                a_type = attachments[0].content_type.split('/')[0]
            elif len(msg.attachments) >= 2:
                for a in msg.attachments:
                    attachments.append(a)
                    if a.content_type.split('/')[0] == 'video':
                        a_type = 'video'

            sending_msg = '''{}\n\n[message link]({})'''.format(msg.content, msg.jump_url)

            embed = discord.Embed()
            embed.add_field(name=msg.author.display_name, value=sending_msg)
            embed.set_footer(text='sent in channel {}'.format(msg.channel.name))

            if len(attachments) >= 2 or a_type == 'video':
                f = []
                print(attachments)
                for a in attachments:
                    f.append(await a.to_file())
                print(f)
                await self.pinning_channel.send(embed=embed, files=f)
            elif len(attachments) == 1:
                embed.set_image(url=attachments[0])
                await self.pinning_channel.send(embed=embed)
            else:
                await self.pinning_channel.send(embed=embed)
        
        '''
            attachment.type = 'image/<png/jpeg/etc>' for images, 'video/<webm/mp4/etc>' for videos
        '''

client = PinClient()
client.run(token)
