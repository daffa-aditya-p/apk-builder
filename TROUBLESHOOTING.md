# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### 1. Installation Issues

#### Python packages tidak terinstall

**Gejala:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solusi:**
```bash
# Update pip
pip install --upgrade pip

# Install dengan opsi tambahan
pip install -r requirements.txt --user

# Atau manual satu-satu
pip install requests PyGithub cryptography pyyaml colorama
```

#### Permission denied saat install

**Gejala:**
```
Permission denied: ...
```

**Solusi:**
```bash
# Pastikan file executable
chmod +x install.sh
chmod +x build-apk

# Atau gunakan prefix pkg
pkg install python git
```

---

### 2. Authentication Issues

#### Login gagal dengan kredensial default

**Gejala:**
```
❌ Password salah!
```

**Solusi:**
1. Cek lagi username & password:
   - Username: `Daffa`
   - Password: `daffajago123`
2. Case sensitive!
3. Atau register user baru

#### File session error

**Gejala:**
```
Error reading session file
```

**Solusi:**
```bash
# Reset session
rm ~/.apk-builder/session.json
rm ~/.apk-builder/users.json

# Restart tool
./build-apk
```

---

### 3. GitHub Token Issues

#### Token invalid

**Gejala:**
```
❌ Token tidak valid! Status: 401
```

**Solusi:**
1. Generate token baru di: https://github.com/settings/tokens
2. Pastikan pilih scope **`repo`** (full control)
3. Copy token **sebelum** menutup halaman
4. Paste di menu Setup GitHub

#### Token expired

**Gejala:**
```
Bad credentials
```

**Solusi:**
```bash
# Hapus token lama
rm ~/.apk-builder/github_token.txt

# Setup token baru
./build-apk
# Pilih: 5. Setup GitHub Token
```

---

### 4. Project Configuration Issues

#### Direktori project tidak ditemukan

**Gejala:**
```
❌ Direktori tidak ditemukan: /path/to/project
```

**Solusi:**
1. Pastikan path benar dan ada
2. Gunakan path absolute
3. Di Termux biasanya: `/sdcard/Acode/nama-project`
4. Cek dengan: `ls -la /sdcard/Acode/`

#### App ID tidak valid

**Gejala:**
```
❌ App ID tidak valid! (harus format: com.xxx.xxx)
```

**Solusi:**
- Format yang benar: `com.namaanda.namaapp`
- Contoh: `com.mycompany.myapp`
- Lowercase semua
- Tidak ada spasi
- Minimal 2 titik

#### Icon tidak ditemukan

**Gejala:**
```
⚠️  File icon tidak ditemukan
```

**Solusi:**
1. Pastikan path icon benar
2. Format yang didukung: PNG, JPG
3. Ukuran rekomendasi: 512x512 px
4. Atau skip (akan pakai icon default)

---

### 5. GitHub Actions Build Issues

#### Build gagal di GitHub Actions

**Gejala:**
Build status: `failed` atau `error`

**Solusi:**
1. Buka link GitHub Actions yang ditampilkan
2. Klik workflow yang gagal
3. Lihat log error di setiap step
4. Common causes:
   - File project tidak ter-upload
   - Config.xml error
   - Cordova build error
   - Permission/dependency issue

#### Tidak ada workflow yang triggered

**Gejala:**
```
Belum ada build yang dijalankan
```

**Solusi:**
1. Pastikan repository sudah dibuat
2. Cek di: `https://github.com/username/apk-builds`
3. Pastikan file `.github/workflows/build-apk.yml` ada
4. Trigger manual dari GitHub:
   - Go to Actions tab
   - Select workflow
   - Click "Run workflow"

#### Build terlalu lama

**Gejala:**
Build running lebih dari 15 menit

**Solusi:**
1. Normal: 5-10 menit
2. Cek status di GitHub Actions
3. Jika stuck, cancel dan retry:
   - Go to Actions
   - Click workflow
   - Cancel workflow
   - Trigger build ulang

---

### 6. Upload/Download Issues

#### Upload files gagal

**Gejala:**
```
❌ Gagal upload: 404 Not Found
```

**Solusi:**
1. Cek GitHub token masih valid
2. Cek repository exists
3. Cek koneksi internet
4. Retry upload

#### Download APK gagal

**Gejala:**
```
❌ Tidak ada artifact yang ditemukan
```

**Solusi:**
1. Pastikan build sudah selesai (status: success)
2. Cek di GitHub Actions → Artifacts
3. Download manual dari browser:
   ```
   https://github.com/username/apk-builds/actions
   ```
4. Artifact expire setelah 30 hari

#### File tidak ter-extract

**Gejala:**
APK download berupa ZIP

**Solusi:**
```bash
# Extract di Termux
cd ~/apk-builds
unzip NamaApp-1.0.0.zip

# APK ada di dalam ZIP
ls -la *.apk
```

---

### 7. Keystore Issues

#### Keytool tidak ditemukan

**Gejala:**
```
⚠️  Keytool tidak ditemukan
```

**Solusi:**
1. Normal di Termux (tidak ada Java)
2. Keystore akan dibuat otomatis saat build di cloud
3. Atau install Java di Termux (opsional):
   ```bash
   pkg install openjdk-17
   ```

#### Sign APK gagal

**Gejala:**
```
apksigner: command not found
```

**Solusi:**
```bash
# Install apksigner
pkg install apksigner

# Atau download manual dari Android SDK
```

---

### 8. Runtime Issues

#### Import error

**Gejala:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solusi:**
```bash
# Install ulang dependencies
pip install -r requirements.txt

# Atau spesifik
pip install module-name
```

#### Colorama tidak tersedia

**Gejala:**
Plain text tanpa warna

**Solusi:**
```bash
# Install colorama
pip install colorama

# Tool tetap berjalan tanpa colorama (fallback mode)
```

---

### 9. APK Installation Issues

#### APK tidak bisa di-install

**Gejala:**
"App not installed" atau "Parse error"

**Solusi:**
1. Enable "Install from Unknown Sources":
   - Settings → Security
   - Allow unknown sources
2. Cek APK tidak corrupt:
   - Size harus > 1 MB
   - Bukan file kosong
3. Uninstall versi lama dulu
4. Cek Android version compatibility

#### App crash saat dibuka

**Gejala:**
"App has stopped"

**Solusi:**
1. Cek log di Logcat:
   ```bash
   adb logcat
   ```
2. Cek permission di AndroidManifest
3. Test di emulator dulu
4. Debug JavaScript errors

---

### 10. Network Issues

#### Timeout saat upload/download

**Gejala:**
```
Connection timeout
```

**Solusi:**
1. Cek koneksi internet
2. Gunakan WiFi yang stabil
3. Retry beberapa kali
4. Upload file besar memakan waktu

#### GitHub API rate limit

**Gejala:**
```
API rate limit exceeded
```

**Solusi:**
1. Tunggu 1 jam
2. Dengan token: 5000 requests/hour
3. Tanpa token: 60 requests/hour
4. Gunakan token yang valid

---

## Debug Tips

### Enable Debug Mode

Edit `build-apk` dan tambahkan di awal:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Logs

```bash
# Termux logs
logcat | grep -i python

# GitHub Actions logs
# Buka di browser: https://github.com/username/apk-builds/actions
```

### Test Components

```bash
# Test Python
python --version
python -c "import requests; print('OK')"

# Test Git
git --version

# Test network
ping github.com
```

---

## Still Need Help?

1. **Check README.md** - Dokumentasi lengkap
2. **Check QUICKSTART.md** - Panduan cepat
3. **GitHub Issues** - Report bug atau tanya
4. **GitHub Discussions** - Diskusi dengan community

---

## Useful Commands

```bash
# Reset everything
rm -rf ~/.apk-builder
./install.sh

# Check Python dependencies
pip list | grep -E "requests|PyGithub|cryptography|pyyaml|colorama"

# Check disk space
df -h

# Check file permissions
ls -la build-apk

# Re-download workflow file
cd .github/workflows
wget https://raw.githubusercontent.com/daffa-aditya-p/apk-builder/main/.github/workflows/build-apk.yml
```

---

**Happy Debugging! 🐛**
