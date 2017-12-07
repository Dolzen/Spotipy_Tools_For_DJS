from __future__ import print_function
import os
import Tkinter
import spotipy
import urllib
#AUTH STUFF
import spotipy
import webbrowser
from spotipy import oauth2
import youtube_downloader_lucky
import os

"""
os.environ["SPOTIPY_CLIENT_ID"] = "e27671f553c6494bbd40bc1abe0b9372"
os.environ["SPOTIPY_CLIENT_SECRET"] = "a0ca026a4bec439989ebe593df1820f2"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost/callback"
def prompt_for_user_token(username, scope=None, client_id = None,
        client_secret = None, redirect_uri = None):
    ''' prompts the user to login if necessary and returns
        the user token suitable for use with the spotipy.Spotify
        constructor

        Parameters:

         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app

    '''

    if not client_id:
        client_id = os.getenv('SPOTIPY_CLIENT_ID')

    if not client_secret:
        client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    if not redirect_uri:
        redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

    if not client_id:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

            Get your credentials at
                https://developer.spotify.com/my-applications
        ''')
        raise spotipy.SpotifyException(550, -1, 'no credentials set')

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
        scope=scope, cache_path=".cache-" + username )

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        print('''

            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.

        ''')
        auth_url = sp_oauth.get_authorize_url()
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except:
            print("Please navigate here: %s" % auth_url)

        print()
        print()
        try:
            response = raw_input("Enter the URL you were redirected to: ")
            print(response)
            response = response[:(len(response)-1)]
            print(response)
        except NameError:
            response = input("Enter the URL you were redirected to: ")

        print()
        print()

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None
username='neddann'
scope = 'user-library-read'
token = prompt_for_user_token(username, scope)







print('')
print('')
print('')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Lisa's Mixtape ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('')


test_track = 'kanye west all of the lights'
do_tempo = False
download_songs = False
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
print ('Seed Song -> ',test_track_name)
print ('Target Tempo ->' , target_tempo)
print (' ')

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

    print (track_name,'-',artist_string,' ')
    i += 1
print('')

if do_tempo == True:
    print("Getting Tempo of songs")
    print(image_urls)
    print(est_durations)

    for those in found_keys:
        test_track_data = sp.audio_features(str(those))
        unpacked_track = sp.track(str(those))
        found_albums.append()
        est_durations.append(int((test_track_data[0]['duration_ms'])/1000))
        tempos.append(test_track_data[0]['tempo'])
        #print unpacked_image['images']
        print("NO IMAGE FOUND")

#print(tempos)

print(image_urls)
a = 0
os.chdir('webfiles')
for items in image_urls:
    title = found_titles[a]
    a += 1
    try:
        f = open(title + '_image.jpeg', 'wb')
        f.write(urllib.urlopen(items).read())
        f.close()

    except:
        print('filename error, couldnt write image')





if download_songs == True:
    import youtube_downloader_lucky
    est_time = 0
    os.chdir('songs')
    i = 0
    print("Downloading Songs")
    print("")
    for those in found_youtube_queries:
        spotify_data = {'title':found_titles[i], 'artist':found_artist_names[i], 'album':found_albums[i],'tracknumber':track_numbers[i]}
        youtube_downloader_lucky.download(those,est_durations[i],image_urls[i],spotify_data)
        i += 1
"""

class Song_seeder:

    def __init__(self,tolken=None):
        os.environ["SPOTIPY_CLIENT_ID"] = "e27671f553c6494bbd40bc1abe0b9372"
        os.environ["SPOTIPY_CLIENT_SECRET"] = "a0ca026a4bec439989ebe593df1820f2"
        os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost://callback"


        self.username = 'neddann'
        self.scope = 'user-library-read'
        #self.token = self.prompt_for_user_token(str(self.username), str(self.scope))
        if tolken is not None:
            print('using other token')
            self.token = tolken
        self.sp = spotipy.Spotify(auth=self.token)


        print('')
        print('')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Lisa's Mixtape ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('')
        print('')


        self.do_tempo = False
        self.download_songs = False
        self.cwd = os.getcwd()
    def prompt_for_user_token(username, scope=None, client_id=None,
                              client_secret=None, redirect_uri=None):
        ''' prompts the user to login if necessary and returns
            the user token suitable for use with the spotipy.Spotify
            constructor

            Parameters:

             - username - the Spotify username
             - scope - the desired scope of the request
             - client_id - the client id of your app
             - client_secret - the client secret of your app
             - redirect_uri - the redirect URI of your app

        '''

        if not client_id:
            client_id = os.getenv('SPOTIPY_CLIENT_ID')

        if not client_secret:
            client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

        if not redirect_uri:
            redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

        if not client_id:
            print('''
                You need to set your Spotify API credentials. You can do this by
                setting environment variables like so:

                export SPOTIPY_CLIENT_ID='your-spotify-client-id'
                export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
                export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

                Get your credentials at
                    https://developer.spotify.com/my-applications
            ''')
            raise spotipy.SpotifyException(550, -1, 'no credentials set')

        sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                       scope=scope, cache_path=".cache-" + str(username))

        # try to get a valid token for this user, from the cache,
        # if not in the cache, the create a new (this will send
        # the user to a web page where they can authorize this app)

        token_info = sp_oauth.get_cached_token()

        if not token_info:
            print('''

                User authentication requires interaction with your
                web browser. Once you enter your credentials and
                give authorization, you will be redirected to
                a url.  Paste that url you were directed to to
                complete the authorization.

            ''')
            auth_url = sp_oauth.get_authorize_url()
            try:
                webbrowser.open(auth_url)
                print("Opened %s in your browser" % auth_url)
            except:
                print("Please navigate here: %s" % auth_url)

            print()
            print()
            try:
                response = raw_input("Enter the URL you were redirected to: ")
                print(response)
                response = response[:(len(response) - 1)]
                print(response)
            except NameError:
                response = input("Enter the URL you were redirected to: ")

            print()
            print()
            try:
                code = sp_oauth.parse_response_code(response)
                token_info = sp_oauth.get_access_token(code)
            except:
                token_info = None
        # Auth'ed API request
        if token_info:
            return token_info['access_token']
        else:
            return None

    def write_images(self):
        mydir = 'webfiles/'
        filelist = [f for f in os.listdir(mydir) if f.endswith(".jpeg")]
        for f in filelist:
            os.remove(os.path.join(mydir, f))
        image_urls = self.image_urls
        print(image_urls)
        a = 0
        os.chdir('webfiles')

        for items in self.image_urls:
            title = self.found_titles[a]
            a += 1
            try:
                f = open(title + '_image.jpeg', 'wb')
                f.write(urllib.urlopen(items).read())
                f.close()

            except:
                print('filename error, couldnt write image')

    def clear_images(self):
        mydir = 'webfiles/'
        filelist = [f for f in os.listdir(mydir) if f.endswith(".jpeg")]
        for f in filelist:
            os.remove(os.path.join(mydir, f))


    def write_image(self,index,source=None,title_string=None):

        mydir = self.cwd + '/webfiles/'
        filelist = [f for f in os.listdir(mydir) if f.endswith(".jpeg")]
        image_url = self.image_urls[index]
        if source != None:
            image_url = source
        print(image_url)
        #os.chdir('webfiles')
        title = self.found_titles[index]
        if source != None:
            image_url = source
        if title_string != None:
            title = title_string
        print(mydir + title + '_image.jpeg')
        try:
            f = open(mydir + title + '_image.jpeg', 'wb')
            f.write(urllib.urlopen(image_url).read())
            f.close()
        except:
            print('filename error, couldnt write image')



    def get_from_seed(self,test_track):
        import sys
        # print(sys.argv)
        if len(sys.argv) > 1:
            # print('getting other arguments')
            test_track = sys.argv[1]

        test_track_obj = self.sp.search(test_track, limit=1, type='track')
        test_track_id = test_track_obj['tracks']['items'][0]['id']
        test_track_name = test_track_obj['tracks']['items'][0]['name']
        self.sourced_song = test_track_name
        artist_string = ''
        artist_objs =  test_track_obj['tracks']['items'][0]['artists']
        for those in artist_objs:
            if artist_string != '':
                artist_string = artist_string + ', ' + those['name']
            else:
                artist_string = those['name']
        self.sourced_song_artist = artist_string
        try:
            self.sourced_song_image_url = test_track_obj['tracks']['items'][0]['album']['images'][0]['url']
        except:
            print("NO IMAGE")
            self.sourced_song_image_url = None

        test_track = test_track_id
        test_track_data = self.sp.audio_features(str(test_track))

        target_tempo = int(round(test_track_data[0]['tempo']))
        min_tempo = target_tempo - 5
        max_tempo = target_tempo + 1
        print('Seed Song -> ', test_track_name)
        print('Target Tempo ->', target_tempo)
        print(' ')

        kwargs = {"min_danceability": 0.6, "min_tempo": min_tempo, "max_tempo": max_tempo, "target_tempo": target_tempo,
                  'time_signature': 4}
        results = self.sp.recommendations(seed_tracks=[test_track], limit=20, **kwargs)

        self.tracks = results['tracks']
        self.found_track_names = []
        self.found_artist_names = []
        self.found_youtube_queries = []
        self.image_urls = []
        self.est_durations = []
        self.found_titles = []
        self.found_albums = []
        self.track_numbers = []
        i = 0
        self.found_keys = []
        print("=======================")
        print(" MATCHING SONGS ")
        print("=======================")
        for track_obj in self.tracks:
            track_name = track_obj['name']
            artist_objs = track_obj['artists']
            self.found_titles.append(track_name)
            self.est_durations.append(int((track_obj['duration_ms']) / 1000))
            self.found_albums.append(track_obj['album']['name'])
            self.track_numbers.append(track_obj['track_number'])
            try:
                self.image_urls.append(track_obj['album']['images'][0]['url'])
            except:
                print("NO IMAGE")
                self.image_urls.append(None)
            artist_string = ''
            for those in artist_objs:
                if artist_string != '':
                    artist_string = artist_string + ', ' + those['name']
                else:
                    artist_string = those['name']
            self.found_artist_names.append(artist_string)
            self.found_track_names.append(track_name)
            self.found_keys.append(track_obj['id'])
            self.found_youtube_queries.append(track_name + '-' + artist_string)

            print(track_name, '-', artist_string, ' ')
            i += 1
        print('')

        self.found_titles = self.found_titles
        self.image_urls = self.image_urls
        return self.found_track_names,[0]*len(self.found_titles)
    def download_a_song(self,title,index):
        pass

        song_title = self.found_track_names[index]
        artist_string = self.found_artist_names[index]
        #print('downloading above')
        query = song_title + '-' + artist_string
        found_title = song_title
        found_artist_name = artist_string
        found_album = self.found_albums[index]
        track_number = self.track_numbers[index]
        est_duration = self.est_durations[index]
        image_urls = self.image_urls[index]
        print("Image URLS")
        print(image_urls)
        i = 0
        print("Downloading Songs")
        print("")

        spotify_data = {'title': song_title, 'artist': found_artist_name, 'album': found_album,
                            'tracknumber': track_number}
        youtube_downloader_lucky.download(query, est_duration, image_urls[i], spotify_data)


    def clear(self):
        self.found_titles = []
        self.image_urls = []