import os
import random
from musixmatch import Musixmatch
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('API_KEY')
musixmatch = Musixmatch(api)
translator = GoogleTranslator(source='auto', target='en')

def get_track_id(country='fr'):
    response = musixmatch.chart_tracks_get(country=country, page_size=90, page=1, f_has_lyrics=True)
    track_list = response['message']['body']['track_list']
    return random.choice(track_list)['track']['track_id']

def get_lyrics(track_id):
    response = musixmatch.track_lyrics_get(track_id=track_id)
    lyrics = response['message']['body']['lyrics']['lyrics_body']
    return lyrics.splitlines()

def translate_lines(lyrics):
    translations = translator.translate_batch(lyrics)
    for original, translation in zip(lyrics, translations):
        if translation:
            print(f"{original} -> {translation}")

translate_lines(get_lyrics(get_track_id()))
