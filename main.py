from os import getenv
from dotenv import load_dotenv
from discord.ext import commands
import discord
#import cowparser

load_dotenv()

# initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents, help_command=None)

# display a message when the bot is ready
@bot.event
async def on_ready():
  print(f"{bot.user.name} has connected to Discord !")

@bot.command(name='help')
async def help(ctx):
  # react with a thumb up
  await ctx.message.add_reaction('👍')
  await ctx.send("help")

bot.run(getenv('DISCORD_TOKEN'))