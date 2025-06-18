import discord
from discord.ext import commands
import os
import asyncio
from herp import BOTTOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

client = commands.Bot(command_prefix = '?', intents = intents)


@client.event
async def on_ready():
    print(f"Hi")


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

# print(initial_extensions)

# async def load_cogs():
#     for extension in initial_extensions:
#         await client.load_extension(extension)

async def main():
    async with client:
        await load_cogs()
        await client.start(BOTTOKEN)

asyncio.run(main())