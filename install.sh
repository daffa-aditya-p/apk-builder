#!/bin/bash

# APK Builder - Installation Script for Termux
# This script will install all dependencies and setup the tool

echo "╔═══════════════════════════════════════════════╗"
echo "║                                               ║"
echo "║         🚀 APK BUILDER INSTALLATION 🚀        ║"
echo "║                                               ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# Check if running in Termux
if [ ! -d "$PREFIX" ]; then
    echo "⚠️  Warning: Not running in Termux!"
    echo "This script is optimized for Termux."
    read -p "Continue anyway? (y/n): " choice
    if [ "$choice" != "y" ]; then
        exit 0
    fi
fi

echo "📦 Step 1: Updating packages..."
pkg update -y || apt-get update -y
echo "✅ Packages updated!"
echo ""

echo "📦 Step 2: Installing dependencies..."
pkg install -y python git || apt-get install -y python3 git
echo "✅ Dependencies installed!"
echo ""

echo "📦 Step 3: Installing Python packages..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Python packages installed!"
else
    echo "❌ Failed to install Python packages"
    echo "Trying with pip3..."
    pip3 install -r requirements.txt
fi
echo ""

echo "📦 Step 4: Making build-apk executable..."
chmod +x build-apk
echo "✅ Executable created!"
echo ""

echo "📦 Step 5: Creating config directory..."
mkdir -p ~/.apk-builder
echo "✅ Config directory created!"
echo ""

# Optional: Create alias
echo "📦 Step 6: Creating alias (optional)..."
SHELL_RC=""
if [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [ ! -z "$SHELL_RC" ]; then
    if ! grep -q "alias build-apk" "$SHELL_RC"; then
        echo "" >> "$SHELL_RC"
        echo "# APK Builder alias" >> "$SHELL_RC"
        echo "alias build-apk='$(pwd)/build-apk'" >> "$SHELL_RC"
        echo "✅ Alias added to $SHELL_RC"
        echo "   Run: source $SHELL_RC"
    else
        echo "⚠️  Alias already exists"
    fi
fi
echo ""

echo "╔═══════════════════════════════════════════════╗"
echo "║                                               ║"
echo "║          ✅ INSTALLATION COMPLETE! ✅          ║"
echo "║                                               ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "📚 Next steps:"
echo ""
echo "1. Run the tool:"
echo "   ./build-apk"
echo ""
echo "2. Or if alias is set:"
echo "   build-apk"
echo ""
echo "3. Default credentials:"
echo "   Username: Daffa"
echo "   Password: daffajago123"
echo ""
echo "4. Get GitHub Token:"
echo "   https://github.com/settings/tokens"
echo ""
echo "Happy building! 🎉"
