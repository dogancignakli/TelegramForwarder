from telethon import TelegramClient,events

api_id = "Your Api Id Here"
api_hash = "Your api hash here"
client = TelegramClient('DoganSlx', api_id, api_hash)
fromChat = 111111111 # Chat from which bot will read data
toChat = 'The chat that you want to forward messages'

@client.on(events.NewMessage(chats=fromChat))
async def event_handler(event):
    source_channel = await client.get_entity(fromchat)
    destination_channel = await client.get_entity(toChat)
    messages = await client.get_messages(source_channel,limit=1)
    for x in messages:
        print(x.text)
    await client.forward_messages(destination_channel,messages)

client.start()
client.run_until_disconnected()
async def main():
    me = await client.get_me()
   

