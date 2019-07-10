import discord
from discord.ext import commands


class Reload(commands.Cog):

    def __init__(self, bot):
        # Set variables 'bot' and 'prefix'
        self.bot = bot

    # Define the help command
    @commands.command(
        name='reload',
        description='Reloads an extension',
        aliases=['r']
    )
    async def reload_command(self, ctx, arg):
        if ctx.author.id == 509078480655351820:
            try:
                self.bot.reload_extension(arg)
                embed = discord.Embed(colour=discord.Color.gold(
                ), title=f"Reload", description=f"Reloaded {arg}")

                embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=str(
                    ctx.author.avatar_url))  # Sets the footer of the embed

                return await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(colour=discord.Color.gold(
                ), title=f"Reload", description=f"Error whilst reloading: {arg}\n{e}")

                embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=str(
                    ctx.author.avatar_url))  # Sets the footer of the embed

                return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Reload(bot))
