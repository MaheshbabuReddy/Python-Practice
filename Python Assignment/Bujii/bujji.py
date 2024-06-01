import pyttsx3
from datetime import datetime as dt 
import speech_recognition as sr
import wikipedia
import pywhatkit as pk
import os

listener = sr.Recognizer()
speaker= pyttsx3.init('sapi5')
voices= speaker.getProperty('voices') #getting details of current voice
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate',150)

vr_name ='bujji'

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

text='Hi Mahesh, Iam your buji , how can i help you'
speak(text)
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bujji" in command:
                command = command.replace(vr_name+' ','')
                #print(command)
                #speak(command)
    except:
        print('Nee Microphone chusukooo...')
    return command
def notepade():
    open = os.system('notepad')
    return open
def vscode():
    open = os.system('start code')
    return open
def chrome():
    open = os.system('start chrome')
    return open
def google():
    search = my_command.replace('google','')
    search = my_command.replace('search','')
    search = my_command.replace('bujji','')
    result = pk.search(search)
    return result
def youtube():
    message = my_command.replace('play','')
    play= pk.playonyt(message)
    return play

while True:
    my_command = take_command()
    if 'stop' in my_command:
        print("See you again Mahesh")
        speak("See you again Mahesh")
        break
    elif 'time' in my_command:
        time = dt.now().strftime("%I:%M %p")
        print(time)
        speak(time)
    elif 'who is' in my_command or 'about' in my_command:
        search = my_command.replace('who is','')
        results = pk.info(search, line=2) 
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'google' in my_command or 'what' in my_command or 'search' in my_command:
        result = google()
        speak('here results of your search ')
    elif 'notepad' in my_command:
        result = notepade()
        speak("here your Notepad is opened")
    elif 'code' in my_command or 'open vs code' in my_command:
        result = vscode()
        speak("here your vs code  is opened")
    elif 'chrome' in my_command:
        result = my_command.replace('open','')
        result = chrome()
        speak("here your chrome is opened")
    elif 'play' in my_command or 'youtube' in my_command:
        result = youtube()
        speak('Here your youtube video is playing')