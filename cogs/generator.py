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

        # Set variables 'bot' and 'config'
        self.bot = bot
        self.config = config

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
                if arg == '[MVP+]':
                    color = (0, 255, 255)
                    # Write text to the image we created
                    fnt = ImageFont.truetype(
                        './fonts/Minecraftia-Regular.ttf', 15)
                    d = ImageDraw.Draw(img)
                    d.text((7, 5), f"[MVP", font=fnt, fill=color)
                    d.text((46, 3), f"+", font=fnt, fill=(255, 77, 77))
                    d.text((55, 5), f"]", font=fnt, fill=color)
                else:
                    if arg == '[MVP++]':
                        color = (255, 255, 0)
                        # Write text to the image we created
                        fnt = ImageFont.truetype(
                            './fonts/Minecraftia-Regular.ttf', 15)
                        d = ImageDraw.Draw(img)
                        d.text((7, 5), f"[MVP", font=fnt, fill=color)
                        d.text((46, 3), f"++", font=fnt, fill=(255, 77, 77))
                        d.text((65, 5), f"]", font=fnt, fill=color)
                    else:
                        if arg == '[VIP+]':
                            color = (120, 187, 55)
                            # Write text to the image we created
                            fnt = ImageFont.truetype(
                                './fonts/Minecraftia-Regular.ttf', 15)
                            d = ImageDraw.Draw(img)
                            d.text((7, 5), f"[VIP", font=fnt, fill=color)
                            d.text((46, 3), f"+", font=fnt,
                                   fill=(255, 255, 255))
                            d.text((55, 5), f"]", font=fnt, fill=color)
                        else:
                            if arg == '[VIP]':
                                color = (120, 187, 55)
                                # Write text to the image we created
                                fnt = ImageFont.truetype(
                                    './fonts/Minecraftia-Regular.ttf', 15)
                                d = ImageDraw.Draw(img)
                                d.text((7, 5), f"[VIP]",
                                       font=fnt, fill=color)
                            else:
                                if arg == '[MVP]':
                                    color = (0, 255, 255)
                                    # Write text to the image we created
                                    fnt = ImageFont.truetype(
                                        './fonts/Minecraftia-Regular.ttf', 15)
                                    d = ImageDraw.Draw(img)
                                    d.text((7, 5), f"[MVP]",
                                           font=fnt, fill=color)
                                else:
                                    fnt = ImageFont.truetype(
                                        './fonts/Minecraftia-Regular.ttf', 15)
                                    d = ImageDraw.Draw(img)
                                    d.text((7, 5), f"{arg}",
                                           font=fnt, fill=color)
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
            # Create an embed
            embed = discord.Embed(colour=discord.Color.red(
            ), title=f"Error!", description=f"An unknown error occured!\n{err}")

            # Send a message
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Generator(bot))
