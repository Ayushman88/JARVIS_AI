import webbrowser
import speech_recognition as sr
import os
import datetime
import pyjokes

def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.pause_threshold = 0.8
        r.non_speaking_duration = 0.1
        try:
            audio = r.listen(mic, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
        except KeyboardInterrupt:
            print("Listening interrupted.")
            return ""


if __name__ == '__main__':
    print('PyCharm')
    say("Hello Sir, I am JARVIS A.I")

    while True:
        print('Listening....')
        query = takeCommand()

        if not query:
            continue

        if query.lower() == "quit":
            break

        sites = [
            ["youtube", "http://youtube.com"],
            ["wikipedia", "http://wikipedia.com"],
            ["google", "http://google.com"],
            ["my github", "https://github.com/Ayushman88"],
            ["my course", "https://www.apnacollege.in/path-player?courseid=delta&unit=64afc1f3e9ddc127450c69a7Unit"],
            ["anime", "https://aniwatch.to/home"],
            ["instagram", "https://www.instagram.com/____ayushman___/"]
        ]

        commands = {
            "open spotify": "Opening Spotify sir...",
            "open whatsapp": "Opening Whatsapp sir...",
            "the time": f"Sir, the time is {datetime.datetime.now().strftime('%H:%M:%S')}",
            "how old are you": "I am an artificial intelligence program, I don't have an age."
                               " But I was Created on 17th July 2023 by Ayushman",
            "tell me a joke": pyjokes.get_joke()
        }

        command_matched = False

        for site in sites:
            if f"open {site[0].lower()}" in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                command_matched = True
                break

        for command, response in commands.items():
            if command in query.lower():
                say(response)
                if "spotify" in command:
                    os.system("open -a Spotify")
                elif "whatsapp" in command:
                    os.system("open -a WhatsApp")
                command_matched = True
                break

        if "tell me a joke" in query.lower():
            say(pyjokes.get_joke())
            command_matched = True

        if not command_matched:
            say("Sorry, I didn't catch that. Can you please repeat?")
