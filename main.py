import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import pyaudio

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
        speek('Good Morning'+ MASTER)

    elif hour >= 12 and hour < 18:
        speek('Good Afternoon'+ MASTER)
    
    else:
        speek('Good Evening' + MASTER)

    speek('I am Jarvis. How may i help you? ')

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
    while True:
        query = takeCommand()

        if query.lower() == 'stop' or query.lower() == 'close' or  query.lower() == 'exit' or query.lower()== '':
            break

        else:

            if 'wikipedia' in query.lower():
                speek('Searching wikipedia....')
                query.replace('wikipedia','')
                result = wikipedia.summary(query, sentences= 2)
                print(result)
                speek(result)

            elif 'open facebook' in query.lower():
                url = 'facebook.com'
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            
            elif 'open twitter' in query.lower():
                url = 'twitter.com'
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
            
            elif 'open zomato' in query.lower():
                url = 'zomato.com'
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)

            elif 'open swiggy' in query.lower():
                url = 'swiggy.com'
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)

            elif 'play music' in query.lower():
                if not any(True for x in os.listdir(r'D:\\Movie\\Movie') if x.split(".")[-1] in ['mp3','mp4','ogg','wav']):
                    speek('Sorry, Music not available')
                else:
                    songs_dir = "D:\\Movie\\Movie"
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir, songs[0]))

            elif 'time' in query.lower():
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speek(f'The time is {strTime}')

            elif 'open code' in query.lower():
                speek('Opening VS Code...')
                codePath = "C:\\Users\\shini\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                
            elif 'open youtube' in query.lower():
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

            elif 'what' or 'who' or 'where' or 'why' or 'how' or 'what' or 'which' or 'how long' or 'how much' or 'how many' in query.lower():
                speek('Please repeate your question')
                que = takeCommand()
                url = f'https://www.google.com/search?q={que}'
                print(que)
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)          

            # elif 'play news' or 'open news' or 'play Aaj Tak news' in query.lower():
            #     url = 'https://www.youtube.com/watch?v=cJPNkWgEQ_4'
            #     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #     webbrowser.get(chrome_path).open(url)

            # elif 'open youtube' in query.lower():
            #     url = 'youtube.com'
            #     chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #     webbrowser.get(chrome_path).open(url)
main()