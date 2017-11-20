from __future__ import unicode_literals
import youtube_dl
from os import listdir
from os.path import isfile, join
import subprocess
from timeit import default_timer as timer
start = timer()
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

base_url = "https://www.1001tracklists.com"
test_song = '/track/9hj8kbp/zhu-faded/index.html'
original_song_string ='ZHU - Faded'
tracklist_max = 3
tracklist_query = {'class':'tlInfo'}

def absoluteFilePaths(directory):
    paths = []
    for root, dirs, files in os.walk(os.path.abspath("../path/to/dir/")):
        for file in files:
            #print(os.path.join(root, file))
            paths.append( os.path.join(root, file))
    return paths


def get_soup(url,attrs):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    tracklists = soup.findAll(attrs=attrs)
    return tracklists


song_tracklist_obj = get_soup(base_url+test_song,tracklist_query)

tracklist_urls = []
tracklist_titles = []
i = 0
for tracklist in song_tracklist_obj:

    if i > tracklist_max:
        break
    tlLink = tracklist.contents[1]
    title = tlLink.contents[1].contents[0]
    url = base_url+ tlLink.contents[1].attrs['href']
    tracklist_titles.append(title)
    tracklist_urls.append(url)
    #print 'title',title
    #print 'url',url
    #url = tlLink.contents[]
    #print('')
    #print vid['hre
    #print vid
    i += 1




recommended_songs = []
for i in range(0,len(tracklist_urls)):
    test_track_list_url   = tracklist_urls[i]
    test_track_list_title = tracklist_titles[i]
    print "Checking Tracklist",test_track_list_title
    print('========================')
    #print test_track_list_title, test_track_list_url

    song_query = {'class':'tlToogleData'}
    current_tracklist_obj = get_soup(test_track_list_url,attrs=song_query)


    target_song_number = 0
    for song_objs in current_tracklist_obj:
        song_innards = song_objs.contents[1]
        if 'content' in song_innards.attrs:
            title = song_innards.attrs['content']
            #print title, original_song_string
            #print(title==original_song_string)
            if title == original_song_string:
                print "Song was number   -> ",target_song_number + 1,'       ',original_song_string
                if target_song_number != len(song_objs)-1:
                    if 'content' in current_tracklist_obj[target_song_number+1].contents[1].attrs:
                        next_song = current_tracklist_obj[target_song_number+1].contents[1].attrs['content']
                    else:
                        next_song = None
                print"Previous song     ->            ",previous_song
                print'Next song         ->            ',next_song
                if previous_song is not None:
                    recommended_songs.append(previous_song)
                if next_song is not None:
                    recommended_songs.append(next_song)
        if target_song_number != 0:
            previous_song = title
        else:
            previous_song = None
        target_song_number += 1
    print('')
    print('')


for those in recommended_songs:
    print(those)