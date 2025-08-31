# Configuration for Persona Assistant
ASSISTANT_NAME = "Persona"
WAKE_WORDS = ["hey persona", "persona", "jarvis"]

# WhatsApp Configuration
DEFAULT_CONTACTS = {
    "self": "+1234567890",  # Replace with your actual number
    "work": "+1234567890",  # Replace with work contact
}

# Work Assistant Settings
BREAK_REMINDER_INTERVAL = 45  # minutes
DAILY_WORK_GOAL = 8  # hours

# Vision Settings
FACE_DETECTION_INTERVAL = 2  # seconds
USER_ABSENCE_THRESHOLD = 10  # seconds before considering user "left"

# Speech Settings
SPEECH_RATE = 180  # words per minute
VOICE_TIMEOUT = 5  # seconds
PHRASE_TIME_LIMIT = 10  # seconds

# Reminder Settings
DEFAULT_REMINDER_DELAY = 5  # minutes

# File paths
DATA_DIRECTORY = "data"
LOG_DIRECTORY = "logs"