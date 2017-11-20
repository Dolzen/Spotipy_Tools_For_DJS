import os
import Tkinter
import spotipy
import youtube_downloader_lucky
#top = Tkinter.Tk()
os.environ["SPOTIPY_CLIENT_ID"] = "e27671f553c6494bbd40bc1abe0b9372"
os.environ["SPOTIPY_CLIENT_SECRET"] = "a0ca026a4bec439989ebe593df1820f2"
os.environ["SPOTIPY_REDIRECT_URI"] = "localhost:/callback"
#export SPOTIPY_CLIENT_ID='e27671f553c6494bbd40bc1abe0b9372'
#export SPOTIPY_CLIENT_SECRET='a0ca026a4bec439989ebe593df1820f2'
#export SPOTIPY_REDIRECT_URI='localhost://returnAfterLogin'
#test seed 28yU9kjRYIU68AjYF3yWFp







username='neddann'
scope = 'user-library-read'
token = 'BQDH7EoMNmyTvOgpWVJ9AfTBF7EUBLpE2fbBlEkp_U4bx7Gm6HGB3ksvik2qmAulTUCalRACwp13lPXBEHmsZ03jpgxsDT-6uhT8RORzWjUB5H08236XwGwJMOOtQcGvQku5FrlIwg7yOWjohbaUiOtNN052sKa9CQFCeMDg-BtLqoqiQ1w6d_OQOIeRU-oMK4M59ZwIT4l0sv81ZacEKtFQTbaFyau0tflCbV6t3s-hDbaNLxgh85pZHWar5QE72PL--jHv2cPFGGjZjFIwb_uY9robAzGHgAJMw5tA1-As--PEIpnEvc_Nxz89QQqTlODY3g'
sp = spotipy.Spotify(auth=token)



input_album_string = 'kaytranada 99.9%'
import sys
#print(sys.argv)
if len(sys.argv) > 1:
    #print('getting other arguments')
    input_album_string = sys.argv[1]



album_return_obj = sp.search(input_album_string, limit=1, type='album')
#print(album_return_obj)
if len(album_return_obj['albums']['items']) == 0:
    print("No Matching Albums Found")
    exit()
album_id = album_return_obj['albums']['items'][0]['id']
album_name = album_return_obj['albums']['items'][0]['name']
try:
    album_image_url = album_return_obj['albums']['items'][0]['images'][0]['url']
except:
    album_image_url = None
#print(album_id)
input_album_string = album_id
test_track_data = sp.audio_features(str(input_album_string))

#target_tempo = int(round(test_track_data[0]['tempo']))
#min_tempo = target_tempo-5
#max_tempo = target_tempo+1
print 'Album -> ',album_name
#print 'Target Tempo ->' , target_tempo
print ' '

#kwargs = {"min_danceability":0.6,"min_tempo": min_tempo, "max_tempo":max_tempo,"target_tempo":target_tempo,'time_signature':4}
#results = sp.recommendations(seed_tracks=[input_album_string], limit=20, **kwargs)
results = sp.album(album_id)
all_tracks=False
#while all_tracks == False3
#     try
#        next = results.next

tracks = results['tracks']['items']
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
print(" Album Tracks ")
print("=======================")
for track_obj in tracks:
    track_name = track_obj['name']
    artist_objs = track_obj['artists']
    found_titles.append(track_name)
    est_durations.append(int((track_obj['duration_ms']) / 1000))
    #found_albums.append(track_obj['album']['name'])
    track_numbers.append(track_obj['track_number'])
    try:
        image_urls.append(track_obj['album']['images'][0]['url'])
    except:
        #print("NO IMAGE")
        image_urls.append(None)
    artist_string = ''

    for those in artist_objs:
        if artist_string != '':
            artist_string = artist_string + ', ' + those['name']
        else:
            artist_string = those['name']
        break
    found_artist_names.append(artist_string)
    found_track_names.append(track_name)
    found_keys.append(track_obj['id'])
    found_youtube_queries.append(track_name+'-'+artist_string)

    print track_name,'-',artist_string,' ',est_durations[i]
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

#hits = 0
#for track in found_track_names:
#    #print(track)
#    if track in target_list_name:
#        hits += 1
#print('')
#print("Accuracy - out of 16 ",hits)


est_time = 0
os.chdir('songs')

i = 0
for those in found_youtube_queries:
    spotify_data = {'title':found_titles[i], 'artist':found_artist_names[i], 'album':album_name,'tracknumber':track_numbers[i]}
    youtube_downloader_lucky.download(those,est_durations[i],album_image_url,spotify_data)
    i += 1
