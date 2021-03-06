# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:39:18 2017

@author: SolitudalAutocracy
"""
import sys
import functools
import discord
import asyncio
import logging
import dataGet
from sendMessage import sendMessage
import initCommands
import ast
import os
import sqlite3

logging.basicConfig(level=logging.INFO)
client = discord.Client()

commands = initCommands.init_commands()

class MyClient(discord.Client):
    @client.event
    async def on_ready():
        """if os.path.exists("/user_data.db"): first_start = True
        with sqlite3.connect('user_data.db') as db:
            if first_start = True:
                cursor = db.cursor()"""
                #cursor.execute("""create table """)

        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        await client.change_presence(game=discord.Game(name='Innominatus Realms'))
        print('------')
        client.login()
        '''for server in client.servers:
            for channel in server.channels:
                print(str(channel.type))
                if str(channel.type) == "voice":
                    exit
                else:
                    print("Sent: " + str(channel))
                    await client.send_message(channel, 'The official Innominatus discord bot is coming online!')
        '''

    
    @client.event
    async def on_message(message):
        import sys

        def str_to_class(str):
            return getattr(str, sys.modules[command])
        if message.content.startswith("i!"):
            args = message.content[2:]
            args = args.split()
            command = args[0].lower()
            print(command)
            command = initCommands.command.registeredCommands[command]
            await command.runCommand(message, args, client)
        print(message.channel.name)
        if message.channel.name in ["bronze-servers", "silver-servers", "gold-servers", "platinum-servers", "emerald-servers"]:
            if "https://discord.gg/" in message.content:
                emojis = {}
                for i in message.server.emojis:
                    emojis[i.name] = i
                print(str(emojis))
                f = open("valid_invites.txt", "r")
                invites = ast.literal_eval(f.read())
                for i in invites:
                    if i in message.content:
                        print("Add reaction")
                        await client.add_reaction(message, emojis["verified"])
                        break
                f.close()


    

print("Enter the client token.")
client_id = input()
"""print("Input embed message")
message = input()
print("input channel ID")
channelID = input()"""

client.run(str(client_id))
