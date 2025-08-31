# modules/memory.py
import sqlite3
import json
import os
from datetime import datetime

class Memory:
    def __init__(self):
        print("Memory module initialized.")
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'persona_memory.db')
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_database()
    
    def _init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                assistant_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                reminder_time DATETIME,
                created_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                completed BOOLEAN DEFAULT FALSE
            )
        ''')
        
        conn.commit()
        conn.close()

    def remember(self, key, value):
        """Store data in memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Convert value to JSON if it's not a string
        if not isinstance(value, str):
            value = json.dumps(value)
        
        cursor.execute('''
            INSERT OR REPLACE INTO memory (key, value, timestamp)
            VALUES (?, ?, ?)
        ''', (key, value, datetime.now()))
        
        conn.commit()
        conn.close()

    def recall(self, key):
        """Retrieve data from memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT value FROM memory WHERE key = ?', (key,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            try:
                return json.loads(result[0])
            except json.JSONDecodeError:
                return result[0]
        return None
    
    def log_interaction(self, user_input, assistant_response):
        """Log conversation for context"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO interactions (user_input, assistant_response, timestamp)
            VALUES (?, ?, ?)
        ''', (user_input, assistant_response, datetime.now()))
        
        conn.commit()
        conn.close()
    
    def add_reminder(self, message, reminder_time=None):
        """Add a reminder"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO reminders (message, reminder_time, created_time)
            VALUES (?, ?, ?)
        ''', (message, reminder_time, datetime.now()))
        
        conn.commit()
        conn.close()
    
    def get_pending_reminders(self):
        """Get all pending reminders"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, message, reminder_time FROM reminders 
            WHERE completed = FALSE
            ORDER BY reminder_time ASC
        ''')
        
        reminders = cursor.fetchall()
        conn.close()
        return reminders
    
    def get_recent_interactions(self, limit=10):
        """Get recent conversation history"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT user_input, assistant_response, timestamp 
            FROM interactions 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        
        interactions = cursor.fetchall()
        conn.close()
        return interactions