import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import os

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",175)

NOTES_FILE="jarvis_notes.txt"

def speak(text):
    '''Convert text to speech and also print it.'''
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 21:
        greeting = "Good afternon"
    speak(f"{greeting}! I am Jarvis , your personal assisstant AI .How can I help You Today?")

def take_command():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio=recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio,language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("sorry, I didn,t catch that. could you repeat?")
        return "none"
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return "none"

def handle_command(query):

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "open google" in query:
        speak("Opening google")
        webbrowser.open("https://google.com")

    elif "open youtube" in query:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")

    elif "search" in query or "wikipedia" in query:
        speak("Searching wikipedia...")
        topic = query.replace("search","").replace("wikipedia","").replace("for","").strip()
        try:
            result = wikipedia.summary(topic,sentences=2)
            speak("According to wikipedia,")
            speak(result)
        except Exception:
            speak("Sorry, I couldn,t find anything on that topic.")

    elif "joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "note" in query or "remember" in query:
        speak("What should I note down?")
        note_content = take_command()
        if note_content != "none":
            with open(NOTES_FILE, "a") as f:
                f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} - {note_content}\n")
            speak("I ve saved that note for you.")

    elif "read notes" in query or "my notes" in query:
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                notes = f.read()
            speak("Here are your notes.")
            print(notes)
        else:
            speak("you don't have any notes saved yet.")

    elif "who are you" in query or "your name" in query:
        speak("I am jarvis , A mini AI assistant.")

    elif "exit" in query or "stop" in query or "quit" in query:
        speak("Goodbye! Have a great day Himanshu")
        return False

    else:
        speak("I am not sure how to help with that yet. you can ask me the time,"
              "date, to open google or youtube , search wikipedia, tell a joke," \
              "or take a note.")
    return True

def main():
    wish_user()
    running = True
    while running:
        query = take_command()
        if query != "none":
            running = handle_command(query)

if __name__=="__main__":
    main()
