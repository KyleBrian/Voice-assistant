import speech_recognition as sr
import pyttsx3

# this method is for taking the commands and recognizing the command from the
# speech_Recognition module we will use the recongizer method for recognizing

def takeCommand():

# Initialize the recognizer
    r = sr.Recognizer()

# Set the microphone as the audio source
    mic = sr.Microphone()

# Set the language to English
    with mic as source:
            print('Listening')

#voice properties
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    

# seconds of non-speaking audio before a phrase is considered complete
    audio = r.listen(source)
    r.energy_threshold = 500
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_ratio = 1.5
    r.pause_threshold = 0.5
    r.phrase_threshold = 0.3


# Now we will be using the try and catch method so that if sound is recognized
# it is good else we will have exception handling

    try:
            print("Recognizing")
# for Listening the command in english we can also use 'hi-In'
# for hindi recognizing
            Query = r.recognize_google(audio, language='en')
            print("the command is printed=", Query)

    except sr.UnknownValueError:
        speak.Speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak.Speak("Sorry, my speech service is down.")