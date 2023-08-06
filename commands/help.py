import discord,os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
INVITE=os.getenv('INVITE_LINK')

##################################################################
## = = = = = = = = = =[ HELP COMMAND GROUP ]= = = = = = = = = = ##

@commands.group(name='help', invoke_without_command=True, description="List all available categories.")
async def help_command(ctx):
    bot_name = ctx.bot.user.name
    bot_avatar = ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url

    embed = discord.Embed(title=bot_name, color=discord.Color.blue())
    embed.set_author(name=bot_name, icon_url=bot_avatar)
    embed.set_footer(text=f"Use `{ctx.prefix}help <category>` for more info regarding a category.")

    embed.description = f"My prefix for this server is `{ctx.prefix}`.\nType `{ctx.prefix}help <category_name>` for more info on a command.\n[Invite Link]({INVITE})"

    embed.add_field(name="Categories", value="• :crown: Owner\n• :shield: Moderation\n• :gear: Utility", inline=True)

    bot_info = f"Bot ID: {ctx.bot.user.id}\n"
    bot_info += f"Bot Owner: <@527489750815342625>\n"
    embed.add_field(name="Bot Info", value=bot_info, inline=True)

    await ctx.send(embed=embed)

##################################################################


###############################################################
## = = = = = = = = = =[ CATEGORIES HELP ]= = = = = = = = = = ##

@help_command.command(name='owner')
async def owner(ctx):
    bot_name = ctx.bot.user.name
    bot_avatar = ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url

    embed = discord.Embed(title='Owner Commands', color=discord.Color.blue())
    embed.set_author(name=bot_name, icon_url=bot_avatar)
    embed.set_footer(text=f"Use `{ctx.prefix}help <command>` for more commands.")


    categories = {
        "off": "Shuts the bot down.",
        "server": "Commands related to server count.",
        "uptime": "Display the bot's uptime.",
    }

    embed.description = f"These are the `OWNER-ONLY` commands that cannot be accessed by anyone else.\n Type `{ctx.prefix}help <command>` for more info on commands.\n"

    for category, description in categories.items():
        embed.add_field(name=f'{ctx.prefix}{category}', value=description, inline=False)

    await ctx.send(embed=embed)

@help_command.command(name='moderation')
async def moderation(ctx):
    bot_name = ctx.bot.user.name
    bot_avatar = ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url

    embed = discord.Embed(title='Moderation Commands', color=discord.Color.blue())
    embed.set_author(name=bot_name, icon_url=bot_avatar)
    embed.set_footer(text=f"Use `{ctx.prefix}help <command>` for more commands.")


    categories = {
        "warn": "Warns a user, automatic mute after 3 warns.",
        "mute": "Mutes a user.",
        "unmute": "Unmutes a previously muted user.",
        "kick": "Kicks a user from the server.",
        "ban": "Bans a user from the server, sends a DM.",
        "unban": "Unbans a previously banned user from a server.",
        "silentban": "Bans a user without notifying.",
        "voice`...`": "Commands for voice channel management."
    }

    embed.description = f"Type `{ctx.prefix}help <command>` for more info on commands.\n"

    for category, description in categories.items():
        embed.add_field(name=f'{ctx.prefix}{category}', value=description, inline=False)

    await ctx.send(embed=embed)

@help_command.command(name='utility')
async def utility(ctx):
    bot_name = ctx.bot.user.name
    bot_avatar = ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url

    embed = discord.Embed(title='Utility Commands', color=discord.Color.blue())
    embed.set_author(name=bot_name, icon_url=bot_avatar)
    embed.set_footer(text=f"Use `{ctx.prefix}help <command>` for more commands.")


    categories = {
        "avatar": "Displays the avatar of a user/server.",
        "channel`...`": "Manage server channels using subcommands.",
        "firstmsg": "Takes the user to the very first message of a channel.",
        "info`...`": "Provides basic info using subcommands.",
        "list`...`": "Makes a list using subcommands.",
        "mc": "Displays number of members in the server.",
        "timer": "Starts a countdown timer for the time specified.",
        "translate": "Translates any text to English language."
    }

    embed.description = f"Type `{ctx.prefix}help <command>` for more info on commands.\n"

    for category, description in categories.items():
        embed.add_field(name=f'{ctx.prefix}{category}', value=description, inline=False)

    await ctx.send(embed=embed)

################################################################


###################################################################
## = = = = = = = = = =[ OWNER COMMANDS HELP ]= = = = = = = = = = ##



###################################################################


########################################################################
## = = = = = = = = = =[ MODERATION COMMANDS HELP ]= = = = = = = = = = ##

def create_embed():
    embed = discord.Embed(description="```diff\n- <> = required argument\n- [] = optional argument```", color=discord.Color.blue())
    return embed    

@help_command.command(name='ban', description=f"Shows command usage for `ban` command.")
async def ban(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Bans a user from the server and sends a DM to the banned user.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user to ban.\n`reason` : (Optional) The reason for the ban.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}ban <user> [reason=None]`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='kick', description=f"Shows command usage for `kick` command.")
async def kick(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Kicks a user from the server.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user to kick.\n`reason` : (Optional) The reason for the kick.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}kick <user> [reason=None]`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='mute', description=f"Shows command usage for `mute` command.")
async def mute(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Mutes a user in the server.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user to mute.\n`duration` : (Optional) The duration of mute (Indefinite mute if not specified).", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}mute <user> [duration=None]`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='silentban', description=f"Shows command usage for `silentban` command.")
async def silentban(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Silently bans a user from the server without notifying the user.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user ID to ban.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}silentban <user>`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='unban', description=f"Shows command usage for `unban` command.")
async def unban(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Unbans a previously banned user.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user ID to unban.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}unban <user>`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='unmute', description=f"Shows command usage for `unmute` command.")
async def unmute(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Unmutes a previously muted user.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user ID to unmute.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}unmute <user>`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='warn', description=f"Shows command usage for `warn` command.")
async def warn(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Warns a user. Mutes the user automatically after 'max warns'. Set 'max warns' first with `setmaxwarns <amount>`", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user to warn.\n`reason` : Reason for warning the user.(Optional)", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}warn <user> [reason=None]`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='voice', description=f"Shows command usage for `voice` command.")
async def voice(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Commands for Voice Channel Management.\nList of all available commands :", inline=False)
    embed.add_field(name="Parameters", value="`command` : The subcommand to be used.\n`user` : ID of the user.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}voice <command> <user>`", inline=False)
    embed.add_field(name=f"{ctx.prefix}voice mute <user>", value="Mutes a user in a voice channel.", inline=True)
    embed.add_field(name=f"{ctx.prefix}voice unmute <user>", value="Unmutes a user in a voice channel.", inline=True)
    embed.add_field(name=f"{ctx.prefix}voice kick <user>", value="Kicks a user from a voice channel.", inline=True)
    embed.add_field(name=f"{ctx.prefix}voice deafen <user>", value="Deafens a user in a voice channel.", inline=True)
    embed.add_field(name=f"{ctx.prefix}voice undeafen <user>", value="Undeafens a user in a voice channel.", inline=True)
    embed.add_field(name=f"{ctx.prefix}voice move <user>", value="Moves all users from the author's voice channel to the specified target channel.", inline=True)
    await ctx.send(embed=embed)

@help_command.command(name='nick', description=f"Shows command usage for `nick` command.")
async def nick(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Changes the nickname of a user.", inline=False)
    embed.add_field(name="Parameters", value="`user` : The user ID who's nickname is to be changed.\n`new_nickname` : New nickname to be set.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}nick <user> <new_nickname>`", inline=False)
    await ctx.send(embed=embed)

@help_command.command(name='role', description=f"Shows command usage for `role` command.")
async def role(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Commands for User Roles Management.\nList of all available commands :", inline=False)
    embed.add_field(name="Parameters", value="`command` : The subcommand to be used.\n`user` : ID of the user.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}voice <command> <user>`", inline=False)
    embed.add_field(name=f"{ctx.prefix}role give <user> <role> [role +n]", value="Gives role to the mention user. Multiple roles can be assigned in one command.", inline=True)
    embed.add_field(name=f"{ctx.prefix}role remove <user> <role> [role +n]", value="Removes role from the mention user. Multiple roles can be removed in one command.", inline=True)
    await ctx.send(embed=embed)

@help_command.command(name='clear', description=f"Shows command usage for `clear` command.")
async def clear_messages(ctx):
    embed = create_embed()
    embed.set_author(name="Moderation", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="", value="> Clears messages from a channel.", inline=False)
    embed.add_field(name="Parameters", value="`amount` : The amount of messages to be cleared from the channel.", inline=False)
    embed.add_field(name="Usage", value=f"`{ctx.prefix}clear <amount>`", inline=False)
    await ctx.send(embed=embed)


########################################################################


#####################################################################
## = = = = = = = = = =[ UTILITY COMMANDS HELP ]= = = = = = = = = = ##



#####################################################################