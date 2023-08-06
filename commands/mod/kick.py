import discord
from discord.ext import commands

@commands.command(description="Kick a user from the server and send them a DM.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason="No reason provided."):
    try:
        await user.send(f"You have been kicked from the server {ctx.guild.name} for the following reason: {reason}")
        await ctx.guild.kick(user, reason=reason)
        embed = discord.Embed(title="Kick User", description=f"{user.name} has been kicked from the server.", color=discord.Color.green())
        await ctx.send(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(title="Kick User", description="I couldn't send a DM to the user. They have been kicked, but I don't have permission to DM them.", color=discord.Color.orange())
        await ctx.send(embed=embed)
    except discord.NotFound:
        embed = discord.Embed(title="Kick User", description="User not found.", color=discord.Color.red())
        await ctx.send(embed=embed)
