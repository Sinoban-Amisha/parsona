# modules/whatsapp.py
from datetime import datetime, timedelta
import webbrowser
import urllib.parse

class WhatsApp:
    def __init__(self):
        print("WhatsApp module initialized.")
        self.contacts = {
            # Default contacts - user can add more
            'self': '+1234567890',  # User's own number
        }
    
    def send_message(self, contact, message, schedule_time=None):
        """Send WhatsApp message to contact using web interface"""
        try:
            # Get phone number from contact name
            phone_number = self.contacts.get(contact.lower())
            if not phone_number:
                return f"Contact '{contact}' not found. Available contacts: {list(self.contacts.keys())}"
            
            # Clean phone number (remove + and spaces)
            clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
            
            # Encode message for URL
            encoded_message = urllib.parse.quote(message)
            
            # Create WhatsApp web URL
            whatsapp_url = f"https://web.whatsapp.com/send?phone={clean_number}&text={encoded_message}"
            
            # Open in browser
            webbrowser.open(whatsapp_url)
            
            return f"WhatsApp web opened to send message to {contact}: {message}"
        
        except Exception as e:
            return f"Error opening WhatsApp: {str(e)}"
    
    def add_contact(self, name, phone_number):
        """Add a new contact"""
        self.contacts[name.lower()] = phone_number
        return f"Contact {name} added successfully"
    
    def list_contacts(self):
        """List all available contacts"""
        return list(self.contacts.keys())
    
    def send_status_update(self, status_message):
        """Send status update to user's own number"""
        print(f"📱 WhatsApp Status Update: {status_message}")
        # For demo purposes, just print instead of actually sending
        return f"Status logged: {status_message}"