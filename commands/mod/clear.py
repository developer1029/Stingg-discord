import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount <= 0:
        await ctx.send(embed=discord.Embed(description="Please provide a valid number of messages to clear.", color=discord.Color.red()))
        return

    messages = []
    async for message in ctx.channel.history(limit=amount + 1):
        messages.append(message)

    await ctx.channel.delete_messages(messages)

    response = discord.Embed(description=f"Cleared {amount} messages in this channel.", color=discord.Color.red())
    await ctx.send(response, delete_after=5)