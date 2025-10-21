# Bot Telegram Cuaca Pekanbaru

Bot yang dapat mengambil data hasil analysis perkiraan cuaca di BMKG melalui API, bot yang dapat di gunakan melalui aplikasi/app telegram untuk bertanya mengenai cuaca dini hari hingga prediksi cuaca 3 hari dan 7 hari.

Bot yang di rancang melalui program python dan menggunakan framework php yang di gunakan untuk mengelola backend.

---

## 📋 Dependensi dan Library

### Core Dependencies
Berikut adalah library utama yang perlu di install untuk menjalankan python:

```
python-telegram-bot==20.7
requests==2.31.0
aiohttp==3.9.1
python-dotenv==1.0.0
```

### Dependencies dari python-telegram-bot
```
anyio==4.1.0
certifi==2023.11.17
charset-normalizer==3.3.2
frozenlist==1.4.0
h11==0.14.0
httpcore==1.0.2
httpx==0.25.2
idna==3.6
multidict==6.0.4
sniffio==1.3.0
urllib3==2.1.0
yarl==1.9.4
```

### Timezone
```
pytz==2023.3
```

---

## 🚀 Cara Menjalankan dan Uji Coba

### Menjalankan Bot Python
Masuk ke folder `python-bot` dan jalankan di bash:

```bash
python run.py
```

### Menjalankan Backend PHP
Pada bash ke dua, jalankan:

```bash
php artisan migration
php artisan serve
```

---

## 📦 Instalasi

1. Clone repository ini
2. Install dependencies Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Install dependencies PHP (Laravel):
   ```bash
   composer install
   ```
4. Setup file `.env` untuk konfigurasi bot dan database
5. Jalankan migrasi database dan start service sesuai panduan di atas

---

## 🌤️ Fitur

- ☀️ Cuaca dini hari
- 📅 Prediksi cuaca 3 hari
- 📆 Prediksi cuaca 7 hari
- 🔄 Data real-time dari API BMKG
- 📱 Akses mudah melalui Telegram

---

## 🛠️ Teknologi

- **Bot**: Python 3.x dengan python-telegram-bot
- **Backend**: PHP dengan Laravel Framework
- **API**: BMKG Weather API
- **Database**: MySQL

## 👤 Author

[Raidit Akbar]
