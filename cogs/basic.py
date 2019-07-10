import discord
from discord.ext import commands

import json


class Basic(commands.Cog):

    def __init__(self, bot):
        # Load the config
        config = json.load(open('config/config.json'))

        # Set variables 'bot' and 'prefix'
        self.bot = bot
        self.prefix = config['prefix']

    # Define a new command
    @commands.command(
        name='help',
        description='Displays a help menu',
        aliases=['p']
    )
    async def help_command(self, ctx):
        embed = discord.Embed(colour=discord.Color.gold(
        ), title=f"Help Menu", description=f"Hi, I'm a bot that generates Hypixel Rank Images!\n\nMy prefix currently is ``{self.prefix}``")

        embed.add_field(name="Basic Commands",
                        value="``help``, ``ping``, ``info``")

        embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=str(
            ctx.author.avatar_url))  # Sets the footer of the embed

        await ctx.send(embed=embed)
        return


def setup(bot):
    bot.add_cog(Basic(bot))
