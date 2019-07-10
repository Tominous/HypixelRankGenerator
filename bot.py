from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

import discord
import json
import logging

# Load the config file
config = json.load(open('config/config.json'))

# Get the bot prefix
prefix = config["prefix"]

# Initialize the bot
bot: commands.Bot = commands.Bot(
    command_prefix=prefix, status=discord.Status.online, activity=discord.Game(name='Loading...'))

# Remove the default help command so that we can use our own
bot.remove_command("help")

# Set the logging level to INFO
logging.basicConfig(level=logging.INFO)

# List of Cogs
cogs = ['cogs.basic']


@bot.event
async def on_ready():
    # Get number of members
    members = 0
    for guild in bot.guilds:
        members = members + guild.member_count

    # Log bot info
    logging.info('----------------------')
    logging.info(f'Logged in as {bot.user}')
    logging.info(f'ID: {bot.user.id}')
    logging.info(f'Guilds: {len(bot.guilds)}')
    logging.info(f'Members: {members:,d}')
    logging.info('----------------------')

    # Load Cogs
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f"Error while loading cogs: {e}")

    # Change presnce
    await bot.change_presence(activity=discord.Game(name=f'Providing rank images for {members:,d} users | {prefix} help'))

bot.run(config['token'])
