import asyncio, discord
from discord.ext import commands


def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)

@commands.command(name='join', description='Connects the bot to a voice channel.')
@is_admin()
async def join(ctx, channel: discord.VoiceChannel = None):
    if channel is None and ctx.author.voice:
        channel = ctx.author.voice.channel
    elif channel is None and not ctx.author.voice:
        embed = discord.Embed(description="You are not connected to any voice channel.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return

    voice_client = ctx.guild.voice_client

    if voice_client is None:
        await channel.connect()
        embed = discord.Embed(description=f"Connected to {channel.mention}", color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        await voice_client.move_to(channel)
        embed = discord.Embed(description=f"Moved to {channel.mention}", color=discord.Color.green())
        await ctx.send(embed=embed)



@commands.command(name='leave', description='Disconnects the bot from voice channel.')
@is_admin()
async def leave(ctx):
    voice_client = ctx.guild.voice_client

    if voice_client:
        await voice_client.disconnect()
        embed = discord.Embed(description="Left the voice channel.", color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="Not connected to any voice channel.", color=discord.Color.red())
        await ctx.send(embed=embed)


@commands.command(name='vcc', description='Counts the users in a specified voice channel.')
@is_admin()
async def vcc(ctx, channel_id: int):
    voice_channel = ctx.guild.get_channel(channel_id)
    if not voice_channel:
        embed = discord.Embed(description=":x: I couldn't find a voice channel with that ID.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return

    num_users = len(voice_channel.members)
    num_bots = len([m for m in voice_channel.members if m.bot])
    num_humans = num_users - num_bots

    embed = discord.Embed(description=f"There are **{num_humans} humans** and **{num_bots} bots** in **{voice_channel.name}**.", color=discord.Color.green())
    await ctx.send(embed=embed)