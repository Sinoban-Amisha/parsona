import speech_recognition as sr
import pyttsx3

class Speech:
    def __init__(self):
        print("Speech module initialized.")
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except Exception as e:
            print("Sorry, could not understand.")
            return ""

    def speak(self, text):
        print(f"Persona says: {text}")
        self.engine.say(text)
        self.engine.runAndWait()