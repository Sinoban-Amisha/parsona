# ui/desktop.py
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.assistant import PersonaAssistant

class PersonaUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Persona - Personal Desktop Assistant")
        self.root.geometry("500x400")
        self.root.configure(bg='#2c3e50')
        
        self.assistant = None
        self.assistant_thread = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🤖 PERSONA", 
            font=("Arial", 24, "bold"),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            self.root,
            text="Your Personal Desktop Assistant",
            font=("Arial", 12),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='#2c3e50')
        status_frame.pack(pady=10)
        
        self.status_label = tk.Label(
            status_frame,
            text="Status: Ready to start",
            font=("Arial", 11),
            fg='#e74c3c',
            bg='#2c3e50'
        )
        self.status_label.pack()
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            buttons_frame,
            text="🚀 Start Assistant",
            command=self.start_assistant,
            font=("Arial", 12, "bold"),
            fg='white',
            bg='#27ae60',
            width=15,
            height=2
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(
            buttons_frame,
            text="⏹️ Stop Assistant",
            command=self.stop_assistant,
            font=("Arial", 12, "bold"),
            fg='white',
            bg='#e74c3c',
            width=15,
            height=2,
            state='disabled'
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        # Features frame
        features_frame = tk.LabelFrame(
            self.root,
            text="Features Active",
            font=("Arial", 11, "bold"),
            fg='#ecf0f1',
            bg='#34495e',
            relief='groove'
        )
        features_frame.pack(pady=20, padx=20, fill='x')
        
        self.features_text = tk.Text(
            features_frame,
            height=8,
            width=50,
            font=("Arial", 10),
            bg='#34495e',
            fg='#ecf0f1',
            state='disabled'
        )
        self.features_text.pack(pady=10, padx=10)
        
        # Initialize features display
        self.update_features_display()
    
    def start_assistant(self):
        """Start the assistant in a separate thread"""
        if not self.assistant:
            self.assistant = PersonaAssistant()
        
        def run_assistant():
            self.assistant.start()
        
        self.assistant_thread = threading.Thread(target=run_assistant, daemon=True)
        self.assistant_thread.start()
        
        # Update UI
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.status_label.config(text="Status: Active and Monitoring", fg='#27ae60')
        
        self.update_features_display()
        messagebox.showinfo("Assistant Started", "Persona is now active and monitoring your workspace!")
    
    def stop_assistant(self):
        """Stop the assistant"""
        if self.assistant:
            self.assistant.stop()
        
        # Update UI
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.status_label.config(text="Status: Stopped", fg='#e74c3c')
        
        self.update_features_display()
        messagebox.showinfo("Assistant Stopped", "Persona has been stopped.")
    
    def update_features_display(self):
        """Update the features display"""
        self.features_text.config(state='normal')
        self.features_text.delete(1.0, tk.END)
        
        if self.assistant and self.assistant.is_running:
            features = [
                "✅ Continuous Vision Monitoring",
                "✅ Voice Activation ('Hey Persona')",
                "✅ Natural Language Processing",
                "✅ Work Session Tracking",
                "✅ Smart Reminders",
                "✅ WhatsApp Integration",
                "✅ File Management",
                "✅ System Monitoring",
                "",
                "Say 'Hey Persona' to interact!",
                "Available commands:",
                "- 'What time is it?'",
                "- 'Set a reminder'",
                "- 'Send a message'",
                "- 'Start work session'",
                "- 'Open file [filename]'",
                "- 'System stats'"
            ]
        else:
            features = [
                "⏸️ Vision Monitoring: Inactive",
                "⏸️ Voice Activation: Inactive", 
                "⏸️ Work Tracking: Inactive",
                "⏸️ Reminders: Inactive",
                "",
                "Click 'Start Assistant' to activate all features"
            ]
        
        self.features_text.insert(1.0, "\n".join(features))
        self.features_text.config(state='disabled')
    
    def run(self):
        """Run the UI"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            if self.assistant:
                self.assistant.stop()

def launch_ui():
    """Launch the desktop UI"""
    ui = PersonaUI()
    ui.run()

if __name__ == "__main__":
    launch_ui()