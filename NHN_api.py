import os
import time

import requests
app_key = os.environ.get('NHN_KEY')
secret_key = os.environ.get('NHN_secret_key')

file_path = 'C:/Users/JUNNY/Desktop/TTS/doctor_1.wav'

url = 'https://speech.api.nhncloudservice.com/v1.0/appkeys/jEYgf8XX36mxjLoY/stt'
start_time = time.time()
headers = {
    'Authorization': secret_key
}

files = {
    'audio': open(file_path, 'rb')
}

response = requests.post(url, headers=headers, files=files)

end_time = time.time();

print("Time: ", end_time - start_time)
if response.status_code == 200:
    print("Response from API:", response.text)
else:
    print("Error:", response.status_code, response.text)

files['audio'].close()