from telegram import Update
from telegram.ext import ContextTypes
from bot.services.api_service import ApiService
from bot.services.formatter_service import FormatterService

api_service = ApiService()
formatter = FormatterService()

async def cuaca_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /cuaca"""
    await update.message.reply_text("⏳ Mengambil data cuaca...")

    user_id = update.effective_user.id
    data = api_service.get_today_weather(user_id)

    if not data or not data.get('success'):
        await update.message.reply_text(
            "❌ Gagal mengambil data cuaca. Silakan coba lagi."
        )
        return

    response = formatter.format_today(data)
    await update.message.reply_text(response, parse_mode='Markdown')

async def prakiraan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /prakiraan"""
    await update.message.reply_text("⏳ Mengambil data prakiraan cuaca...")

    user_id = update.effective_user.id
    data = api_service.get_forecast(7, user_id)

    if not data or not data.get('success'):
        await update.message.reply_text(
            "❌ Gagal mengambil data cuaca. Silakan coba lagi."
        )
        return

    response = formatter.format_forecast(data, 7)
    await update.message.reply_text(response, parse_mode='Markdown')
