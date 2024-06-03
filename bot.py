import discord
from discord.ext import commands
from genpass import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def password(ctx, num = 10):
    await ctx.send(gen_pass(num))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
@bot.command()
async def purge(ctx, num: int):
    await ctx.channel.purge(limit=num)
    await ctx.send("")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("fdsfsdfsd")
