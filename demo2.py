import gradio as gr
import openai
import config
import pyttsx3
import speech_recognition as sr
import threading

openai.api_key = config.OPENAI_API_KEY

conversation = []
assistant_active = False

recognizer = sr.Recognizer()

def transcribe_and_submit(audio_path):
    global conversation

    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    conversation.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)

    system_message = response["choices"][0]["message"]
    conversation.append(system_message)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Convert system message to speech
    engine.say(system_message['content'])

    # Wait for the speech to finish
    engine.runAndWait()

    chat_transcript = ""
    
    for message in conversation:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

def listen_for_trigger():
    global conversation, assistant_active

    while True:
        with sr.Microphone() as source:
            print("Listening for trigger phrase...")
            audio = recognizer.listen(source, timeout=10)  # Set the timeout value as needed
            try:
                recognized_text = recognizer.recognize_google(audio).lower()
                if "start recording" in recognized_text:
                    print("Trigger phrase detected. Starting recording.")

                    conversation = []
                    assistant_active = True

                    # Start recording
                    audio_input = recognizer.listen(source, timeout=10)  # Set the timeout value as needed
                    print("Recording completed.")

                    # Save audio to temporary file
                    audio_path = "temp_audio.wav"
                    with open(audio_path, "wb") as f:
                        f.write(audio_input.get_wav_data())

                    # Process audio and submit to model
                    transcribe_and_submit(audio_path)

                    print("Assistant session complete.")
                    assistant_active = False
            except sr.UnknownValueError:
                pass

listen_thread = threading.Thread(target=listen_for_trigger)
listen_thread.start()

ui = gr.Interface(fn=transcribe_and_submit, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")
ui.launch(server_name="127.0.0.1", server_port=7861)

