"""
Script to create gcloud vm instances that compress videos on youtube using ffmpeg

Useful gcloud commands:

gcloud compute instances create instance-3-4 --project=jadusay --zone=us-central1-a --machine-type=e2-micro --metadata-from-file=startup-script=startup_script.sh
gcloud compute instances delete instance-3-4 --project=jadusay --zone=us-central1-a --quiet
gcloud compute ssh instance-3-4 --project=jadusay --zone=us-central1-a
rsync -Pavz $(gcloud compute instances list --project='jadusay' --filter="name=instance-3-4" --format "get(networkInterfaces[0].accessConfigs[0].natIP)"):video_compression/log ./ && tail log

"""


import os, subprocess


links = [
# "https://youtu.be/3Q64HFJ8whM",
# "https://youtu.be/G2S186Me5MQ",
"https://youtu.be/X3qCBfpCLng",
"https://youtu.be/yDJHfonI1Xw",
"https://youtu.be/0Edl3zydN94",
"https://youtu.be/QZh_X8RBQVE",
"https://youtu.be/W_GMwLLxtMo",
"https://youtu.be/bNFeLCKYsqM",
"https://youtu.be/o1PuNMly8nI",
"https://youtu.be/VPfXA2aV2dM",
"https://youtu.be/b1CYGENds0o",
]

startup_script = '\
#!/bin/bash\n\
apt update\n\
apt -y install python3-pip\n\
apt -y install rsync\n\
apt -y install ffmpeg\n\
apt -y install git\n\
git clone https://github.com/physicsinstyleofvivek/video_compression.git /home/mayank/video_compression\n\
cd /home/mayank/video_compression\n\
pip3 install -r requirements.txt --no-cache-dir\n\
python3 youtube_download.py . {link}\n\
python3 compress.py . > log 2>&1 < /dev/null'

cmd = 'gcloud compute instances create \
        {instance} --project=jadusay --zone=us-central1-a --machine-type=e2-micro \
        --metadata=startup-script="{startup_script}"'

n=7
for link in links:
    instance = f'instance-3-{n}'
    cmd_ = cmd.format(instance=instance, startup_script=startup_script.format(link=link))
    subprocess.run(cmd_, shell=True).check_returncode()
    n+=1