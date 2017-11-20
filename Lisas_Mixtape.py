import os
import Tkinter
import spotipy

os.environ["SPOTIPY_CLIENT_ID"] = "e27671f553c6494bbd40bc1abe0b9372"
os.environ["SPOTIPY_CLIENT_SECRET"] = "a0ca026a4bec439989ebe593df1820f2"
os.environ["SPOTIPY_REDIRECT_URI"] = "localhost:/callback"
#export SPOTIPY_CLIENT_ID='e27671f553c6494bbd40bc1abe0b9372'
#export SPOTIPY_CLIENT_SECRET='a0ca026a4bec439989ebe593df1820f2'
#export SPOTIPY_REDIRECT_URI='localhost://returnAfterLogin'
#test seed 28yU9kjRYIU68AjYF3yWFp






username='neddann'
scope = 'user-library-read'
print('')
print('')
print('')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Lisa's Mixtape ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print''


test_track = 'kaytranada Track uno'
token = 'BQDGDG2npZdQWKybUUFG4QJO5GxqQOZXdRJuJ9LgwI6vHIuX7O5xsR7KPaFgDEMeJHofFjIcxH1BowSM0igWdGcTK0Kke4398jRyoROUs-SnsBWOpugs3NbREzbP1R07W7lGURmMV9reQt1iJfZOj_F4AxY4Qm36dgkb09rJWu01vbt7gtS-NgGxlXoKf23OFvxTtEfuPoqut2p0iYTvP0Rj72hPryO3p1e1R8_h5k6LB8luIbgkeAPEODoVq3hai6JpAv9G2pG41C347dYw2ecG78EVg8ElSb-60vF91wOahYghymUGHJmxkZ3nfYr4v5LlMA'
sp = spotipy.Spotify(auth=token)


import sys
#print(sys.argv)
if len(sys.argv) > 1:
    #print('getting other arguments')
    test_track = sys.argv[1]



test_track_obj = sp.search(test_track,limit=1,type='track')
test_track_id = test_track_obj['tracks']['items'][0]['id']
test_track_name = test_track_obj['tracks']['items'][0]['name']
test_track = test_track_id
test_track_data = sp.audio_features(str(test_track))

target_tempo = int(round(test_track_data[0]['tempo']))
min_tempo = target_tempo-5
max_tempo = target_tempo+1
print 'Seed Song -> ',test_track_name
print 'Target Tempo ->' , target_tempo
print ' '

kwargs = {"min_danceability":0.6,"min_tempo": min_tempo, "max_tempo":max_tempo,"target_tempo":target_tempo,'time_signature':4}
results = sp.recommendations(seed_tracks=[test_track],limit=20,**kwargs)


target_list_name = [
    '2112'
    ,'The Game'
    ,'Kids'
    ,'She Loves You'
    ,'Hoover - Adam K Remix'
    ,'Cold Blooded'
    ,'La Funky'
    ,"I Don't Wanna Go Home"
    ,'Prophecy'
    ,'Feel The Volume'
    ,'All I Know'
    ,'Together - Live From Spotify NYC'
    ,'US'
    ,'Teach Me - Radio Edit'
    ,'IPlayYouListen'
    ,'Intro (Neon City'
    ,'Eagle eyes - Lucas & Steve Remix Edit'
    ,'Static'
]
target_list_artist = [
    'Destructo'
    ,'Jauz'
    ,'Jerry Folk'
    ,'Claptone'
    ,'EDX'
    ,'ZHU'
    ,'Desctucto, Oliver'
    ,'Tchami,Malaa'
    ,'EDX'
    ,'ZHU'
    ,'Felix Jaehn, Polina'
    ,'CAZZETTE, Newtimers'
    ,'Kaskade, CID'
    ,'Bakermat'
    ,'ODESZA'
    ,'ZHU'
    ,'Felix Jaehn, Lost Frequencies, Linying, Lucas & Steve'
    ,'CAZZETTE'
]
tracks = results['tracks']
found_track_names = []
found_artist_names = []
found_youtube_queries = []
image_urls = []
est_durations = []
tempos = []
found_titles = []
found_albums = []
track_numbers = []
i = 0
found_keys = []
print("=======================")
print(" MATCHING SONGS ")
print("=======================")
for track_obj in tracks:
    track_name = track_obj['name']
    artist_objs = track_obj['artists']
    found_titles.append(track_name)
    est_durations.append(int((track_obj['duration_ms']) / 1000))
    found_albums.append(track_obj['album']['name'])
    track_numbers.append(track_obj['track_number'])
    try:
        image_urls.append(track_obj['album']['images'][0]['url'])
    except:
        print("NO IMAGE")
        image_urls.append(None)
    artist_string = ''
    for those in artist_objs:
        if artist_string != '':
            artist_string = artist_string + ', ' + those['name']
        else:
            artist_string = those['name']
    found_artist_names.append(artist_string)
    found_track_names.append(track_name)
    found_keys.append(track_obj['id'])
    found_youtube_queries.append(track_name+'-'+artist_string)

    print track_name,'-',artist_string,' '
    i += 1
print('')
print("Getting Tempo of songs")
#print(image_urls)
#print(est_durations)

#for those in found_keys:
    #test_track_data = sp.audio_features(str(those))
    #unpacked_track = sp.track(str(those))
    #ound_albums.append()
#    est_durations.append(int((test_track_data[0]['duration_ms'])/1000))
    #tempos.append(test_track_data[0]['tempo'])
#    print unpacked_image['images']
#    print("NO IMAGE FOUND")

#print(tempos)

hits = 0
for track in found_track_names:
    #print(track)
    if track in target_list_name:
        hits += 1
print('')
#print("Accuracy - out of 16 ",hits)

import youtube_downloader_lucky
est_time = 0
os.chdir('songs')






i = 0
print("Downloading Songs")
print""
for those in found_youtube_queries:
    spotify_data = {'title':found_titles[i], 'artist':found_artist_names[i], 'album':found_albums[i],'tracknumber':track_numbers[i]}
    youtube_downloader_lucky.download(those,est_durations[i],image_urls[i],spotify_data)
    i += 1
