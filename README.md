# Jarvis AI WhatsApp Voice Assistant

A Windows-optimized Python desktop assistant that listens for "Hey Jarvis", understands voice commands, speaks responses, and controls WhatsApp Web through Playwright.

## Features

- Wake word flow: "Hey Jarvis ..."
- Microphone listening with `SpeechRecognition`
- Faster Whisper transcription
- Offline text-to-speech with `pyttsx3`
- WhatsApp Web automation with persistent Playwright login
- Send messages, read unread chats, open chats, send files, archive, and mute
- Rule-based command understanding plus transformer-backed sentiment
- Spam detection and smart reply helpers
- Reminder, memory, busy mode, and auto reply state
- Dark CustomTkinter GUI with microphone animation, logs, and command history
- SQLite persistence for commands, conversations, reminders, and memory

## Setup On Windows

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

3. If `pyaudio` fails to install, install the Microsoft C++ Build Tools or use a prebuilt wheel matching your Python version.

4. Start the app.

```powershell
python main.py
```

5. Click **Open WhatsApp** or say "Hey Jarvis open WhatsApp". Scan the QR code once. The browser profile is saved in `browser_profile/`.

## Environment Settings

Create a `.env` file in the project root when you want custom settings:

```env
ASSISTANT_NAME=Jarvis
WAKE_WORD=hey jarvis
OWNER_NAME=Boss
VOICE_AUTH_PHRASE=jarvis authorize
WHISPER_MODEL_SIZE=base
WHISPER_DEVICE=cpu
WHISPER_COMPUTE_TYPE=int8
HEADLESS_BROWSER=false
AUTO_REPLY_ENABLED=false
BUSY_MODE_ENABLED=false
```

## Example Voice Commands

- "Hey Jarvis open WhatsApp"
- "Hey Jarvis jarvis authorize"
- "Hey Jarvis send message to Mom saying I am on my way"
- "Hey Jarvis read unread messages"
- "Hey Jarvis read latest messages from Family"
- "Hey Jarvis send file C:\Users\ASUS\Pictures\photo.jpg to Rahul"
- "Hey Jarvis archive Office Group"
- "Hey Jarvis mute Family"
- "Hey Jarvis enable auto reply"
- "Hey Jarvis busy mode on"
- "Hey Jarvis remind me to call Rahul in 10 minutes"
- "Hey Jarvis remember office pin is 1234"
- "Hey Jarvis what is office pin"

## Module Guide

- `main.py` starts the GUI or CLI mode.
- `utils/config.py` manages environment settings and runtime folders.
- `utils/logger.py` configures console and rotating file logs.
- `database/models.py` stores memory, reminders, conversations, and command history.
- `voice/recognizer.py` handles microphone capture, wake word detection, and transcription.
- `voice/speaker.py` handles threaded text-to-speech.
- `whatsapp/automation.py` wraps WhatsApp Web actions using Playwright.
- `ai/nlp.py` parses commands, analyzes sentiment, detects spam, and creates smart replies.
- `assistant/core.py` orchestrates every subsystem.
- `gui/app.py` provides the CustomTkinter desktop UI.

## Notes

WhatsApp Web changes its DOM occasionally. The automation module uses resilient selectors where possible, but if WhatsApp changes a menu label or icon name, update `whatsapp/automation.py`.

For privacy, all app data is local by default. Speech fallback through `recognize_google` may use Google recognition if Whisper fails.
