import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import os

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0],id)
engine.setProperty("rate",175)

NOTES_FILE="jarvis_notes.txt"

def speak(text):
    '''Convert text to speech and also print it.'''
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour