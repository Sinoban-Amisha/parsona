from modules.vision import Vision
from modules.speech import Speech
from modules.nlp import NLP
from modules.memory import Memory
from modules.assistant import PersonaAssistant
import time

# Try to import GUI, make it optional
try:
    from ui.desktop import launch_ui
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False
    print("Note: GUI not available (tkinter not installed)")

def main():
    print("🤖 Welcome to Persona - Your Personal Desktop Assistant!")
    print("=====================================")
    
    while True:
        print("\nSelect Mode:")
        print("1. Simple Mode (Face Detection Only)")
        print("2. 🚀 Full Assistant Mode (Jarvis-like Experience)")
        if GUI_AVAILABLE:
            print("3. 🖥️ Desktop GUI Mode")
            print("4. Exit")
        else:
            print("3. Exit")
        print("=====================================")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            simple_mode()
        elif choice == "2":
            full_assistant_mode()
        elif choice == "3":
            if GUI_AVAILABLE:
                print("Launching Desktop GUI...")
                launch_ui()
            else:
                print("Goodbye!")
                break
        elif choice == "4" and GUI_AVAILABLE:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def simple_mode():
    """Original simple face detection mode"""
    print("\n--- Simple Face Detection Mode ---")
    vision = Vision()
    vision.detect_face()

def full_assistant_mode():
    """Advanced personal assistant mode"""
    print("\n🚀 Starting Full Assistant Mode...")
    print("=====================================")
    
    # Initialize the assistant
    assistant = PersonaAssistant()
    
    try:
        # Start the assistant
        assistant.start()
        
        print("\n🎯 Persona is now active!")
        print("Features available:")
        print("- Continuous vision monitoring")
        print("- Voice activation (say 'Hey Persona')")
        print("- Work session tracking")
        print("- WhatsApp messaging")
        print("- File management")
        print("- Smart reminders")
        print("\nCommands you can try:")
        print("- 'q' to return to main menu")
        print("- 'status' to check assistant status")
        print("- 'stats' to see system stats")
        print("- 'say <message>' to test voice processing")
        print("- 'help' for more commands")
        print("=====================================\n")
        
        # Keep assistant running until user chooses to exit
        while True:
            user_input = input().strip().lower()
            if user_input == 'q':
                break
            elif user_input == 'status':
                status = assistant.get_status()
                print(f"Assistant Status: {status}")
            elif user_input == 'stats':
                stats = assistant.work_assistant.get_system_stats()
                print(f"System Stats: {stats}")
            elif user_input.startswith('say '):
                # Manual text input for testing
                message = user_input[4:]
                assistant._handle_voice_command(message)
            elif user_input == 'help':
                print("Commands: 'q' (quit), 'status', 'stats', 'say <message>', 'help'")
                print("Voice commands: 'Hey Persona', 'What time is it?', 'Set reminder', etc.")
            else:
                if user_input:
                    print("Unknown command. Type 'help' for available commands.")
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nShutting down assistant...")
    
    finally:
        # Clean shutdown
        assistant.stop()
        print("Returned to main menu.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting Persona. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please restart the application.")