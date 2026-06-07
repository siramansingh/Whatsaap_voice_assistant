"""Application entrypoint."""

from __future__ import annotations

import argparse

from gui.app import JarvisGUI
from utils.config import ensure_runtime_dirs
from utils.logger import configure_logging, get_logger

logger = get_logger(__name__)


def run_gui() -> None:
    ensure_runtime_dirs()
    app = JarvisGUI()
    app.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Jarvis AI WhatsApp Voice Assistant")
    parser.add_argument("--no-gui", action="store_true", help="Run a small command-line shell instead of the GUI.")
    args = parser.parse_args()

    configure_logging()

    if args.no_gui:
        from assistant.core import JarvisAssistant

        assistant = JarvisAssistant(on_log=print, on_status=lambda status: print(f"Status: {status}"))
        print("Jarvis CLI ready. Type commands or 'exit'.")
        try:
            while True:
                command = input("> ").strip()
                if command.lower() in {"exit", "quit"}:
                    break
                assistant.handle_text_command(command)
        finally:
            assistant.shutdown()
        return

    logger.info("Starting Jarvis GUI")
    run_gui()


if __name__ == "__main__":
    main()
