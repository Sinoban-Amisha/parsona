# modules/assistant.py
import threading
import time
import re
from datetime import datetime
from modules.vision import Vision
from modules.speech import Speech
from modules.nlp import NLP
from modules.memory import Memory
from modules.work_assistant import WorkAssistant
from modules.whatsapp import WhatsApp

class PersonaAssistant:
    def __init__(self):
        print("Initializing Persona Assistant...")
        
        # Initialize all modules
        self.vision = Vision()
        self.speech = Speech()
        self.nlp = NLP()
        self.memory = Memory()
        self.work_assistant = WorkAssistant()
        self.whatsapp = WhatsApp()
        
        # State
        self.is_running = False
        self.conversation_active = False
        
        # Set up callbacks
        self.vision.add_callback(self._handle_vision_event)
        
        print("Persona Assistant ready!")
    
    def start(self):
        """Start the assistant in full operation mode"""
        print("Starting Persona Assistant...")
        self.is_running = True
        
        # Start continuous monitoring
        self.vision.start_continuous_monitoring()
        self.speech.start_continuous_listening(self._handle_voice_command)
        self.work_assistant.start_scheduler()
        
        # Welcome message
        self.speech.speak("Hello! I'm Persona, your personal assistant. I'm now monitoring your workspace and ready to help.")
        
        return "Assistant started successfully"
    
    def stop(self):
        """Stop the assistant"""
        print("Stopping Persona Assistant...")
        self.is_running = False
        
        self.vision.stop_continuous_monitoring()
        self.speech.stop_continuous_listening()
        
        self.speech.speak("Goodbye! I'll be here when you need me.")
        return "Assistant stopped"
    
    def _handle_vision_event(self, event):
        """Handle vision-related events"""
        current_time = datetime.now().strftime('%H:%M:%S')
        
        if event == 'user_arrived':
            # User came back to workspace
            self.memory.remember('last_seen', current_time)
            
            # Check for reminders
            reminders = self.memory.get_pending_reminders()
            if reminders:
                self.speech.speak("Welcome back! You have pending reminders.")
            
            # Optionally send WhatsApp status
            self.whatsapp.send_status_update(f"User returned to workspace at {current_time}")
        
        elif event == 'user_left':
            # User left workspace
            if self.work_assistant.current_session:
                suggestion = self.work_assistant.suggest_break()
                if suggestion:
                    print(f"Break suggestion: {suggestion}")
    
    def _handle_voice_command(self, text):
        """Process voice commands through NLP"""
        if not text:
            return
        
        # Process through NLP
        command, params = self.nlp.process(text)
        response = self._execute_command(command, params)
        
        # Log interaction
        self.memory.log_interaction(text, response)
        
        # Speak response
        self.speech.speak(response)
    
    def _execute_command(self, command, params):
        """Execute commands based on NLP processing"""
        try:
            if command == 'greeting':
                return self.nlp.generate_response(command, params)
            
            elif command == 'time':
                return self.nlp.generate_response(command, params)
            
            elif command == 'date':
                return self.nlp.generate_response(command, params)
            
            elif command == 'reminder':
                message = params.get('message', 'Task reminder')
                result = self.work_assistant.set_reminder(message, 5)  # 5 minutes default
                return result
            
            elif command == 'whatsapp':
                contact = params.get('contact', 'self')
                message = params.get('message', 'Hello from Persona!')
                result = self.whatsapp.send_message(contact, message)
                return result
            
            elif command == 'file_operation':
                operation = params.get('operation')
                filename = params.get('filename', '')
                
                if operation == 'open':
                    return self.work_assistant.open_file(filename)
                elif operation == 'find':
                    return self.work_assistant.find_files(filename)
                else:
                    return f"File operation '{operation}' not yet implemented"
            
            elif command == 'work_help':
                original_text = params.get('original_text', '')
                if 'start session' in original_text or 'start work' in original_text:
                    # Extract task name
                    task_match = re.search(r'(?:start (?:work )?session (?:on |for )?)(.*)', original_text)
                    task_name = task_match.group(1).strip() if task_match else "Work Session"
                    return self.work_assistant.start_work_session(task_name)
                elif 'end session' in original_text:
                    return self.work_assistant.end_work_session()
                elif 'stats' in original_text or 'system' in original_text:
                    stats = self.work_assistant.get_system_stats()
                    return f"System stats: CPU {stats['cpu_usage']}%, Memory {stats['memory_usage']}%"
                else:
                    return "I can help you start work sessions, check system stats, or manage files. What would you like to do?"
            
            elif command == 'vision_command':
                status = self.vision.get_workspace_status()
                if status['user_present']:
                    return "I can see you! You're currently in your workspace."
                else:
                    return "I don't see you in the workspace right now."
            
            elif command == 'goodbye':
                return "Goodbye! I'll continue monitoring in the background."
            
            else:
                return self.nlp.generate_response(command, params)
        
        except Exception as e:
            return f"I encountered an error processing that command: {str(e)}"
    
    def get_status(self):
        """Get current assistant status"""
        status = {
            'running': self.is_running,
            'vision_monitoring': self.vision.is_monitoring,
            'speech_listening': self.speech.is_listening,
            'user_present': self.vision.is_user_present(),
            'current_work_session': self.work_assistant.current_session is not None
        }
        return status