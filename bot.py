import os
from discord.ext import commands
 
bot = commands.Bot(command_prefix = '#')
 
@bot.event
async def on_ready():
    print ("I am awake")
 
async def react(message):
    custom_emojis = [                  
    "<:CheckMark:955457250393194568>"
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
      if emoji in guild_emoji_names:
          await message.add_reaction(emoji)
 
@bot.event                                             
async def on_message(message):
    if message.channel.id == 669491331365732352:                
      await react(message)

bot.run(os.environ['TOKEN']) 
