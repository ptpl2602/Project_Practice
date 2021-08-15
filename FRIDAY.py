import pyttsx3
import datetime
import speech_recognition as sr           #viết tắt
import webbrowser as wb                   #thư viện tra cứu trên gg
import os

friday=pyttsx3.init()                     #tạo object friday
voice=friday.getProperty('voices')        #lấy giọng của google
friday.setProperty('voice', voice[1].id)    #voice[0].id = giọng nam || voice[1].id = giọng nữ

#Tạo hàm để nói
def speak(audio):
    print('F.R.I.D.A.Y.:' + ' ' + audio)
    friday.say(audio)
    friday.runAndWait()

#Tạo hàm cho biết thời gian hiện tại
def time():
    Time=datetime.datetime.now().strftime("%I:%M %p")     # %I:giờ | %M:phút | %p:am hoặc pm
    speak(Time)

#Tạo hàm welcome
def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning sir")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    speak("How can I help you?")

#Tạo hàm ra lệnh
def command():
    c=sr.Recognizer()                     #Object giúp cho Friday nhận giọng nói
    with sr.Microphone() as source:       #Nhận giọng nói từ Micro
        c.pause_threshold=1               #Dừng 1s trước khi nghe lệnh mới
        audio=c.listen(source)
        
    '''Hàm try: ... except: được sử dụng trong việc xử lý lỗi và ngoại lệ trong Python
    Có 2 kiểu lỗi:
        - Syntax Error
        - Exception
    - Duyệt lần lượt nếu kh có lỗi ngoại lệ nào thì try: sẽ chạy, còn kh thì except sẽ hoạt động'''
    
    try:
        query=c.recognize_google(audio,language='en')          #viết lệnh nhận giọng TA từ google
        print("PhuongLinh: " + query)
    except sr.UnknownValueError:
        print("Please repeat or type the command ")
        query=str(input('Your order is: '))
    return query


def main():
    welcome()
    while True:
        query=command().lower()             #lấy mệnh lệnh chuyển thành kh viết hoa để dễ nhận diện
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"         #dẫn đường link gg để tra cứu
            wb.get().open(url)                                      #open đường link đã tìm thấy
            speak(f'Here is your {search} on google')
            
        if "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"http://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "open video" in query:
            habbit=r"D:\test\habbits.mp4"
            os.startfile(habbit)                #open file habbit
            
        elif "time" in query:
            time()
            
        elif "quit" in query:
            speak("Goodbye Boss")
            quit()
            
main()