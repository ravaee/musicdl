import urllib2 
from bs4 import BeautifulSoup
import string
import os
import subprocess
import random
import pytube

def file_read(file):
        content_array = []
        with open(file) as txt:
                for line in txt:
                        content_array.append(line)
                return content_array


def make_query(names):
    quesries = []
    for name in names:
         if any(char.isalpha() or char.isdigit() for char in name):
            quesries.append('https://www.youtube.com/results?search_query=' + string.replace(name, ' ', '+'))
        
    return quesries


def fetch_url(queries):
    urls = []
    for query in queries:
        url = query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        vid = 'https://www.youtube.com' + soup.find(attrs={'class':'yt-uix-tile-link'})['href']
        urls.append(vid)
    return urls


def download(urls,names):
    found = False
    for index , url in enumerate(urls):
        print("seraching to find " + names[index])
        yt = pytube.YouTube(url)
        vids = yt.streams.all()
        for i in range(len(vids)):
            if "audio/mp4" in str(vids[i]):
                vnum = i
                found = True
        if found == True:
            print names[index] + " has found and start downloading ..."
            found = False 
            if not os.path.exists("downloads"):
                os.makedirs("downloads")
            parent_dir = "downloads"
            vids[vnum].download(parent_dir)
            print names[index] + " has downloaded and saved on 'DOWNLOAD' folder in root"
        else:
            print names[index] + " not found trying others ..."







print("================================================================================ \n\n")
print(" __  __       _                               _   ____                       _")
print("|  \/  | ___ | |__   __ _ _ __ ___   __ _  __| | |  _ \ __ ___   ____ _  ___(_)")
print("| |\/| |/ _ \| '_ \ / _` | '_ ` _ \ / _` |/ _` | | |_) / _` \ \ / / _` |/ _ \ |")
print("| |  | | (_) | | | | (_| | | | | | | (_| | (_| | |  _ < (_| |\ V / (_| |  __/ |")
print("|_|  |_|\___/|_| |_|\__,_|_| |_| |_|\__,_|\__,_| |_| \_\__,_| \_/ \__,_|\___|_|")
print("\n \n")
print("Email : ravaeimohamad@gmail.com")
print("Instagram : https://www.instagram.com/mohamad_ravaei/")
print("linkedin : https://www.linkedin.com/in/mohamad-ravaei-4abb45106/")
print("faceBook : https://www.facebook.com/mohamad.ravaei.5 \n\n")
print("================================================================================ \n\n")

print("__ Starting fething information and searching your goals please wait a moment __  " )

names = file_read('selection.txt')
queries = make_query(names)
urls = fetch_url(queries)
download(urls,names)

