#!/bin/bash

# Useful gcloud commands:
# gcloud compute instances create instance-3-4 --project=jadusay --zone=us-central1-a --machine-type=e2-micro --metadata-from-file=startup-script=startup_script.sh
# gcloud compute instances delete instance-3-4 --project=jadusay --zone=us-central1-a --quiet
# gcloud compute ssh instance-3-4 --project=jadusay --zone=us-central1-a
# rsync -Pavz $(gcloud compute instances list --project='jadusay' --filter="name=instance-3-4" --format "get(networkInterfaces[0].accessConfigs[0].natIP)"):video_compression/log ./ && tail log

apt update
apt -y install python3-pip
apt -y install rsync
apt -y install ffmpeg
apt -y install git


git clone https://github.com/physicsinstyleofvivek/video_compression.git /home/mayank/video_compression

cd /home/mayank/video_compression

pip3 install -r requirements.txt --no-cache-dir

python3 youtube_download.py . "https://youtu.be/pdFXovEXdZk"

python3 compress.py . > log 2>&1 < /dev/null

printf 'startup-script completed'


