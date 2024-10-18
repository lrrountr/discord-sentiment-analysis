#!/usr/bin/env python3
import os

import discord

from sentiments.vader_sentiment import vader_sentiment
from sentiments.text_blob import text_blob_sentiment
from sentiments.transformers import transformers_sentiment

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def fetch_all_messages(channel, limit=None):
    all_messages = []
    async for message in channel.history(limit=limit):
        all_messages.append(message)

    return all_messages


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        for guild in self.guilds:
            print(f'Guild: {guild.name} (ID: {guild.id})')

            # Get all channels in the guild
            for channel in guild.channels:
                print(f'Channel: {channel.name} (ID: {channel.id}, Type: {channel.type})')
        
                if isinstance(channel, discord.TextChannel):
                    channel = self.get_channel(channel.id)
                    if channel:
                         all_messages = await fetch_all_messages(channel)  
                         for message in all_messages:
                            if message.content:
                                # Perform sentiment analysis using different libraries
                                print(f'{message.author}: {message.content}')
                                vader_sentiment(message.content)
                                text_blob_sentiment(message.content)    
                                transformers_sentiment(message.content)
                    # Close the bot after fetching the messages                            
                    await self.close()  


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.messages = True  # Enables receiving message events

    client = MyClient(intents=intents)
    client.run(BOT_TOKEN)