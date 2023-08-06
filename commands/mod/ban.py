import discord
from discord.ext import commands

def create_embed(title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

@commands.command(description="Ban a user from the server.")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    if ctx.author.top_role <= user.top_role:
        embed = create_embed("Permission Error", "You don't have the required permissions to ban this user.", discord.Color.red())
        await ctx.send(embed=embed)
        return

    try:
        await user.send(f"You have been banned from {ctx.guild.name}. Reason: {reason}")
    except discord.Forbidden:
        pass

    await ctx.guild.ban(user, reason=reason)
    embed = create_embed("User Banned", f"{user.name} has been banned from the server.", discord.Color.green())
    await ctx.send(embed=embed)
