"""
Modul Konfigurasi APK Builder
Menangani setup project dan konfigurasi aplikasi
"""
import os
import json
from pathlib import Path

# Handle both absolute and relative imports
try:
    from .permissions import get_permission_by_id, display_permissions
except ImportError:
    from permissions import get_permission_by_id, display_permissions

class APKConfig:
    def __init__(self):
        self.config = {
            "project_type": "",
            "project_dir": "",
            "app_name": "",
            "app_id": "",
            "version": "",
            "version_code": 1,
            "icon_path": "",
            "permissions": [],
            "display_options": {
                "orientation": "portrait",
                "fullscreen": False,
                "statusbar": True
            }
        }
    
    def setup_project(self):
        """Setup konfigurasi project secara interaktif"""
        print("\n" + "="*50)
        print("     SETUP PROJECT APK BUILDER")
        print("="*50 + "\n")
        
        # Pilih jenis project
        print("Pilih Jenis Project:")
        print("1. HTML (Static Web)")
        print("2. React")
        
        while True:
            choice = input("\nPilihan (1/2): ").strip()
            if choice == "1":
                self.config["project_type"] = "html"
                break
            elif choice == "2":
                self.config["project_type"] = "react"
                break
            else:
                print("❌ Pilihan tidak valid!")
        
        # Lokasi direktori project
        while True:
            project_dir = input("\nLokasi Direktori Project (contoh: /sdcard/Acode/myproject): ").strip()
            if os.path.exists(project_dir):
                self.config["project_dir"] = project_dir
                break
            else:
                print(f"❌ Direktori tidak ditemukan: {project_dir}")
                create = input("Buat direktori baru? (y/n): ").strip().lower()
                if create == 'y':
                    try:
                        os.makedirs(project_dir, exist_ok=True)
                        self.config["project_dir"] = project_dir
                        break
                    except Exception as e:
                        print(f"❌ Gagal membuat direktori: {e}")
        
        # Nama aplikasi
        while True:
            app_name = input("\nNama Aplikasi: ").strip()
            if app_name:
                self.config["app_name"] = app_name
                break
            print("❌ Nama aplikasi tidak boleh kosong!")
        
        # App ID
        while True:
            app_id = input("\nApp ID (contoh: com.example.myapp): ").strip()
            if app_id and "." in app_id:
                self.config["app_id"] = app_id
                break
            print("❌ App ID tidak valid! (harus format: com.xxx.xxx)")
        
        # Versi APK
        while True:
            version = input("\nVersi APK (contoh: 1.0.0): ").strip()
            if version:
                self.config["version"] = version
                break
            print("❌ Versi tidak boleh kosong!")
        
        # Version Code
        while True:
            try:
                version_code = input("\nVersion Code (angka, contoh: 1): ").strip()
                self.config["version_code"] = int(version_code)
                break
            except ValueError:
                print("❌ Version code harus berupa angka!")
        
        # Icon APK
        icon_path = input("\nPath Icon APK (kosongkan jika menggunakan default): ").strip()
        if icon_path and os.path.exists(icon_path):
            self.config["icon_path"] = icon_path
        elif icon_path:
            print("⚠️  File icon tidak ditemukan, akan menggunakan icon default")
        
        # Pilih Permissions
        self._setup_permissions()
        
        # Display Options
        self._setup_display_options()
        
        print("\n✅ Konfigurasi project selesai!")
        return self.config
    
    def _setup_permissions(self):
        """Setup permissions yang diperlukan"""
        print("\n" + "="*50)
        print("     PILIH IZIN/PERMISSION APLIKASI")
        print("="*50)
        
        display_permissions()
        
        print("Masukkan nomor izin yang diperlukan (pisahkan dengan koma)")
        print("Contoh: 1,2,4,6,7")
        print("Atau ketik 'skip' untuk melewati\n")
        
        perm_input = input("Pilihan: ").strip()
        
        if perm_input.lower() != 'skip':
            perm_ids = [p.strip() for p in perm_input.split(',')]
            
            for perm_id in perm_ids:
                perm = get_permission_by_id(perm_id)
                if perm:
                    self.config["permissions"].append(perm["permission"])
                    print(f"✅ Ditambahkan: {perm['name']}")
                else:
                    print(f"⚠️  ID tidak valid: {perm_id}")
        
        # Tambah INTERNET secara default jika belum ada
        internet_perm = "android.permission.INTERNET"
        if internet_perm not in self.config["permissions"]:
            self.config["permissions"].append(internet_perm)
            print(f"\n✅ Menambahkan permission INTERNET (default)")
    
    def _setup_display_options(self):
        """Setup opsi tampilan aplikasi"""
        print("\n" + "="*50)
        print("     PENGATURAN TAMPILAN")
        print("="*50 + "\n")
        
        # Orientasi
        print("Orientasi Layar:")
        print("1. Portrait (Vertikal)")
        print("2. Landscape (Horizontal)")
        print("3. Auto (Otomatis)")
        
        orientation_choice = input("\nPilihan (1/2/3) [default: 1]: ").strip() or "1"
        orientations = {"1": "portrait", "2": "landscape", "3": "auto"}
        self.config["display_options"]["orientation"] = orientations.get(orientation_choice, "portrait")
        
        # Fullscreen
        fullscreen = input("\nFullscreen Mode? (y/n) [default: n]: ").strip().lower()
        self.config["display_options"]["fullscreen"] = fullscreen == 'y'
        
        # Status bar
        if not self.config["display_options"]["fullscreen"]:
            statusbar = input("\nTampilkan Status Bar? (y/n) [default: y]: ").strip().lower()
            self.config["display_options"]["statusbar"] = statusbar != 'n'
    
    def save_config(self, filename="apk_config.json"):
        """Simpan konfigurasi ke file"""
        config_dir = Path.home() / ".apk-builder"
        config_dir.mkdir(exist_ok=True)
        
        config_path = config_dir / filename
        with open(config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        
        print(f"\n💾 Konfigurasi disimpan: {config_path}")
        return config_path
    
    def load_config(self, filename="apk_config.json"):
        """Load konfigurasi dari file"""
        config_dir = Path.home() / ".apk-builder"
        config_path = config_dir / filename
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                self.config = json.load(f)
            return True
        return False
    
    def display_config(self):
        """Tampilkan konfigurasi saat ini"""
        print("\n" + "="*50)
        print("     RINGKASAN KONFIGURASI")
        print("="*50)
        print(f"\n📱 Nama Aplikasi: {self.config.get('app_name', '-')}")
        print(f"📦 App ID: {self.config.get('app_id', '-')}")
        print(f"🔢 Versi: {self.config.get('version', '-')} (code: {self.config.get('version_code', '-')})")
        print(f"📂 Jenis Project: {self.config.get('project_type', '-').upper()}")
        print(f"📁 Direktori: {self.config.get('project_dir', '-')}")
        print(f"\n🔐 Permissions: {len(self.config.get('permissions', []))} izin")
        for perm in self.config.get('permissions', []):
            print(f"   - {perm}")
        print(f"\n🎨 Tampilan:")
        print(f"   - Orientasi: {self.config['display_options']['orientation']}")
        print(f"   - Fullscreen: {'Ya' if self.config['display_options']['fullscreen'] else 'Tidak'}")
        print(f"   - Status Bar: {'Ya' if self.config['display_options']['statusbar'] else 'Tidak'}")
        print("="*50 + "\n")
