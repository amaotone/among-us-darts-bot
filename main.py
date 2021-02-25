import os
import re
import random
import discord

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
MESSAGE_PATTERN = re.compile(r"^/roll\s+#(?P<channel>\w+)\s?(?P<message>.*)")
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def get_voice_channel_members(message: discord.Message):
    data = {"voice_channels": message.guild.voice_channels}
    return data


@client.event
async def on_message(message: discord.Message):
    text = message.content
    match = MESSAGE_PATTERN.match(text)
    if message.author.bot or match is None:
        if text.startswith("/roll"):
            await message.channel.send("Usage: `/roll #[voice_channel_name] [message]`")
        return

    channels = message.guild.voice_channels
    for ch in channels:
        if ch.name == match.group("channel"):
            member = random.choice(ch.members)
            msg = (
                f"{match.group('message')}に選ばれました！"
                if match.group("message")
                else "あなたが選ばれました！"
            )
            await member.send(msg)
            return

    await message.channel.send(f"#{match.group('channel')}は存在しません")


while True:
    client.run(TOKEN)