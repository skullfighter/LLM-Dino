import cv2
import numpy as np
import pyautogui
import time
import requests
import mss
from PIL import Image

# === CONFIG ===
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"
SPEED = 0.05  # Dino speed (adjust as needed)

# Screenshot region just in front of the Dino
DETECTION_REGION = {
    'top': 272,
    'left': 922,
    'width': 233,
    'height': 190
}

# === FUNCTIONS ===

def capture_screen(region):
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
        return np.array(img)

def detect_obstacle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    obstacle_pixels = cv2.countNonZero(thresh)
    return obstacle_pixels > 50  # Adjust this threshold if needed

def ask_llm_jump_or_not(obstacle_detected):
    prompt = (
        f"There is {'an' if obstacle_detected else 'no'} obstacle ahead in the Dino game. "
        f"Should the Dino jump? Reply with yes or no."
    )
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    reply = response.json()['response'].strip().lower()
    return "yes" in reply
     
def perform_jump():
    pyautogui.press('space')

# === MAIN LOOP ===
print("LLM Dino bot is starting in 3 seconds... Focus the game window!")
time.sleep(3)

while True:
    frame = capture_screen(DETECTION_REGION)
    obstacle = detect_obstacle(frame)
    should_jump = ask_llm_jump_or_not(obstacle)
    print(f"Obstacle: {obstacle} → Jump: {should_jump}")
    if should_jump:
        perform_jump()
    time.sleep(SPEED)
