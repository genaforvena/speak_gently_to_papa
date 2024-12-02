# Telegram Message Blocker

This project aims to prevent sending messages in Telegram when a specific contact is open. It intercepts the Enter key to block message sending.

## Features

- Detects when the Telegram window with the contact "Papa" is open.
- Blocks the Enter key to prevent message sending.

## Usage

1. Clone this repository.
2. Ensure you have the required Python libraries:
   - `pynput`
   - `pygetwindow`
3. Run the script:
   ```bash
   python main.py
