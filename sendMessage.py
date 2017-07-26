import discord
import asyncio

client = discord.Client()
@client.event
async def sendMessage(message, client, messageSend):
    await client.send_message(message.channel, messageSend)
async def sendEmbedMessage(message, client, messageSend):
    await client.send_message(message.channel, embed=messageSend)
async def sendDirectMessage(message, client, messageSend):
    await client.send_message(message.author, messageSend)
async def sendChannelMessage(message, channel, client, messageSend):
    await client.send_message(channel, messageSend)
async def sendEmbedChannelMessage(message, channel, client, messageSend):
    await client.send_message(message.channel, embed=messageSend)
