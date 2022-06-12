import discord
import random
import random
import asyncio
import sys

client = commands.Bot(command_prefix = '!')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Bot Ready")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Bot", description="!help - This Message\n!nsfw - NSFW Command here", color=(16734093))
    await ctx.send(embed=embed)

##NSFW Command Below

@client.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        ##NSFW content here. Replace this message with your code to be excecuted in discord NSFW channels
    else:
        await ctx.send("This command can only be used in a NSFW channel")

##This source code is for if you wish to put NSFW commands in your discord.py bots




botdev = [BOTOWNERIDSHERE]

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.command()
async def restart(ctx):
    if ctx.author.id in botdev:
        await ctx.send("Restarting... This may take some time")
        restart_program()
    else:
        await ctx.send("This command can only be used by Boomerang Rosalina/Boomerang Peach Developers")
        return



client.run("BOTTOKENHERE")
