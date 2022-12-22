from config import token, guild

import discord
from discord import app_commands
import asyncio

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync(guild = discord.Object(id=guild))
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.context_menu(name='pin', guild=discord.Object(id=guild))
async def pin(interaction: discord.Interaction, msg: discord.Message):
    pc = client.get_channel(855127902416273468)
    
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
        await pc.send(embed=embed, files=f)
    elif len(attachments) == 1:
        embed.set_image(url=attachments[0])
        await pc.send(embed=embed)
    else:
        await pc.send(embed=embed)

    '''
        attachment.type = 'image/<png/jpeg/etc>' for images, 'video/<webm/mp4/etc>' for videos
    '''

    await interaction.response.send_message('ok')

client.run(token)