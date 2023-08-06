import discord
from discord.ext import commands

async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Please check the command usage.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bad argument. Please provide a valid argument.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

async def on_error(event, *args, **kwargs):
    # Handle generic errors here
    print(f"An error occurred in {event}: {args[0]}")
