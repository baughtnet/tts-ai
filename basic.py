# import libraries
import speech_recognition as sr

r = sr.Recognizer

while True:
    try:
        with sr.Microphone() as source:
            print("Say something!!!")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"Recognized text: {text}")

    except:
        print("You were trying to be funny")
        r = sr.Recognizer()
        continue
