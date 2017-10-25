'''Lucario: a shitty bot'''
import discord
import lucario
import asyncio
import json
import sys #to catch errors in debug!
client = discord.Client(max_messages=100)

with open('config.json') as data:
    config = json.load(data)

#ACTUAL BOT SHIT

@client.event
async def on_ready():
    '''you know what this is'''
    print("Logged in as {}".format(client.user.name))
    print(client.user.id)
    print("---------")

@client.event
async def on_message(message):
    '''you also know what this is'''
    if message.content.startswith(config['invoker']) and message.author.id != client.user.id and len(message.content) > 1:
        command = message.content.split()[0][len(config['invoker']):].lower()
        
        if command in lucario.base.functions:
            if message.channel.is_private or message.channel.permissions_for(message.server.me).send_messages:
                await client.send_typing(message.channel)
                await lucario.base.functions[command](message,client)
            else:
                print("\n============\nThe bot ran into a permission error, can't talk in a channel!\n=========\n")
                
@lucario.base.lucafunc
async def reboot(message, client):
    '''Owner command to reboot bot'''
    if message.author.id == config["owner_id"]:
        await client.close()


client.run(config['token'])
