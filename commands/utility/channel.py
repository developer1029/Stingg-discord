import discord
from discord.ext import commands

@commands.group(invoke_without_command=True, description="Manage server channels.")
async def channel(ctx):
    available_subcommands = [command.name for command in channel.commands]
    embed = discord.Embed(title='Available subcommands for `channel`', description="\n".join(available_subcommands), color=discord.Colour.blue())
    await ctx.send(embed=embed)

@channel.command(description="Deletes the current channel and creates a clone of it.")
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    channel = ctx.channel

    new_channel = await channel.clone(reason="Nuked!")
    await channel.delete(reason="Nuked!")

    await ctx.send(f"#{new_channel.mention} has been nuked! 💥💣")

@channel.command(description="Rename a specified channel.")
@commands.has_permissions(manage_channels=True)
async def rename(ctx, channel: discord.abc.GuildChannel, *, new_name):
    await channel.edit(name=new_name, reason="Channel rename")
    await ctx.channel.send(embed=discord.Embed(description=f'Channel renamed successfully to {channel.mention}.', color=discord.Color.blue()))

@channel.command(name='clone', description="Clone a specified channel.")
@commands.has_permissions(manage_channels=True)
async def clone(ctx, channel: discord.abc.GuildChannel):
    new_channel = await channel.clone(reason="Channel cloned")
    await ctx.send(f"{channel.mention} has been cloned to {new_channel.mention}.")
