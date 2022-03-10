import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os
from PIL import Image
import subprocess
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import pywhatkit
import pyjokes
import datetime
import wikipedia

class person:
    name = ''

    def setName(self, name):
        self.name = name


class assistance:
    name = ''

    def setName(self, name):
        self.name = name

def there_exists(terms):

    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()


# Listen for the audio and convert to text


def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)

        audio = r.listen(source, 5, 5)  # listening to audio source
        print("looking at the database")
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:

            engine_speak('Sorry boss, i did not get what you said. Can you please repeat?')

        except sr.RequestError:
            engine_speak("Sorry boss, my server is down")  # Recognizer is not connected

        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()


#  Get the string and make audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to voice
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # to play the sound
    print(asistance_obj.name + ":", audio_string)  # print what you say on terminal
    os.remove(audio_file)  # remove the audio

def respond(voice_data):
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass


    if there_exists(['hey', 'hi', 'hello', 'Good morning ', 'holla ', 'wassup']):
        greetings = ["Hi Boss!, What are we going to do today?" + person_obj.name,
                     "Hi Boss!, How can i help you?" + person_obj.name,
                     "Hi Boss!, Whats up?" + person_obj.name,
                     "Hi Boss!, What do you need from me?" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)

    # she search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("For") [-1]
        url = "http://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for " + search_term  + "on google")

        # she search youtube
    if there_exists(["search on youtube about"]):
        search_term = voice_data.split("for")[-1]
        url = "http://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for " + search_term + "on youtube")

    if there_exists(["play on youtube"]):
        search_term = voice_data.split("for")[-1]
        pywhatkit.playonyt(search_term)
        engine_speak("Here is what i found for " + search_term + "on youtube")


person_obj = person()
asistance_obj = assistance()
asistance_obj.name = ' Monkey '
engine = pyttsx3.init()

while ( 1 ):
    voice_data = record_audio("Recording")  # getting the voice input
    print("Done!")
    print("Q:", voice_data)
    respond(voice_data)  # responsed


