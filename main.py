# Ponytails >>>

import discord
import hidden
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Archiving NOW!"))
    print(f'We have logged in as {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Here is the ping: {round(bot.latency * 1000)} ms')


@bot.command()
async def messages(ctx):
    counter = 0
    async for message in ctx.channel.history(limit=50):
        if message.author == bot.user:
            counter += 1
    await ctx.send(counter)


@bot.command()
async def repeat(ctx, str):
    await ctx.send(str)

bot.run(hidden.key)