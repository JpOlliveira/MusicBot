import random
from discord.ext import commands,tasks
import discord
from discord import app_commands
import logging
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="!!",intents=discord.Intents.all(),application_id=int(os.getenv("BOT_ID")))

class SubButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.timeout=600

        #botaourl = discord.ui.Button(label="Divirta-se")
        #self.add_item(botaourl)

@bot.event
async def on_ready(): 
    print("Estou online!")

@bot.command()
@commands.is_owner() 
async def sync(ctx,guild=None):
    if guild == None:
        await bot.tree.sync()
    else:
        await bot.tree.sync(guild=discord.Object(id=int(guild)))
    await ctx.send("**Sincronizado!** Se você chegou até aqui, dá uma força para a gente se inscrevendo no YouTube!",view=SubButton())

async def main():
    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

        
        TOKEN = os.getenv("DISCORD_TOKEN")
        await bot.start(TOKEN)

asyncio.run(main())

