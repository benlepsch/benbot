""" Benbot
By Ben Lepsch
Revised, re-revised, peer reviewed, and ultimately shamed by Vaughn Woerpel

"mer your mn saskek yiolc"
- a wise hermit
"""
import discord
from discord.ext import commands
import os

class Benbot(commands.Bot):
    def __init__(self, *args, **kwargs):
        """Initialize the bot class"""
        super().__init__(*args, **kwargs)

    async def load_extensions(self) -> None:
        """Load all cogs by walking the packages in exts."""
        print("Loading extensions")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await client.load_extension(f"cogs.{filename[:-3]}")
        print("Extensions loaded")

    async def sync_app_commands(self) -> None:
        """Sync the command tree to the guild"""
        await self.tree.sync()
        await self.tree.sync(guild=discord.Object(os.getenv('GUILD')))

        print("Command tree synced")

    async def setup_hook(self) -> None:
        """Replacing default setup_hook to run on startup"""
        await self.load_extensions()
        await self.sync_app_commands()
        game = discord.Game('Marvel Rivals')
        await self.change_presence(status=discord.Status.online, activity=game)

        print("[Benbot]: Loaded")


if __name__ == "__main__":
    intents = discord.Intents.all()
    client = Benbot(command_prefix="_", intents=intents)
    client.run(os.getenv('DISCORD_TOKEN'))
