from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,

)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    filters,
    MessageHandler,

)

import os
import requests
import logging

from warnings import filterwarnings
from telegram.warnings import PTBUserWarning

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


TELEGRAM_BOT_TOKEN = ''
VIDEO_FILE_PATH = 'video/video.mp4'
AUDIO_FILE_PATH = 'audio/audio.mp3'
CHANNEL_LINK = 'https://t.me/prmngr'
CHANNEL_USERNAME = '@prmngr'

_bots = """
🤖 Bizning Botlar:

    👉 @tiktokwatermark_removerBot
    👉 @music_recognizerBot
    👉 @musicfindmebot
    👉 @anonyiobot
    👉 @usellbuybot
    👉 @thesaver_bot
    
📞 Contact: @abdibrokhim
📞 Contact: @contactdevsbot

📢 Channel: @prmngr

👻 Developer: @abdibrokhim
"""

_ads = """
🗣 Biz bilan bog\'lanish uchun:

    🤖 @contactdevsbot
    👻 @abdibrokhim
    
🗣 Bizning kanal: @prmngr
🗣 Reklama: @prmngr
🗣 Yangiliklar: @prmngr

🗣 Xullas hamma narsa shetda, krurasila 💩: @prmngr
"""


(MAIN,
 INSTAGRAM,
 INSTAGRAM_POST,
 INSTAGRAM_REEL,
 INSTAGRAM_STORY,
 ) = range(5)


async def ads_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text=_ads)


async def bots_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text=_bots)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('↗️ Kanalga go', url=CHANNEL_LINK)]])

    await update.message.reply_text("Assalomu alaykum, {}!".format(user.first_name))
    await update.message.reply_text(
        "Botga xush kelibsiz\n\nBotdan foydalanish uchun /menu bosing\n\n⬇️ Kanalimizga obuna bo'ling! ⬇️",
        reply_markup=reply_markup)


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # member = await context.bot.getChatMember(chat_id=CHANNEL_USERNAME, user_id=update.effective_user.id)

    buttons = [
        [
            KeyboardButton(text="🟣 Instagram", ),
        ],
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await update.message.reply_text(
        "Quyidagi ko'rsatilgan menyudan o'zingizga kerakli bo'limni tanlang\n\nReklama /ads, Botlar /bots",
        reply_markup=reply_markup)

    return MAIN


async def instagram_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [
            KeyboardButton(text="🟣 Post", ),
        ],
        [
            KeyboardButton(text="🟣 Reel", ),
        ],
        [
            KeyboardButton(text="🟣 Stories", ),
        ],
        [
            KeyboardButton(text="🔙 Orqaga", ),
        ],
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await update.message.reply_text("Quyidagi ko'rsatilgan menyudan o'zingizga kerakli bo'limni tanlang",
                                    reply_markup=reply_markup)

    return INSTAGRAM


async def instagram_post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Instagram post linkini yuboring",
                                    reply_markup=ReplyKeyboardMarkup([
                                        ["🔙️ Orqaga"]],
                                        resize_keyboard=True))

    return INSTAGRAM_POST


async def instagram_reel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Instagram reel linkini yuboring",
                                    reply_markup=ReplyKeyboardMarkup([
                                        ["🔙️ Orqaga"]],
                                        resize_keyboard=True))
    return INSTAGRAM_REEL


async def instagram_story_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Instagram story linkini yuboring",
                                    reply_markup=ReplyKeyboardMarkup([
                                        ["🔙️ Orqaga"]],
                                        resize_keyboard=True))
    return INSTAGRAM_STORY


async def instagram_post_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    link = update.message.text
    print(link)

    if link != '':
        await update.message.reply_text(text='🔎 Izlanmoqda...')
        url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/index"

        querystring = {"url": link}

        headers = {
            "X-RapidAPI-Key": "abdcae06e1msh6684906bfdbf574p134a43jsne849763a8cb4",
            "X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        result = response.json()

        try:
            for i in result['media']:
                await update.message.reply_photo(photo=i)
        except Exception as e:
            print(e)
            await update.message.reply_photo(photo=result['media'], write_timeout=100)
    else:
        await update.message.reply_text(text='Linkingizni yuboring')

    return INSTAGRAM


async def instagram_reel_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    link = update.message.text
    print(link)

    if link != '':
        await update.message.reply_text(text='🔎 Izlanmoqda...')
        url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/index"

        querystring = {"url": link}

        headers = {
            "X-RapidAPI-Key": "abdcae06e1msh6684906bfdbf574p134a43jsne849763a8cb4",
            "X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        result = response.json()

        try:
            response = requests.get(result['media'])
            with open(VIDEO_FILE_PATH, 'wb') as f:
                f.write(response.content)

            await update.message.reply_video(video=open(VIDEO_FILE_PATH, 'rb'), write_timeout=1000)

            os.remove(VIDEO_FILE_PATH)
        except Exception as e:
            print(e)
            await update.message.reply_text(text='Bu linkda hech narsa yo\'q')
    else:
        await update.message.reply_text(text='Linkingizni yuboring')

    return INSTAGRAM


async def instagram_story_link_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    link = update.message.text
    print(link)

    if link != '':
        await update.message.reply_text(text='🔎 Izlanmoqda...')
        url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/story/index"

        querystring = {"url": link}

        headers = {
            "X-RapidAPI-Key": "abdcae06e1msh6684906bfdbf574p134a43jsne849763a8cb4",
            "X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        result = response.json()
        try:
            for i in result['stories']:
                if i['type'] == 'Image':
                    await update.message.reply_photo(photo=i['media'], write_timeout=100)
                if i['type'] == 'Video':
                    response = requests.get(i['media'])
                    with open(VIDEO_FILE_PATH, 'wb') as f:
                        f.write(response.content)

                    await update.message.reply_video(video=open(VIDEO_FILE_PATH, 'rb'), write_timeout=1000)

                    os.remove(VIDEO_FILE_PATH)
        except Exception as e:
            print(e)
            if result['type'] == 'Image':
                await update.message.reply_photo(photo=result['media'], write_timeout=100)
            if result['type'] == 'Video':
                response = requests.get(result['media'])
                with open(VIDEO_FILE_PATH, 'wb') as f:
                    f.write(response.content)

                await update.message.reply_video(video=open(VIDEO_FILE_PATH, 'rb'), write_timeout=1000)

                os.remove(VIDEO_FILE_PATH)
    else:
        await update.message.reply_text(text='Linkingizni yuboring')

    return INSTAGRAM


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bekor qilindi")
    await update.message.reply_text("Qaytadan boshlash uchun\n/start ni bosing", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).read_timeout(100).get_updates_read_timeout(100).build()
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start_handler),
            CommandHandler('menu', menu_handler),
        ],
        states={
            MAIN: [
                MessageHandler(filters.Regex(".*Instagram$"), instagram_handler),
            ],
            INSTAGRAM: [
                MessageHandler(filters.Regex(".*Post$"), instagram_post_handler),
                MessageHandler(filters.Regex(".*Reel$"), instagram_reel_handler),
                MessageHandler(filters.Regex(".*Stories$"), instagram_story_handler),
                MessageHandler(filters.Regex(".*Orqaga$"), menu_handler),
            ],
            INSTAGRAM_POST: [
                MessageHandler(filters.Regex(".*Orqaga$"), instagram_handler),
                MessageHandler(filters.TEXT & (~filters.COMMAND), instagram_post_link_handler)
            ],
            INSTAGRAM_REEL: [
                MessageHandler(filters.Regex(".*Orqaga$"), instagram_handler),
                MessageHandler(filters.TEXT & (~filters.COMMAND), instagram_reel_link_handler)
            ],
            INSTAGRAM_STORY: [
                MessageHandler(filters.Regex(".*Orqaga$"), instagram_handler),
                MessageHandler(filters.TEXT & (~filters.COMMAND), instagram_story_link_handler)
            ],
        },
        fallbacks=[
            CommandHandler('cancel', cancel_handler),
            CommandHandler('start', start_handler),
            CommandHandler('menu', menu_handler),
            CommandHandler('instagram', instagram_handler),
            CommandHandler('ads', ads_handler),
            CommandHandler('bots', bots_handler),
        ],
    )
    app.add_handler(conv_handler)

    print("updated...")
    app.run_polling()
