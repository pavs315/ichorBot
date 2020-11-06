import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    harry_potter = [
        'I hope you\'re pleased with yourselves. We could all have been killed — or worse, expelled. Now if you don\'t mind, I\'m going to bed.',
        'Yer a wizard Harry.','When in doubt, go to the library. ','Dobby is free', 'Honestly, if you were any slower, you’d be going backward'
        ,'I’ll be in my bedroom, making no noise and pretending I’m not there.','Mischief Managed!','Twitchy little ferret, aren’t you, Malfoy?',
        'I mean, it\'s sort of exciting, isn\'t it, breaking the rules?','I am a wizard, not a baboon brandishing a stick.'

    ]


    if message.content == 'test':
        response = random.choice(harry_potter)
        await message.channel.send(response)

    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)

