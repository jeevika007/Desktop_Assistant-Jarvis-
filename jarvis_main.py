import pyttsx3
import speech_recognition
import requests
import bs4
import datetime
import pyjokes
import os
import pyautogui
import smtplib



for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("WELCOME MA'AM ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif i == 2 and a != pw:
        exit()

    elif a != pw:
        print("Try Again")


from INTRO import play_gif
play_gif()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    rm = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        rm.pause_threshold = 1
        rm.energy_threshold = 300
        audio = rm.listen(source, 0, 4)

        try:
            print("Understanding...")
            query = rm.recognize_google(audio)
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshitamaurya007@gmail.com')
    server.sendmail("harshitamaurya007@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok ma'am, You can call me anytime")
                    break

                # 2.0
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                #####

                elif "hello" in query:
                    speak("Hello ma'am, how are you?")
                elif "i am fine" in query:
                    speak("that's great ma'am")
                elif "how are you" in query:
                    speak("Perfect ma'am")
                elif "thank you" in query:
                    speak("you are welcome ma'am")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,ma'am")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, ma'am")
                    volumedown()

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me" + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me" + remember.read())

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "temperature" in query:
                    search = "temperature in kanpur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = bs4.BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in kanpur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = bs4.BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Ma'am, the time is {strTime}")
                elif "joke" in query:
                    joke_1 = pyjokes.get_joke('hi', 'neutral')
                    speak(joke_1)

                elif "open" in query:  # EASY METHOD
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,Ma'am")

                elif "email to" in query:
                    query = query.replace("jarvis", "")
                    try:
                        speak("What should I send?")
                        content = str(input("Enter the mail: "))
                        to = str(input("Enter the Email: "))
                        sendEmail(to, content)
                        speak("Email has been sent!")

                    except Exception as e:
                        print(e)
                        speak("Sorry, could not send the email.")

                elif "finally sleep" in query:
                    speak("Going to sleep, Ma'am")
                    exit()