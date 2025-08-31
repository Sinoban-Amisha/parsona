# 🤖 Persona - Personal Desktop Assistant

A fully functional personal desktop assistant inspired by Jarvis, featuring continuous monitoring, voice interaction, work assistance, and smart integrations.

## ✨ Features

### 🎯 Core Capabilities
- **Continuous Vision Monitoring**: Always watching your workspace, detects when you arrive/leave
- **Voice Activation**: Responds to "Hey Persona" or "Jarvis" 
- **Natural Language Processing**: Understands and processes natural speech
- **Persistent Memory**: Remembers conversations, preferences, and data
- **Smart Reminders**: Set and receive intelligent reminders

### 💼 Work Assistant
- **Work Session Tracking**: Monitor your productivity and work sessions
- **File Management**: Open, find, and manage files with voice commands
- **System Monitoring**: Check CPU, memory, and disk usage
- **Break Suggestions**: Smart break reminders based on work duration

### 📱 Communication
- **WhatsApp Integration**: Send messages and status updates
- **Status Notifications**: Get notified about your workspace activity
- **Conversation Logging**: All interactions are saved for context

### 🖥️ Multiple Interfaces
- **Command Line**: Interactive terminal interface
- **Desktop GUI**: Modern graphical interface
- **Voice Only**: Hands-free operation
- **Background Service**: Always-on monitoring

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Running the Assistant

#### Option 1: Quick Start (Recommended)
```bash
python3 start.py
```

#### Option 2: Interactive Menu
```bash
python3 main.py
```

#### Option 3: Desktop GUI
```bash
python3 ui/desktop.py
```

#### Option 4: Demo Mode
```bash
python3 demo.py
```

## 🗣️ Voice Commands

Once activated (say "Hey Persona"), try these commands:

### Basic Interaction
- "Hello" / "Hi"
- "What time is it?"
- "What's today's date?"

### Work Management  
- "Start work session [task name]"
- "End work session"
- "System stats"
- "Help with my work"

### File Operations
- "Open file [filename]"
- "Find file [search term]"

### Reminders & Communication
- "Set a reminder to [task]"
- "Send message to [contact] [message]"

### Vision & Monitoring
- "Can you see me?"
- "Monitor my workspace"

## 📋 System Requirements

- Python 3.8+
- Webcam (for vision monitoring)
- Microphone (for voice commands)
- Internet connection (for speech recognition)

## 🔧 Configuration

Edit `config.py` to customize:
- WhatsApp contacts
- Wake words
- Timing settings
- File paths

## 🏗️ Architecture

The assistant consists of modular components:

- **Vision Module**: Face detection and continuous monitoring
- **Speech Module**: Speech recognition and text-to-speech
- **NLP Module**: Natural language understanding and response generation
- **Memory Module**: Data persistence and conversation history
- **Work Assistant**: Productivity and file management features
- **WhatsApp Module**: Communication integration
- **Assistant Controller**: Coordinates all modules

## 📈 Capabilities Summary

✅ **Continuous user monitoring**  
✅ **Voice-activated commands**  
✅ **Natural conversation**  
✅ **Work productivity tracking**  
✅ **File management**  
✅ **Smart reminders**  
✅ **WhatsApp messaging**  
✅ **System monitoring**  
✅ **Persistent memory**  
✅ **Multiple interfaces (CLI, GUI, Voice)**  

## 🛠️ Development

To extend functionality:
1. Add new command patterns in `modules/nlp.py`
2. Implement command handlers in `modules/assistant.py`
3. Add new modules for additional features

## 📝 License

This project is open source and available under the MIT License.