# Voice Assistant Web Application

---

## Overview

The Voice Assistant Web Application is a Flask-based project that integrates OpenAI's GPT-3.5 model, speech recognition, and text-to-speech capabilities. It allows users to interact with the assistant using voice commands, providing text and audio responses.

---

## Features

- Start and stop the assistant via a user-friendly web interface.
- The assistant listens for a trigger phrase, captures user input, processes it with OpenAI's GPT-3.5 model, and responds with synthesized speech.
- Displays responses as text on the web interface alongside audio playback.

---

## Prerequisites

- Python 3.x
- OpenAI API Key
- Flask
- SpeechRecognition
- pyttsx3
- jQuery (via CDN)

---

## Installation and Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. **Set up Virtual Environment**:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure OpenAI API Key**:
   - Replace config.OPENAI_API_KEY in the config.py file with your OpenAI API key

5. **Run the Application**:
   ```
   flask run app.py
   ```

6. **Access the Application**: 
   - Open a browser and navigate to http://localhost:port where the port or entire URL will be specified in the terminal output

---

## File Structure

- **app.py**: Flask application containing routes and assistant logic

- **templates/index.html**: HTML template for web interface

- **requirements.txt**: List of required Python packages

- **static/css/style.css**: CSS for styling the application

---

## Usage Instructions

1. **Navigate to the application in your web browser**

2. **Click the Start Assistant button to activate the voice assitant**

3. **Speak the trigger phrase ("start") followed by your question or command**

4. **View the assistant's response on the interface or listen to the synthesized audio**

5. **Click the Stop Assistant button to deactivate the assitant**

---

## Technology Stack

- **Backend**: Flask, Python

- **Frontend**: HTML, CSS, Javascript, jQuery

- **APIs**: OpenAI (GPT-3.5)

- **Speech Processing**: SpeechRecognition, pyttsx3

---

## Key Dependencies

- **Flask==2.3.3**

- **openai==0.27.8**

- **pyttsx3==2.90**

- **SpeechRecognition==3.10.0**

- **gunicorn==21.2.0**

- **Jinja2==3.1.2**

- **Werkzeug==2.3.7**

---

## Troubleshooting

- Ensure the OpenAI API Key is correctly configured in config.py

- Verify your microphone is functioning and accessible to the application

- Check the browser console or Flask logs for errors if the assitant does not respond

---

## Future Enhancements

- Add natural language understanding capabilities for broader command recognition

- Enhance error handling for audio transcription and API calls

- Integrate additional voice control features

---

## Acknowledgements

- **Built using [OpenAI API](https://openai.com)**

- **Framework provided by [Flask](https://flask.palletsprojects.com/en/stable/)**

---

## License

This project is licensed under the MIT license. See the [MIT license](https://opensource.org/license/mit) for more details.


