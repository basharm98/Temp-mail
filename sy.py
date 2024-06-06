from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant

app = Client(
    "subscription",
    api_id="25829176",
    api_hash="160b2bf653ee7dd974bd6d09a7968cd1",
    bot_token="6841893746:AAEw6rjO14pLOI12h1YY4DzqER39WtY-gd0"
)

channel = "R_O_L_I_X_5"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("- اشتراك -", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"عذرًا عزيزي [{user}](tg://openmessage?user_id={user_id}) عليك الإشتراك بقناة البوت أولا.",
        reply_markup = markup
    )
    
if __name__ == "__main__": app.run()