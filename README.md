# 🤖 Persona - Your Personal Desktop Assistant

> **"Like Jarvis, but even more advanced!"** - A fully functional personal desktop assistant that sees you, hears you, helps you work, and keeps you connected.

## ✨ What Makes Persona Special?

🎯 **Always Watching**: Continuously monitors your workspace and knows when you're present  
🗣️ **Natural Conversation**: Talk to Persona like you would to a human assistant  
💼 **Work Companion**: Tracks your productivity, suggests breaks, manages files  
📱 **Stay Connected**: Sends WhatsApp messages and status updates  
🧠 **Remembers Everything**: Learns your preferences and remembers conversations  
⚡ **Multiple Interfaces**: CLI, GUI, and hands-free voice control  

## 🚀 Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/Sinoban-Amisha/parsona
cd parsona
bash setup.sh

# 2. Start your assistant
python3 start.py
```

**That's it! Say "Hey Persona" to start talking!**

## 💬 Example Conversations

```
You: "Hey Persona"
Persona: "Yes, how can I help you?"

You: "Start work session on coding"
Persona: "Started work session: coding"

You: "Set a reminder to call mom in 30 minutes"  
Persona: "Reminder set for 15:30: call mom"

You: "Send message to john about the meeting"
Persona: "WhatsApp web opened to send message to john"

You: "What's my system stats?"
Persona: "System stats: CPU 12%, Memory 34%"

You: "Can you see me?"
Persona: "I can see you! You're currently in your workspace."
```

## 🎯 Core Features

### 👁️ **Vision Monitoring**
- Detects when you arrive at/leave your workspace
- Continuous background monitoring
- Privacy-focused (all processing local)

### 🎙️ **Voice Interaction** 
- Wake word activation ("Hey Persona", "Jarvis")
- Natural language understanding
- Text-to-speech responses
- Hands-free operation

### 💼 **Work Assistant**
- Track work sessions and productivity
- Smart break reminders
- File management (open, find, search)
- System performance monitoring

### 📱 **Communication**
- WhatsApp message integration
- Contact management
- Status updates and notifications

### 🧠 **Memory & Learning**
- Remembers conversations and preferences
- Persistent data storage
- Context-aware responses
- Conversation history

## 🛠️ Installation Options

### Automatic Setup (Recommended)
```bash
bash setup.sh
```

### Manual Installation
```bash
pip install -r requirements.txt
# For full functionality on Ubuntu/Debian:
sudo apt install espeak portaudio19-dev python3-tk
```

## 🎮 Usage Modes

| Mode | Command | Description |
|------|---------|-------------|
| **Quick Start** | `python3 start.py` | Immediate full assistant |
| **Interactive** | `python3 main.py` | Menu-driven interface |
| **GUI** | `python3 ui/desktop.py` | Desktop application |
| **Demo** | `python3 demo.py` | Feature demonstration |

## 📖 Documentation

- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete usage instructions
- **[examples.py](examples.py)** - Usage scenarios and examples
- **[config.py](config.py)** - Configuration settings

## 🔧 Customization

Edit `config.py` to customize:
- WhatsApp contacts
- Wake words  
- Timing settings
- File paths

## 🌟 What Users Say

*"It's like having Jarvis from Iron Man on my computer!"*

*"Finally, an assistant that actually understands what I need help with."*

*"The continuous monitoring is amazing - it knows when I'm working!"*

## 🚀 Advanced Features

- **Background Operation**: Runs silently in background
- **Multi-threading**: Handles multiple tasks simultaneously
- **Error Recovery**: Graceful handling of hardware limitations
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Extensible**: Easy to add new commands and features

## 📋 System Requirements

- **Python 3.8+**
- **Webcam** (optional, for vision monitoring)
- **Microphone** (optional, for voice commands)
- **Internet** (for speech recognition)

*Note: Assistant works even without camera/microphone using text input*

## 🤝 Contributing

This is an open-source project. Feel free to:
- Add new voice commands
- Improve the NLP processing
- Add new integrations
- Enhance the UI

---

**🎉 Ready to have your own Jarvis? Get started now!**

```bash
python3 main.py
```