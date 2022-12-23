# Ponytails >>>
import pandas as pd
import discord
import hidden
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)


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
async def archive(ctx):

    messages_data = pd.DataFrame(columns=['content', 'attachment', 'author', 'time'])

    async for message in ctx.channel.history(limit=1000, oldest_first=True):

        try:
            message_attach = message.attachments[0].url
        except IndexError:
            message_attach = ""

        data = pd.DataFrame({'content': message.content,
                             'attachment': message_attach,
                             'author': message.author.name,
                             'time': str(message.created_at)[:16]},
                            index=[0])
        messages_data = pd.concat([messages_data, data], ignore_index=True)

    file = "messages_data.csv"
    messages_data.to_csv(file)

    await ctx.send("Here is your archive!", file=discord.File(file))


@bot.command()
async def repeat(ctx, string):
    await ctx.send(string)

bot.run(hidden.key)
