# modules/nlp.py
import nltk
import re
from datetime import datetime
import os

class NLP:
    def __init__(self):
        print("NLP module initialized.")
        # Download required NLTK data if not present
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        # Command patterns
        self.command_patterns = {
            'greeting': [r'\b(hello|hi|hey|good morning|good afternoon|good evening)\b'],
            'time': [r'\b(what time|current time|time now)\b'],
            'date': [r'\b(what date|current date|today\'s date)\b'],
            'weather': [r'\b(weather|temperature|forecast)\b'],
            'reminder': [r'\b(remind me|set reminder|reminder)\b'],
            'file_operation': [r'\b(open file|find file|create file|delete file)\b'],
            'whatsapp': [r'\b(send message|whatsapp|message|text)\b'],
            'work_help': [r'\b(help with work|work assistance|productivity|start session|end session|stats|system stats)\b'],
            'vision_command': [r'\b(look at|see|watch|monitor|detect|can you see)\b'],
            'goodbye': [r'\b(goodbye|bye|see you|exit|quit)\b']
        }

    def process(self, text):
        """Process natural language input and return command and parameters"""
        if not text:
            return None, {}
        
        text = text.lower().strip()
        
        # Find matching command
        for command, patterns in self.command_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return command, self._extract_parameters(text, command)
        
        # If no specific command found, return as general query
        return 'general', {'text': text}
    
    def _extract_parameters(self, text, command):
        """Extract parameters from text based on command type"""
        params = {}
        
        if command == 'reminder':
            # Extract time and message for reminders
            time_match = re.search(r'\b(\d{1,2}):(\d{2})\b', text)
            if time_match:
                params['time'] = f"{time_match.group(1)}:{time_match.group(2)}"
            
            # Extract the reminder message (everything after common reminder phrases)
            reminder_text = re.sub(r'\b(remind me to|set reminder to|remind me|set reminder|reminder)\b', '', text).strip()
            params['message'] = reminder_text if reminder_text else "reminder task"
        
        elif command == 'whatsapp':
            # Extract contact and message
            contact_match = re.search(r'\bto ([a-zA-Z\s]+)', text)
            if contact_match:
                params['contact'] = contact_match.group(1).strip()
            
            message_match = re.search(r'\bmessage (.+)', text)
            if message_match:
                params['message'] = message_match.group(1).strip()
        
        elif command == 'file_operation':
            # Extract file name and operation
            if 'open' in text:
                params['operation'] = 'open'
            elif 'create' in text:
                params['operation'] = 'create'
            elif 'delete' in text:
                params['operation'] = 'delete'
            elif 'find' in text:
                params['operation'] = 'find'
            
            # Extract filename
            file_match = re.search(r'\bfile ([a-zA-Z0-9._\-]+)', text)
            if file_match:
                params['filename'] = file_match.group(1)
        
        params['original_text'] = text
        return params

    def generate_response(self, command, params):
        """Generate appropriate response for commands"""
        responses = {
            'greeting': "Hello! I'm Persona, your personal assistant. How can I help you today?",
            'time': f"The current time is {datetime.now().strftime('%H:%M:%S')}",
            'date': f"Today's date is {datetime.now().strftime('%B %d, %Y')}",
            'weather': "I'd be happy to help with weather information. Let me check that for you.",
            'reminder': f"I'll remind you about: {params.get('message', 'your task')}",
            'whatsapp': f"I'll send a message to {params.get('contact', 'your contact')}",
            'work_help': "I'm here to help with your work. What do you need assistance with?",
            'vision_command': "I'm watching and ready to help with visual tasks.",
            'goodbye': "Goodbye! I'll be here when you need me.",
            'general': "I understand you said something, but I'm not sure how to help with that specific request."
        }
        
        return responses.get(command, "I'm not sure how to handle that request.")