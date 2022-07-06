from urllib import response
import discord
import requests
from discord.ext import taks, commands
from discord.ui import *

CHANNEL_ID = ""
TIKTOK_USERNAME = ""
BOT_TOKEN = ""

intents = discord.intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
headers = {'user-agent': 'YOUR-USER-AGENT'}


@tasks.loop(minutes=10)
async def updateTiktok():
    response = requests.get(f"https://www.tiktok.com/node/share/user/@{TIKTOK_USERNAME}?aid=1988", headers=headers).json()[
        'userInfo']['stats']['followerCount']
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.edit(name=f"Followers: {response}")


@bot.event
async def on_ready():
    updateTiktok.start()
bot.run(BOT_TOKEN)
