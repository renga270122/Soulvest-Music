import json
import os

PIN_FILE = "data/soulprompt_pins.json"

def load_pins():
    if os.path.exists(PIN_FILE):
        with open(PIN_FILE, "r") as f:
            return json.load(f)
    return []

def save_pin(prompt, reply, tag):
    pins = load_pins()
    pins.append({"prompt": prompt, "reply": reply, "tag": tag})
    with open(PIN_FILE, "w") as f:
        json.dump(pins, f, indent=2)
