import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os
from pydub import AudioSegment
from pydub.playback import play

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'YOUR_REDIRECT_URI'

# Spotify authentication
scope = 'user-library-read'
username = 'YOUR_USERNAME'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# Group songs by genre
def group_songs_by_genre(song_titles):
    genres = {}

    for title in song_titles:
        results = sp.search(q=f'track:{title}', type='track', limit=1)
        if results and 'items' in results['tracks'] and 'artists' in results['tracks']['items'][0]:
            artist_id = results['tracks']['items'][0]['artists'][0]['id']
            artist = sp.artist(artist_id)

            if artist and 'genres' in artist:
                for genre in artist['genres']:
                    if genre in genres:
                        genres[genre].append(title)
                    else:
                        genres[genre] = [title]

    return genres

#  BPM analysis
def get_bpm(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    return audio.frame_rate

# music key detection
def detect_key(audio_file_path):
    # Implement music key detection algorithm (e.g., using a library like librosa)
    pass

# Group songs by genre
song_titles = ["Song Title 1", "Song Title 2", "Song Title 3"]
grouped_songs = group_songs_by_genre(song_titles)

# 7. Analyze songs for BPM and key
for genre, songs in grouped_songs.items():
    for song_title in songs:
        audio_file_path = f"audio/{song_title}.mp3"  # Adjust the path to your audio files
        bpm = get_bpm(audio_file_path)
        key = detect_key(audio_file_path)
        print(f"Song: {song_title}, Genre: {genre}, BPM: {bpm}, Key: {key}")

from random import shuffle

# Transition optimization and musical flow logic
def optimize_transitions(songs):
    # You can implement your own logic here for optimizing transitions.
    # For simplicity, we'll shuffle the songs.
    shuffle(songs)
    return songs

def create_dj_set(songs):
    dj_set = optimize_transitions(songs)
    return dj_set

song_titles = ["Song Title 1", "Song Title 2", "Song Title 3"]
grouped_songs = group_songs_by_genre(song_titles)

dj_set_list = []
for genre, songs in grouped_songs.items():
    optimized_songs = create_dj_set(songs)
    dj_set_list.extend(optimized_songs)

print("Optimized DJ Set List:")
for i, song in enumerate(dj_set_list, start=1):
    print(f"{i}. {song}")
