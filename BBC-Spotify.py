# Radio BBC to Spotify Playlist
import re
import requests

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
    playlist_id = input('Spotify Playlist ID: ')
    spotify_url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(
        playlist_id=playlist_id)
    print("Spotify Endpoint: " + spotify_url)
    OAuth_Token = input('Spotify OAuth Token: ')
    headersAuth = {
        'Authorization': 'Bearer ' + str(OAuth_Token),
    }
    response = requests.post(spotify_url, headers=headersAuth, json={
                             'uris': tracks_spotify}, verify=True)
    print("Resultado: " + str(response.json()))
