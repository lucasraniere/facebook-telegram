from telethon import TelegramClient, events, sync

api_id = '17552079'
api_hash = '9b853f9b09b1fde9f89457b61f65db80'

clt = TelegramClient('Lucas_Raniere', api_id, api_hash)
clt.start()
