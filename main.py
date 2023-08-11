import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import keyboard
import datetime
import requests
from bs4 import BeautifulSoup
import json
import webbrowser
import pyautogui
import time
import operator
import sys
import pywhatkit as kit 
import cv2
import wikipedia
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(response):
    print("Assistant:", response)
    engine.say(response)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Sara Your Personal AI Assistant. Please tell me how may I Assist You?")

def takeCommand():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)   
        #speak("Say that again please...")   
        print("Say that again please...")  
        return "None"
    return query.lower()

def TakeHindi():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='hi')
            print(f"User said: {query}\n")

        except Exception as e:
        # print(e)    
            #speak("Say that again please...")  
            print("Say that again please...")  
            return "None"
        return query.lower()

def run_sara():

    def OpenApps():
        speak("Ok Boss , Wait a Second!")

        if 'chrome' in query:
            speak("Opening chrome!")
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'vm' in query:
            speak("Opening vm!")
            codePath = "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"
            os.startfile(codePath)

        elif 'pycharm' in query:
            speak("Opening PyCharm!")
            codePath = "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.3\bin\pycharm64.exe"
            os.startfile(codePath)

        elif 'python codes file' in query:
            speak("Opening PyCharm!")
            codePath = "C:\\Users\\skato\\OneDrive\\Desktop"
            os.startfile(codePath)

        elif 'code' in query:
            speak("Opening python codes files!")
            codePath = "C:\\Users\\skato\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'youtube' in query:
            speak("Opening youtube!")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening google!")
            webbrowser.open("google.com")

        elif 'mail' in query:
            speak("Opening mail!")
            webbrowser.open("mail.com")

        elif 'stackoverflow' in query:
            speak("Opening stacjoverflow!")
            webbrowser.open("stackoverflow.com")

        elif 'amazon' in query:
            speak("Opening amazon!")
            webbrowser.open("amazon.com")

        elif 'flipcart' in query:
            speak("Opening flipcart!")
            webbrowser.open("flipcart.com")

        elif 'naukri' in query:
            speak("Opening naukri!")
            webbrowser.open("naukri.com")

        elif 'google map' in query:
            speak("Opening google map!")
            webbrowser.open("google map.com")

        elif 'udemy' in query:
            speak("Opening udemy!")
            webbrowser.open("udemy.com")

        elif 'chatgpt' in query:
            speak("Opening chatgpt!")
            webbrowser.open("chatgpt.com")

        elif 'github' in query:
            speak("Opening github!")
            webbrowser.open("github.com")

        elif 'whatsapp' in query:
            speak("Opening whatsapp!")
            webbrowser.open("whatsapp.com")

        elif 'spotify' in query:
            speak("Opening spotify!")
            webbrowser.open("spotify.com")

        speak("Your Command Has Been Completed Succesfully!")

    def TaskPlay():

        if 'play' in query:
            song = query.replace('play','  ')
            speak("Playing" + song)
            pywhatkit.playonyt(song)

    def search_wikipedia(query):
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.WikipediaException:
            speak("Sorry, I couldn't find any relevant information on Wikipedia.")

    def YoutubeAuto():

        if 'pause' in comm:
            pyautogui.hotkey('k')

        elif 'play' in comm:
            pyautogui.hotkey('space bar')

        elif 'restart' in comm:
            pyautogui.hotkey('0')

        elif 'mute' in comm:
            pyautogui.hotkey('m')

        elif 'skip' in comm:
            pyautogui.hotkey('1')

        elif 'full screen' in comm:
            pyautogui.hotkey('f')

        speak("Done Boss!")

    def Temp():
        search = "temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside is {temperature}")


    if __name__ == "__main__":
            wishMe()

    while True:
    # if 1:

        query = takeCommand()

        if 'hello' in query:
            speak("Hello Boss , I Am Sara .")
            speak("How May I Assist You?")

        elif 'how are you' in query:
            speak("I Am Fine Boss!")
            speak("Whats About You?")

        elif 'you need a break' in query:
            speak("Ok Boss , You Can Call Me Aany Time")
            break

        elif 'i love you' in query:
            speak("I Love You Too boss!")
            speak("But As   AI Friend!")

        elif 'marry' in query:
            speak("This is one of those things we both have to agree on!")
            speak("I would like to just be friends. But thank you for love though!")

        elif 'good girl' in query:
            speak("Thank you boss!")

        elif 'are you single' in query:
            speak("No Boss")
            speak("I am in Relationship with wifi!")

        elif 'my world' in query:
            speak("Yours Mom Dad is your World!")
        
        elif 'i am good' in query:
            speak("ok")

        elif 'my favourite colour' in query:
            speak("You favourite Colour is Black")

        elif 'my favourite hero' in query:
            speak("Prabhas Is Your Most Favourit Hero Boss")

        elif 'my favourite singer' in query:
            speak("Guru Randhava Is Your Favourite Singer")

        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'websit' in query:
            speak("Ok Boss!")
            speak("Opening website!")
            query = query.replace("Anna","")
            query = query.replace("website","")
            query = query.replace("  ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("This What I Found!")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...") 
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open chrome' in query:
            OpenApps()

        elif 'open vm' in query:
            OpenApps()

        elif 'open PyCharm' in query:
            OpenApps()

        elif 'open python codes file' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open google' in query:
            OpenApps()
 
        elif 'open mail' in query:
            OpenApps()
 
        elif 'open stackoverflow' in query:
            OpenApps()

        elif 'open amazon' in query:
            OpenApps()

        elif 'open flipcart' in query:
            OpenApps()

        elif 'open naukri' in query:
            OpenApps()

        elif 'open google map' in query:
            OpenApps()

        elif 'open udemy' in query:
            OpenApps()

        elif 'open chatgpt' in query:
            OpenApps()

        elif 'open github' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open spotify' in query:
            OpenApps()

        elif 'open play music' in query:
            OpenApps()

        elif 'play' in query:
            TaskPlay()

        elif 'paus' in query:
            pyautogui.hotkey('k')

        elif 'start' in query:
            pyautogui.hotkey('space bar')

        elif 'restart' in query:
            pyautogui.hotkey('0')

        elif 'mute' in query:
            pyautogui.hotkey('m')

        elif 'skip' in query:
            pyautogui.hotkey('1')

        elif 'full screen' in query:
            pyautogui.hotkey('f')

        elif 'youtube tools ' in query:
            YoutubeAuto()

        elif 'temperature' in query:
            Temp()

        elif 'you need a break' in query:
            speak("Ok Boss, You Can Call Me Any Time!")
            speak("Just Say Wakeup Sara")
            break

        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
            
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")

        elif 'my location' in query:
            speak("Ok Boss , Wait A Second")
            speak("I Am Tracking Your Location")
            webbrowser.open("https://www.google.com/maps/place/Pune,+Maharashtra+411032/@18.5815568,73.9195308,14z/data=!3m1!4b1!4m6!3m5!1s0x3bc2c6b34b728c8f:0x83e1c9ed4200a082!8m2!3d18.5930989!4d73.921781!16s%2Fg%2F1hhw711y_?entry=ttu")
            speak("Your Location  Has Been Tracked")

        elif 'jokes' in query:
            speak("Ok Boss!")
            speak("Getting Jokes for You!")
            get = pyjokes.get_joke()
            speak(get)
            speak("How was it!")

        elif 'repeat my words' in query:
            speak("Yours Repeatation Command Has Been Enabled!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "increase volume by 1" in query:
            speak("Increasing volume by 1")
            pyautogui.press("volumeup")

        elif "increase volume by 2" in query:
            speak("Increasing volume by 2")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 3" in query:
            speak("Increasing volume by 3")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 4" in query:
            speak("Increasing volume by 4")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup") 

        elif "increase volume by 5" in query:
            speak("Increasing volume by 5")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 6" in query:
            speak("Increasing volume by 6")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 7" in query:
            speak("Increasing volume by 7")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 8" in query:
            speak("Increasing volume by 8")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "increase volume by 9" in query:
            speak("Increasing volume by 9")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "decrease volume by 1" in query:
            speak("Decreasing volume by 1")
            pyautogui.press("volumedown")

        elif "decrease volume by 2" in query:
            speak("Decreasing volume by 2")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 3" in query:
            speak("Decreasing volume by 3")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 4" in query:
            speak("Decreasing volume by 4")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 5" in query:
            speak("Decreasing volume by 5")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 6" in query:
            speak("Decreasing volume by 6")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 7" in query:
            speak("Decreasing volume by 7")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 8" in query:
            speak("Decreasing volume by 8")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "decrease volume by 9" in query:
            speak("Decreasing volume by 9")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "drag visual studio to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)

        elif 'type' in query: #10
            query = query.replace("type", "")
            pyautogui.write(f"{query}")
            speak(f"typing {query} ")
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, Now its {strTime}")

        elif "who are you" in query:
            print('My Name Is Sara')
            speak('My Name Is Sara')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')

        elif "who created you" in query:
            print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
            speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')

        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'press enter' in query:
            query = query.replace("anna","")
            query = query.replace("press enter","")
            pyautogui.hotkey('enter')
        
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        elif 'close code' in query:
            os.system("taskkill /f /im code.exe")
        elif 'close vm' in query:
            os.system("taskkill /f /im vm.exe")
        elif 'close pycharm' in query:
            os.system("taskkill /f /im pycharm.exe")


        elif 'press enter' in query:
            query = query.replace("anna","")
            query = query.replace("press enter","")
            pyautogui.hotkey('enter')

        elif 'open command prompt' in query:
            pyautogui.hotkey('window', 'R')

        elif "channel analytics" in query:
            webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default")

        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'alarm' in query:
            speak("Tell Me The Time !")
            time = input(": Enter The time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H,%M,%S")

                if now == time:
                    speak("Time To Weak Up Boss!")
                    speak("Alarm Closed!")
                
                elif now>time:
                    break
            
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("Anna","")
            speak("You Told Me To Remind ;"+rememberMsg)
            remeber = open('date.txt','w')
            remeber.write(rememberMsg)
            remeber.close()

        elif 'what do you remember' in query:
              remeber = open('date.txt','r')
              speak("You Told me to :"+remeber.read())  

        elif 'my favourite song' in query:
            speak("Ok Boss , Starting song!")
            music_dir = 'C:\\Users\\skato\\Music\\music 1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Your song has been started!")
            speak("Enjoy Your song!")

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Anna","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This is what i found for you boss!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Seakable Data ")

        elif "search" in query:
            import wikipedia as googleScrap
            speak("Sure, what would you like to search for?")
            query = takeCommand()
            query = query.replace("Anna","")
            query = query.replace("search","")
            speak("This is what i found for you boss!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Seakable Data ")

run_sara()

    