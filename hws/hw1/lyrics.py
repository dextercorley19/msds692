import sys
from bs4 import BeautifulSoup
import requests
import argparse
import numpy as np
import re


def get_content_soup_from_url(url):
    result = requests.get(url)
    content = result.text
    return BeautifulSoup(content, "lxml")


def clean_text(text):
    """Given a string of text return clean text
    Clean issues with text
    "1. Hola" --> "Hola" 
    "Hola." --> "Hola" 
    "Hola (L)" --> "Hola"
    "Hola (1790)"  --> "Hola"
    "Hola 1790"  --> "Hola"
    """
    # your coode here
    text = re.sub(r'^\d+\.\s*', '', text)
    text = re.sub(r'\s*\([^)]*\)', '', text)
    text = re.sub(r'\s*\d*\.?\s*$', '', text)
    text = text.strip()
    return text

def process_row(row):
    """ Inputs a row of a table and returns the song, album and url

    The input should follow this format:
        <tr valign="bottom">
        <td align="left">
        Ain't No Cure For Love </td>
        <td align="left">
        <a href="album9.html" style="text-decoration:none">I'm Your Man (L)</a> </td>
        </tr>
    Ouputs: three strings, as shown in the example
        "Ain't No Cure For Love", "I'm Your Man", "album9.html"

    To ensure cleanliness and avoid duplicates, the following actions are performed:
      -- remove "(L)"
      -- remove years
    from album names and song names
    """
    # your code here
    
    songs = row.find('td')
    song = songs.get_text(strip=True)
    
    albums = row.find('a')
    album = albums.get_text(strip=True)
    
    link = albums['href']
    
    album = clean_text(album)
    song = clean_text(song)
    return song, album, link


def get_albums():
    """ Scrape album names from 
    "https://www.leonardcohenfiles.com/songind.html"

    Return a list of unique names in alfabetical order
    To ensure cleanliness and avoid duplicates, the following actions are performed:
      -- remove "(L)"
      -- remove years
    """
    # your coode here
    url = "https://www.leonardcohenfiles.com/songind.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    albums = soup.find_all('a')
    h = {}

    for i in range(len(albums)):
        h[clean_text(albums[i].text)] = h.get(albums[i],0)

    h = sorted(h)
    albums = h[2:32]
    return albums
    
    

def get_songs():
    """ Scrape song urls from
    "https://www.leonardcohenfiles.com/songind.html"

    Return a list of unique names in alfabetical order
    Some cleaning to avoid duplicates:
      -- remove "(L)"
    """
     # your coode here
    url = "https://www.leonardcohenfiles.com/songind.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    songs = soup.find_all('td', {'align': 'left'})

    song_titles = []
    for i in songs:
        if not i.find('a'):
            if "Musical, lyrics by Leonard Cohen." not in i.text:
                song_title = clean_text(i.get_text(strip=True))
                song_titles.append(song_title)

    song_titles = set(song_titles)
    song_titles = sorted(song_titles)
    return song_titles

def scrape_lyrics_from_url(song, url):
    """ Given a song and a url return the lyric of the song
    
    Inputs:
       song: string example: "Bird on the Wire"
       url: 'https://www.leonardcohenfiles.com/album2.html'
    
    Return the text of the lyrics:
    
    Like a bird on the wire,
    like a drunk in a midnight choir
    I have tried in my way to be free.
    Like a worm on a hook, 
    ...
    
    """
     # your coode here
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    blocks = soup.find_all('blockquote')
    song_numbers = []
    song_link = ""
    for i in soup.find_all('a', href=True):
        song_numbers.append(i['href'])
        
        if song.lower() in i.text.lower():
            song_link = i['href']
            

    song_link = int(song_link[1:])

    song_numbers = song_numbers[:-4]
    for i,v in enumerate(song_numbers):
        song_numbers[i] = int(song_numbers[i][1:])

    h = {}
    counter = 0
    for i in range(len(song_numbers)):
        h[song_numbers[i]] = counter
        counter += 1

    which_block = h[song_link]
    lyrics = blocks[which_block]
    return str(lyrics)



def get_lyrics(s):
    """ Given an input song scrape and return the lyric
    """
     # your coode here
     

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="Generates a list of songs", action='store_true')
    parser.add_argument("-a", help="Generates a list of albums", action='store_true')
    parser.add_argument("-l", help="Print lyrics for a given song", type=str)
    args = parser.parse_args()
    if args.s:
        songs = get_songs()
        for song in songs:
            print(song)
    if args.a:
        albums = get_albums()
        for a in albums:
            print(a)
    if args.l:
        lyric = get_lyrics(args.l)
        if lyric is None:
            print("No lyric was found")
        else:
            print(lyric)
