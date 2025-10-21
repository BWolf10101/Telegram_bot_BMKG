from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.services.api_service import ApiService

api_service = ApiService()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /start"""
    user_id = update.effective_user.id

    # Cek apakah user sudah set lokasi
    current_location = api_service.get_user_location(user_id)

    location_msg = ""
    if current_location and current_location.get('success'):
        loc = current_location['data']['location']
        location_msg = f"\n\n📍 Lokasi Anda: {loc['name']}, Kec. {loc['district']}"
    else:
        location_msg = "\n\n⚠️ Anda belum memilih lokasi. Pilih lokasi terlebih dahulu!"

    keyboard = [
        [InlineKeyboardButton("🌤 Cuaca Hari Ini", callback_data='today')],
        [InlineKeyboardButton("📅 Prakiraan 7 Hari", callback_data='forecast_7')],
        [InlineKeyboardButton("📅 Prakiraan 3 Hari", callback_data='forecast_3')],
        [InlineKeyboardButton("📍 Pilih Lokasi", callback_data='choose_district')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_msg = (
        "👋 Selamat datang di *Bot Cuaca BMKG Pekanbaru*!\n\n"
        "Saya dapat memberikan informasi cuaca dan prakiraan cuaca "
        "untuk berbagai lokasi di Kota Pekanbaru dari BMKG."
        f"{location_msg}\n\n"
        "*Perintah yang tersedia:*\n"
        "/start - Menu utama\n"
        "/cuaca - Cuaca hari ini\n"
        "/prakiraan - Prakiraan 7 hari\n"
        "/pilihlokasi - Pilih lokasi\n"
        "/lokasi - Lihat lokasi saat ini"
    )

    await update.message.reply_text(
        welcome_msg,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
