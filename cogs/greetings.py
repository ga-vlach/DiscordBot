import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, client):
        
        self.client = client
        print("greet loaded")

    #command
    @commands.command()
    async def hello(self, ctx):
        
        await ctx.send("Hello there")

    #event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        channel = self.client.get_channel(1025022560347357248)
        await channel.send(f"Welcome <@!{member.id}>")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        channel = self.client.get_channel(1025022560347357248)
        await channel.send(f"Bye <@!{member.id}>")


async def setup(client):
    
    await client.add_cog(Greetings(client))