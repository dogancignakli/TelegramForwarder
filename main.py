from telethon import TelegramClient,events

api_id = 3932493
api_hash = '04c9d06a0d44124fec4213db770fb7f7'
client = TelegramClient('DoganSlx', api_id, api_hash)
coinlegs = 882632305
yevmiyeciler = 'https://t.me/joinchat/IudzGql11hEwDNqm'

@client.on(events.NewMessage(chats=coinlegs))
async def event_handler(event):
    source_channel = await client.get_entity(coinlegs)
    destination_channel = await client.get_entity(yevmiyeciler)
    messages = await client.get_messages(source_channel,limit=1)
    for x in messages:
        print(x.text)
    #await client.send_message(destination_channel,message="HelloFromDoganSLX1.6")
    await client.forward_messages(destination_channel,messages)

client.start()
client.run_until_disconnected()
    # await client.send_message(destination_channel,message="HelloFromDoganSLX1.6")
    # await client.forward_messages(destination_channel,messages)

#     global chat
#     global sender
#     global chat_id
#     global sender_id
#     chat = await event.get_chat()
#     sender = await event.get_sender()
#     chat_id = event.chat_id
#     sender_id = event.sender_id



async def main():
    me = await client.get_me()
    #print(me.stringify())

    # async for dialog in client.iter_dialogs():
    #     print(dialog.name,'has ID',dialog.id)
   # await client.send_message(1001364508253,'Telethon Python API Test')
   # source_channel  = await client.get_entity(sender)
    #destination_channel = await client.get_entity('https://t.me/joinchat/IudzGql11hEwDNqm')
    # messages = await client.get_messages(source_channel,limit=1)
    # for x in messages:
    #     print(x.text)
   # await client.send_message(destination_channel,message="HelloFromDoganSLX1.6")
   # await client.forward_messages(destination_channel,messages)




