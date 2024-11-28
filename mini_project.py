import webbrowser
import sys
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def engine_talk(message):
    """Convert text to speech."""
    print(f"TTS: {message}")
    engine.say(message)
    engine.runAndWait()

def listen_command():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            engine_talk("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            engine_talk("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine_talk("Sorry, there seems to be an issue with the speech recognition service.")
            return ""
        except Exception as ex:
            print("An error occurred while recognizing your voice.")
            engine_talk("An error occurred while recognizing your voice.")
            return ""

def run_alexa():
    """Main functionality of the assistant."""
    print("Clearing background noise... Please wait")
    engine_talk("Clearing background noise... Please wait")
    print("\n")
    print("Hello, I am Mini Alexa. How can I help you?")
    engine_talk("Hello, I am Mini Alexa. How can I help you?")
    
    while True:
        try:
            # Listen for the command
            command = listen_command()
            if not command:  # If no command is captured
                continue

            # Process the command
            if 'open gmail' in command:
                print("Opening Gmail...")
                engine_talk("Opening Gmail...")
                webbrowser.open_new('https://mail.google.com/')
            elif 'open youtube' in command:
                print("Opening YouTube...")
                engine_talk("Opening YouTube...")
                webbrowser.open_new('https://www.youtube.com/')
            elif 'open instagram' in command:
                print("Opening Instagram...")
                engine_talk("Opening Instagram...")
                webbrowser.open_new('https://www.instagram.com/')
            elif 'open stack overflow' in command:
                print("Opening Stack Overflow...")
                engine_talk("Opening Stack Overflow...")
                webbrowser.open_new('https://stackoverflow.com/')
            elif "who made you" in command or "who created you" in command:
                print("I have been created by Sanket.")
                engine_talk("I have been created by Sanket.")
            elif 'open github' in command:
                print("Opening GitHub...")
                engine_talk("Opening GitHub...")
                webbrowser.open_new('https://github.com/')
            elif 'bye' in command or 'stop' in command or 'tata' in command:
                print("Goodbye, have a nice day!")
                engine_talk("Goodbye, have a nice day!")
                sys.exit()
            elif 'thank you' in command:
                print("You're welcome.")
                engine_talk("You're welcome.")
            else:
                print("Here is what I found on the internet...")
                engine_talk("Here is what I found on the internet...")
                search = 'https://www.google.com/search?q=' + command
                webbrowser.open(search)
        except Exception as ex:
            print("An error occurred.")
            engine_talk("An error occurred.")

# Run the assistant
if __name__ == "__main__":
    run_alexa()
