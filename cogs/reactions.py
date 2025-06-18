import discord
from discord.ext import commands


class Reactions(commands.Cog):

    def __init__(self, client):
        
        self.client = client
        print("react loaded")

    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.content.startswith("lol"):
            channel = message.channel
            await channel.send("lmao")
        
        if message.content.startswith("thequickbrownfox"):  
            await message.add_reaction("🦊")


async def setup(client):
    
    await client.add_cog(Reactions(client))