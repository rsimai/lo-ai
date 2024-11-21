#!/usr/bin/python3
#
# transcriptions with localAI, audio file as argument

import requests
import sys

def transcribe_audio(file_path, model_name):
    try:
        with open(file_path, 'rb') as audio_file:
            files = {'file': (file_path, audio_file, 'multipart/form-data')}  # Explicitly set content type to audio/ogg
            response = requests.post(url, files=files, data={'model': model_name})
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error transcribing audio: {e}")
        return None

url = "http://localhost:8080/v1/audio/transcriptions"
file_path = sys.argv[1]
model_name = "whisper-1"

transcription = transcribe_audio(file_path, model_name)

if transcription:
    if 'text' in transcription:
        print(transcription['text'])
    else:
        print("No text field")
