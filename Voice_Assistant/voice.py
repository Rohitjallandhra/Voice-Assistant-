
import pyttsx3
import speech_recognition as  sr
import  webbrowser
import datetime

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not Understand")

def sppechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
 while True:

    data1 = sptext().lower()

    if "your name" in data1:
        name="my name is peater"
        sppechtx(name)
    elif "old are you" in data1:
        age ="i am 20 years old"
        sppechtx(age)
    elif 'time' in data1:
        time=datetime.datetime.now().strftime("%I%M%p")
        sppechtx(time)
    elif 'youtube' in data1:
        webbrowser.open("https://www.youtube.com/")
    elif 'instagram' in data1:
        webbrowser.open("https://www.instagram.com/")
    elif 'web page' in data1:
        webbrowser.open("https://aitooltree.com/")
    elif "exit" in data1:
        sppechtx("thank you")
        break























