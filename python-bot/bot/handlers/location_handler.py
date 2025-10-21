from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from bot.services.api_service import ApiService

api_service = ApiService()

# States untuk conversation
CHOOSING_DISTRICT, CHOOSING_LOCATION, SEARCHING = range(3)

async def pilih_lokasi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /pilihlokasi"""
    user_id = update.effective_user.id

    # Cek lokasi user saat ini
    current_location = api_service.get_user_location(user_id)

    current_msg = ""
    if current_location and current_location.get('success'):
        loc = current_location['data']['location']
        current_msg = f"\n📍 *Lokasi saat ini:* {loc['name']}, Kec. {loc['district']}\n"

    keyboard = [
        [InlineKeyboardButton("📍 Pilih Kecamatan", callback_data='choose_district')],
        [InlineKeyboardButton("🔍 Cari Lokasi", callback_data='search_location')],
        [InlineKeyboardButton("📋 Lihat Semua Lokasi", callback_data='all_locations')],
        [InlineKeyboardButton("🔙 Kembali", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    msg = (
        f"🗺 *Pengaturan Lokasi*{current_msg}\n"
        "Pilih cara untuk mengatur lokasi Anda:"
    )

    await update.message.reply_text(
        msg,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def choose_district_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tampilkan daftar kecamatan"""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("⏳ Mengambil daftar kecamatan...")

    # Ambil semua lokasi dan kelompokkan per kecamatan
    locations_data = api_service.get_locations()

    if not locations_data or not locations_data.get('success'):
        await query.edit_message_text("❌ Gagal mengambil data lokasi. Silakan coba lagi.")
        return

    locations = locations_data['data']
    districts = {}

    for loc in locations:
        district = loc['district']
        if district not in districts:
            districts[district] = []
        districts[district].append(loc)

    # Buat keyboard dengan daftar kecamatan
    keyboard = []
    for district in sorted(districts.keys()):
        count = len(districts[district])
        keyboard.append([
            InlineKeyboardButton(
                f"{district} ({count} lokasi)",
                callback_data=f"district_{district}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data='back_to_location_menu')])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "📍 *Pilih Kecamatan:*",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def district_selected_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler ketika kecamatan dipilih"""
    query = update.callback_query
    await query.answer()

    district_name = query.data.replace('district_', '')

    await query.edit_message_text("⏳ Mengambil daftar kelurahan...")

    # Ambil lokasi untuk kecamatan ini
    locations_data = api_service.get_locations()

    if not locations_data or not locations_data.get('success'):
        await query.edit_message_text("❌ Gagal mengambil data lokasi")
        return

    locations = [loc for loc in locations_data['data'] if loc['district'] == district_name]

    # Buat keyboard dengan daftar kelurahan
    keyboard = []
    for loc in locations:
        keyboard.append([
            InlineKeyboardButton(
                loc['name'],
                callback_data=f"setloc_{loc['id']}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data='choose_district')])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"📍 *Kecamatan {district_name}*\n\nPilih kelurahan:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def search_location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk pencarian lokasi"""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🔍 *Cari Lokasi*\n\n"
        "Ketik nama kelurahan atau kecamatan yang ingin Anda cari.\n"
        "Contoh: `Tampan`, `Marpoyan`, `Binawidya`\n\n"
        "Ketik /batal untuk membatalkan.",
        parse_mode='Markdown'
    )

    return SEARCHING

async def process_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Proses pencarian lokasi"""
    keyword = update.message.text

    if keyword.lower() == '/batal':
        await update.message.reply_text("❌ Pencarian dibatalkan")
        return ConversationHandler.END

    # Cari lokasi
    result = api_service.search_locations(keyword)

    if not result or not result.get('success'):
        await update.message.reply_text(
            f"❌ Tidak ditemukan lokasi dengan kata kunci: *{keyword}*\n\n"
            "Coba kata kunci lain atau ketik /batal",
            parse_mode='Markdown'
        )
        return SEARCHING

    locations = result['data']

    if len(locations) == 0:
        await update.message.reply_text(
            f"❌ Tidak ditemukan lokasi dengan kata kunci: *{keyword}*\n\n"
            "Coba kata kunci lain atau ketik /batal",
            parse_mode='Markdown'
        )
        return SEARCHING

    # Buat keyboard dengan hasil pencarian
    keyboard = []
    for loc in locations:
        keyboard.append([
            InlineKeyboardButton(
                f"{loc['name']}, Kec. {loc['district']}",
                callback_data=f"setloc_{loc['id']}"
            )
        ])

    keyboard.append([InlineKeyboardButton("🔙 Batal", callback_data='back_to_location_menu')])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🔍 Hasil pencarian untuk *{keyword}*:\n\nPilih lokasi:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

    return ConversationHandler.END

async def all_locations_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tampilkan semua lokasi"""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("⏳ Mengambil daftar lokasi...")

    locations_data = api_service.get_locations()

    if not locations_data or not locations_data.get('success'):
        await query.edit_message_text("❌ Gagal mengambil data lokasi")
        return

    locations = locations_data['data']

    # Kelompokkan per kecamatan
    districts = {}
    for loc in locations:
        district = loc['district']
        if district not in districts:
            districts[district] = []
        districts[district].append(loc)

    # Buat pesan dengan daftar semua lokasi
    msg = "📋 *Daftar Semua Lokasi*\n\n"

    for district in sorted(districts.keys()):
        msg += f"*{district}:*\n"
        for loc in districts[district]:
            msg += f"  • {loc['name']}\n"
        msg += "\n"

    msg += "\nGunakan /pilihlokasi untuk memilih lokasi Anda."

    # Split message jika terlalu panjang
    if len(msg) > 4000:
        chunks = [msg[i:i+4000] for i in range(0, len(msg), 4000)]
        for chunk in chunks:
            await query.message.reply_text(chunk, parse_mode='Markdown')
    else:
        await query.edit_message_text(msg, parse_mode='Markdown')

async def set_location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set lokasi user"""
    query = update.callback_query
    await query.answer()

    location_id = int(query.data.replace('setloc_', ''))
    user_id = update.effective_user.id

    await query.edit_message_text("⏳ Menyimpan lokasi...")

    # Set lokasi user
    result = api_service.set_user_location(user_id, location_id)

    if not result or not result.get('success'):
        await query.edit_message_text("❌ Gagal menyimpan lokasi. Silakan coba lagi.")
        return

    loc = result['data']['location']

    keyboard = [
        [InlineKeyboardButton("🌤 Lihat Cuaca", callback_data='today')],
        [InlineKeyboardButton("🔙 Menu Utama", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"✅ *Lokasi berhasil disimpan!*\n\n"
        f"📍 {loc['name']}, Kec. {loc['district']}\n"
        f"🏙 {loc['city']}, {loc['province']}\n\n"
        "Sekarang Anda akan mendapatkan informasi cuaca untuk lokasi ini.",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def back_to_location_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kembali ke menu lokasi"""
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    current_location = api_service.get_user_location(user_id)

    current_msg = ""
    if current_location and current_location.get('success'):
        loc = current_location['data']['location']
        current_msg = f"\n📍 *Lokasi saat ini:* {loc['name']}, Kec. {loc['district']}\n"

    keyboard = [
        [InlineKeyboardButton("📍 Pilih Kecamatan", callback_data='choose_district')],
        [InlineKeyboardButton("🔍 Cari Lokasi", callback_data='search_location')],
        [InlineKeyboardButton("📋 Lihat Semua Lokasi", callback_data='all_locations')],
        [InlineKeyboardButton("🔙 Kembali", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    msg = (
        f"🗺 *Pengaturan Lokasi*{current_msg}\n"
        "Pilih cara untuk mengatur lokasi Anda:"
    )

    await query.edit_message_text(
        msg,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def lokasi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /lokasi - lihat lokasi saat ini"""
    user_id = update.effective_user.id

    current_location = api_service.get_user_location(user_id)

    if not current_location or not current_location.get('success'):
        keyboard = [
            [InlineKeyboardButton("📍 Pilih Lokasi", callback_data='choose_district')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "❌ Anda belum mengatur lokasi.\n\n"
            "Gunakan tombol di bawah atau ketik /pilihlokasi untuk memilih lokasi.",
            reply_markup=reply_markup
        )
        return

    loc = current_location['data']['location']

    keyboard = [
        [InlineKeyboardButton("🌤 Lihat Cuaca", callback_data='today')],
        [InlineKeyboardButton("📍 Ubah Lokasi", callback_data='choose_district')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"📍 *Lokasi Anda Saat Ini:*\n\n"
        f"🏘 {loc['name']}\n"
        f"🏙 Kec. {loc['district']}\n"
        f"📍 {loc['city']}, {loc['province']}\n"
        f"🔢 Kode: `{loc['code']}`",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
