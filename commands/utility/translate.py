import discord
from discord.ext import commands
from googletrans import Translator

translator = Translator()

@commands.command(description="Translate a message to English.")
async def translate(ctx, *, message: str):
    try:
        translated = translator.translate(message, src='auto', dest='en')
        await ctx.send(embed=discord.Embed(title="Translation", description=translated.text))
    except Exception as e:
        await ctx.send("An error occurred during translation.")
