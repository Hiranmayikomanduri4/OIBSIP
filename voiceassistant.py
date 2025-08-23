import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import wikipedia
import datetime
import webbrowser
from scipy.io.wavfile import write

def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()   # re-init each time (fix for only first line issue)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # choose voice
    engine.say(text)
    engine.runAndWait()

def listen():
    fs = 44100  # Sample rate
    seconds = 3 # Recording duration
    
    speak("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()  
    
    write("input.wav", fs, recording)  
    
    r = sr.Recognizer()
    with sr.AudioFile("input.wav") as source:
        audio = r.record(source)
    
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def main():
    # Intro
    speak("Hello, I am your assistant. What is your name?")
    name = listen()
    if name.strip() == "":
        name = "friend"
    speak(f"Nice to meet you, {name}. I am ready to help you.")
    
    while True:
        query = listen()

        if "exit" in query or "quit" in query:
            speak(f"Goodbye {name}! Have a nice day.")
            break

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "who is" in query or "what is" in query:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, I couldn't find information on that.")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        else:
            speak("Sorry, I don’t know that command yet.")

if __name__ == "__main__":
    main()
