# 🚀 APK Builder Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Termux](https://img.shields.io/badge/platform-Termux-green.svg)](https://termux.com/)
[![GitHub Actions](https://img.shields.io/badge/build-GitHub%20Actions-brightgreen.svg)](https://github.com/features/actions)

Build Android APK langsung dari Termux **tanpa perlu install Java**! Tool ini menggunakan GitHub Actions sebagai cloud builder, jadi perangkat kamu tidak akan berat.

> 🎯 **Perfect for:** Web developers, Termux users, students, hobbyists who want to convert web apps to Android APK without complex setup!

## ✨ Fitur

- 📱 **Build APK** dari project HTML atau React
- 🔐 **Keystore Manager** untuk sign APK
- ☁️ **Cloud Build** menggunakan GitHub Actions (gratis!)
- 🎨 **Kustomisasi lengkap** (nama, icon, permissions, dll)
- 🔒 **Autentikasi sederhana** untuk keamanan
- 📦 **Auto download** APK hasil build

## 🎯 Flowchart Proses Build

```
Mulai
  ↓
Pilih Jenis Proyek (HTML/React)
  ↓
Konfigurasi Proyek:
  - Nama & App ID
  - Versi
  - Icon
  - Permissions (30+ opsi)
  - Display Options
  ↓
Upload ke GitHub
  ↓
Build di Cloud (GitHub Actions)
  ↓
Download APK
  ↓
Selesai
```

## 📋 Persyaratan

### Di Termux

1. Python 3.8+
2. Git
3. Aplikasi Acode (opsional, untuk coding)

### Di GitHub

1. Akun GitHub (gratis)
2. Personal Access Token

## 🔧 Instalasi

### 1. Install di Termux

```bash
# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install python git -y

# Clone repository
git clone https://github.com/daffa-aditya-p/apk-builder.git
cd apk-builder

# Install Python dependencies
pip install -r requirements.txt

# Buat executable
chmod +x build-apk
```

### 2. Setup GitHub Token

1. Buka: https://github.com/settings/tokens
2. Klik **"Generate new token"** → **"Generate new token (classic)"**
3. Beri nama: `APK Builder`
4. Pilih scope: **✅ repo** (full control of private repositories)
5. Klik **"Generate token"**
6. **Copy** token yang muncul (hanya muncul sekali!)

## 🎮 Cara Penggunaan

### Jalankan Tool

```bash
./build-apk
```

atau

```bash
python build-apk
```

### 1. Autentikasi

Saat pertama kali, login dengan:
- **Username**: `Daffa`
- **Password**: `daffajago123`

Atau buat akun baru dengan memilih **Register**.

### 2. Menu Utama

```
1. 📦 Build APK        - Build APK dari project
2. ✍️  Sign APK        - Sign APK dengan keystore
3. 🔑 Buat Keystore    - Buat keystore baru
4. 📋 Lihat Keystore   - Lihat daftar keystore
5. ⚙️  Setup GitHub     - Setup GitHub token
6. 📊 Cek Status       - Cek progress build
7. 📥 Download APK     - Download hasil build
8. 🚪 Logout           - Keluar dari akun
9. ❌ Keluar           - Tutup aplikasi
```

## 📱 Build APK - Tutorial Lengkap

### Step 1: Setup GitHub Token (Sekali saja)

1. Pilih menu **5. Setup GitHub**
2. Paste token yang sudah kamu copy
3. Tool akan otomatis validasi token

### Step 2: Siapkan Project

Project harus di folder Acode (atau folder lain yang mudah diakses):

```
/sdcard/Acode/myproject/
├── index.html
├── style.css
├── script.js
├── assets/
│   ├── logo.png
│   └── images/
└── ...
```

### Step 3: Build APK

1. Pilih menu **1. Build APK**

2. **Pilih jenis project:**
   ```
   1. HTML (Static Web)
   2. React
   ```

3. **Masukkan lokasi project:**
   ```
   /sdcard/Acode/myproject
   ```

4. **Konfigurasi aplikasi:**
   
   - **Nama Aplikasi**: `My Awesome App`
   - **App ID**: `com.mycompany.awesomeapp`
     - Format: `com.namaperusahaan.namaapp`
     - Harus unik!
   
   - **Versi**: `1.0.0`
   - **Version Code**: `1` (angka, naik setiap update)
   
   - **Icon**: `/sdcard/Acode/myproject/icon.png`
     - Kosongkan untuk default
     - Rekomendasi: 512x512 px

5. **Pilih Permissions:**

   Masukkan nomor permission yang dibutuhkan (pisahkan dengan koma):
   
   ```
   Contoh: 1,2,6,7,18
   ```

   **Daftar Lengkap Permissions:**

   | No | Permission | Keterangan |
   |----|-----------|------------|
   | 1  | Internet | Akses internet |
   | 2  | Kamera | Gunakan kamera |
   | 3  | Audio/Mic | Rekam audio |
   | 4  | GPS | Lokasi akurat |
   | 5  | Network Location | Lokasi dari jaringan |
   | 6  | Read Storage | Baca file |
   | 7  | Write Storage | Tulis file |
   | 8  | Read Contacts | Baca kontak |
   | 9  | Write Contacts | Edit kontak |
   | 10 | Read Calendar | Baca kalender |
   | 11 | Write Calendar | Edit kalender |
   | 12 | Send SMS | Kirim SMS |
   | 13 | Phone State | Status telepon |
   | 14 | Call Phone | Panggil telepon |
   | 15 | Read Notifications | Akses notifikasi |
   | 16 | WiFi State | Info WiFi |
   | 17 | Change WiFi | Ubah WiFi |
   | 18 | Network State | Status jaringan |
   | 19 | Read SMS | Baca SMS |
   | 20 | Receive SMS | Terima SMS |
   | 21 | Vibrate | Getaran |
   | 22 | Bluetooth | Koneksi Bluetooth |
   | 23 | Bluetooth Admin | Kelola Bluetooth |
   | 24 | Boot Completed | Jalankan saat boot |
   | 25 | Foreground Service | Service foreground |
   | 26 | Wake Lock | Cegah sleep |
   | 27 | Install Packages | Install app |
   | 28 | Read Logs | Baca log sistem |
   | 29 | Body Sensors | Sensor tubuh |
   | 30 | Call Log | Riwayat panggilan |

6. **Display Options:**
   
   - **Orientasi:**
     - 1 = Portrait (vertikal)
     - 2 = Landscape (horizontal)
     - 3 = Auto
   
   - **Fullscreen:** y/n
   - **Status Bar:** y/n

7. **Review & Konfirmasi**
   
   Tool akan menampilkan ringkasan konfigurasi.
   Ketik `y` untuk melanjutkan.

8. **Build Process:**
   
   Tool akan:
   - ✅ Upload file ke GitHub
   - ✅ Trigger build di GitHub Actions
   - ✅ Tampilkan link untuk monitor progress

### Step 4: Monitor Build

1. Tunggu 5-10 menit
2. Pilih menu **6. Cek Status Build**
3. Atau buka link yang ditampilkan di browser

### Step 5: Download APK

1. Setelah build selesai
2. Pilih menu **7. Download APK**
3. APK akan tersimpan di:
   ```
   ~/apk-builds/NamaApp-1.0.0.zip
   ```
4. Extract file zip untuk mendapatkan APK

## 🔑 Keystore Management

### Buat Keystore Baru

1. Pilih menu **3. Buat Keystore**
2. Masukkan informasi:
   - Nama keystore: `myapp`
   - Alias: `myapp-key`
   - Password: (min 6 karakter)
   - Info developer (opsional)

### Sign APK

1. Pilih menu **2. Sign APK**
2. Pilih keystore yang akan digunakan
3. Masukkan path APK yang akan di-sign
4. Tool akan menampilkan command untuk sign manual

> **Note:** Sign APK memerlukan `apksigner` atau `jarsigner`. Di Termux, install dengan:
> ```bash
> pkg install apksigner
> ```

## 📁 Struktur Project

```
apk-builder/
├── build-apk              # Main executable
├── requirements.txt       # Python dependencies
├── src/
│   ├── auth.py           # Autentikasi
│   ├── config.py         # Konfigurasi APK
│   ├── permissions.py    # Daftar permissions
│   ├── keystore_manager.py  # Kelola keystore
│   └── github_builder.py # GitHub integration
├── .github/
│   └── workflows/
│       └── build-apk.yml # GitHub Actions workflow
└── README.md
```

## 🏗️ Cara Kerja

1. **Local (Termux):**
   - User input konfigurasi
   - Tool upload project ke GitHub repository
   - Trigger GitHub Actions workflow

2. **Cloud (GitHub Actions):**
   - Install Cordova & dependencies
   - Generate Android project
   - Configure permissions & settings
   - Build APK
   - Upload sebagai artifact

3. **Download:**
   - User download APK dari GitHub
   - Ready to install!

## 🔒 Keamanan & Privacy

- 🔐 Password di-hash dengan SHA-256
- 🗝️ GitHub token disimpan lokal di `~/.apk-builder/`
- 📦 Keystore disimpan aman di device
- 🚫 Tidak ada data yang dikirim ke server lain

## ❓ Troubleshooting

### Build gagal?

1. **Cek GitHub Actions:**
   ```
   https://github.com/username/apk-builds/actions
   ```

2. **Cek log error:**
   - Klik workflow yang gagal
   - Lihat step mana yang error
   - Perbaiki konfigurasi

### Permission error?

- Pastikan app memiliki permission yang sesuai
- Jangan pilih permission yang tidak diperlukan

### APK tidak bisa di-install?

- Enable "Install from Unknown Sources" di Android
- Cek signature APK
- Pastikan App ID unik

### GitHub token invalid?

1. Regenerate token di GitHub
2. Pilih menu **5. Setup GitHub**
3. Paste token yang baru

## 💡 Tips & Tricks

1. **Icon yang bagus:**
   - Gunakan ukuran 512x512 px
   - Format PNG dengan background transparan
   - Tools: Canva, Figma, GIMP

2. **App ID yang baik:**
   - Format: `com.namaanda.namaapp`
   - Lowercase, no spaces
   - Harus unik di Play Store

3. **Permissions minimal:**
   - Hanya pilih permission yang benar-benar dibutuhkan
   - Terlalu banyak permission = suspicious

4. **Testing:**
   - Test APK di device fisik
   - Cek semua fitur berfungsi
   - Fix bug sebelum publish

## 🤝 Kontribusi

Contributions are welcome! Silakan:

1. Fork repository
2. Buat branch baru
3. Commit changes
4. Push dan buat Pull Request

## 📝 License

MIT License - Bebas digunakan untuk project apapun!

## 👨‍💻 Author

**Daffa Aditya P**
- GitHub: [@daffa-aditya-p](https://github.com/daffa-aditya-p)

## 🙏 Credits

- Cordova - Framework untuk build hybrid app
- GitHub Actions - Free cloud builder
- Termux - Linux environment for Android

---

**Selamat membuat APK! 🎉**

Jika ada pertanyaan atau masalah, silakan buat issue di GitHub repository.
