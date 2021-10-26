"""
Downloads highest resolution youtube video from the given links

Usage: python3 youtube_download.py <path>
"""

from pytube import YouTube 
import os, sys


path = sys.argv[1]
link = sys.argv[2]
links=[
link
]

# download
for i,link in enumerate(links): 
    
    YouTube(link).streams.filter(progressive=True, file_extension='mp4') \
    .order_by('resolution') \
    .desc() \
    .first().download(path) \
    
    print(f'Downloaded {i}') 