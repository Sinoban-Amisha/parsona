import cv2
import os
import threading
import time
from datetime import datetime

class Vision:
    def __init__(self):
        print("Vision module initialized.")
        # Path to Haar Cascade file
        cascade_path = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        # Monitoring state
        self.is_monitoring = False
        self.monitor_thread = None
        self.user_present = False
        self.last_detection_time = None
        self.callbacks = []  # For notifying other modules

    def detect_face(self):
        """Manual face detection mode"""
        try:
            # Start webcam
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Warning: Camera not available. Face detection disabled.")
                return
            
            print("Press 'q' to quit.")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow("Face Detection - Persona", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Camera error: {e}")
            print("Face detection not available in this environment.")
    
    def start_continuous_monitoring(self):
        """Start continuous background monitoring"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.monitor_thread = threading.Thread(target=self._continuous_monitor, daemon=True)
            self.monitor_thread.start()
            print("Continuous monitoring started.")
    
    def stop_continuous_monitoring(self):
        """Stop continuous monitoring"""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        print("Continuous monitoring stopped.")
    
    def _continuous_monitor(self):
        """Background monitoring loop"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Warning: Could not open camera for monitoring")
            return
        
        while self.is_monitoring:
            ret, frame = cap.read()
            if not ret:
                time.sleep(1)
                continue
            
            # Detect faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            
            current_time = datetime.now()
            user_detected = len(faces) > 0
            
            # Update user presence status
            if user_detected:
                if not self.user_present:
                    print(f"[{current_time.strftime('%H:%M:%S')}] User detected - Welcome back!")
                    self._notify_callbacks('user_arrived')
                self.user_present = True
                self.last_detection_time = current_time
            else:
                if self.user_present and self.last_detection_time:
                    # User left if no detection for 10 seconds
                    if (current_time - self.last_detection_time).seconds > 10:
                        print(f"[{current_time.strftime('%H:%M:%S')}] User left workspace")
                        self.user_present = False
                        self._notify_callbacks('user_left')
            
            time.sleep(2)  # Check every 2 seconds
        
        cap.release()
    
    def add_callback(self, callback_func):
        """Add callback function for vision events"""
        self.callbacks.append(callback_func)
    
    def _notify_callbacks(self, event):
        """Notify all registered callbacks about vision events"""
        for callback in self.callbacks:
            try:
                callback(event)
            except Exception as e:
                print(f"Error in vision callback: {e}")
    
    def is_user_present(self):
        """Check if user is currently present"""
        return self.user_present
    
    def get_workspace_status(self):
        """Get current workspace status"""
        status = {
            'user_present': self.user_present,
            'monitoring_active': self.is_monitoring,
            'last_detection': self.last_detection_time.isoformat() if self.last_detection_time else None
        }
        return status