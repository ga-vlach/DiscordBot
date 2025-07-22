import discord
from discord.ext import commands
import random
import asyncio
import sqlite3

class Fun(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client
        print("games loaded")


    @commands.command()
    async def rps(self, ctx):
            
        choices = ["Rock", "Paper", "Scissors"]
        # channel = message.channel
                
        await ctx.send("Rock, paper, scissors... SHOOT!")

        bot_choice = choices[random.randint(0,2)]

        try:
            msg = await self.client.wait_for('message', timeout = 15.0)
                
        except asyncio.TimeoutError:
            await ctx.send("You ran out of time! Be faster next time!")

        else:
            #converts the user's message to lowercase, so user input isn't case sensitive
            if not (msg.content.lower().startswith("rock")
                or msg.content.lower().startswith("paper")
                or msg.content.lower().startswith("scissors")):

                await ctx.send("Invalid input. You can only use rock, paper, or scissors!")
                return

            if (msg.content.lower().startswith("rock")):
                if (bot_choice == "Rock"):
                    result = "It's a draw!"
                if (bot_choice == "Scissors"):
                    result = "You win! You beat  me!"
                if (bot_choice == "Paper"):
                    result = "I won! Better luck next time!"
            
            if (msg.content.lower().startswith("scissors")):
                if (bot_choice == "Rock"):
                    result = "I won! Better luck next time!"
                if (bot_choice == "Scissors"):
                    result = "It's a draw!"
                if (bot_choice == "Paper"):
                    result = "You win! You beat me!"
            
            if (msg.content.lower().startswith("paper")):
                if (bot_choice == "Rock"):
                    result = "You win! You beat me!"
                if (bot_choice == "Scissors"):
                    result = "I won! Better luck next time!"
                if (bot_choice == "Paper"):
                    result = "It's a draw!"
            
            await ctx.send(bot_choice)
            await ctx.send(result)


    #inputs the member that joins the server in the database and inputs necessary info inside it
    @commands.Cog.listener()
    async def on_member_join(self, member):

        userid = member.id
        username = member.name
        
        conn = sqlite3.connect("leveling.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO uservalues VALUES (?, ?, ?, ?)", (userid, username, 0, 0))
        conn.commit()

        conn.close()


    #updates the user's xp and level data if needed
    @commands.Cog.listener()
    async def on_message(self, message):
        
        user = message.author.id

        conn = sqlite3.connect("leveling.db")
        cur = conn.cursor()
        cur.execute("SELECT xp, level FROM uservalues WHERE userid = ?", (user,))
        results = cur.fetchone()
        
        #updates user's xp every message
        old_xp = results[0]
        level = results[1]
        new_xp = old_xp + 1
        xp_req = 2 * (level + 1) * 2.5

        #checks if user is eligible for a level up
        if new_xp == xp_req:

            level += 1
            new_xp = 0

            await message.channel.send(f"Congratulations! You leveled up! You're now level {level}!")


        cur.execute("UPDATE uservalues SET xp = ?, level = ? WHERE userid = ?", (new_xp, level, user))
        conn.commit()
        conn.close()
    

    #displays the specified person's username, xp and level
    @commands.command()
    async def rank(self, message, user: discord.User=None):

        if user == None:
            
            username = message.author.name
        else:

            username = user.name

        conn = sqlite3.connect("leveling.db")
        cur = conn.cursor()
        cur.execute("SELECT username, xp, level FROM uservalues WHERE username = ?", (username,))
        result = cur.fetchone()
        
        await message.channel.send(f"``{result[0]}``\n``xp: {result[1]}``\n``level: {result[2]}``")



async def setup(client):
    
    await client.add_cog(Fun(client))
