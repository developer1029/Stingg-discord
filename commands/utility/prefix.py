import discord
from discord.ext import commands

def get_prefix(bot, message):
    return custom_prefixes.get(message.guild.id, "!")

@commands.command(description="Set a custom prefix for this server.")
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, prefix: str):
    global custom_prefixes
    custom_prefixes[ctx.guild.id] = prefix
    embed = discord.Embed(title='Prefix changed', description=f"The custom prefix for this server has been changed to `{prefix}`.", color=discord.Color.green())
    embed.set_footer(text=f"Type `{prefix}help` for help commands.")
    await ctx.send(embed=embed)


custom_prefixes = {}
