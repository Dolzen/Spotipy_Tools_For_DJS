from __future__ import unicode_literals
import youtube_dl
from os import listdir
from os.path import isfile, join
import subprocess
from timeit import default_timer as timer
start = timer()
import os
import shutil
import urllib
import urllib2
from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK


#textToSearch = 'control movement'

def get_sec(time_str):
    m, s = time_str.split(':')
    return  int(m) * 60 + int(s)


def search_youtube(string):
    query = urllib.quote(string)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup



def download(textToSearch,est_time,image_url,spotify_data):
    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    def my_hook(d):
        if d['status'] == 'finished':
            #print('Done downloading, now converting ...')
            pass

    def absoluteFilePaths(directory):
        paths = []
        for root, dirs, files in os.walk(os.path.abspath("../path/to/dir/")):
            for file in files:
                #print(os.path.join(root, file))
                paths.append( os.path.join(root, file))
        return paths


    soup = search_youtube(textToSearch)
    vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    times = soup.findAll(attrs={'class':"video-time"})

    #for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #    pass
        #print vid['title']

    i = 0
    found_appropriate_video = False
    while found_appropriate_video == False:
        title = vids[i]['title']
        lower_title = title.lower()
        found_appropriate_video = True
        if "official music video" in title or 'official video' in lower_title:
            print("FOUND OFFICIAL MUSIC VIDEO")
            # Recursive call, String now excludes music video phrase
            found_appropriate_video = False
            i += 1
        time_string = str(times[i].next)
        if len(time_string) <= 5:

            print(time_string)
            run_time = get_sec(time_string)
            # print "Time  of vid is: ",   run_time
            # print "Estimated Time is: ", est_time

            difference = int(run_time) - int(est_time)
            if difference < 0:
                difference = difference * -1
            if difference > 60:
                #print("THIS VIDEO IS NOT THE RIGHT LENGTH")
                #print(difference,run_time,est_time)
                #return
                i += 1
                found_appropriate_video = False
        else:
            i += 1
    di = i
    print "Name of video I'm downloading is: ",title
    i = 0

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    cwd = os.getcwd()
    current_dir = cwd
    title = title.replace('"', "'")
    vid_path = 'https://www.youtube.com' + vids[di]['href']
    onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]

    if title +'.mp3' not in onlyfiles:
        if not os.path.isdir('tmp'):
            os.mkdir('tmp')
        os.chdir('tmp')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_path])
        try:
            f = open(title+'_image.jpeg', 'wb')
            f.write(urllib.urlopen(image_url).read())
            f.close()
        except:
            print('filename error, couldnt write image')

        audio = MP3(title+'.mp3', ID3=ID3)

        # add ID3 tag if it doesn't exist
        try:
            audio.add_tags()
        except error:
            pass
        tmp_files = [f for f in listdir(cwd+'/tmp') if isfile(join(cwd+'/tmp', f))]

        for l in range(0,len(tmp_files)):
            print(tmp_files[l])
            print('.jpeg'in tmp_files[l])
            if '.jpeg'in tmp_files[l]:
                image_path = tmp_files[l]
        audio.tags.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime='image/png',  # image/jpeg or image/png
                type=3,  # 3 is for the cover image
                desc=u'Cover',
                data=open(image_path).read()
            )
        )
        audio.save()
        try:
            audio = EasyID3(title+'.mp3')
        except:
            pass
            print("PROBLEM")
        try:
            #print(spotify_data['tracknumber'])
            audio['tracknumber'] = int(spotify_data['tracknumber'])
        except:
            pass
            #print "Couldn't Insert tracknumber"
        audio['artist']     = spotify_data['artist']
        audio['title']      = spotify_data['title']
        audio['album']      = spotify_data['album']
        try:
            audio['tempo']   = spotify_data["tempo"]
        except:
            pass
        audio.save()
        os.remove(image_path)

        try:
            tags = ID3(title+'.mp3')
            tags['TRCK'] =  TRCK(encoding=3, text=str(spotify_data['tracknumber']))
        except ID3NoHeaderError:
            print "Adding ID3 header;",
            tags = ID3()
        tags.save()
        print(cwd + '/tmp/'+ title+'.mp3')
        os.rename(current_dir+'/tmp/' +title + '.mp3',current_dir+title+ '.mp3' )
        os.chdir(current_dir)
