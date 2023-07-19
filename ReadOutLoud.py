import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # You can adjust the speaking speed (default is 200)
    engine.say(text)
    engine.runAndWait()

def main():
    print("Type something, and I'll read it aloud!")
    while True:
        user_input = input("> ")
        if user_input.lower() in ('exit', 'quit', 'q'):
            break
        speak_text(user_input)

if __name__ == "__main__":
    main()
