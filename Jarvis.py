''' Jarvis Assistant by Akshay Jain '''

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sphinx
import pocketsphinx
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir, Please tell me how may I help you?")

def takeCommand():
    # It takes microphone input from user and returns a string input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said : {query}\n")
    
    except Exception as e:
        try:
            query = r.recognize_sphinx(audio)
            print(f"User Said : {query}\n")
        except:
            print(e)
            print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akshayjain222002@gmail.com', 'password')
    server.sendmail('akshayjain222002@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            try :
                results = wikipedia.summary(query, sentences=1)
                print(results)
                speak(results)
            except :
                speak("Please check your Internet Connection")
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            # print(songs)
            music_file_index = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[music_file_index])) # Play any random song from list
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir, the time is {strTime}")

        elif "code" in query:
            vsCodePath = r"C:\Users\aksha\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(vsCodePath)

        elif "email" in query:
            try:
                speak("What Should I Say?")
                content = takeCommand()
                to = "akshayjain222002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except:
                speak("Sorry, Email is not sent at this moment")
        
        elif "quit" in query: # Quit Jarvis assistant
            speak("Okay sir, I'm going to sleep")
            exit()
