import os
import psutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

API_ID = 30643923
API_HASH = "7646ef13834d9dfaa75fa34c7385ba92"
BOT_TOKEN = "8923773279:AAGCZtNC8c9etrJXskBvxbLbYTf0M1KKzII"

app = Client("my_music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    caption = (
        f"——「 <b>Coffee Pupu Music🎧</b> 」——\n\n"
        f"Holaa {message.from_user.first_name} !!\n\n"
        f"I Am The Fast And Powerful Music Player Bot With Some Awesome Features.\n\n"
        f"➡️ <b>Uptime:</b> 16h:38m:0s\n"
        f"➡️ <b>Server Storage:</b> {disk}%\n"
        f"➡️ <b>CPU Load:</b> {cpu}%\n"
        f"➡️ <b>RAM Consumption:</b> {ram}%\n\n"
        f"Click On The Help Button To Get Information About My Modules And Commands."
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Add Me In Your Group", url="https://t.me/your_bot_username?startgroup=true")],
        [InlineKeyboardButton("Help And Commands", callback_data="help_menu")],
        [
            InlineKeyboardButton("Owner", url="https://t.me/owner_username"),
            InlineKeyboardButton("Support", url="https://t.me/support_chat")
        ],
        [
            InlineKeyboardButton("Channel", url="https://t.me/channel_username"),
            InlineKeyboardButton("Source Code", url="https://github.com/your-repo")
        ]
    ])
    
    photo_url = "https://files.catbox.moe/example.jpg"
    
    await message.reply_photo(
        photo=photo_url,
        caption=caption,
        reply_markup=buttons
    )

async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    web_app = web.Application()
    web_app.add_routes([web.get("/", handle)])
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 8080)))
    await site.start()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(web_server())
    print("Bot is running on Cloud...")
    app.run()
  
