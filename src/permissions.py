"""
Modul untuk mengelola Android Permissions
"""

ANDROID_PERMISSIONS = {
    "1": {
        "name": "Akses Internet",
        "permission": "android.permission.INTERNET",
        "description": "Mengakses jaringan internet"
    },
    "2": {
        "name": "Akses Kamera",
        "permission": "android.permission.CAMERA",
        "description": "Menggunakan kamera perangkat"
    },
    "3": {
        "name": "Akses Audio/Microphone",
        "permission": "android.permission.RECORD_AUDIO",
        "description": "Merekam audio dari mikrofon"
    },
    "4": {
        "name": "Akses Lokasi Akurat (GPS)",
        "permission": "android.permission.ACCESS_FINE_LOCATION",
        "description": "Mengakses lokasi GPS akurat"
    },
    "5": {
        "name": "Akses Lokasi Perkiraan (Jaringan)",
        "permission": "android.permission.ACCESS_COARSE_LOCATION",
        "description": "Mengakses lokasi dari jaringan"
    },
    "6": {
        "name": "Baca Penyimpanan Internal",
        "permission": "android.permission.READ_EXTERNAL_STORAGE",
        "description": "Membaca file dari penyimpanan"
    },
    "7": {
        "name": "Tulis Penyimpanan Internal",
        "permission": "android.permission.WRITE_EXTERNAL_STORAGE",
        "description": "Menulis file ke penyimpanan"
    },
    "8": {
        "name": "Baca Kontak",
        "permission": "android.permission.READ_CONTACTS",
        "description": "Membaca daftar kontak"
    },
    "9": {
        "name": "Tulis Kontak",
        "permission": "android.permission.WRITE_CONTACTS",
        "description": "Menambah/edit kontak"
    },
    "10": {
        "name": "Baca Kalender",
        "permission": "android.permission.READ_CALENDAR",
        "description": "Membaca acara kalender"
    },
    "11": {
        "name": "Tulis Kalender",
        "permission": "android.permission.WRITE_CALENDAR",
        "description": "Menambah/edit acara kalender"
    },
    "12": {
        "name": "Kirim SMS",
        "permission": "android.permission.SEND_SMS",
        "description": "Mengirim pesan SMS"
    },
    "13": {
        "name": "Baca Status Telepon",
        "permission": "android.permission.READ_PHONE_STATE",
        "description": "Membaca status telepon"
    },
    "14": {
        "name": "Panggil Telepon Langsung",
        "permission": "android.permission.CALL_PHONE",
        "description": "Melakukan panggilan telepon"
    },
    "15": {
        "name": "Baca Notifikasi",
        "permission": "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE",
        "description": "Mengakses notifikasi sistem"
    },
    "16": {
        "name": "Akses WiFi State",
        "permission": "android.permission.ACCESS_WIFI_STATE",
        "description": "Melihat informasi WiFi"
    },
    "17": {
        "name": "Ubah WiFi State",
        "permission": "android.permission.CHANGE_WIFI_STATE",
        "description": "Mengubah status WiFi"
    },
    "18": {
        "name": "Akses Network State",
        "permission": "android.permission.ACCESS_NETWORK_STATE",
        "description": "Melihat status jaringan"
    },
    "19": {
        "name": "Baca SMS",
        "permission": "android.permission.READ_SMS",
        "description": "Membaca pesan SMS"
    },
    "20": {
        "name": "Terima SMS",
        "permission": "android.permission.RECEIVE_SMS",
        "description": "Menerima pesan SMS masuk"
    },
    "21": {
        "name": "Vibrate",
        "permission": "android.permission.VIBRATE",
        "description": "Menggunakan vibrator perangkat"
    },
    "22": {
        "name": "Bluetooth",
        "permission": "android.permission.BLUETOOTH",
        "description": "Menggunakan koneksi Bluetooth"
    },
    "23": {
        "name": "Bluetooth Admin",
        "permission": "android.permission.BLUETOOTH_ADMIN",
        "description": "Mengelola Bluetooth"
    },
    "24": {
        "name": "Boot Completed",
        "permission": "android.permission.RECEIVE_BOOT_COMPLETED",
        "description": "Jalankan saat boot selesai"
    },
    "25": {
        "name": "Foreground Service",
        "permission": "android.permission.FOREGROUND_SERVICE",
        "description": "Jalankan service di foreground"
    },
    "26": {
        "name": "Wake Lock",
        "permission": "android.permission.WAKE_LOCK",
        "description": "Mencegah perangkat tidur"
    },
    "27": {
        "name": "Install Packages",
        "permission": "android.permission.REQUEST_INSTALL_PACKAGES",
        "description": "Install aplikasi"
    },
    "28": {
        "name": "Baca Log",
        "permission": "android.permission.READ_LOGS",
        "description": "Membaca log sistem"
    },
    "29": {
        "name": "Akses Body Sensors",
        "permission": "android.permission.BODY_SENSORS",
        "description": "Akses sensor tubuh (detak jantung, dll)"
    },
    "30": {
        "name": "Baca Call Log",
        "permission": "android.permission.READ_CALL_LOG",
        "description": "Membaca riwayat panggilan"
    }
}

def get_permissions_list():
    """Dapatkan daftar semua permissions"""
    return ANDROID_PERMISSIONS

def get_permission_by_id(perm_id):
    """Dapatkan permission berdasarkan ID"""
    return ANDROID_PERMISSIONS.get(str(perm_id))

def display_permissions():
    """Tampilkan daftar permissions yang tersedia"""
    print("\n=== Daftar Izin/Permission Android ===\n")
    for key, perm in sorted(ANDROID_PERMISSIONS.items(), key=lambda x: int(x[0])):
        print(f"{key:2}. {perm['name']}")
    print("\n")
