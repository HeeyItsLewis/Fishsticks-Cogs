import discord
from discord.ext import commands
from random import randint
from random import choice
import random
import aiohttp
import asyncio
import os
from .utils import checks

class fishsticks:
    "MEOW"
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)

    async def fishsticks(self):
        quote = ['WADIYATALKINABEET {}', 'YOU FUKIN DRUGGO {}', 'NAH NAH MAN POPCOIN {}', 'HEROIN ITS GOOD FOR YOUR CHOLESTEROL {}']
        emoji = ['Kippa',' TheTarFu']
        fishsticks = choice(quote).format(choice(emoji))
        await self.bot.say(fishsticks)

def setup(bot):
    n = fishsticks(bot)
    bot.add_cog(n)
