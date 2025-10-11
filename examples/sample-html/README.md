# Sample HTML Project

Ini adalah contoh project HTML sederhana yang bisa di-convert menjadi APK menggunakan APK Builder Tool.

## 📁 File Structure

```
sample-html/
├── index.html    # Main HTML file
├── style.css     # Styling
├── script.js     # JavaScript logic
└── README.md     # This file
```

## 🚀 Cara Menggunakan

1. **Copy folder ini ke Acode:**
   ```bash
   cp -r examples/sample-html /sdcard/Acode/
   ```

2. **Jalankan APK Builder:**
   ```bash
   ./build-apk
   ```

3. **Pilih menu Build APK:**
   - Jenis: HTML
   - Direktori: `/sdcard/Acode/sample-html`
   - Isi konfigurasi lainnya

4. **Tunggu build selesai dan download APK!**

## ✨ Features

- ✅ Responsive design
- ✅ Modern gradient UI
- ✅ Interactive button
- ✅ Device info display
- ✅ Cordova-ready
- ✅ Animation effects

## 🎨 Kustomisasi

Anda bisa mengubah:

- **Warna**: Edit gradient di `style.css`
- **Konten**: Edit teks di `index.html`
- **Fitur**: Tambah fungsi di `script.js`

## 📝 Permissions Yang Dibutuhkan

Untuk project basic ini, cukup:
- ✅ Internet (permission #1)
- ✅ Network State (permission #18)

Jika ingin tambah fitur:
- Camera → permission #2
- Location → permission #4 atau #5
- Storage → permission #6 dan #7

## 🔧 Tips Development

1. **Test di browser dulu:**
   ```bash
   # Di Termux
   python -m http.server 8000
   ```
   Buka: http://localhost:8000

2. **Edit dengan Acode:**
   - Install Acode dari Play Store
   - Buka folder project
   - Edit langsung dengan syntax highlighting

3. **Test APK:**
   - Build APK
   - Install di device
   - Test semua fitur

## 🐛 Troubleshooting

**Styling tidak muncul:**
- Pastikan `style.css` ada di folder yang sama
- Check path di `<link>` tag

**JavaScript error:**
- Buka Chrome DevTools
- Check Console untuk error
- Fix di `script.js`

## 📚 Learn More

- [HTML Tutorial](https://www.w3schools.com/html/)
- [CSS Tutorial](https://www.w3schools.com/css/)
- [JavaScript Tutorial](https://www.w3schools.com/js/)
- [Cordova Documentation](https://cordova.apache.org/docs/)

---

Happy coding! 🎉
