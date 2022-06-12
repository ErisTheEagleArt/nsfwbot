THIS SOURCE CODE IS FOR PEOPLE WHO WANT TO MAKE NSFW COMMANDS IN THEIR DISCORD.PY BOTS FOR DISCORD.


FILES
- nsfwcommand.py = Basic command for everything
- nsfwoverall.py = Is how it would look in a general discord bot.


REQUIREMENTS
- Packages: discord.py
- Knowledge: Has some knowledge of discord.py


SETUP FOR NSFWOVERALL.PY
1. client.run("BOTTOKENHERE") replace BOTTOKENHERE with your bot token
2. Replace <##NSFW content here> with your code
3. In botdev = [BOTOWNERIDSHERE], replace BOTOWNERIDSHERE with your Staff user ids. Seperating with comma.
- Example botdev = [720847987756105809, 872608213076426763]
4. (Optional): In client = commands.Bot(command_prefix = '!'), replace ! with the prefix you want.


HOW IT WORKS:
if ctx.channel.is_nsfw(): detects if the command is being run in a NSFW enabled channel (or Age-restricted channel with discord's current channel name). But I will refere to these 18+ channels as NSFW channels
This it is excuted in a NSFW channel, it triggers the code within the "if ctx.channel.is_nsfw():"
If it is triggered outside of NSFW enabled channels, it will trigger the else statement of the code with in this case would be: "This command can only be used in a NSFW channel"


DISCLAIMER:
Any NSFW content not suitable to be on discord sfw channels must stay in NSFW marked channels (Or Age-restricted channels as with Discord's name changes)