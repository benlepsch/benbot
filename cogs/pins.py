""" Pins (A Benbot Cog)

    This cog handles a pins channel, and adding to that channel

"""

import discord
from discord import app_commands
from discord.ext import commands
import os

GUILD = os.getenv('GUILD')
PINS_CHANNEL = os.getenv('PINS_CHANNEL')
YACHTS_CHANNEL = os.getenv('YACHTS_CHANNEL')

class Pins(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = bot.get_guild(int(GUILD))
        self.channel = self.guild.get_channel(int(PINS_CHANNEL))
        self.yachts = self.guild.get_channel(int(YACHTS_CHANNEL))
        self.pin_menu = app_commands.ContextMenu(
                name = "pin",
                callback=self.pin_ctx
            )
        self.bot.tree.add_command(self.pin_menu)
    
    async def pin_ctx(self, interaction: discord.Interaction, msg: discord.Message):
        
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
            await self.channel.send(embed=embed, files=f)
        elif len(attachments) == 1:
            embed.set_image(url=attachments[0])
            await self.channel.send(embed=embed)
        else:
            await self.channel.send(embed=embed)

        '''
            attachment.type = 'image/<png/jpeg/etc>' for images, 'video/<webm/mp4/etc>' for videos
        '''

        await interaction.response.send_message('ok')
    

async def setup(bot: commands.Bot):
  """ Sets up the cog

     Parameters
     -----------
     bot: commands.Bot
        The main cog runners commands.Bot object
  """
  await bot.add_cog(Pins(bot))
  print("[Pins]: Loaded")

  await bot.yachts.send('awake')