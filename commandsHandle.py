from sendMessage import *
import random
import asyncio
import csv
import dataGet
import discord
import Assets.ProgressBar
import ast

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
                formattedMessage = discord.Embed(title='Help', description="**The help for your query is below.**", colour=0xF97508)
                formattedMessage.add_field(name="Command:", value=i[0], inline=True)
                formattedMessage.add_field(name="Usage:", value=i[1], inline=True)
                formattedMessage.add_field(name="Description", value=i[2], inline=True)
                await sendEmbedMessage(message, client, formattedMessage)
    else:
        formattedMessage = discord.Embed(title='Help',
                                         description="""**All commands are shown below. Use i!help [command] for more detailed help.**""",
                                         colour=0xF97508)
        for i in commandsHelp:
            if len(i) == 3:
                print(str(i))
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
    managementInvite = "https://discord.gg/4nfpW3"
    listInvite = "https://discord.gg/7vsp57M"
    communityInvite = "https://discord.gg/43X8kJ5"

    if len(args) > 1:
        #print(args[1].lower())
        if args[1].lower() == "community":
            await sendDirectMessage(message, client, "The invite to the community server: "+communityInvite)
        elif args[1].lower() == "listing":
            await sendDirectMessage(message, client, "The invite to the list server: "+listInvite)
        elif args[1].lower() == "management":
            await sendDirectMessage(message, client, "The invite to the management server: "+managementInvite)
        else:
            await sendDirectMessage(message, client, "That is not a server.")
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

async def progress(message, args, client):
    if len(args) > 2:

        if args[1].isdigit() and args[2].isdigit() and args[3].isdigit():
            progress = Assets.ProgressBar.form_progress_bar(int(args[1]), int(args[2]), int(args[3]))
            await sendMessage(message, client, str(progress))

async def verify(message, args, client):
    if args[1].lower() == "add":
        try:
            client.get_invite(args[2])
            f = open("valid_invites.txt", "r")
            valid_invites = f.read()
            valid_invites = ast.literal_eval(valid_invites)
            f.close()
            if isinstance(valid_invites, str):
                valid_invites = [args[2]]
            else:
                valid_invites.append(str(args[2]))
            f = open("valid_invites.txt", "w")
            f.write(str(valid_invites))
            f.close()
        except discord.NotFound:
            await sendMessage(message, client, "Invite not found/valid.")
        except:
            print("Exception")
            raise Exception
    elif args[1].lower() == "remove":
        f = open("valid_invites.txt", "r")
        valid_invites = f.read()
        valid_invites = ast.literal_eval(valid_invites)

        f.close()
        if args[2] in valid_invites:
            valid_invites.remove(args[2])
        else:
            await sendMessage(message, client, "Invite not verified.")
        f = open("valid_invites.txt", "w")
        f.write(str(valid_invites))
        f.close()
    else:
        await sendMessage(message, client, "Argument 1 is not given or valid.")