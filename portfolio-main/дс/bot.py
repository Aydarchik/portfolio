import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    images1 = os.listdir('m2_l1/images')
    img_name = random.choice(images1)
    with open(f'm2_l1/images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def randomN(ctx):
    n = random.randint(1, 100)
    await ctx.send(n)
@bot.command()
async def stop(ctx):
    await ctx.send('СТОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО')
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def SendPepe(ctx):
    await ctx.send("https://imgur.com/gallery/fB2m0gd")

bot.run("") 