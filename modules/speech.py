import speech_recognition as sr
import threading
import time
from datetime import datetime

# Try to import pyttsx3, handle gracefully if not available
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Warning: pyttsx3 not available, speech output disabled")

class Speech:
    def __init__(self):
        print("Speech module initialized.")
        self.recognizer = sr.Recognizer()
        self.engine = None
        
        # Initialize TTS engine if available
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                
                # Configure voice
                voices = self.engine.getProperty('voices')
                if voices:
                    # Try to use a female voice if available
                    for voice in voices:
                        if 'female' in voice.name.lower():
                            self.engine.setProperty('voice', voice.id)
                            break
                
                # Set speech rate
                self.engine.setProperty('rate', 180)
            except Exception as e:
                print(f"Warning: TTS engine initialization failed: {e}")
                self.engine = None
        
        # Continuous listening state
        self.is_listening = False
        self.listen_thread = None
        self.callback_func = None

    def listen(self):
        """Single speech recognition attempt"""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                try:
                    # Adjust for ambient noise
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                except sr.WaitTimeoutError:
                    return ""
            
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, could not understand.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
        except Exception as e:
            print(f"Microphone not available: {e}")
            return ""

    def speak(self, text):
        """Text-to-speech output"""
        print(f"Persona says: {text}")
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}")

    def start_continuous_listening(self, callback_func):
        """Start continuous speech recognition in background"""
        try:
            # Check if microphone is available
            test_mic = sr.Microphone()
            with test_mic as source:
                pass  # Test if we can access microphone
            
            if not self.is_listening:
                self.is_listening = True
                self.callback_func = callback_func
                self.listen_thread = threading.Thread(target=self._continuous_listen, daemon=True)
                self.listen_thread.start()
                print("Continuous listening started. Say 'Hey Persona' to activate.")
        except Exception as e:
            print(f"Warning: Microphone not available: {e}")
            print("Voice commands disabled. Use text input instead.")
    
    def stop_continuous_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
        if self.listen_thread:
            self.listen_thread.join(timeout=2)
        print("Continuous listening stopped.")
    
    def _continuous_listen(self):
        """Background listening loop"""
        try:
            microphone = sr.Microphone()
            
            with microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
            
            while self.is_listening:
                try:
                    with microphone as source:
                        # Listen for wake word with shorter timeout
                        audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
                    
                    try:
                        text = self.recognizer.recognize_google(audio).lower()
                        
                        # Check for wake words
                        if any(wake_word in text for wake_word in ['hey persona', 'persona', 'jarvis']):
                            print(f"[{datetime.now().strftime('%H:%M:%S')}] Wake word detected!")
                            self.speak("Yes, how can I help you?")
                            
                            # Listen for the actual command
                            command_text = self._listen_for_command()
                            if command_text and self.callback_func:
                                self.callback_func(command_text)
                    
                    except sr.UnknownValueError:
                        # Ignore if speech not recognized
                        pass
                    except sr.RequestError:
                        # Handle API errors gracefully
                        time.sleep(1)
                
                except sr.WaitTimeoutError:
                    # Normal timeout, continue listening
                    pass
                except Exception as e:
                    print(f"Error in continuous listening: {e}")
                    time.sleep(2)
        except Exception as e:
            print(f"Could not start continuous listening: {e}")
            self.is_listening = False
    
    def _listen_for_command(self):
        """Listen for command after wake word"""
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
            
            text = self.recognizer.recognize_google(audio)
            print(f"Command received: {text}")
            return text
        
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            self.speak("I didn't catch that. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Error processing command: {e}")
            return ""