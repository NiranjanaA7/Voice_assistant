import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
import pyjokes
import os
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    text_area.insert(tk.END, text + '\n')

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 0.5  # Reduce pause threshold to improve response time
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Processing.. ")
        text = r.recognize_google(audio, language='en-in')
        print(f'You said: {text}\n')

    except Exception as e:
        print(e)
        speak('Please tell the command again')
        text = 'none'

    return text

def start_voice_thread():
    threading.Thread(target=continuous_listening).start()

def continuous_listening():
    while True:
        command = get_audio().lower()
        entry.delete(0, tk.END)
        entry.insert(0, command)
        on_button_click()
        if 'stop' in command or 'exit' in command:
            break

def get_weather():
    api_key = '2c6b9a3ab808aed89b4b80801ffdf013'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    speak('Please tell the city name')
    city_name = get_audio().lower()

    response = requests.get(f'{base_url}?q={city_name}&appid={api_key}')
    data = response.json()

    if data['cod'] == '404':
        return 'City not found'
    else:
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        result = f"The weather is {weather_desc}. Temperature: {temperature} K. Humidity: {humidity}%. Wind Speed: {wind_speed} m/s."
        return result


def play_music():
    song = entry.get()
    speak('playing ' + song)
    pywhatkit.playonyt(song)

def search_web():
    speak('What should I search for?')
    query = continuous_listening()
    pyautogui.write(query)
    pyautogui.press('enter')

def get_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak('Current time is ' + time)

def get_joke():
    speak(pyjokes.get_joke())

def get_story():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
    who = ['namjoon', 'Jin', 'Yoongi', 'Jhope', 'Jimin', 'Taehyung', 'Jungkook']
    residence = ['Korea', 'India', 'Germany', 'Japan', 'England']
    went = ['cinema', 'university', 'seminar', 'school', 'laundry']
    happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    speak(random.choice(when) + ', ' + random.choice(who) + ' who lived in ' + random.choice(
        residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

def on_button_click():
    command = entry.get().lower()
    if 'play' in command:
        play_music()
    elif 'search' in command:
        search_web()
    elif 'time' in command:
        get_time()
    elif 'weather' in command:
        speak('Please wait, getting weather information...')
        weather_info = get_weather()
        speak(weather_info)
        print(weather_info)
    elif 'joke' in command:
        get_joke()
    elif 'story' in command:
        get_story()
    elif 'hello' in command or 'hi' in command:
        speak('hello how can i help you')
    elif 'name' in command or 'call you' in command:
        speak('you can call me rain')
    elif 'how are you' in command:
        speak('I am fine. You are very kind to ask')
        speak("How are you")
    elif 'fine' in command or "good" in command:
         speak("It's good to know that your fine")
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'thank you' in command:
        speak('you are welcome')
    elif 'minimize' in command or 'minimise' in command:
        pyautogui.hotkey('win', 'down', 'down')
    elif 'close the window' in command:
        pyautogui.hotkey('ctrl', 'w')
    elif 'maximize' in command:
        pyautogui.hotkey('win', 'up', 'up')
    elif 'open notepad' in command:
        speak('opening notepad')
        os.startfile('C:\\Windows\\System32\\notepad.exe')
        while True:
            nquery = continuous_listening().lower()
            if 'paste' in nquery:
                pyautogui.hotkey('ctrl', 'v')
            elif 'save this file' in nquery:
                pyautogui.hotkey('ctrl', 's')
                speak('Please specify a name for this file')
                nsquery = continuous_listening()
                pyautogui.write(nsquery)
                pyautogui.press('enter')
            elif 'type' in nquery:
                speak('what should i write..')
                while True:
                     wn = continuous_listening()
                     if wn == 'exit typing':
                        speak('exiting')
                        break
                     else:
                        pyautogui.write(wn)
            elif 'close notepad' in nquery:
                    speak('closing notepad')
                    pyautogui.hotkey('ctrl', 'w')

    elif 'who i am' in command:
        speak('If you talk then definetly your human.')

def start_gui():
    global entry, text_area
    window = tk.Tk()
    window.title("Voice Assistant")
    window.configure(bg='lightgray')

    label = tk.Label(window, text="Enter Command:", bg='lightgray', fg='black', font=('Arial', 12))
    label.grid(row=0, column=0, padx=10, pady=10)

    entry = tk.Entry(window, width=50, bg='white', fg='black', font=('Arial', 12))
    entry.grid(row=0, column=1, padx=10, pady=10)

    mic_image = tk.PhotoImage(file='microphone.png').subsample(2, 2)  # Path to your microphone image
    mic_button = tk.Button(window, image=mic_image, command=start_voice_thread, bg='lightgray', bd=0)
    mic_button.grid(row=0, column=2, padx=10, pady=10)

    button = tk.Button(window, text="Enter", command=on_button_click, bg='lightgray', fg='black', font=('Arial', 12))
    button.grid(row=1, column=1, padx=10, pady=10)

    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, bg='white', fg='black', font=('Arial', 12))
    text_area.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    window.mainloop()

start_gui()


if __name__ == "__main__":
    start_gui()
