
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
