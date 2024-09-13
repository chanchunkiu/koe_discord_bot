from dotenv import load_dotenv
import discord
from discord.ext import commands
from typing import Final
import os
from google_ai import generate_response  # Import the generate_script function

load_dotenv()
TOKEN: Final = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def hi(ctx):
    await ctx.send('Ah! hihi! Whats on your mind?')
@client.command()
async def bye(ctx):
    await ctx.send('Bye bye!')

@client.command()
async def koe(ctx, *, message):
    try:
        response = generate_response(message)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {str(e)}")
        print(f"Unexpected error in koe command: {str(e)}")

client.run(TOKEN)