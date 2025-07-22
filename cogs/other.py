import discord
from discord.ext import commands
import requests

class Other(commands.Cog):

    def __init__(self, client):
        
        self.client = client
        print("other loaded")

    #displays the specified person's profile picture
    @commands.command()
    async def pfp(self, ctx, user: discord.User=None):

        if user == None:
            #typing only the command with no specified user sends this message
            await ctx.send("**Usage:**\n `?pfp {user}`")
        else:

            await ctx.send(user.display_avatar)
    
    @commands.command()
    async def quote(self, ctx):

        r = requests.get("https://www.affirmations.dev/")
        
        quote = r.json()

        await ctx.send(quote["affirmation"])


async def setup(client):

    await client.add_cog(Other(client))