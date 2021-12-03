import discord
import asyncio
import json
from discord.ext import commands
from blurple import ui
with open("config.json") as file:
    info = json.load(file)
    token = info["token"]
    prefix = info["prefix"]
credit = "Made by https://github.com/evo0616lution"
bot = commands.Bot(command_prefix=prefix, help_command=None)
@bot.event
async def on_ready():
    print(credit)
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)}"))


@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help", description=f"Yes")
  embed.set_thumbnail(url=bot.user.avatar_url)




@bot.command()
async def warn(ctx, member: discord.Member = None, *, arg = None):
  if member != None:
    if arg != None:
      try:
        await member.send(f"You recieved a warning in {ctx.message.guild.name} for reason {arg}")
      except:
        await ctx.send("Cannot warn: Target has disabled DMs")
      await ctx.send(embed=ui.Alert(ui.Style.SUCCESS, title="Member warned via DMs")
    else:
      try:
        await member.send(f"You recieved a warning in {ctx.message.guild.name} - No reason given!")
       except:
         await ctx.send("Cannot warn: Target has disabled DMs")
       await ctx.send(embed=ui.Alert(ui.Style.SUCCESS, title="Member warned via DMs!")
  else:
    await ctx.send("Please provide a user")




bot.run(token)
