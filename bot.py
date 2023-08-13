from aiogram import Bot, Dispatcher, types, executor
from config import BotConfig
import os
from messages import *
from datetime import datetime
from analytics import *
cfg = BotConfig(os.getenv("DOT_ENV_PATH", ".env"))

bot = Bot(token=cfg.token)
dp = Dispatcher(bot)
mygroup = Group(cfg.telegram_group_id, "Test")
# Define a command handler
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if int(message.from_id) == int(cfg.admin_tg_id):
        print("Message: ", message)
        await message.reply(welcome)
    else:
        await message.reply("Siz hozircha bu botdan foydalan olmaysiz.")

@dp.message_handler(commands=['analytics'])
async def analytics_command(message: types.Message):
    if int(message.from_id) == int(cfg.admin_tg_id):
        data = mygroup.get()
        res = GetAnalyticsMessage(data)
        await message.reply(res)
    else:
        await message.reply("Siz hozircha bu botdan foydalan olmaysiz.")

@dp.message_handler(content_types=types.ContentTypes.TEXT, chat_type=types.ChatType.GROUP)
async def handle_group_message(message: types.Message):
    print(message.chat.id)
    # print(message)
    if message['chat']['id'] != cfg.telegram_group_id:
        return
    messageToCreate = {
        "member": {
            "id":message['from']['id'],
            "username": message['from']['username']
        },
        "text":message["text"],
        "id": message["message_id"]
    }
    try:
        mygroup.addMessage(messageToCreate)
        mygroup.save()
    except Exception as ex:
        print("error while adding message and saving",ex)



# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)   
    except Exception:
        print("Good bye")