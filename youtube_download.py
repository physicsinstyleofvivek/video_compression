"""
Downloads highest resolution youtube video from the given links

Usage: python3 youtube_download.py <path>
"""

from pytube import YouTube 
import os, sys


path = sys.argv[1]

links=[
'https://youtu.be/9zODiE6Qjts',
'https://youtu.be/pdFXovEXdZk',
'https://youtu.be/3Q64HFJ8whM',
'https://youtu.be/G2S186Me5MQ',
'https://youtu.be/X3qCBfpCLng',
'https://youtu.be/yDJHfonI1Xw',
'https://youtu.be/0Edl3zydN94',
'https://youtu.be/QZh_X8RBQVE',
'https://youtu.be/W_GMwLLxtMo',
'https://youtu.be/bNFeLCKYsqM',
'https://youtu.be/o1PuNMly8nI',
'https://youtu.be/VPfXA2aV2dM',
'https://youtu.be/b1CYGENds0o',
]

# download
for i,link in enumerate(links): 
    
    YouTube(link).streams.filter(progressive=True, file_extension='mp4') \
    .order_by('resolution') \
    .desc() \
    .first().download(path) \
    
    print(f'Downloaded {i}') 