"""
Modul GitHub Builder
Menangani upload project dan trigger build APK via GitHub Actions
"""
import os
import json
import time
import base64
import requests
from pathlib import Path

class GitHubBuilder:
    def __init__(self, github_token=None):
        self.token = github_token
        self.api_base = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}" if self.token else ""
        }
        self.repo_owner = None
        self.repo_name = None
        self.default_branch = "main"
        self.workflow_source = Path(__file__).resolve().parent.parent / ".github" / "workflows" / "build-apk.yml"
    
    def setup_github_token(self):
        """Setup GitHub token secara interaktif"""
        config_dir = Path.home() / ".apk-builder"
        config_dir.mkdir(exist_ok=True)
        token_file = config_dir / "github_token.txt"
        
        # Cek apakah token sudah ada
        if token_file.exists():
            with open(token_file, 'r') as f:
                token = f.read().strip()
                if token:
                    use_existing = input("\n✅ GitHub token ditemukan. Gunakan token yang ada? (y/n): ").strip().lower()
                    if use_existing == 'y':
                        self.token = token
                        self.headers["Authorization"] = f"token {self.token}"
                        return True, "Token berhasil dimuat"
        
        print("\n" + "="*50)
        print("     SETUP GITHUB TOKEN")
        print("="*50)
        print("\nUntuk build APK di cloud, diperlukan GitHub Personal Access Token")
        print("\nCara mendapatkan token:")
        print("1. Buka: https://github.com/settings/tokens")
        print("2. Klik 'Generate new token' → 'Generate new token (classic)'")
        print("3. Beri nama: 'APK Builder'")
        print("4. Pilih scope: 'repo' (full control)")
        print("5. Klik 'Generate token' dan copy token-nya")
        print("\n" + "="*50 + "\n")
        
        token = input("Paste GitHub Token di sini: ").strip()
        
        if not token:
            return False, "Token tidak boleh kosong!"
        
        # Test token
        test_url = f"{self.api_base}/user"
        test_headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}"
        }
        
        try:
            response = requests.get(test_url, headers=test_headers)
            if response.status_code == 200:
                user_data = response.json()
                print(f"\n✅ Token valid! Login sebagai: {user_data['login']}")
                
                # Simpan token
                with open(token_file, 'w') as f:
                    f.write(token)
                
                self.token = token
                self.headers["Authorization"] = f"token {self.token}"
                return True, "Token berhasil disimpan"
            else:
                return False, f"Token tidak valid! Status: {response.status_code}"
        except Exception as e:
            return False, f"Gagal validasi token: {str(e)}"
    
    def create_or_get_repo(self, repo_name="apk-builds"):
        """Buat atau dapatkan repository untuk build"""
        if not self.token:
            return False, "GitHub token belum di-setup!"
        
        # Dapatkan user info
        user_url = f"{self.api_base}/user"
        response = requests.get(user_url, headers=self.headers)
        
        if response.status_code != 200:
            return False, "Gagal mendapatkan info user"
        
        user_data = response.json()
        self.repo_owner = user_data['login']
        self.repo_name = repo_name
        
        # Cek apakah repo sudah ada
        repo_url = f"{self.api_base}/repos/{self.repo_owner}/{repo_name}"
        response = requests.get(repo_url, headers=self.headers)
        
        if response.status_code == 200:
            repo_data = response.json()
            self.default_branch = repo_data.get("default_branch", "main")
            print(f"✅ Repository '{repo_name}' sudah ada")
            workflow_ready, workflow_message = self._ensure_workflow_file()
            if not workflow_ready:
                return False, workflow_message
            return True, f"Repository: {self.repo_owner}/{repo_name}"
        
        # Buat repository baru
        print(f"\n🔄 Membuat repository '{repo_name}'...")
        
        create_url = f"{self.api_base}/user/repos"
        payload = {
            "name": repo_name,
            "description": "APK Build Repository - Created by APK Builder Tool",
            "private": False,  # Bisa diubah jadi True kalau mau private
            "auto_init": True
        }
        
        response = requests.post(create_url, headers=self.headers, json=payload)
        
        if response.status_code == 201:
            repo_data = response.json()
            self.default_branch = repo_data.get("default_branch", "main")
            print(f"✅ Repository '{repo_name}' berhasil dibuat!")
            workflow_ready, workflow_message = self._ensure_workflow_file()
            if not workflow_ready:
                return False, workflow_message
            return True, f"Repository: {self.repo_owner}/{repo_name}"
        else:
            return False, f"Gagal membuat repository: {response.json().get('message', 'Unknown error')}"
    
    def upload_project_files(self, config):
        """Upload file project ke GitHub repository"""
        if not self.repo_owner or not self.repo_name:
            return False, "Repository belum di-setup!"
        
        project_dir = Path(config['project_dir'])
        if not project_dir.exists():
            return False, f"Direktori project tidak ditemukan: {project_dir}"
        
        print(f"\n🔄 Mengupload project files...")
        
        try:
            # Buat branch baru untuk build ini
            branch_name = f"build-{int(time.time())}"
            
            # Dapatkan SHA dari default branch
            ref_url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/git/refs/heads/{self.default_branch}"
            response = requests.get(ref_url, headers=self.headers)
            
            if response.status_code != 200:
                return False, "Gagal mendapatkan info default branch repository"
            
            main_sha = response.json()['object']['sha']
            
            # Buat branch baru
            create_ref_url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/git/refs"
            payload = {
                "ref": f"refs/heads/{branch_name}",
                "sha": main_sha
            }
            
            response = requests.post(create_ref_url, headers=self.headers, json=payload)
            if response.status_code != 201:
                print(f"⚠️  Gagal membuat branch baru, menggunakan default branch")
                branch_name = self.default_branch
            
            # Upload file config
            config_content = json.dumps(config, indent=2)
            self._upload_file("build-config.json", config_content, branch_name)
            
            # Upload project files
            uploaded_files = []
            
            source_dir = project_dir
            if config.get('project_type') == 'react':
                react_build_candidates = [project_dir / "build", project_dir / "dist"]
                source_dir = next((candidate for candidate in react_build_candidates if candidate.exists()), project_dir)
            
            for file_path in source_dir.rglob("*"):
                if not file_path.is_file() or self._should_skip_path(file_path):
                    continue
                
                rel_path = file_path.relative_to(source_dir)
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                try:
                    text_content = content.decode('utf-8')
                    success = self._upload_file(f"www/{rel_path.as_posix()}", text_content, branch_name)
                except UnicodeDecodeError:
                    binary_content = base64.b64encode(content).decode()
                    success = self._upload_file(f"www/{rel_path.as_posix()}", binary_content, branch_name, is_binary=True)
                
                if success:
                    uploaded_files.append(str(rel_path))
            
            print(f"✅ Berhasil upload {len(uploaded_files)} file")
            
            return True, {
                "branch": branch_name,
                "uploaded_files": uploaded_files
            }
        
        except Exception as e:
            return False, f"Error saat upload: {str(e)}"

    def _should_skip_path(self, file_path):
        """Skip files/folders yang tidak relevan untuk upload build"""
        parts = set(file_path.parts)
        ignored_dirs = {".git", ".github", "node_modules", "__pycache__", ".next", ".cache", "venv", ".venv"}
        if ignored_dirs.intersection(parts):
            return True
        if file_path.name.startswith("."):
            return True
        return False

    def _ensure_workflow_file(self):
        """Pastikan workflow build tersedia di repository target"""
        if not self.workflow_source.exists():
            return False, f"Workflow template tidak ditemukan: {self.workflow_source}"
        
        with open(self.workflow_source, "r", encoding="utf-8") as f:
            workflow_content = f.read()
        
        uploaded = self._upload_file(
            ".github/workflows/build-apk.yml",
            workflow_content,
            self.default_branch
        )
        if not uploaded:
            return False, "Gagal menyiapkan workflow build di repository target"
        return True, "Workflow siap digunakan"
    
    def _upload_file(self, file_path, content, branch, is_binary=False):
        """Upload single file ke repository"""
        url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
        
        # Cek apakah file sudah ada
        response = requests.get(url, headers=self.headers, params={"ref": branch})
        
        if not is_binary:
            content_encoded = base64.b64encode(content.encode()).decode()
        else:
            content_encoded = content
        
        payload = {
            "message": f"Upload {file_path}",
            "content": content_encoded,
            "branch": branch
        }
        
        # Jika file sudah ada, perlu SHA untuk update
        if response.status_code == 200:
            payload["sha"] = response.json()['sha']
        
        response = requests.put(url, headers=self.headers, json=payload)
        
        if response.status_code in [200, 201]:
            print(f"  ✅ {file_path}")
            return True
        else:
            print(f"  ❌ {file_path}: {response.status_code}")
            return False
    
    def trigger_build(self, config, branch="main"):
        """Trigger GitHub Actions untuk build APK"""
        if not self.repo_owner or not self.repo_name:
            return False, "Repository belum di-setup!"
        
        print(f"\n🔄 Memulai build APK di GitHub Actions...")
        
        # Trigger workflow dispatch
        workflow_url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/actions/workflows/build-apk.yml/dispatches"
        
        payload = {
            "ref": branch,
            "inputs": {
                "app_name": config.get('app_name', 'MyApp'),
                "app_id": config.get('app_id', 'com.example.app'),
                "version": config.get('version', '1.0.0')
            }
        }
        
        response = requests.post(workflow_url, headers=self.headers, json=payload)
        
        if response.status_code == 204:
            print(f"✅ Build dimulai!")
            print(f"\n📊 Monitor progress:")
            print(f"   https://github.com/{self.repo_owner}/{self.repo_name}/actions")
            
            # Tunggu sebentar dan cek status
            time.sleep(5)
            
            return True, f"Build triggered di branch {branch}"
        else:
            return False, f"Gagal trigger build: {response.status_code} - {response.text}"
    
    def check_build_status(self):
        """Cek status build terakhir"""
        if not self.repo_owner or not self.repo_name:
            return False, "Repository belum di-setup!"
        
        runs_url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/actions/runs"
        response = requests.get(runs_url, headers=self.headers, params={"per_page": 1})
        
        if response.status_code == 200:
            data = response.json()
            if data['total_count'] > 0:
                run = data['workflow_runs'][0]
                
                status = run['status']
                conclusion = run.get('conclusion', 'in_progress')
                
                print(f"\n📊 Status Build Terakhir:")
                print(f"   Status: {status}")
                print(f"   Conclusion: {conclusion}")
                print(f"   URL: {run['html_url']}")
                
                return True, {"status": status, "conclusion": conclusion, "url": run['html_url']}
            else:
                return False, "Belum ada build yang dijalankan"
        
        return False, "Gagal cek status"
    
    def download_apk(self, output_dir=None):
        """Download APK hasil build"""
        if not output_dir:
            output_dir = Path.home() / "apk-builds"
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n🔄 Mencari APK hasil build...")
        
        # Dapatkan artifacts terakhir
        artifacts_url = f"{self.api_base}/repos/{self.repo_owner}/{self.repo_name}/actions/artifacts"
        response = requests.get(artifacts_url, headers=self.headers)
        
        if response.status_code == 200:
            data = response.json()
            if data['total_count'] > 0:
                artifact = data['artifacts'][0]
                
                print(f"📦 Ditemukan: {artifact['name']}")
                print(f"   Size: {artifact['size_in_bytes'] / 1024 / 1024:.2f} MB")
                
                # Download artifact
                download_url = artifact['archive_download_url']
                
                print(f"🔄 Downloading...")
                response = requests.get(download_url, headers=self.headers, stream=True)
                
                if response.status_code == 200:
                    output_file = output_dir / f"{artifact['name']}.zip"
                    
                    with open(output_file, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    print(f"✅ APK berhasil didownload!")
                    print(f"📁 Lokasi: {output_file}")
                    
                    return True, str(output_file)
                else:
                    return False, f"Gagal download: {response.status_code}"
            else:
                return False, "Tidak ada artifact yang ditemukan"
        
        return False, "Gagal mendapatkan artifacts"
