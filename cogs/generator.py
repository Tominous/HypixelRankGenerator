import discord
import json
import os
import re

from os import path
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont


class Generator(commands.Cog):

    def __init__(self, bot):
        # Load the config
        config = json.load(open('config/config.json'))

        # Load the ranks info
        ranks = json.load(open('config/ranks.json'))

        # Set variables 'bot' and 'config'
        self.bot = bot
        self.config = config
        self.ranks = ranks

    # Define the generate command
    @commands.command(
        name='generate',
        description='Generates a rank',
        aliases=['gen']
    )
    async def generate_command(self, ctx, arg: str):
        # Tell the user that we are generating the image
        message: discord.Message = await ctx.send(':arrows_counterclockwise: **Generating your rank...**')

        # Create a new Image with a transparent background
        if len(arg) <= 9:
            img = Image.new('RGBA', (100, 30), color=(255, 0, 0, 0))
        if len(arg) <= 15:
            img = Image.new('RGBA', (200, 30), color=(255, 0, 0, 0))
        else:
            # Delete the old message
            await message.delete()

            # Create an embed
            embed = discord.Embed(colour=discord.Color.red(
            ), title=f"Error!", description="Your rank is too long!\nMaximum Characters: 15")

            # Send a message
            return await ctx.send(embed=embed)

        # Rank Parsing
        pattern = re.compile(r"^\[.*\]")
        if pattern.match(arg):
             # Font Check
            if path.exists('./fonts/Minecraftia-Regular.ttf'):
                color = (255, 255, 0)
                fnt = ImageFont.truetype('./fonts/Minecraftia-Regular.ttf', 15)
                currentRank = None

                try:
                    currentRank = self.ranks[arg]
                except Exception as e:
                    print(e)
                    d = ImageDraw.Draw(img)
                    d.text((7, 5), f"{arg}", font=fnt, fill=color)

                if currentRank != None:
                    for key in currentRank:
                        d = ImageDraw.Draw(img)
                        d.text((key['pos'][0], key['pos'][1]), f"{key['text']}",
                               font=fnt, fill=(key['color'][0], key['color'][1], key['color'][2]))
                else:
                    # Delete the old message
                    await message.delete()

                    # Create an embed
                    embed = discord.Embed(colour=discord.Color.red(
                    ), title=f"Error!", description="An unknown error occured while generating your rank!")

                    # Send a message
                    return await ctx.send(embed=embed)
            else:
                # Delete the old message
                await message.delete()

                # Create an embed
                embed = discord.Embed(colour=discord.Color.red(
                ), title=f"Error!", description="An error occured while generating your rank\nError: ``The file in: ./fonts/Minecraftia-Regular.ttf`` does not exist!")

                # Send a message
                return await ctx.send(embed=embed)

            # Save the image
            img.save('temp/generated_img.png')

            # Delete the old message
            await message.delete()

            # Create a discord instance of the image
            file = discord.File('temp/generated_img.png')

            # Create an embed
            embed = discord.Embed(
                colour=discord.Color.gold(), title=f"Here's your image")
            embed.set_image(url='attachment://generated_img.png')

            # Send a message with the embed and the file
            return await ctx.send(embed=embed, file=file)
        else:
            # Delete the old message
            await message.delete()

            # Create an embed
            embed = discord.Embed(colour=discord.Color.red(
            ), title=f"Error!", description="Your argument does not match the required format!\nExample: ``[MVP+]``")

            # Send a message
            return await ctx.send(embed=embed)

    @generate_command.error
    async def generate_error(self, ctx, err):
        if isinstance(err, commands.errors.MissingRequiredArgument):
            # Create an embed
            embed = discord.Embed(colour=discord.Color.red(
            ), title=f"Error!", description="You need to supply an argument!\nExample: ``[MVP+]``")

            # Send a message
            return await ctx.send(embed=embed)
        else:
            print(err)
            # Create an embed
            embed = discord.Embed(colour=discord.Color.red(
            ), title=f"Error!", description=f"An unknown error occured!\n{err}")

            # Send a message
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Generator(bot))
