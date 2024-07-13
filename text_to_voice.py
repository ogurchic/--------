from dotenv import load_dotenv
import os
import requests
import json
from pydub import AudioSegment
from pydub.playback import play
import io

# getting api key from .env
load_dotenv()
api_key = os.getenv('TEXT_TO_VOICE_API')

def text_to_speech(text):
    headers = {"Authorization": f"Bearer {api_key}"}

    url = "https://api.edenai.run/v2/audio/text_to_speech"
    payload = {
        "providers": "google",
        "language": "ru-RU",
        "option": "MALE",
        "google": "ru-RU-Standard-B",
        "text": f"{text}",
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    audio_url = result.get('google').get('audio_resource_url')
    r = requests.get(audio_url) 

    audio_file = io.BytesIO(r.content)
    song = AudioSegment.from_file(audio_file, format="mp3")
    play(song)

# text = 'Привет, меня зовут Артур Максимович, я представитель компании орифлейм, как ваши дела? Google В железногорске сейчас 21 °C'
# text_to_speech(text)