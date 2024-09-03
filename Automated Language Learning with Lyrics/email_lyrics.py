import os
import random
import smtplib
from musixmatch import Musixmatch
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Musixmatch and GoogleTranslator
api_key = os.getenv('API_KEY')
musixmatch = Musixmatch(api_key)
translator = GoogleTranslator(source='auto', target='en')

# Email configuration
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
smtp_server = 'smtp.gmail.com'
smtp_port = 587

def send_email(subject, message, from_email, to_email):
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(from_email, to_email, msg)

def get_track_id(country='fr'):
    response = musixmatch.chart_tracks_get(country=country, page_size=90, page=1, f_has_lyrics=True)
    track_list = response['message']['body']['track_list']
    return random.choice(track_list)['track']['track_id']

def get_lyrics(track_id):
    response = musixmatch.track_lyrics_get(track_id=track_id)
    lyrics = response['message']['body']['lyrics']['lyrics_body']
    return lyrics.splitlines()

def translate_lyrics(lyrics):
    translations = translator.translate_batch(lyrics)
    return [f"{original} -> {translation}" for original, translation in zip(lyrics, translations) if translation]

def main():
    track_id = get_track_id()
    lyrics = get_lyrics(track_id)
    lyrics_translation = translate_lyrics(lyrics)
    final_msg = '\n'.join(lyrics_translation)
    
    send_email(
        subject="Lyrics Translation",
        message=final_msg,
        from_email=email,
        to_email=os.getenv('TO_EMAIL')
    )

if __name__ == "__main__":
    main()