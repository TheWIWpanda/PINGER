# check_webhook.py
import discord
import asyncio
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
PING_WEBHOOK_URL = os.getenv("PING_WEBHOOK_URL")

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)
        messages = await channel.history(limit=1).flatten()
        latest = messages[0]
        if latest.webhook_id:
            data = {"content": f"Webhook message detected in <#{CHANNEL_ID}>!"}
            requests.post(PING_WEBHOOK_URL, json=data)
        await self.close()

intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)
asyncio.run(client.start(TOKEN))
