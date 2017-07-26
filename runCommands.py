import discord
import asyncio
import random
import csv
import dataGet
from commands import *
from sendMessage import sendMessage


async def runCommands(message, command, args, client):
    if command == "help":
        await help(message, args, client)
    elif command == "roll":
        await roll(message, args, client)
    elif command == "connect":
        await connect(message, args, client)
    else:
        await client.send_message(message, client, "Sorry, your command was not found")
        
