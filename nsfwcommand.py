@client.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        ##NSFW content here. Replace this message with your code to be excecuted in discord NSFW channels
    else:
        await ctx.send("This command can only be used in a NSFW channel")

##This source code is for if you wish to put NSFW commands in your discord.py bots
