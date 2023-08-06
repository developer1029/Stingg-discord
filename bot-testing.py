import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

user_help_map = {}  # To keep track of users using !help

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(pass_context=True)
async def help(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        user_help_map[ctx.author.id] = ""
        await ctx.send("Start typing your message.")
    else:
        await ctx.send("nahi manunga")

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        if message.author.id in user_help_map:
            if user_help_map[message.author.id] == "":
                user_help_map[message.author.id] = message.content
                await message.channel.send("Message saved. Now sending it to the specified channel.")
                target_channel_id = 1136706832606445660  # Replace with the actual channel ID
                channel = bot.get_channel(target_channel_id)
                if channel is not None:
                    await channel.send(f"Message from {message.author.display_name}: {message.content}")
                else:
                    await message.channel.send("Error: Target channel not found.")
                del user_help_map[message.author.id]
            else:
                await message.channel.send("You've already sent your message.")
        else:
            await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))
