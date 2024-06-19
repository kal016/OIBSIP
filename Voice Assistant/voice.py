import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)  # Use Google Speech Recognition
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to speak out the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Main function to handle user queries
def main():
    speak("Hello! I'm your Python voice assistant. How can I help you?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hello there! How can I assist you?")
        elif "how are you" in query:
            speak("I'm doing great, thank you for asking!")
        elif "what time is it" in query:
            # You can implement time fetching logic here
            speak("I'm sorry, I can't tell the time right now.")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
