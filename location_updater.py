import time
import requests
import random

BASESTATION_URL = "http://localhost:30001/v1/update_location"
SATELLITE_ID = "satellite-group-13"

def generate_random_location():
    """Generates a random location to simulate GPS coordinates."""
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return {"latitude": latitude, "longitude": longitude}

def send_location_update():
    """Generates a new location and sends it to the basestation."""
    location = generate_random_location()
    try:
        response = requests.post(BASESTATION_URL, json={
            "satellite_id": SATELLITE_ID,
            "location": location
        })
        if response.status_code == 200:
            print(f"Location updated successfully: {location}")
        else:
            print(f"Location update failed, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to the basestation: {e}")

def start_location_update():
    """Updates location every 5 minutes."""
    while True:
        send_location_update()
        time.sleep(300)
