import webbrowser
import speech_recognition as sr
import os
import datetime
import pyjokes
import wikipedia

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
    print('JARVIS')
    say("Hello Sir, I am JARVIS A.I")

    is_jarvis_active = False

    while True:
        print('Listening....')
        query = takeCommand()

        if not query:
            continue

        if query.lower() == "quiet" or query.lower() == "by":
            say("Goodbye, Sir. Have a nice day!"
                "SIGNING OFF")
            break

        if query.lower() == 'jarvis':
            if is_jarvis_active:
                say("Yes, sir? How can I assist you?")
            else:
                say("Jarvis is listening, sir. Please go ahead.")
                is_jarvis_active = True
            continue

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
            "tell me a joke": pyjokes.get_joke(),
            "search wikipedia": "What would you like to search on Wikipedia? sir",
            "search google": "What would you like to search on Google? sir"
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
                elif "search wikipedia" in command:
                    say("Sure, what would you like to search on Wikipedia?")
                    query = takeCommand()
                    try:
                        page = wikipedia.page(query)
                        summary = wikipedia.summary(query, sentences=3)
                        say(summary)
                    except wikipedia.DisambiguationError as e:
                        options = e.options[:5]
                        say(f"There are multiple options available. Here are some of them: {', '.join(options)}")
                elif "search google" in command:
                    query = takeCommand()
                    search_query = query.replace("search google", "").strip()
                    google_url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(google_url)
                command_matched = True
                break

        if "tell me a joke" in query.lower():
            say(pyjokes.get_joke())
            command_matched = True

        if not command_matched and is_jarvis_active:
            say("Sorry, I didn't catch that. Can you please repeat?")
        elif not command_matched:
            is_jarvis_active = False
