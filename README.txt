README

The git contains a couple scripts I made for downloading songs from my Spotify account. The songs are downloaded from youtube.

The git is inspired by the functionality of DJay Pro and its song matching feature that uses the Spotify API.


The best way to use these tools is to run the "User Interface.py" script from the command line or your IDE. This launches a Tk applet where you can create a list of songs with BPMs that match the seed and have similar variables such as BPM genre etc.

Select the image tiles to mark them for download. Click the download button and once the app is done it will open the folder where the files are saved.

The youtube downloader is not perfect. If the song is not on youtube it will still download something based on its logic.

Logic of the youtube downloader takes into account duration, 'official music video' and similar strings and some other exclusion variables such as "how to" and "review" in the title.

It would be nice to see some other people good with UI dev to work on this git. All of the code here is based on tutorials found online and isn't very advanced at all. I'd also like to add the ability to download playlists and stream snippets of the  songs from within the app itself. 

To use these scripts you need

A Spotify Developer account and token
python 2.7
Spotipy
Youtube-dl 
Mutagen
Beautiful soup

Change the token to your Spotify developer token in Lisas mixtape to download a playlist from youtube.

The script is initialised to test the accuracy of the playlist generator compared to Djay Pro. 