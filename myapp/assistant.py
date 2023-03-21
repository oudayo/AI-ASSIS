import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import random
from gtts import gTTS
import soundfile
import ffmpeg

from os import path
from django.conf import settings

#
from googlesearch import search
#




def convert_mp3_wav(input_file):
                                                                        

    output_file = str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/output.wav'
    print(output_file)

    stream = ffmpeg.input(input_file)
    stream = ffmpeg.output(stream, output_file, format='wav')
    ffmpeg.run(stream)








r=sr.Recognizer() #Intanciate the speach recognizer

def record_audio(audioFile):

    output_file = str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/output.wav'
    convert_mp3_wav(audioFile) # el fonction hedhi dima tconverti el audio file w tsammih output.wav 
    with sr.AudioFile(output_file) as source:     
        audio = r.record(source)  
    
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio) # use of the google api to recognize what we are saying
    except sr.UnknownValueError:
        voice_data = 'pgoergoperkgpok'
        return voice_data
    return voice_data
    
    





def alpha_speak(audio_string):
    r=sr.Recognizer() #Intanciate the speach recognizer

    tts=gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file= str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/audio_model.mp3'
    
    tts.save(audio_file)


def respond(audioFile):

    voice_data = record_audio(audioFile)


    if 'what time is it' in voice_data:
        alpha_speak(ctime())

    elif 'who are you' in voice_data:
        alpha_speak('I am alpha')

    elif 'what do you offer' in voice_data:
        alpha_speak('we provide psychometric assessment from the most renowned universities globally, like the University of Cambridge, internationally accredited certification, and the list goes on')

    elif 'how are you' in voice_data:
        alpha_speak('I am fine thank you , How can I help you')

    elif 'tell me a joke' in voice_data:
        alpha_speak('I am Rich hahaha')

    elif 'search' in voice_data:
        result = search(voice_data, num_results = 1)
        for r in result:
            alpha_speak("here's what i found ")
            return r

    elif 'goodbye' in voice_data:
        alpha_speak('see you later')

    else: 
        alpha_speak('Sorry I did not get that , Please try again ')


