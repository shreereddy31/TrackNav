import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  
    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")

    except Exception as e:
        # print(e)    
        print("I didn't get you. Say that again please...!") 
        speak("I didn't get you. Say that again please...!")  
        return "NONE"
    return query

#def askMe():

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('18rj1a05e7@gmail.com', 'oduwozscybrrolov')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #driver = webdriver.Chrome() 
    #driver.implicitly_wait(1) 
    #driver.maximize_window() 
    
    print("What's your name, Human?")
    speak("What's your name, Human?") 
    name ='Human'
    name = takeCommand() 
    print("Hello, " + name + '. What can I do for you ?') 
    speak("Hello, " + name + '. What can I do for you ?') 
   
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...\n\t")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening youtube...")
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            print("Opening Facebook...")
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")

        elif 'open amazon' in query:
            print("Opening Amazon...")
            speak("Opening Amazon...")
            webbrowser.open("amazon.in")

        elif 'open flipkart' in query:
            print("Opening Flipkart")
            speak("Opening Flipkart")
            webbrowser.open("flipkart.com")

        elif 'open udemy' in query: 
            print("Opening Udemy...")
            speak("Opening Udemy...")
            webbrowser.open("udemy.com")   

        elif 'open instagram' in query:
            print("Opening Instagram...") 
            speak("Opening Instagram...") 
            webbrowser.open("instagram.com")   


        elif 'play music' in query:
            music_dir = 'F:\\mera paatalu'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'who created you' in query:
            speak("I was created by Hrishi")

        elif "who are you" in query or "define yourself" in query: 
            print("I am April, technically born on 18th April,2020. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra")
            speak("I am April, technically born on 18th April,2020. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etc...") 

        elif 'open code' in query:
            codePath = "C:\\Users\\hrish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif "exit" in query or "bye" in query or "sleep" in query or "quit" or "good night"in query: 

            #print("It was nice meeting you "+ name + ". Hope to see you soon.  :) :)") 
            #speak("It was nice meeting you "+ name + ". Hope to see you soon.") 

            print("It was nice meeting you "+ name +". Hope to see you soon.  :) :)") 
            speak("It was nice meeting you "+ name +". Hope to see you soon.") 
            break
