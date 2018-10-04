# imports
from __future__ import unicode_literals
from bs4 import *
import urllib.request
import os
import youtube_dl
from os.path import expanduser

#code starts here
#downloader
def down(sname):
	ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '320',}],}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:	ydl.download([sname])

# main func
def main():
	sname = input("enter song name(followed by artist name for better resolution)")
	url = "https://www.youtube.com/results?search_query="+sname.replace(" ", "+")
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'html.parser')
	res=soup.find_all('a',{'class':'pl-video-title-link'})
	l=[]
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		l.append('https://www.youtube.com' + vid['href'])
	down(l[1])																	#downloading most appropriate song
	home = expanduser("~")
	#if (not os.path.exists(home + "/Downloads/Music")):
	#	dir =  home + "/Downloads/Music"
	#	os.system(("mkdir %s",%dir))
	#os.system("mv *.mp3 home + "/Downloads/Music")

	  
if __name__ == '__main__':
	main()
