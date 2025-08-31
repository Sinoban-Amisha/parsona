#!/usr/bin/env python3
"""
Persona Assistant - Quick Start Script
This script provides easy ways to launch the assistant
"""

import sys
import os

def quick_start():
    """Quick start the full assistant"""
    print("🚀 Quick Starting Persona Assistant...")
    
    # Import here to avoid issues if modules aren't ready
    try:
        from modules.assistant import PersonaAssistant
        
        assistant = PersonaAssistant()
        assistant.start()
        
        print("\n✅ Persona is now active!")
        print("Say 'Hey Persona' to interact, or press Ctrl+C to stop")
        
        # Keep running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down...")
            assistant.stop()
            
    except ImportError as e:
        print(f"❌ Error importing modules: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error starting assistant: {e}")

def show_help():
    """Show usage help"""
    print("🤖 Persona Assistant - Usage")
    print("=" * 40)
    print("python3 start.py              - Quick start assistant")
    print("python3 main.py               - Interactive menu")
    print("python3 demo.py               - Run demonstration")
    print("python3 ui/desktop.py         - Launch GUI")
    print("python3 start.py --help       - Show this help")

if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
    else:
        import time
        quick_start()