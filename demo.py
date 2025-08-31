#!/usr/bin/env python3
# demo.py - Demonstration of Persona Assistant capabilities

from modules.assistant import PersonaAssistant
from modules.nlp import NLP
from modules.memory import Memory
from modules.work_assistant import WorkAssistant
from modules.whatsapp import WhatsApp
import time

def demo_nlp():
    """Demonstrate NLP capabilities"""
    print("\n🧠 NLP Demo")
    print("=" * 40)
    
    nlp = NLP()
    
    test_inputs = [
        "Hello Persona",
        "What time is it?",
        "Set a reminder to call mom",
        "Send message to work about meeting",
        "Open file document.pdf",
        "Help me with my work",
        "System stats please"
    ]
    
    for text in test_inputs:
        command, params = nlp.process(text)
        response = nlp.generate_response(command, params)
        print(f"Input: '{text}'")
        print(f"Command: {command}")
        print(f"Response: {response}")
        print("-" * 40)

def demo_memory():
    """Demonstrate memory capabilities"""
    print("\n🧠 Memory Demo")
    print("=" * 40)
    
    memory = Memory()
    
    # Store some data
    memory.remember("user_name", "User")
    memory.remember("favorite_color", "blue")
    memory.remember("work_hours", {"start": "09:00", "end": "17:00"})
    
    # Recall data
    print(f"User name: {memory.recall('user_name')}")
    print(f"Favorite color: {memory.recall('favorite_color')}")
    print(f"Work hours: {memory.recall('work_hours')}")
    
    # Test interaction logging
    memory.log_interaction("Hello Persona", "Hello! How can I help you?")
    recent = memory.get_recent_interactions(1)
    print(f"Recent interaction: {recent[0] if recent else 'None'}")

def demo_work_assistant():
    """Demonstrate work assistant capabilities"""
    print("\n💼 Work Assistant Demo")
    print("=" * 40)
    
    work = WorkAssistant()
    
    # Start work session
    result = work.start_work_session("Code Review")
    print(result)
    
    # Get system stats
    stats = work.get_system_stats()
    print(f"System Stats: CPU {stats.get('cpu_usage', 'N/A')}%, Memory {stats.get('memory_usage', 'N/A')}%")
    
    # End session
    time.sleep(1)  # Brief work session
    result = work.end_work_session()
    print(result)
    
    # Find files
    result = work.find_files("py", ".")
    print(f"Python files found: {result}")

def demo_whatsapp():
    """Demonstrate WhatsApp capabilities"""
    print("\n📱 WhatsApp Demo")
    print("=" * 40)
    
    whatsapp = WhatsApp()
    
    # Add contact
    result = whatsapp.add_contact("John", "+1234567890")
    print(result)
    
    # List contacts
    contacts = whatsapp.list_contacts()
    print(f"Available contacts: {contacts}")
    
    # Send status update (demo mode)
    result = whatsapp.send_status_update("Persona demo completed successfully")
    print(result)

def run_demo():
    """Run all demonstrations"""
    print("🤖 PERSONA ASSISTANT DEMO")
    print("=" * 50)
    print("This demo shows the capabilities of your personal assistant")
    print("=" * 50)
    
    demo_nlp()
    demo_memory()
    demo_work_assistant()
    demo_whatsapp()
    
    print("\n✅ Demo completed!")
    print("=" * 50)
    print("To use the full assistant:")
    print("1. Run: python3 main.py")
    print("2. Select option 2 for Full Assistant Mode")
    print("3. Say 'Hey Persona' to interact via voice")
    print("4. Or use the GUI with option 3")

if __name__ == "__main__":
    run_demo()