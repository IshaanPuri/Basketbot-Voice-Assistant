import pyttsx3
import speech_recognition as sr
import pyaudio

'''
Hello everyone I'm Ishaan and this is my Basketbot Voice Assistant. I programmed this using the Speech 
Recognition API and various other Python libraries. Hope you enjoy!
'''

#Setting up the voice of the assistant
engine = pyttsx3.init()
voices = engine.getProperty('voices')   #Getting details of current voice
engine.setProperty('voice', voices[0].id) #Voice selction
#Setting the speaking rate
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 220)


#Speech Recogntion Portion
listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("I AM LISTENING")
        audio = listener.listen(source)
        verbiage = listener.recognize_google(audio)
        print(verbiage)
except:
    pass


