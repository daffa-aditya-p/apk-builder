"""
Modul Autentikasi untuk APK Builder
Menangani login dan registrasi user
"""
import os
import json
import hashlib
from pathlib import Path

class Auth:
    def __init__(self):
        self.config_dir = Path.home() / ".apk-builder"
        self.config_dir.mkdir(exist_ok=True)
        self.session_file = self.config_dir / "session.json"
        self.users_file = self.config_dir / "users.json"
        
        # Inisialisasi user default
        self._init_default_users()
    
    def _init_default_users(self):
        """Inisialisasi user default jika belum ada"""
        if not self.users_file.exists():
            default_users = {
                "Daffa": self._hash_password("daffajago123")
            }
            self._save_users(default_users)
    
    def _hash_password(self, password):
        """Hash password menggunakan SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _load_users(self):
        """Load data user dari file"""
        if self.users_file.exists():
            with open(self.users_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_users(self, users):
        """Simpan data user ke file"""
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)
    
    def _save_session(self, username):
        """Simpan session user yang login"""
        session = {
            "username": username,
            "logged_in": True
        }
        with open(self.session_file, 'w') as f:
            json.dump(session, f, indent=2)
    
    def _clear_session(self):
        """Hapus session"""
        if self.session_file.exists():
            os.remove(self.session_file)
    
    def is_logged_in(self):
        """Cek apakah user sudah login"""
        if self.session_file.exists():
            with open(self.session_file, 'r') as f:
                session = json.load(f)
                return session.get('logged_in', False)
        return False
    
    def get_current_user(self):
        """Dapatkan username user yang sedang login"""
        if self.is_logged_in():
            with open(self.session_file, 'r') as f:
                session = json.load(f)
                return session.get('username')
        return None
    
    def register(self, username, password):
        """Registrasi user baru"""
        users = self._load_users()
        
        if username in users:
            return False, "Username sudah terdaftar!"
        
        if len(password) < 6:
            return False, "Password minimal 6 karakter!"
        
        users[username] = self._hash_password(password)
        self._save_users(users)
        
        return True, "Registrasi berhasil!"
    
    def login(self, username, password):
        """Login user"""
        users = self._load_users()
        
        if username not in users:
            return False, "Username tidak ditemukan!"
        
        password_hash = self._hash_password(password)
        if users[username] != password_hash:
            return False, "Password salah!"
        
        self._save_session(username)
        return True, f"Selamat datang, {username}!"
    
    def logout(self):
        """Logout user"""
        self._clear_session()
        return True, "Logout berhasil!"
