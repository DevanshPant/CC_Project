import requests
import time
import random
import webbrowser
import os
import threading

# Firebase Database URL
FIREBASE_URL = "https://vehicle-tracker-edff8-default-rtdb.firebaseio.com/vehicle_location.json"

# Starting coordinates (Mumbai)
lat = 19.0760
lng = 72.8777

def open_dashboard():
    time.sleep(1.5)  # wait a moment so terminal prints first
    dashboard_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    webbrowser.open(f"file:///{dashboard_path}")
    print("Dashboard opened in browser!")

print("=" * 45)
print("CLOUD VEHICLE TRACKER")
print("=" * 45)
print("Connecting to Firebase...")
print("Opening dashboard in browser...")
print("   [Press Ctrl+C to stop]\n")

# Open browser automatically in background
threading.Thread(target=open_dashboard, daemon=True).start()

while True:
    # Simulate movement
    lat += random.uniform(-0.0005, 0.0005)
    lng += random.uniform(-0.0005, 0.0005)

    data = {
        "latitude": lat,
        "longitude": lng,
        "timestamp": time.time()
    }

    response = requests.put(FIREBASE_URL, json=data)

    if response.status_code == 200:
        print(f"Updated → Lat: {lat:.5f} | Lng: {lng:.5f}")
    else:
        print(f"Error {response.status_code}: {response.text}")

    time.sleep(3)
