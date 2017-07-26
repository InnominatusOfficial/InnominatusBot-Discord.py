from sendMessage import *
import random
import asyncio
import csv
import dataGet
import discord

async def roll(message, args, client):
    if len(args) > 2:
        try:
            print("Try: " +args[1]+" " + args[2])
            messageSend = str(random.randint(int(args[1]), int(args[2])))
            print(messageSend)
            await sendMessage(message, client, messageSend)
        except:
            messageSend = "Exception in range given. Sorry."
            await sendMessage(message, client, messageSend)
    else:
        messageSend = str(random.randint(1,6))
        await sendMessage(message, client, messageSend)

async def help(message, args, client):
    await sendMessage(message, client, "Collecting help.")
    commandsHelp = dataGet.csvRead("commandsHelp.csv")

    if len(args) > 1:

        for i in commandsHelp:
            print(i)
            print(args[1])
            print(i[1])
            if str(i[0]) == str(args[1]):
                print("Loop")
                formattedMessage = discord.Embed(title='Help', description="The help for your query is below.", colour=0xF97508)
                formattedMessage.add_field(name="Command:", value=i[0], inline=True)
                formattedMessage.add_field(name="Usage:", value=i[1], inline=True)
                formattedMessage.add_field(name="Description", value=i[2], inline=True)
                await sendEmbedMessage(message, client, formattedMessage)
    else:
        formattedMessage = discord.Embed(title='Help', description="All commands are shown below. Use i!help [command] for more detailed help.", colour=0xF97508)
        formattedMessage.add_field(name="-----------", value="-----------", inline=False)
        for i in commandsHelp:
            formattedMessage.add_field(name=i[0], value=i[2], inline=False)
        await sendEmbedMessage(message, client, formattedMessage)
        '''formattedMessage.set_author(name='Innominatus', icon_url=client.user.default_avatar_url)
        for i in commandsHelp:
            formattedMessage.add_field(name="Command:", value=i[0], inline=True)
            formattedMessage.add_field(name="Usage:", value=i[1], inline=True)
            formattedMessage.add_field(name="Description", value=i[2], inline=True)
            formattedMessage.add_field(name="-----------", value="-----------", inline=False)
        await sendEmbedMessage(message, client, formattedMessage)'''

async def connect(message, args, client):
    gamingInvite = "https://discord.gg/zGyxDEk"
    programmingInvite = "https://discord.gg/ywjUt3p"
    listInvite = "https://discord.gg/SKPsjyj"
    mainInvite = " https://discord.gg/MnbU2Ra"
    entertainmentInvite = "https://discord.gg/hq66E8C"

    if len(args) > 1:
        #print(args[1].lower())
        if args[1].lower() == "gaming":
            await sendDirectMessage(message, client, "The invite to the gaming server: "+gamingInvite)
        elif args[1].lower() == "programming":
            await sendDirectMessage(message, client, "The invite to the programming server: "+programmingInvite)
        elif args[1].lower() == "list":
            await sendDirectMessage(message, client, "The invite to the list server: "+listInvite)
        elif args[1].lower() == "entertainment":
            await sendDirectMessage(message, client, "The invite to the entertainment server: "+entertainmentInvite)
        else:
            await sendDirectMessage(message, client, "The invite to the main server: "+mainInvite)
    else:
        await sendMessage(message, client, "Please define a server.")

async def announce(message, args, client):
    if len(args) > 1:
        if args[1] == "embed":
            formattedMessage = discord.Embed(title=args[3], description=None, colour=0xF97508)
            channelID = args[2]
            channelID = channelID.replace("<","").replace("#","").replace(">","")
            print(args)
            repeats = 0
            while repeats < 2:
                args.pop(0)
                repeats = repeats+1
            messageSend = args
            messageSend = " ".join(messageSend)
            formattedMessage.add_field(name="Message", value=messageSend, inline=False)
            await sendEmbedChannelMessage(message, channelID, client, formattedMessage)
        else:
            print(args[1])
            channelID = args[1]
            channelID = channelID.replace("<","").replace("#","").replace(">","")
            print(args)
            repeats = 0
            while repeats < 4:
                args.pop(0)
                repeats = repeats+1
            messageSend = args
            messageSend = " ".join(messageSend)
            print(messageSend)
            await sendChannelMessage(message, channelID, client, messageSend)
    else:
        await sendMessage(message, client, "Please define a message.")

async def ping(message, args, client):
    await sendMessage (message, client, "Pong")

async def pong(message, args, client):
    await sendMessage (message, client, "Hmmm, why are you sending me 'pong'? Anything wrong?")
