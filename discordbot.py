from wiki import get_word
import discord
from discord.ext import commands
from random_gif import rng_gif
from ask_command import askcommand

t = open("token.txt")
token = t.read()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game('Developed by Illy!'))


@bot.command()
async def wiki(ctx, args):
    try:
        await ctx.send(f"Word: {get_word(args)[0]}\nDefinition: {get_word(args)[1]}")
    except Exception as error:
        await ctx.send(f"This word probably doesn't exist in my dictionary! Error: {type(error).__name__}  {error}")


@bot.command()
async def gif(ctx):
    await ctx.send(f"Random GIF:\n{rng_gif()}")


@bot.command()
async def ask(ctx, args):
    await ctx.send(askcommand(args))


@bot.command()
async def commands(ctx):
    await ctx.send('Command Prefix: .\nAlways use " " when using multiple words with spaces\nCurrent Commands:')
    await ctx.send(".commands - view this page\n.wiki [word] - get the definition of a word\n.gif - get a random GIF\n.ask - ask a Chatbot some questions")


bot.run(token)
