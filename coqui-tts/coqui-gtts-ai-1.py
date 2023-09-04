# import libraries
import os
import torch
import speech_recognition as sr
import openai
from time import sleep
from playsound import playsound as pl
from TTS.api import TTS

# import openAI API key
openai.api_key = os.environ.get('OPENAI_API')

def speak_txt(command):
    # setup device for torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_name = "tts_models/en/jenny/jenny"
    tts = TTS(model_name)

    # run tts
    file = tts.tts_to_file(text=command, file='/tmp/temp.wav')
    pl(file)

# initialize the recognizer
r = sr.Recognizer()

def record_txt():
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Listening...")
                audio2 = r.listen(source2)
                
                text = r.recognize_google(audio2)

                return text

        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("An unknown error has occured!")

def send_to_chatGPT(messages, model="gpt-3.5-turbo-16k"):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
        

# speech = "This is a public service anouncement.  Is this system even working?"
# speak_txt(speech)

messages = []
while[1]:
    text = record_txt()
    messages.append({"role":"user", "content": text})
    response = send_to_chatGPT(messages)
    speak_txt(response)

    print(response)
