# -*- coding: utf-8 -*-
import base64
import os

import requests
import json

from pydub import AudioSegment

# String 형태의 API 키
api_key = os.environ.get('Google_KEY')

# 원본 .wav 파일 불러오기 및 처리
audio = AudioSegment.from_wav("C:/Users/JUNNY/Desktop/TTS/crying_stt.wav")
audio = audio.set_frame_rate(16000).set_sample_width(2).set_channels(1)

# 변경된 형식으로 저장
converted_file_path = "C:/Users/JUNNY/Desktop/TTS/converted_crying_stt.wav"
audio.export(converted_file_path, format="wav")

# 변환된 오디오 파일을 바이너리 형태로 읽기
with open(converted_file_path, 'rb') as audio_file:
    audio_content = audio_file.read()

# Base64 인코딩으로 오디오 데이터 변환
audio_content_base64 = base64.b64encode(audio_content).decode('utf-8')

# API 요청을 위한 데이터 구성
data = {
    "config": {
        "encoding": "LINEAR16",
        "sampleRateHertz": 16000,
        "languageCode": "ko-KR",
        "useEnhanced": True,


    },
    "audio": {
        "content": audio_content_base64
    }
}


# 요청 URL 구성
url = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyDN9lnD8lu8QxvdheLLeyFU7Wzp8uAJ0XA"

# POST 요청 보내기
response = requests.post(url, data=json.dumps(data))
print(response.content.decode('utf-8'))