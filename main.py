import os
import time

from openai import OpenAI

api_key =   os.environ.get('Open_AI_KEY')
client = OpenAI(api_key=api_key)
file_path = 'C:/Users/JUNNY/Desktop/TTS/doctor_1.wav'

start_time = time.time()
with open(file_path, "rb") as audio_file:
    try:

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        end_time = time.time()
        print("Time: ", end_time - start_time)
        print(transcript)
    except Exception as e:
        print(e)
