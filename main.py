import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send('Hello! I\'m a bot that helps you to solve global warming. Use /info for more information')

    elif message.content.startswith('/info'):
        await message.channel.send('Choose a number between 1-8 with "/" at the start')

    elif message.content.startswith('/1'):
        await message.channel.send('Change a light: Replacing one regular light bulb with a compact fluorescent light bulb will save 150 pounds of carbon dioxide a year.')

    elif message.content.startswith('/2'):
        await message.channel.send('Drive less: Walk, bike, carpool, or take mass transit more often. You will save one pound of carbon dioxide for every mile you don\'t drive!')

    elif message.content.startswith('/3'):
        await message.channel.send('Recycle more: You can save 2,400 pounds of carbon dioxide per year by recycling just half of your household waste.')

    elif message.content.startswith('/4'):
        await message.channel.send('Use less hot water: It takes a lot of energy to heat water. Use less hot water by taking shorter and cooler showers and washing your clothes in cold or warm instead of hot water (more than 500 pounds of carbon dioxide saved per year).')

    elif message.content.startswith('/5'):
        await message.channel.send('Avoid products with a lot of packaging: You can save 1,200 pounds of carbon dioxide if you reduce your garbage by 10 percent.')

    elif message.content.startswith('/6'):
        await message.channel.send('Adjust your thermostat: Moving your thermostat down just 2 degrees in winter and up 2 degrees in summer could save about 2,000 pounds of carbon dioxide a year.')

    elif message.content.startswith('/7'):
        await message.channel.send('Plant a tree: A single tree will absorb one ton of carbon dioxide over its lifetime.')

    elif message.content.startswith('/8'):
        await message.channel.send('Turn off electronic devices: Simply turning off your television, DVD player, stereo, and computer when you are not using them will save you thousands of pounds of carbon dioxide a year.')

    # Hata mesajı ekleme
    elif message.content.startswith('/') and not message.content[1:].isdigit():
        await message.channel.send('Hata! Lütfen geçerli bir sayı girin (1-8 arasında).')

# Bot tokenınızı buraya ekleyin
client.run('MTE2NDYyMjA5NDY3NjU0MTU0MA.GOhD9N.rflR8fsT-_FlsgoB3eP9INJ7eGEvxdJ8hRgd58')
