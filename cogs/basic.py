import discord
from discord.ext import commands

import json
import datetime
import time

class Basic(commands.Cog):

    def __init__(self, bot):
        # Load the config
        config = json.load(open('config/config.json'))

        # Set variables 'bot' and 'prefix'
        self.bot = bot
        self.prefix = config['prefix']

    # Define the help command
    @commands.command(
        name='help',
        description='Displays a help menu',
        aliases=['h']
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

    # Define the ping command
    @commands.command(
        name='ping',
        description='Calculates the bot ping (latency)',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        heartbeat = round(self.bot.latency * 1000)  # Get ping to Discord's Gateway

        a = round(time.time() * 1000)
        message: discord.Message = await ctx.send(':ping_pong: **Pinging...**')
        b = round(time.time() * 1000)
        # Gets the amount of time it takes to send a message
        elapsed = round(b - a)

        embed = discord.Embed(colour=discord.Color.gold(
        ), title=f":ping_pong: Pong!")

        embed.add_field(name="Ping",
                        value=f"{elapsed}ms")

        embed.add_field(name="API Heartbeat",
                        value=f"{heartbeat}ms")

        embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=str(
            ctx.author.avatar_url))  # Sets the footer of the embed

        await message.edit(content="", embed=embed)
        return


def setup(bot):
    bot.add_cog(Basic(bot))
