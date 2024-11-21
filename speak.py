#!/usr/bin/python3
#
# exploring tts with localAI


import requests
import simpleaudio as sa
import tempfile

def send_json_and_receive_output(url, json_data):
    try:
        response = requests.post(url, json=json_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error sending JSON data: {e}")
        return None

the_text = input("Text to speak:")

url = "http://localhost:8080/tts"
data = {"input": the_text, "model": "tts-1"}
audio_content = send_json_and_receive_output(url, data)

if audio_content:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(audio_content)
        temp_filename = f.name

    wave_obj = sa.WaveObject.from_wave_file(temp_filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()



