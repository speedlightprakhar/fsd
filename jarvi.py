import pyttsx3
import UUspeech_recognition as sr
import datetime
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("I am Jarvis. How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Could not understand. Please say that again.")
        return "None"
    return query.lower()

def run_jarvis():
    greet_user()
    while True:
        query = take_command()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Public\\Music"  # Change this path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")

        elif 'exit' in query or 'quit' in query:
            speak("Shutting down. Goodbye, sir.")
            break

        else:
            speak("I'm sorry, I didn't catch that. Could you repeat?")

if __name__ == "__main__":
    run_jarvis()