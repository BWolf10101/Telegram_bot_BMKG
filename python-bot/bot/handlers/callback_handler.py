from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.services.api_service import ApiService
from bot.services.formatter_service import FormatterService

api_service = ApiService()
formatter = FormatterService()

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk button callback"""
    query = update.callback_query

    # Handle different callbacks
    if query.data == 'back':
        await query.answer()
        return await back_to_main_menu(query)

    if query.data == 'back_to_location_menu':
        await query.answer()
        from bot.handlers.location_handler import back_to_location_menu
        return await back_to_location_menu(update, context)

    if query.data == 'choose_district':
        await query.answer()
        from bot.handlers.location_handler import choose_district_handler
        return await choose_district_handler(update, context)

    if query.data.startswith('district_'):
        await query.answer()
        from bot.handlers.location_handler import district_selected_handler
        return await district_selected_handler(update, context)

    if query.data == 'search_location':
        from bot.handlers.location_handler import search_location_handler
        return await search_location_handler(update, context)

    if query.data == 'all_locations':
        await query.answer()
        from bot.handlers.location_handler import all_locations_handler
        return await all_locations_handler(update, context)

    if query.data.startswith('setloc_'):
        await query.answer()
        from bot.handlers.location_handler import set_location_handler
        return await set_location_handler(update, context)

    # Weather callbacks
    await query.answer()
    await query.edit_message_text("⏳ Mengambil data cuaca...")

    user_id = update.effective_user.id

    if query.data == 'today':
        data = api_service.get_today_weather(user_id)
        if data and data.get('success'):
            response = formatter.format_today(data)
        else:
            response = "❌ Gagal mengambil data cuaca. Pastikan Anda sudah memilih lokasi."

    elif query.data == 'forecast_7':
        data = api_service.get_forecast(7, user_id)
        if data and data.get('success'):
            response = formatter.format_forecast(data, 7)
        else:
            response = "❌ Gagal mengambil data cuaca. Pastikan Anda sudah memilih lokasi."

    elif query.data == 'forecast_3':
        data = api_service.get_forecast(3, user_id)
        if data and data.get('success'):
            response = formatter.format_forecast(data, 3)
        else:
            response = "❌ Gagal mengambil data cuaca. Pastikan Anda sudah memilih lokasi."

    else:
        response = "❌ Pilihan tidak valid"

    keyboard = [
        [InlineKeyboardButton("🔙 Kembali ke Menu", callback_data='back')],
        [InlineKeyboardButton("📍 Ubah Lokasi", callback_data='choose_district')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        response,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def back_to_main_menu(query):
    """Kembali ke menu utama"""
    user_id = query.from_user.id

    # Cek lokasi user
    current_location = api_service.get_user_location(user_id)
    location_msg = ""

    if current_location and current_location.get('success'):
        loc = current_location['data']['location']
        location_msg = f"\n\n📍 Lokasi: {loc['name']}, Kec. {loc['district']}"
    else:
        location_msg = "\n\n⚠️ Belum ada lokasi terpilih. Gunakan /pilihlokasi"

    keyboard = [
        [InlineKeyboardButton("🌤 Cuaca Hari Ini", callback_data='today')],
        [InlineKeyboardButton("📅 Prakiraan 7 Hari", callback_data='forecast_7')],
        [InlineKeyboardButton("📅 Prakiraan 3 Hari", callback_data='forecast_3')],
        [InlineKeyboardButton("📍 Pilih Lokasi", callback_data='choose_district')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"Pilih menu cuaca:{location_msg}",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
