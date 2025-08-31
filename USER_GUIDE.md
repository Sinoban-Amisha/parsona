# 🤖 Persona Assistant - User Guide

## Getting Started

### Installation
1. Run the setup script: `bash setup.sh`
2. Or manually install: `pip install -r requirements.txt`

### Quick Start Options

#### Option 1: Quick Launch
```bash
python3 start.py
```
This immediately starts the full assistant with all features active.

#### Option 2: Interactive Menu
```bash
python3 main.py
```
Shows a menu to choose between:
- Simple Mode (basic face detection)
- Full Assistant Mode (complete Jarvis experience)
- GUI Mode (desktop interface)

#### Option 3: Demo Mode
```bash
python3 demo.py          # Basic feature demo
python3 full_demo.py     # Comprehensive conversation demo
```

## 🎯 Using Your Assistant

### Voice Activation
Say any of these to activate:
- "Hey Persona"
- "Persona"
- "Jarvis"

### Text Commands (when voice isn't available)
Use the format: `say <your command>`
Example: `say what time is it`

## 🗣️ Voice Commands Reference

### Basic Interaction
- **"Hello"** - Greet your assistant
- **"What time is it?"** - Get current time
- **"What's today's date?"** - Get current date
- **"Goodbye"** - End conversation

### Work & Productivity
- **"Start work session [on task name]"** - Begin tracking work
- **"End work session"** - Stop current work session
- **"System stats"** - Check CPU, memory usage
- **"Help me with my work"** - General work assistance

### File Management
- **"Open file [filename]"** - Open a file
- **"Find file [search term]"** - Search for files
- **"Create file [filename]"** - Create new file

### Reminders & Scheduling
- **"Set a reminder to [task]"** - Set a 5-minute reminder
- **"Remind me to [task] at [time]"** - Set timed reminder

### Communication
- **"Send message to [contact] about [message]"** - WhatsApp integration
- **"Add contact [name] [phone]"** - Add WhatsApp contact

### Monitoring & Vision
- **"Can you see me?"** - Check if assistant detects you
- **"Monitor my workspace"** - Confirm monitoring is active

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Your contacts for WhatsApp
DEFAULT_CONTACTS = {
    "self": "+1234567890",      # Your number
    "mom": "+1234567891",       # Family
    "work": "+1234567892",      # Work contact
}

# Wake words
WAKE_WORDS = ["hey persona", "persona", "jarvis"]

# Timing settings
BREAK_REMINDER_INTERVAL = 45  # minutes
```

## 📱 WhatsApp Setup

1. Edit `config.py` with your phone number
2. For contacts, use the command: "Add contact mom +1234567890"
3. Send messages with: "Send message to mom about dinner plans"

## 💡 Tips for Best Experience

### For Live Environment (your computer):
1. Ensure webcam and microphone permissions are granted
2. Install espeak for voice output: `sudo apt install espeak`
3. Install pyaudio for microphone: `sudo apt install portaudio19-dev`
4. Use in a quiet environment for better speech recognition

### Privacy & Security:
- All conversations are stored locally in `data/persona_memory.db`
- No data is sent to external servers except for speech recognition
- WhatsApp integration uses browser automation (secure)

## 🚨 Troubleshooting

### Common Issues:

**"Camera not available"**
- Ensure webcam is connected and not used by other apps
- Grant camera permissions to Python/terminal

**"Microphone not available"**
- Install pyaudio: `pip install pyaudio`
- Grant microphone permissions
- Check if microphone is working with other apps

**"TTS engine failed"**
- Install espeak: `sudo apt install espeak espeak-data`
- Or use text-only mode (assistant still works)

**"GUI not available"**
- Install tkinter: `sudo apt install python3-tk`
- Or use CLI mode instead

### Still Works Without:
Even if camera/microphone/voice aren't available, you can still:
- Use text commands (`say <message>`)
- Get work assistance
- Manage files
- Set reminders
- Use WhatsApp integration

## 🎉 Enjoy Your Assistant!

Your Persona assistant is now ready to help you like Jarvis! It will:
- ✅ Continuously monitor your workspace
- ✅ Respond to voice commands
- ✅ Help with work and productivity
- ✅ Send WhatsApp messages
- ✅ Remember conversations and preferences
- ✅ Provide intelligent assistance

**Have fun with your new AI companion!** 🤖✨