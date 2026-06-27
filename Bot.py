import discord
import os
import asyncio
import yt_dlp
from discord import client, voice_client
from discord.ext import commands

BOT_TOKEN = "There is a token here."
CHANNEL_ID = substitute for channel ID

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Also shut the hell up, Jackie!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Okay jackie. Sorry for hurting your feelings.')

@bot.command()
async def yo(ctx):
    await ctx.send('Yo! Have you told Jackie to shut up yet? Well here is your reminder :)')

yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = {
    'before options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_5',
    'options': '-vn'
}

@bot.command()
async def play(ctx, url):
    if ctx.author.voice is None:
        await ctx.send("Bro you ain't in the voice channel.")
        return

    voice_channel = ctx.author.voice.channel

    voice_client = await voice_channel.connect()

    loop = asyncio.get_event_loop()

    data = await loop.run_in_executor(
        None,
        lambda: ytdl.extract_info(url, download=False)
    )

    song = data['url']

    player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

    voice_client.play(player)

    await ctx.send("Here's your song!")

bot.run(BOT_TOKEN)
