# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-10-11

### 🎉 Initial Release

#### ✨ Features
- **Complete APK Builder Tool** untuk Termux
- **Cloud Build** menggunakan GitHub Actions (no Java required!)
- **Autentikasi System** dengan session management
- **Project Configuration** yang lengkap:
  - Support HTML dan React projects
  - App ID, version, version code
  - Custom icon support
  - 30+ Android permissions
  - Display options (orientation, fullscreen, statusbar)
- **Keystore Manager** untuk sign APK
- **GitHub Integration**:
  - Auto create repository
  - Upload project files
  - Trigger workflows
  - Download artifacts
- **Interactive CLI** dengan colorama support
- **Sample HTML Project** untuk testing

#### 📚 Documentation
- Comprehensive README.md
- Quick start guide (QUICKSTART.md)
- Troubleshooting guide (TROUBLESHOOTING.md)
- Sample project documentation

#### 🔧 Technical
- Python 3.8+ support
- GitHub API integration
- Cordova-based Android builds
- Clean modular architecture
- Error handling & fallbacks

#### 🎨 UI/UX
- Colorful terminal output
- Progress indicators
- Clear error messages
- User-friendly prompts
- Banner & headers

### 📦 Components

#### Core Modules
- `auth.py` - Authentication & session management
- `config.py` - APK configuration setup
- `permissions.py` - Android permissions database
- `keystore_manager.py` - Keystore creation & management
- `github_builder.py` - GitHub Actions integration
- `build-apk` - Main CLI application

#### GitHub Actions
- `build-apk.yml` - Workflow untuk build APK di cloud
- Support Cordova
- Auto artifact upload
- Optional release creation

#### Examples
- Sample HTML project dengan modern UI
- Responsive design
- Cordova-ready code

### 🔒 Security
- Password hashing (SHA-256)
- Local token storage
- Secure keystore management
- No data sent to third parties

### 📱 Platform Support
- ✅ Termux (primary)
- ✅ Linux
- ⚠️ macOS (untested)
- ❌ Windows (not supported)

---

## [Unreleased]

### Planned Features
- [ ] React Native support
- [ ] Flutter support
- [ ] Direct APK signing in cloud
- [ ] Multiple GitHub accounts
- [ ] APK optimization
- [ ] Auto icon generation
- [ ] Splash screen customization
- [ ] AdMob integration
- [ ] Firebase integration
- [ ] Play Store metadata generator

### Improvements
- [ ] Better error handling
- [ ] Progress bars
- [ ] Retry mechanisms
- [ ] Caching system
- [ ] Config file validation
- [ ] Diff detection for incremental builds

### Bug Fixes
- [ ] TBD (report issues!)

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Version Format

We use [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for new functionality
- PATCH version for bug fixes

---

**Note:** Dates in format YYYY-MM-DD
