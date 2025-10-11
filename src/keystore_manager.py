"""
Modul Keystore Manager
Mengelola pembuatan dan penyimpanan keystore untuk signing APK
"""
import os
import subprocess
from pathlib import Path
from datetime import datetime

class KeystoreManager:
    def __init__(self):
        self.keystore_dir = Path.home() / ".apk-builder" / "keystores"
        self.keystore_dir.mkdir(parents=True, exist_ok=True)
    
    def create_keystore(self):
        """Buat keystore baru secara interaktif"""
        print("\n" + "="*50)
        print("     BUAT KEYSTORE BARU")
        print("="*50 + "\n")
        
        # Nama keystore
        keystore_name = input("Nama Keystore (contoh: myapp): ").strip()
        if not keystore_name:
            return False, "Nama keystore tidak boleh kosong!"
        
        keystore_path = self.keystore_dir / f"{keystore_name}.keystore"
        
        if keystore_path.exists():
            overwrite = input(f"⚠️  Keystore '{keystore_name}' sudah ada. Timpa? (y/n): ").strip().lower()
            if overwrite != 'y':
                return False, "Pembuatan keystore dibatalkan"
        
        # Informasi keystore
        print("\nMasukkan informasi keystore:")
        
        alias = input("Alias (nama kunci): ").strip() or keystore_name
        password = input("Password keystore (min 6 karakter): ").strip()
        
        if len(password) < 6:
            return False, "Password harus minimal 6 karakter!"
        
        key_password = input("Password key (tekan Enter jika sama dengan password keystore): ").strip()
        if not key_password:
            key_password = password
        
        # Informasi developer
        print("\nInformasi Developer (opsional, bisa dikosongkan):")
        common_name = input("Nama lengkap [Unknown]: ").strip() or "Unknown"
        org_unit = input("Unit organisasi [Unknown]: ").strip() or "Unknown"
        org_name = input("Nama organisasi [Unknown]: ").strip() or "Unknown"
        city = input("Kota [Unknown]: ").strip() or "Unknown"
        state = input("Provinsi/State [Unknown]: ").strip() or "Unknown"
        country = input("Kode negara (2 huruf, contoh: ID) [ID]: ").strip() or "ID"
        
        validity = input("\nMasa berlaku (dalam hari) [10000]: ").strip() or "10000"
        
        # Generate keystore menggunakan keytool
        try:
            print("\n🔄 Membuat keystore...")
            
            # Buat file info keystore
            info = {
                "keystore_path": str(keystore_path),
                "alias": alias,
                "password": password,
                "key_password": key_password,
                "created_at": datetime.now().isoformat(),
                "info": {
                    "CN": common_name,
                    "OU": org_unit,
                    "O": org_name,
                    "L": city,
                    "ST": state,
                    "C": country
                }
            }
            
            dname = f"CN={common_name}, OU={org_unit}, O={org_name}, L={city}, ST={state}, C={country}"
            
            # Cek apakah keytool tersedia
            keytool_cmd = self._find_keytool()
            
            if not keytool_cmd:
                # Jika keytool tidak ada, buat file info saja (untuk mode Termux)
                print("⚠️  Keytool tidak ditemukan. Menyimpan info keystore untuk build di cloud...")
                self._save_keystore_info(keystore_name, info)
                return True, f"Info keystore disimpan: {keystore_name}\n⚠️  Keystore akan dibuat otomatis saat build di GitHub Actions"
            
            # Generate menggunakan keytool
            cmd = [
                keytool_cmd,
                "-genkeypair",
                "-v",
                "-keystore", str(keystore_path),
                "-alias", alias,
                "-keyalg", "RSA",
                "-keysize", "2048",
                "-validity", validity,
                "-storepass", password,
                "-keypass", key_password,
                "-dname", dname
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                self._save_keystore_info(keystore_name, info)
                print(f"\n✅ Keystore berhasil dibuat!")
                print(f"📁 Lokasi: {keystore_path}")
                return True, f"Keystore '{keystore_name}' berhasil dibuat"
            else:
                return False, f"Gagal membuat keystore: {result.stderr}"
        
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def _find_keytool(self):
        """Cari keytool di sistem"""
        # Coba beberapa lokasi umum
        possible_paths = [
            "keytool",  # Di PATH
            "/usr/bin/keytool",
            "/usr/local/bin/keytool",
        ]
        
        # Cek JAVA_HOME
        java_home = os.environ.get("JAVA_HOME")
        if java_home:
            possible_paths.append(os.path.join(java_home, "bin", "keytool"))
        
        for path in possible_paths:
            try:
                result = subprocess.run([path, "-help"], capture_output=True)
                if result.returncode == 0:
                    return path
            except:
                continue
        
        return None
    
    def _save_keystore_info(self, name, info):
        """Simpan informasi keystore"""
        import json
        info_path = self.keystore_dir / f"{name}.json"
        with open(info_path, 'w') as f:
            json.dump(info, f, indent=2)
    
    def list_keystores(self):
        """Tampilkan daftar keystore yang ada"""
        keystores = list(self.keystore_dir.glob("*.keystore"))
        info_files = list(self.keystore_dir.glob("*.json"))
        
        if not keystores and not info_files:
            print("\n⚠️  Belum ada keystore yang dibuat")
            return []
        
        print("\n" + "="*50)
        print("     DAFTAR KEYSTORE")
        print("="*50 + "\n")
        
        result = []
        
        # Tampilkan keystore yang ada
        for ks in keystores:
            name = ks.stem
            info_file = self.keystore_dir / f"{name}.json"
            
            print(f"📦 {name}")
            print(f"   Path: {ks}")
            
            if info_file.exists():
                import json
                with open(info_file) as f:
                    info = json.load(f)
                    print(f"   Alias: {info.get('alias', '-')}")
                    print(f"   Dibuat: {info.get('created_at', '-')}")
            
            print()
            result.append(name)
        
        return result
    
    def get_keystore_info(self, name):
        """Dapatkan informasi keystore"""
        import json
        info_file = self.keystore_dir / f"{name}.json"
        
        if info_file.exists():
            with open(info_file) as f:
                return json.load(f)
        
        return None
    
    def sign_apk(self, apk_path, keystore_name):
        """Sign APK dengan keystore"""
        print("\n" + "="*50)
        print("     SIGN APK")
        print("="*50 + "\n")
        
        if not os.path.exists(apk_path):
            return False, f"File APK tidak ditemukan: {apk_path}"
        
        # Dapatkan info keystore
        info = self.get_keystore_info(keystore_name)
        if not info:
            return False, f"Keystore '{keystore_name}' tidak ditemukan"
        
        keystore_path = info.get('keystore_path')
        if not os.path.exists(keystore_path):
            return False, f"File keystore tidak ditemukan: {keystore_path}"
        
        print(f"📦 APK: {apk_path}")
        print(f"🔐 Keystore: {keystore_name}")
        print(f"🔑 Alias: {info.get('alias')}")
        
        # Untuk saat ini, tampilkan perintah manual
        # Karena di Termux mungkin tidak ada jarsigner/apksigner
        print("\n⚠️  Untuk sign APK manual, gunakan perintah:")
        print(f"\napksigner sign --ks {keystore_path} \\")
        print(f"  --ks-key-alias {info.get('alias')} \\")
        print(f"  --out signed.apk \\")
        print(f"  {apk_path}")
        print(f"\nPassword: {info.get('password')}")
        
        return True, "Info signing ditampilkan"
