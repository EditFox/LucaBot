import discord
import lucario.base as base
import json

with open('config.json') as data:
    config = json.load(data)

@base.lucafunc
async def example(message, client):
    await client.send_message(message.channel, "Yay! I coded a whole entire programming shit on my own")
    
@base.lucafunc
async def help(message, client):
    cmds = []
    for key in base.functions:
        cmds.append(key)
    await client.send_message(message.channel, "***Current Commands:***\n{}".format(", ".join(cmds)))
