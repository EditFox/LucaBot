'''evan's commands'''
import sys
import json
import discord
import lucario.base as base

with open('config.json') as data:
    config = json.load(data)

@base.lucafunc
async def example(message, client):
    '''Example command for beta testing'''
    await client.send_message(message.channel, "this is example code, aaahhhhhh")

@base.lucafunc
async def commands(message, client):
    '''Lists all commands and allows you to actually look at docs of a command'''
    if len(message.content.split()) == 1:
        cmds = []
        for key in base.functions:
            cmds.append(key)
        await client.send_message(message.channel, "***Current Commands:***\n{}".format(", ".join(cmds)))
    if len(message.content.split()) == 2:
        cmd = message.content.split()[1]
        try:
            docs = base.docstrings[cmd]
        except:
            await client.send_message(message.channel, "That's either not a command, or Evan's too lazy to add a docstring to it. ```{}```".format(sys.exc_info()[1]))
            return
        await client.send_message(message.channel, "```{}```".format(docs))

@base.lucafunc
async def debug(message, client):
    '''Debug command for owner'''
    if message.author.id != config["owner_id"]:
        await client.send_message("Can't let you do that, sorry!")
        return
    cmd = message.content[7:]
    try:
        if cmd.startswith("await"):
            completed = await eval(cmd[6:])
        else:
            completed = eval(cmd)
    except Exception as e:
        await client.send_message(message.channel, "`{} > {}`".format(message.author.name, cmd))
        await client.send_message(message.channel, "```{}```".format(sys.exc_info()[1]))
        return
    await client.send_message(message.channel, completed)