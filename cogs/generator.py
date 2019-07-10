import discord
import json

from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

class Generator(commands.Cog):

    def __init__(self, bot):
        # Load the config
        config = json.load(open('config/config.json'))

        # Set variables 'bot' and 'config'
        self.bot = bot
        self.config = config

    # Define the generate command
    @commands.command(
        name='generate',
        description='Generates a rank',
        aliases=['gen']
    )
    async def generate_command(self, ctx):
        # Code
        return

def setup(bot):
    bot.add_cog(Generator(bot))
