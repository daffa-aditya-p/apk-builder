# Contributing to APK Builder

Terima kasih sudah tertarik untuk berkontribusi! 🎉

## 🤝 Cara Berkontribusi

### 1. Report Bugs

Temukan bug? Buat issue dengan informasi:

- **Deskripsi bug** yang jelas
- **Langkah-langkah** untuk reproduce
- **Expected behavior** vs **actual behavior**
- **Screenshots** (jika relevan)
- **Environment**:
  - OS & version
  - Python version
  - Termux version (jika applicable)

### 2. Suggest Features

Ada ide fitur baru? Buat issue dengan:

- **Problem yang ingin diselesaikan**
- **Solusi yang diusulkan**
- **Alternatif** yang sudah dipertimbangkan
- **Use case** dan contoh

### 3. Submit Pull Requests

#### Fork & Clone

```bash
# Fork repository di GitHub
# Clone fork kamu
git clone https://github.com/YOUR_USERNAME/apk-builder.git
cd apk-builder

# Add upstream remote
git remote add upstream https://github.com/daffa-aditya-p/apk-builder.git
```

#### Create Branch

```bash
# Update main branch
git checkout main
git pull upstream main

# Buat branch baru
git checkout -b feature/your-feature-name
# atau
git checkout -b fix/your-bug-fix
```

#### Make Changes

1. **Code Style:**
   - Follow PEP 8 untuk Python code
   - Use meaningful variable names
   - Add comments untuk logic yang kompleks
   - Keep functions small and focused

2. **Testing:**
   - Test perubahan kamu di Termux
   - Test di berbagai skenario
   - Pastikan tidak break existing features

3. **Documentation:**
   - Update README.md jika perlu
   - Update docstrings
   - Add comments untuk code yang kompleks

#### Commit Changes

```bash
# Add files
git add .

# Commit dengan pesan yang jelas
git commit -m "feat: add feature X"
# atau
git commit -m "fix: resolve issue Y"
```

**Commit Message Format:**

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat: add React Native support
fix: resolve GitHub token validation issue
docs: update installation guide
```

#### Push & Create PR

```bash
# Push ke fork kamu
git push origin feature/your-feature-name

# Buat Pull Request di GitHub
# Compare: daffa-aditya-p:main <- YOUR_USERNAME:feature/your-feature-name
```

**PR Checklist:**

- [ ] Code tested and working
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Follows code style
- [ ] Commit messages clear
- [ ] PR description explains changes

---

## 📝 Development Setup

### Prerequisites

```bash
# Termux
pkg install python git

# Python 3.8+
python --version

# Git
git --version
```

### Install Development Dependencies

```bash
# Clone repository
git clone https://github.com/daffa-aditya-p/apk-builder.git
cd apk-builder

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x build-apk
```

### Project Structure

```
apk-builder/
├── build-apk              # Main entry point
├── src/
│   ├── auth.py           # Authentication module
│   ├── config.py         # Configuration module
│   ├── permissions.py    # Permissions database
│   ├── keystore_manager.py  # Keystore management
│   └── github_builder.py # GitHub integration
├── .github/
│   └── workflows/
│       └── build-apk.yml # GitHub Actions workflow
├── examples/
│   └── sample-html/      # Sample project
├── docs/                 # Documentation
└── tests/                # Tests (coming soon)
```

### Running Tests

```bash
# Syntax check
python3 -m py_compile src/*.py

# Run tool
./build-apk

# Manual testing
# - Test each menu option
# - Test with sample project
# - Verify GitHub integration
```

---

## 🎯 Areas for Contribution

### High Priority

1. **Testing Framework**
   - Unit tests untuk modules
   - Integration tests
   - CI/CD pipeline

2. **Error Handling**
   - Better error messages
   - Retry mechanisms
   - Graceful fallbacks

3. **Documentation**
   - Video tutorials
   - More examples
   - Translations

### Medium Priority

1. **New Features**
   - React Native support
   - Flutter support
   - APK signing in cloud
   - Icon generator

2. **Improvements**
   - Progress bars
   - Caching system
   - Config validation
   - Better UI/UX

3. **Platform Support**
   - macOS testing
   - Linux desktop optimization

### Low Priority

1. **Optimizations**
   - Performance improvements
   - Code refactoring
   - Better architecture

2. **Nice to Have**
   - Web interface
   - GUI version
   - Plugin system

---

## 💡 Tips

### Good First Issues

Look for issues labeled:
- `good first issue`
- `beginner friendly`
- `documentation`
- `help wanted`

### Communication

- Be respectful and constructive
- Ask questions if unclear
- Provide context in issues/PRs
- Respond to feedback

### Code Quality

- Keep it simple
- Don't over-engineer
- Write readable code
- Add comments when needed

### Testing

- Test in Termux
- Test edge cases
- Test error scenarios
- Verify on real device

---

## 📞 Getting Help

- **Questions:** Open a Discussion on GitHub
- **Bugs:** Open an Issue
- **Security:** Email privately (see SECURITY.md)

---

## 🙏 Thank You!

Every contribution matters, big or small:
- Code
- Documentation
- Bug reports
- Feature suggestions
- Testing
- Spreading the word

**Contributors akan dicantumkan di README.md** 🌟

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Happy Contributing! 🚀**
