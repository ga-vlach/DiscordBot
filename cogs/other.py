import discord
from discord.ext import commands

class Other(commands.Cog):

    def __init__(self, client):
        
        self.client = client
        print("other loaded")


    @commands.command()
    async def pfp(self, ctx, user: discord.User):

        await ctx.send(user.display_avatar)


async def setup(client):

    await client.add_cog(Other(client))