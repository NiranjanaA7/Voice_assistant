# Voice Assistant Using Python

A powerful voice assistant built with Python, utilizing libraries like `speech_recognition`, `pyttsx3`, `requests`, and `pywhatkit` for functionalities such as speech recognition, text-to-speech conversion, weather updates, YouTube music playing, and more.

## Features

- **Speech Recognition**: Listens to your voice commands using the microphone.
- **Text-to-Speech**: Responds to your commands by speaking.
- **Weather Updates**: Provides current weather information for any city.
- **YouTube Music**: Plays songs directly from YouTube.
- **Web Search**: Searches the web based on your voice commands.
- **Time Telling**: Tells the current time.
- **Jokes and Stories**: Tells jokes and generates random stories.
- **Notepad Automation**: Opens Notepad, types, pastes, saves, and closes based on commands.
- **System Commands**: Minimizes, maximizes, and closes windows, among other tasks.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/voice-assistant.git
    cd voice-assistant
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the microphone image** (Optional):
    - Download a microphone image (e.g., from [here](https://www.flaticon.com/free-icon/microphone_2882831)) and save it in the project directory.

4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Start the application**:
    - Run `main.py` to start the GUI.

2. **Enter commands**:
    - Type your command in the input box or use the microphone button to speak your command.

3. **Voice commands**:
    - Example commands include:
        - `Play [song name]`
        - `Search for [query]`
        - `What's the time?`
        - `What's the weather in [city]?`
        - `Tell me a joke`
        - `Tell me a story`
        - `Open Notepad` (followed by commands like `Type`, `Paste`, `Save this file`, `Close Notepad`)

## Dependencies

- `tkinter`: For creating the graphical user interface.
- `speech_recognition`: For recognizing spoken commands.
- `pyttsx3`: For text-to-speech conversion.
- `requests`: For making HTTP requests to fetch weather data.
- `pywhatkit`: For playing YouTube videos.
- `pyjokes`: For generating jokes.
- `pyautogui`: For controlling the mouse and keyboard.
- `os`: For interacting with the operating system.
- `datetime`: For working with date and time.
- `threading`: For running tasks concurrently.


