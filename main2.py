import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import pyaudio
import subprocess
from tkinter import *


name_file = open("Assistant_name.txt", "r")
name_assistant = name_file.read()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)
MASTER = 'Shivam'


def speek(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speek('Good Morning' + MASTER)

    elif hour >= 12 and hour < 18:
        speek('Good Afternoon' + MASTER)

    else:
        speek('Good Evening' + MASTER)

    speek('I am Jarvis. How may i help you? ')


def makeNote(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        print('Say that again please')
        query = None

    return query


def main():
    wishme()
    if __name__ == '__main__':
        while True:
            query = takeCommand()

            if query.lower() == 'stop' or query.lower() == 'close' or query.lower() == 'exit':
                screen.destroy()
                break

            else:

                if 'wikipedia' in query.lower():
                    speek('Searching wikipedia....')
                    query.replace('wikipedia', '')
                    result = wikipedia.summary(query, sentences=2)
                    # print(result)
                    speek(result)
                    wikipedia_screen(result)
                    # time.sleep(4)

                if 'open facebook' in query.lower():
                    url = 'facebook.com'
                    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(7)

                if 'netflix' in query.lower():
                    url = 'netflix.com'
                    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open_new_tab(url)
                    time.sleep(7)

                if 'open twitter' in query.lower():
                    url = 'twitter.com'
                    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(7)

                if 'open zomato' in query.lower():
                    url = 'zomato.com'
                    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(7)

                if 'open swiggy' in query.lower():
                    url = 'swiggy.com'
                    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(7)

                if 'play music' in query.lower():
                    if not any(True for x in os.listdir(r'D:\\music') if x.split(".")[-1] in ['mp3', 'mp4', 'ogg', 'wav']):
                        speek('Sorry, Music not available')
                        takeCommand()
                    else:
                        songs_dir = "D:\\music"
                        songs = os.listdir(songs_dir)
                        os.startfile(os.path.join(songs_dir, songs[0]))

                if 'time' in query.lower():
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speek(f'The time is {strTime}')

                if 'open code' in query.lower():
                    speek('Opening VS Code...')
                    codePath = "C:\\Users\\sunny saini\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                    time.sleep(7)

                if 'make a note' in query.lower():
                    query = query.replace('make a note', '')
                    makeNote(query)
                    time.sleep(7)

                if 'open youtube' in query.lower():
                    speek('say that you want to watch otherwise say no')
                    choice = takeCommand()
                    if 'no' in choice.lower():
                        url = 'youtube.com'
                        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                        webbrowser.get(chrome_path).open(url)
                    else:
                        url = f'youtube.com/results?search_query={choice}'
                        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                        webbrowser.get(chrome_path).open(url)
                """
                    if 'what' or 'who' or 'where' or 'why' or 'how' or 'what' or 'which' or 'how long' or 'how much' or 'how many' in query.lower():
                        speek('Please repeate your question')
                        que = takeCommand()
                        url = f'https://www.google.com/search?q={que}'
                        print(que)
                        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                        webbrowser.get(chrome_path).open(url)
                        time.sleep(7) """

                if 'news' in query.lower():
                    news = webbrowser.open_new_tab(
                        "https://timesofindia.indiatimes.com/city/mangalore")
                    speek(
                        'Here are some headlines from the Times of India, Happy reading')
                    time.sleep(7)

                if 'who are you' in query.lower() or 'what can you do' in query.lower():
                    speek('I am Jarvis your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra')
        main()


def change_name():

    name_info = name.get()

    file = open("Assistant_name", "w")

    file.write(name_info)

    file.close()

    settings_screen.destroy()

    screen.destroy()


def change_name_window():

    global settings_screen
    global name

    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("300x300")
    settings_screen.iconbitmap('app_icon.ico')

    name = StringVar()

    current_label = Label(
        settings_screen, text="Current name: " + name_assistant)
    current_label.pack()

    enter_label = Label(
        settings_screen, text="Please enter your Virtual Assistant's name below")
    enter_label.pack(pady=10)

    Name_label = Label(settings_screen, text="Name")
    Name_label.pack(pady=10)

    name_entry = Entry(settings_screen, textvariable=name)
    name_entry.pack()

    change_name_button = Button(
        settings_screen, text="Ok", width=10, height=1, command=change_name)
    change_name_button.pack(pady=10)


def info():

    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')

    creator_label = Label(info_screen, text="Created by ")
    creator_label.pack()

    Age_label = Label(info_screen, text=" at the requirement of client")
    Age_label.pack()

    for_label = Label(info_screen, text="For-- ")
    for_label.pack()


def wikipedia_screen(text):

    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    wikipedia_screen.iconbitmap('app_icon.ico')

    message = Message(wikipedia_screen, text=text)
    message.pack()


def main_screen():

    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text=name_assistant, width=300,
                       bg="black", fg="white", font=("Calibri", 13))
    """name_label.pack()
    img1 = Image.open('start.png')
    img2 = img1.resize((10,12))"""

    microphone_photo = PhotoImage(file='assistant_logo.png')
    microphone_button = Button(image=microphone_photo, command=main)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file="settings.png")
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.pack(pady=10)

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    screen.mainloop()


main_screen()
