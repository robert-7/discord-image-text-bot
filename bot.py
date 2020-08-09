# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(
    name="img_txt",
    help="Takes a picture name and some text and returns and image templated with your text.",
)
async def img_templater(ctx):
    my_filename = "images/you_should_be_asleep.jpg"
    with open(my_filename, "rb") as fh:
        f = discord.File(fh, filename=my_filename)
    await ctx.send(file=f)


@bot.command(name="quote", help="Responds with a random quote by Austin")
async def random_quote(ctx, person="austin"):
    if person == "austin":
        quotes = ["Why are you awake? You should be asleep!", "Who wants a smoothie?!"]
    response = random.choice(quotes)
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("Something went wrong! Yell at Robert to fix it! :Makaaah:")


bot.run(TOKEN)
