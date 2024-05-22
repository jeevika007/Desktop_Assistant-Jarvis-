import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  # Takes the input from source through microphone function
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)  # Use to cancel the noise coming from Source
        audio = recognizer.listen(source)  # listen function listens from source
    try:
        print("Recognizing...")
        data = recognizer.recognize_google(audio)
        print(data)
        return data
    except sr.UnknownValueError:
        print("Not Understanding")


def speechtxt(x):  # pyttsx3
    engine = pyttsx3.init()  # default voice
    voices = engine.getProperty('voices')  # voice properties
    engine.setProperty('voice',voices[0].id)  # male voice, use voice as we need only one type of voice
    # 0 for male voice and 1 for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)  # setting the rate of the assistant
    # speak
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':   # Splits the Program into parts
    # if sptext().lower() == "hey jarvis" :
    # we do this that when this is spoken to assistant then it works further otherwise no
    data1 = sptext().lower()
    if "your name" in data1:
        name = "my name is jarvis"
        speechtxt(name)
    elif "old are you" in data1:
        age = "i am two days old"
        speechtxt(age)
    elif "time" in data1:
        time = datetime.datetime.now().strftime("%H:%M")
        speechtxt(time)
    elif "youtube" in data1:
        webbrowser.open("https://www.youtube.com/")
    elif "google" in data1:
        webbrowser.open("https://www.google.com/")
    elif "joke" in data1:
        joke_1 = pyjokes.get_joke('hi','neutral')
        speechtxt(joke_1)
    # else:
    #     print("thanks")
