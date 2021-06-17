import discord, asyncio
from token_folder import token

class PinClient(discord.Client):
    async def on_ready(self):
        print('logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------')

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

    """
        how will i make this
        i think i'll hard code channels so that it'll be 
        sexy babeys exclusive bot

        so there will be a #pins channel 
        and there will be a command ..pin <message id>
        all the bot has to do is take the message contents and 
        send it in the pins channel, plus who it's from
        and a link to the original message below

        like 

        ZinkIThink: <message>
        <original message link>


        but i could see problems with the bot resending gifs
        or images/videos or emoji

        so let's take baby steps here and make a bot to re send
        a message first
    """

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        # # test method to make sure attachments/gifs work
        # if message.content.startswith('..resend'):
        #     # format: ..resend <message id>
        #     # first step is make sure there actually is a message id
        #     m_id = message.content.split()[1]
        #     msg = await message.channel.fetch_message(m_id)

        #     # get the list of attachments
        #     attachments = []

        #     # have to convert from type Attachemnt to type File for sending
        #     for attached in msg.attachments:
        #         attachments.append(await attached.to_file())

        #     # send it back
        #     await message.channel.send(msg.content, files=attachments)

        # if message.content.startswith('..send_embed'):
        #     embed = discord.Embed()
        #     embed.add_field(name="vaughn!:", value="""use embeds actually\n\n[message link]({})""".format(message.jump_url), inline=False)
        #     embed.set_image(url="https://media.discordapp.net/attachments/644752766736138241/855131201077248011/image0.png")
        #     embed.set_footer(text='sent in channel "' + message.channel.name + '"')
        #     await message.channel.send(embed=embed)

        # real deal right here
        if message.content.startswith('..pin'):
            m_id = message.content.split()[1]
            msg = await message.channel.fetch_message(m_id)

            attachment = None
            if len(msg.attachments) != 0:
                attachment = msg.attachments[0].url
            
            sending_msg = '''{}\n\n[message link]({})'''.format(msg.content, msg.jump_url)

            embed = discord.Embed()
            embed.add_field(name=msg.author.display_name, value=sending_msg)

            if attachment is not None:
                embed.set_image(url=attachment)
            
            embed.set_footer(text='sent in channel {}'.format(msg.channel.name))

            await self.pinning_channel.send(embed=embed)

client = PinClient()
client.run(token)