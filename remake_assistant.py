import pyttsx3
import datetime
import os
import time
import pyaudio
import wikipedia
import speech_recognition as sr
import webbrowser as wb

friday=pyttsx3.init()                            #create object Friday
voice=friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print(f'F.R.I.D.A.Y. : {audio}')
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M %p")
    speak(Time)

def help_me():
    speak("""FRIDAY can help you to execute the command:
        1. Welcome
        2. Time
        3. Find on Google
        4. Find on youtube
        5. Open word
        6. Open excel
        7. Open Video
        8. Quit.""")

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("Good Morning sir")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >=18 and hour < 24:
        speak("Good Evening sir")
    speak("How can I help you?")
    help_me()

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Linh: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the commnad ")
        query=str(input("Your order is: "))
    return query
    

def main():
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search Boss?")
            search=command().lower()
            url=f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google.')
        
        elif "youtube" in query:
            speak("What should I search Boss?")
            search=command().lower()
            url=f"http://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Youtube.')
            
        elif "excel" in query:
            speak("Open Microsoft Excel")
            os.startfile('C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
        
        elif "word" in query:
            speak("Open Microsoft Word")
            os.startfile('C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE')
            
        elif "open video" in query:
            speak("Open Video")
            os.startfile(r"E:\history.mp4")
        
        elif ("time" or "What time is it") in query:
            time()
        
        elif "quit" in query:
            speak("FRIDAY is quitting Sir, goodbye Boss.")
            quit()
            
        else:
            speak("The result is not available")
        
main()