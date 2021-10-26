"""Usage:
    nohup python3 compress.py <mp4dir>  > log 2>&1 < /dev/null &
"""

import os, glob, subprocess
import numpy as np
import sys

print(os.system('tree'))

path = sys.argv[1]

os.chdir(path)
if not os.path.isdir('compressed'):
    os.mkdir('compressed')

for file_ in np.sort(glob.glob('*.mp4')):
    infile = file_.replace(' ', '\ ')
    outfile = f'compressed/{infile}'
    if os.path.isfile(outfile):
        continue
    cmd = f'ffmpeg -i {infile} -c:v libx265 -crf 34 -preset veryslow -tag:v hvc1 -c:a aac {outfile}'
    subprocess.run(cmd, shell=True).check_returncode()






