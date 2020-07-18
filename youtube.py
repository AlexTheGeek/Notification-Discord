import json
import time
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

#Discord configurtion
WEBHOOK_ID = ""
WEBHOOK_TOKEN = ""

#Google/YouTube configuration
api_key = ""
channel_id = ""
id_before = None

try:
    while True:
        base_video_url = 'https://www.youtube.com/watch?v='
        search_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId="+channel_id+"&maxResults=1&order=date&key="+api_key
        info = None
        r = requests.get(search_url, timeout=15)
        r.raise_for_status()
        info = r.json()
        if info == None:
            print('Error')
            time.sleep(900)
        else:
            item = info['items']
            item_u = item[0]
            identifiant = item_u['id']
            video_id = identifiant['videoId']
            print(video_id)
            if video_id != id_before:
                print('send')
                id_before = video_id
                webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
                webhook.send("Nouvelle vidéo sur Youtube ! \n"+base_video_url+video_id)
            else:
                print('not send')
        time.sleep(900)
except KeyboardInterrupt:
    print('Stop')
