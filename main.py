import discord, os, asyncio
from discord.ext import commands
from dotenv import load_dotenv
from commands.help import help_command
from commands.error_handlers import *
from commands.owner.off import off
from commands.owner.uptime import uptime
from commands.owner.server_count import server
from commands.utility.avatar import avatar
from commands.utility.list import list
from commands.utility.info import info
from commands.utility.firstmsg import firstmsg
from commands.utility.timer import timer
from commands.utility.channel import channel
from commands.utility.member_count import member_count
from commands.utility.translate import translate
from commands.utility.prefix import prefix, custom_prefixes
from commands.utility.vcjoiner import join, leave, vcc
from commands.mod.ban import ban
from commands.mod.kick import kick
from commands.mod.mute import mute
from commands.mod.silentban import silentban
from commands.mod.unban import unban
from commands.mod.unmute import unmute
from commands.mod.warn import warn, setmaxwarns
from commands.mod.voice import voice
from commands.mod.nickname import nick
from commands.mod.role import role
from commands.mod.clear import clear

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

def get_prefix(bot, message):
    return custom_prefixes.get(message.guild.id, PREFIX)

async def update_activity():
    while True:
        await bot.change_presence(discord.Activity(type=discord.ActivityType.listening, name=f"'{PREFIX}' as prefix"))
        await asyncio.sleep(3)
        await bot.change_presence(discord.Activity(type=discord.ActivityType.playing, name='with Photron\'s code'))
        await asyncio.sleep(3)

def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)

bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all(), help_command=None)

bot.add_command(help_command)
bot.add_command(join)
bot.add_command(leave)
bot.add_command(vcc)
bot.add_command(voice)
bot.add_command(prefix)
bot.add_command(off)
bot.add_command(uptime)
bot.add_command(server)
bot.add_command(avatar)
bot.add_command(list)
bot.add_command(info)
bot.add_command(firstmsg)
bot.add_command(timer)
bot.add_command(channel)
bot.add_command(member_count)
bot.add_command(translate)
bot.add_command(ban)
bot.add_command(unban)
bot.add_command(silentban)
bot.add_command(kick)
bot.add_command(mute)
bot.add_command(unmute)
bot.add_command(warn)
bot.add_command(setmaxwarns)
bot.add_command(nick)
bot.add_command(role)
bot.add_command(clear)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{PREFIX}help | STINGG"), status=discord.Status.online)
    print(f'{bot.user.name}#{bot.user.discriminator} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command()
@is_admin()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')

def get_log_settings(guild):
    return bot.guild_settings.get(guild.id, {})

@bot.event
async def on_member_join(member):
    settings = get_log_settings(member.guild)
    log_channel_id = settings.get("log_channel")
    log_message = settings.get("log_message", "User {user} has joined the server.")
    if log_channel_id:
        log_channel = bot.get_channel(log_channel_id)
        if log_channel:
            await log_channel.send(log_message.format(user=member.mention))

@bot.event
async def on_member_remove(member):
    settings = get_log_settings(member.guild)
    log_channel_id = settings.get("log_channel")
    log_message = settings.get("log_message", "User {user} has left the server.")
    if log_channel_id:
        log_channel = bot.get_channel(log_channel_id)
        if log_channel:
            await log_channel.send(log_message.format(user=member.mention))

bot.guild_settings = {}

bot.add_listener(on_command_error, 'on_command_error')
bot.add_listener(on_error, 'on_error')

custom_prefixes=custom_prefixes
bot.run(TOKEN)
