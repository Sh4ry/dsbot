import discord
from genpass import gen_pass

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Abbiamo effettuato l'accesso come {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Ciao! Sono un bot!')
    elif message.content.startswith('$password'):
        num = message.content[10:]
        try:
            num = int(num)
        except: await message.channel.send("Errore di formattazione! Devi inserire $password num")
        await message.channel.send(gen_pass(num))
    else:
        await message.channel.send("Non è possibile elaborare questo comando, mi dispiace!")

client.run("nf ikjdsbn")
