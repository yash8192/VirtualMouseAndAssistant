import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import time
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyautogui
import psutil  # for checking battery
import pywhatkit
import pyjokes
import pyscreenshot
import screen_brightness_control as pct
import cv2
from bs4 import BeautifulSoup
import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[2].id)
t = ""
hour = int(datetime.datetime.now().hour)
minutes=int(datetime.datetime.now().minute)
zz=str(hour)+str(minutes)
#zz=int(zz)
def speak(audio):
    print(f":{audio}")


    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        # speak("??? ???")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
       # speak(pyjokes.get_joke())
        # speak("??? ???")

    else:
        speak("Good Evening!")
        # speak("??? ???")

    speak("I am Light Buddy")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .75
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def exercise_lunch():
    ''''
    pyautogui.press("esc")
    speak("verification successful")
    speak("welcome yash sir")
    '''''
    if hour >= 6 and hour < 8:
        speak("have yo done your yoga say yes if you done your yoga or say no if you not done your exercise")
        query1 = takeCommand().lower()
        print(query1)
        if "yes" in query1:
            speak("Please tell me how may I help you")
            inputuser()
        elif "none" in query1:
            exercise_lunch()
        elif "no" in query1:
            speak("first do yoga its take only ten minutes then do work")
            exercise = "10 minute Morning Yoga for Beginners"
            pywhatkit.playonyt(exercise)
            time.sleep(60)
            # time.sleep(600)
            exercise_lunch()
        else:
            speak("please first answer my question in yes or no")
            exercise_lunch()
    #########################################################################################################################
    if hour >= 12 and hour < 14:
        speak("have you done your lunch say yes if you done your lunch or say no if you not done your lunch")
        query1 = takeCommand().lower()
        if "yes" in query1:
            speak("Please tell me how may I help you")
            inputuser()
        elif "none" in query1:
            exercise_lunch()
        elif "no" in query1:
            speak(
                "first do your lunch it is important to do lunch on time i will come after 20 min to check you that you had finish your lunch or not")
            # time.sleep(1200)
            time.sleep(60)
            exercise_lunch()
        else:
            speak("please first answer my question in yes or no")
            exercise_lunch()


    ##########################################################################################################################

    if hour >= 19 and hour < 20 and minutes < 16:
        speak("have yo done your exercise say yes if you done your exercise or say no if you not done your exercise")
        query1 = takeCommand().lower()
        if "yes" in query1:
            speak("Please tell me how may I help you")
            inputuser()
        elif "none" in query1:
            exercise_lunch()
        elif "no" in query1:
            speak("first do exercise its take only twenty minutes then do work")
            exercise = "20 MIN KILLER HIIT Full Body Workout (No Equipment, No Repeat, Cardio At Home)"
            pywhatkit.playonyt(exercise)
            # time.sleep(1200)
            time.sleep(1)
            exercise_lunch()
        else:
            speak("please first answer my question in yes or no")
            exercise_lunch()

    ########################################################################################################################
    else:
        speak("Please tell me how may I help you")
        inputuser()


def inputuser():
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "brightness" in query or " brightness" in query or " brightness " in query:
            brightness(query)
        elif 'search ' in query:
            seasrch = query.replace('search', '')

            pywhatkit.search(seasrch)
        elif "screenshot" in query or " screenshot " in query or " screenshot " in query:

            print("yash")
            image = pyscreenshot.grab()
            image.show()
            t = str(time.time())
            # time.sleep(1)
            # To save the screenshot
            image.save(t + ".png")
        elif 'open' in query:
            open(query)

        elif "time" in query or " time" in query:
            tim = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + tim)
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'temperature ' in query or ' temperature' in query or ' temperature ' in query:
            url=f"https://www.google.com/search?q={query}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"the outside temprature is {temp} celcius")
            # search = query.replace('search', '')
            #pywhatkit.search(query)

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        elif 'google' in query or ' google' in query or 'page' in query or 'volume' in query:
            google(query)
        elif 'youtube' in query or 'you tube' in query or ' youtube' in query.lower() or 'music' in query or 'screen' in query or 'song':
            youtube(query)
            ''''

        '''''
        elif "go to tab" in query or "go to tab " in query:
            # x = w2n.word_to_num(query)
            if (any(map(str.isdigit, query))):
                emp_str = ""
                for m in query:
                    if m.isdigit():
                        emp_str = emp_str + m
                with pyautogui.hold('ctrl'):

                    pyautogui.press(emp_str)
                print("yes")
            else:
                x = query.replace("to", "2", 1)
                emp_str = ""
                for m in x:
                    if m.isdigit():
                        emp_str = emp_str + m
                with pyautogui.hold('ctrl'):

                    pyautogui.press(emp_str)
                print(x)

                print(emp_str)
        elif "new tab" in query or "new tab " in query:
            with pyautogui.hold('ctrl'):
                pyautogui.press("t")

        elif "brightness" in query or " brightness" in query:
            brightness(query)

        ''''
        elif "switch tab" in query or "switch tab" in query:

            with pyautogui.hold('ctrl'):

                pyautogui.press(emp_str)
        '''''


def youtube(query):
    if 'song' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif "full screen " in query or "ull screen" in query or "full screen" in query or "ull screen " in query:
        pyautogui.press("f")
    elif "small screen " in query or "mall screen" in query or "all screen" in query or "small screen " in query:
        pyautogui.press("f")
    elif "back music " in query:
        pyautogui.press('j')
    elif "forward music " in query:
        pyautogui.press('l')
    elif "fast music" in query or "ast music" in query:
        with pyautogui.hold('shift'):
            pyautogui.press(".")
    elif "slow music" in query or "low music" in query or "slow music " in query or "low muisc " in query:
        with pyautogui.hold('shift'):
            pyautogui.press(",")
    elif "stop music" in query or "pause music " in query or "ause music" in query or " ase music" in query or "top music" in query or "hot music " in query:
        pyautogui.press('space')
    elif "play music " in query or "lay music" in query or "chalu music" in query or "start music" in query or "tart music" in query:
        pyautogui.press('space')


def brightness(query):
    if "increase brightness" in query or "increase brightness " in query:
        x = pct.get_brightness()
        y = x[0] 

        if (y >= 100):
            y=100
        else:
            y = y + 10
            pct.set_brightness(y)
            print(y)


    elif "decrease brightness" in query or " decrease brightness " in query:
        x = pct.get_brightness()
        y = x[0]
        if (y <= 0):
            y=0
        else:
            y = y - 10
            pct.set_brightness(y)
            print(y)


def open(query):
    if 'open google' in query:
        webbrowser.open_new_tab("http://www.google.com")
    elif 'open youtube' in query or 'open you tube' in query:
        webbrowser.open_new_tab("http://www.youtube.com")
    elif 'open stackoverflow' in query or 'open stack overflow' in query or 'open stack over flow' in query:
        webbrowser.open_new_tab("https://stackoverflow.com/")
    elif 'open gmail' in query:
        webbrowser.open_new_tab("http://www.gmail.com")
    elif 'open facebook' in query:
        webbrowser.open_new_tab("http://www.facebook.com")
    elif 'open instagram' in query or 'open instagram' in query:
        webbrowser.open_new_tab("http://www.instagram.com")


def google(query):
    print("google")
    if 'search' in query or ' search ' in query or ' search' in query:
        search = query.replace('search', '')
        pywhatkit.search(query)
    elif "down page " in query or "page down" in query:
        pyautogui.scroll(-400)
    elif "upar page " in query or "page upar" in query or "up page" in query or "page up" in query:

        pyautogui.scroll(400)
    elif "volume up " in query or "up volume" in query:
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("volumeup")
    elif "volume down " in query or "down volume" in query:
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("volumedown")


if __name__ == "__main__":
    ''''
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')  # load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 2  # number of persons you want to Recognize

    names = ['', 'yash']  # names, leave first empty bcz counter starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
    cam.set(3, 640)  # set video FrameWidht
    cam.set(4, 480)  # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # flag = True

    while True:

        ret, img = cam.read()  # read the frames using the above created object

        converted_image = cv2.cvtColor(img,
                                       cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                exercise_lunch()


            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()
    '''''

    wishMe()
    #print(zz)
    exercise_lunch()