import time
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            print("Enter key pressed. Blocking message.")
            return False  # Block the Enter key
    except AttributeError:
        pass

def main():
    print("Monitoring for Telegram messages to 'Papa'.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
