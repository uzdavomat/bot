import  asyncio
from  aiogram import  Bot,Dispatcher
from aiogram.types import  Message
from  aiogram.filters import  CommandStart

TOKEN = "8526293245:AAHI7InyR8mzUbkdt1ohoPWLNSBmOy_Ugdc"
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: Message):
    await  message.answer('Salem')



async def main():
    await  dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

print('tamamlandi')





