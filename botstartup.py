import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import asyncio
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello And Welcome To The Server We Hope You Have A Quacking Time Here. Got A Question? Feel free To Ask!')
    print('Sent message to ' + member.name)
    
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="for .help", type=3))
    print("Running...")




@client.event
async def on_message(message):
    if message.content == '.ping':
        await client.send_message(message.channel,'Pong')
    if message.content == '.invite':
        await client.send_message(message.channel,'https://discordapp.com/oauth2/authorize?&client_id=518430532116414464&scope=bot&permissions=8')

    if message.content == '.default':
        em = discord.Embed(description='Dedault Dance Boiiiiii')
        em.set_image(url='https://cdn.discordapp.com/attachments/488600981765095438/513075944685174784/1708785.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '.No u':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/417038164646166551/486237014493233165/image.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '.gopnik':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/348532429348143114/486258427706736640/image.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.No Anime':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/465353505125695491/486266510088863747/image.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.Ass':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/476093333840723978/486266493982736395/image.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.sc':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/417038164646166551/486267619763027968/unnamed.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '.noswearing':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/476093333840723978/486270543037988874/image.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.yolk':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/476093333840723978/486271945290022922/PicsArt_08-11-12.27.36.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.help':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/417038164646166551/486274441723117580/Blank_e66e734c445117d6e2906d055c374a71.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '.Big Smoke':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/417038164646166551/486280915438272512/maxresdefault.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '.SexyMomo':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/462106200100700173/485548557017808911/JPEG_20180828_233621.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.Discord':
        await client.send_message(message.channel,'')
    if message.content == 'Hi':
        await client.send_message(message.channel,'HI HOE')
    if message.content == '.Sorry':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/346424860878307341/486340688259186718/image.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.coinflip'):
        randomlist = ['heads','tails',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('.embarrass'):
        randomlist = ['You learned Asian culture by watching hentai','Video gamers rock! Brofist!','delet this','You held your pee in for a whole hour during fantastic beasts and where to find them','You couldnt teach your son how to ride a bike cause you cant ride one yourself.','You still wet the bed','You are part of the hacker group known as 4chan',]
        await client.send_message(message.channel,(random.choice(randomlist)))

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = [ ]
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Have Been Cleared!')


    @client.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

    @client.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    

client.run('NTE4NDMwNTMyMTE2NDE0NDY0.DuQslA.qTIh7MlCiwOaAFjnYWKd82q1C04')
