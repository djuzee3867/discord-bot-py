import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix=';', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODYyMzc1MjM1MTEzOTc1ODM4.YOXbhg.Te6gQTked6S3QpWMwPDi_zM7d2M")