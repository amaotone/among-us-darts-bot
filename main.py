import os
import random
import discord
from discord.ext import commands
from typing import Optional

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command()
async def darts(ctx: commands.Context, channel_name: str, name: Optional[str] = None):
    if ctx.author.bot:
        return
    await ctx.message.delete()

    channel_name = channel_name.lstrip("#")
    channels = ctx.guild.voice_channels
    for ch in channels:
        if ch.name == channel_name:
            if not ch.members:
                await ctx.send(f"#{channel_name}には誰もいません")
                return
            member = random.choice(ch.members)
            msg = f"{name}に選ばれました！" if name is not None else "あなたが選ばれました！"
            await member.send(msg)
            return

    await ctx.send(f"#{channel_name}が存在しません")


TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
