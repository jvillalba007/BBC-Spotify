# Radio BBC to Spotify Playlist
import re
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

url = input('BBC URL: ')
regex = r"(https?:\/\/open.spotify.com\/(track|user|artist|album)\/[a-zA-Z0-9]+(\/playlist\/[a-zA-Z0-9]+|)|spotify:(track|user|artist|album):[a-zA-Z0-9]+(:playlist:[a-zA-Z0-9]+|))"
data_html = ""
tracks = ('')
lenght = 0


tracks_spotify = []

try:
    response = requests.get(url)
    if response.ok:
        data_html = response.text
        print('Buena Respuesta para', url, response.status_code)
        tracks = re.findall(regex, data_html)
        lenght = len(tracks) // 2
    else:
        print('Mala respuesta para', url, response.status_code)
except requests.exceptions.ConnectionError as exc:
    print(exc)

print("Total de Canciones: " + str(lenght))

if len(tracks) > 0:
    for track in range(lenght):
        track_spotify = tracks[track][0].replace(
            "https://open.spotify.com/track/", "spotify:track:")
        tracks_spotify.append(track_spotify)
    File_Playlist = open("playlist.txt", "r")    
    playlist_id = File_Playlist.read().splitlines()[0]
    spotify_url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(
        playlist_id=playlist_id)
    File_Playlist.close()    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="http://localhost:7777/callback",
                                               scope="playlist-modify-public,playlist-modify-private"
                                               ))
    print(sp.playlist_add_items(playlist_id, tracks_spotify))
