#!/bin/bash
# setup.sh - Installation script for Persona Assistant

echo "🤖 Setting up Persona Assistant..."
echo "=================================="

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is required but not installed"
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Install system dependencies for voice and vision (Ubuntu/Debian)
if command -v apt-get &> /dev/null; then
    echo "🔧 Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y espeak espeak-data libespeak1 libespeak-dev
    sudo apt-get install -y portaudio19-dev python3-pyaudio
    sudo apt-get install -y python3-tk  # For GUI support
fi

# Create necessary directories
mkdir -p data logs

echo "✅ Setup complete!"
echo ""
echo "🚀 To start Persona Assistant:"
echo "   python3 start.py      (Quick start)"
echo "   python3 main.py       (Interactive menu)"
echo "   python3 demo.py       (Demo mode)"
echo ""
echo "📝 Edit config.py to customize settings"
echo "📖 Check README.md for full documentation"