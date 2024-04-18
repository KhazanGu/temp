from openai import OpenAI
import time
import os
import requests

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print("start time:-", start)

def download_mp3(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("MP3 downloaded successfully")
    else:
        print("Failed to download MP3")

# Example usage
url = "https://volcdn1.kuangshi.fun/vip/app/audio/ios/kyb/2024/04/2024_04_17_18_14_31_video_62776361.wav"
filename = "downloaded_file.wav"
download_mp3(url, filename)

print("recognize time:-", start)

audio_file= open("downloaded_file.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

end = time.time()
print("end time:-", end)

print(transcription.text)
