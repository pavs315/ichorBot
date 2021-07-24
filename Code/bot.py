import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client()
muteme_members = set()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(type=discord.ActivityType.playing, name="to .help"))
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break
            
        print(f"ichorBot is available on the server {guild.name}")
  

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    
    
#test
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     harry_potter = [
#         'I hope you\'re pleased with yourselves. We could all have been killed — or worse, expelled. Now if you don\'t mind, I\'m going to bed.',
#         'Yer a wizard Harry.','When in doubt, go to the library. ','Dobby is free', 'Honestly, if you were any slower, you’d be going backward'
#         ,'I’ll be in my bedroom, making no noise and pretending I’m not there.','Mischief Managed!','Twitchy little ferret, aren’t you, Malfoy?',
#         'I mean, it\'s sort of exciting, isn\'t it, breaking the rules?','I am a wizard, not a baboon brandishing a stick.'

#     ]
    
#     if message.content == 'test':
#         response = random.choice(harry_potter)
#         await message.channel.send(response)

#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
        
    
    
@client.event
async def on_message(message):
    global muteme_members

    if message.author == client.user:
        return
    if message.content.startswith('.'):
        # print(message)
        if message.author.voice and message.author.voice.channel:
            channel = message.author.voice.channel
        else:
            await message.channel.send("You are not connected to a voice chat")
            return

        connected_members = channel.members
        if message.content.startswith('.help'):
            help_message = """```
Simple server muting bot            
# Commands:
.muteme                     | to mute yourself
.shut @User1 @User2         | mutes the mentioned user
.muteall                    | Mutes everyone that is currently not muted
.unmuteall                  | Unmutes everyone
```"""
            await message.channel.send(help_message)

        if message.content.startswith('.muteall'):
            for member in connected_members:
                await member.edit(mute=True)
            await message.channel.send("All members muted")

        if message.content.startswith('.unmute'):
            for member in connected_members:
                if member not in muteme_members:
                    await member.edit(mute=False)
            await message.channel.send("Everyone unmuted")

        if message.content.startswith('.muteme'):
            member = message.author
            muteme_members.add(member)
            await member.edit(mute=True)
            await message.channel.send(f"{member.name} muted themselves")

        if message.content.startswith('.shut'):
            users = message.content.split(' ')[1:]
            if len(users) == 0:
                await message.channel.send("Mention atleast one user in the voice chat.")
            else:
                for user in users:
                    import re
                    member = discord.utils.get(connected_members, id=int(re.search(r'\d+', user).group()))
                    if member is None:
                        invalid_user = discord.utils.get(message.guild.members, id=int(user[3:-1]))
                        await message.channel.send(f"{invalid_user.name} is not connected to voice channel")
                        return
                    muteme_members.add(member)
                    await member.edit(mute=True)
                muteme_members_str = '\n - '.join([member.name for member in muteme_members])
                await message.channel.send(f"Shut \n {muteme_members_str} up")

        if message.content.startswith('.unmuteall'):
            for member in connected_members:
                muteme_members = set()
                await member.edit(mute=False)
            await message.channel.send("All members unmuted.")

 
client.run(TOKEN)

