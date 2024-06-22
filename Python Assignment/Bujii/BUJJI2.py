import pyttsx3
from datetime import datetime as dt
import speech_recognition as sr
import wikipedia
import pywhatkit as pk
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

vr_name = 'bujji'

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if vr_name in command:
                command = command.replace(vr_name + ' ', '')
    except:
        print('Nee Microphone chusukooo...')
    return command

def notepade():
    os.system('notepad')

def vscode():
    os.system('start code')

def chrome():
    os.system('start chrome')

def google_search(command):
    search = command.replace('google', '').replace('search', '').replace(vr_name, '')
    pk.search(search)

def youtube_play(command):
    message = command.replace('play', '').replace('on youtube', '')
    pk.playonyt(message)
def about():
    speak("I am bujji version 1.0 . I can help you various tasks like playing vidoes , and Acts as Google search engine")

def handle_command(command):
    if 'stop' in command or 'get lost'in command or 'quit' in command:
        speak("See you again Mahesh")
        return False
    elif 'time' in command:
        time = dt.now().strftime("%I:%M %p")
        speak(time)
    elif 'who is' in command:
        search = command.replace('who is', '').replace('get', '')
        results = pk.info(search, lines=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'google' in command or 'what' in command or 'search' in command:
        google_search(command)
        speak('Here are the results of your search.')
    elif 'notepad' in command:
        notepade()
        speak("Notepad is opened")
    elif 'code' in command or 'open vs code' in command:
        vscode()
        speak("Visual Studio Code is opened")
    elif 'chrome' in command:
        chrome()
        speak("Chrome is opened")
    elif 'play' in command or 'youtube' in command:
        youtube_play(command)
        speak('Playing the video on YouTube')
    elif 'yourself' in command or 'about' in command:
        about()
    return True

# Tkinter GUI
def start_listening():
    while True:
        command = take_command()
        if not handle_command(command):
            break

def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("400x400")
    root.configure(bg="Black")

    label = tk.Label(root, text="BUJJI", font=("italic", 24) ,bg='#ffa500')
    label.pack(pady=20)

    mic_image = Image.open(r"C:\temp\PythonPractice\Python Assignment\Bujii\mic.png")
    mic_image = mic_image.resize((100, 100), Image.BICUBIC)
    mic_photo = ImageTk.PhotoImage(mic_image)

    mic_button = tk.Label(root, image=mic_photo, bg="orange")
    mic_button.pack(pady=10)
    mic_button.bind("<Button-1>", lambda e: start_listening())

    root.mainloop()

if __name__ == "__main__":
    text = 'Hi Mahesh, I am your buji, how can I help you'
    speak(text)
    create_gui()
