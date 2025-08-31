# modules/work_assistant.py
import os
import subprocess
import psutil
from datetime import datetime, timedelta
import schedule
import time
import threading

class WorkAssistant:
    def __init__(self):
        print("Work Assistant module initialized.")
        self.reminders = []
        self.work_sessions = []
        self.current_session = None
        self.scheduler_running = False
        self.scheduler_thread = None
    
    def start_work_session(self, task_name):
        """Start a new work session"""
        if self.current_session:
            self.end_work_session()
        
        self.current_session = {
            'task': task_name,
            'start_time': datetime.now(),
            'breaks': 0
        }
        return f"Started work session: {task_name}"
    
    def end_work_session(self):
        """End current work session"""
        if not self.current_session:
            return "No active work session"
        
        session = self.current_session
        session['end_time'] = datetime.now()
        session['duration'] = session['end_time'] - session['start_time']
        
        self.work_sessions.append(session)
        self.current_session = None
        
        return f"Work session ended. Duration: {session['duration']}"
    
    def suggest_break(self):
        """Suggest a break based on work duration"""
        if not self.current_session:
            return None
        
        work_duration = datetime.now() - self.current_session['start_time']
        
        # Suggest break every 45 minutes
        if work_duration.seconds > 2700:  # 45 minutes
            return "You've been working for a while. Consider taking a 10-minute break!"
        
        return None
    
    def open_file(self, filename):
        """Open a file using default application"""
        try:
            if os.path.exists(filename):
                if os.name == 'nt':  # Windows
                    os.startfile(filename)
                elif os.name == 'posix':  # macOS and Linux
                    subprocess.call(['xdg-open', filename])
                return f"Opened file: {filename}"
            else:
                return f"File not found: {filename}"
        except Exception as e:
            return f"Error opening file: {str(e)}"
    
    def find_files(self, pattern, search_path="."):
        """Find files matching pattern"""
        try:
            found_files = []
            for root, dirs, files in os.walk(search_path):
                for file in files:
                    if pattern.lower() in file.lower():
                        found_files.append(os.path.join(root, file))
                if len(found_files) >= 10:  # Limit results
                    break
            
            if found_files:
                return f"Found {len(found_files)} files:\n" + "\n".join(found_files[:10])
            else:
                return f"No files found matching '{pattern}'"
        except Exception as e:
            return f"Error searching files: {str(e)}"
    
    def get_system_stats(self):
        """Get current system performance stats"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            stats = {
                'cpu_usage': cpu_percent,
                'memory_usage': memory.percent,
                'memory_available': f"{memory.available / (1024**3):.1f} GB",
                'disk_usage': disk.percent,
                'disk_free': f"{disk.free / (1024**3):.1f} GB"
            }
            
            return stats
        except Exception as e:
            return {"error": str(e)}
    
    def set_reminder(self, message, minutes_from_now):
        """Set a reminder for specified minutes from now"""
        reminder_time = datetime.now() + timedelta(minutes=minutes_from_now)
        reminder = {
            'message': message,
            'time': reminder_time,
            'completed': False
        }
        self.reminders.append(reminder)
        
        # Schedule the reminder
        schedule.every().day.at(reminder_time.strftime("%H:%M")).do(
            self._trigger_reminder, message
        ).tag(f"reminder_{len(self.reminders)}")
        
        if not self.scheduler_running:
            self.start_scheduler()
        
        return f"Reminder set for {reminder_time.strftime('%H:%M')}: {message}"
    
    def _trigger_reminder(self, message):
        """Trigger a reminder"""
        print(f"\n🔔 REMINDER: {message}")
        return schedule.CancelJob  # Remove this reminder after triggering
    
    def start_scheduler(self):
        """Start the background scheduler"""
        if not self.scheduler_running:
            self.scheduler_running = True
            self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
            self.scheduler_thread.start()
    
    def _run_scheduler(self):
        """Background scheduler loop"""
        while self.scheduler_running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def get_work_summary(self):
        """Get summary of work sessions"""
        if not self.work_sessions:
            return "No completed work sessions"
        
        total_time = sum([session['duration'].seconds for session in self.work_sessions])
        hours = total_time // 3600
        minutes = (total_time % 3600) // 60
        
        return f"Today's work: {len(self.work_sessions)} sessions, {hours}h {minutes}m total"