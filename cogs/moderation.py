import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Moderation(commands.Cog):

    def __init__(self, client):
        
        self.client = client
        print("moderation loaded")
    

    @commands.has_permissions(kick_members = True)
    @commands.command(pass_context = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):

        await member.kick(reason = reason)
    
    @commands.has_permissions(ban_members = True)
    @commands.command(pass_context = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):

        await member.ban(reason = reason)


async def setup(client):
    
    await client.add_cog(Moderation(client))


