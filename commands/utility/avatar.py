import discord
from discord.ext import commands

@commands.command(aliases=['av'], description='Displays the avatar of a user/server.')
async def avatar(ctx, *, arg=None):
    if arg is None or arg.lower() == 'me' or arg.lower() in ['av', 'avatar']:
        user = ctx.author
    elif arg.lower() == 'server':
        if ctx.guild:
            user = ctx.guild
        else:
            await ctx.send("This command can only be used in a server.")
            return
    else:
        try:
            user_id = int(arg)
            user = await ctx.bot.fetch_user(user_id)
        except (ValueError, discord.NotFound):
            await ctx.send("User not found.")
            return

    embed = discord.Embed(title=f"{'Server' if isinstance(user, discord.Guild) else 'User'} Avatar", color=discord.Color.blue())

    if isinstance(user, discord.Guild) and user.icon:
        embed.set_image(url=user.icon.url)
    elif isinstance(user, discord.User) and user.avatar:
        embed.set_image(url=user.avatar.url)

    await ctx.send(embed=embed)
