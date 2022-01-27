from telethon import TelegramClient, events
import asyncio

api_id = 10200986
api_hash = '527ea2efe24288e143ad4d94471a5350'

my_channel_id = -1001760892428
channels = [-1001165661800, -1001247701635, -1001454892384]

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)


client.start()
client.run_until_disconnected()