#!/usr/bin/env python3
import datetime
import json
import time
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

WEBHOOK_ID_LIVE = ""
WEBHOOK_TOKEN_LIVE = ""

WEBHOOK_ID_VOD = ""
WEBHOOK_TOKEN_VOD = ""

# Upload image to server
#webhook.send(file=discord.File("latest_img.jpg"))

# global configuration
client_id = ""  # don't change this
# get oauth token value by typing `streamlink --twitch-oauth-authenticate` in terminal
oauth_token = ""
refresh = 5.0
# user configuration
username = ""
last_status = 1


def check_user():
    # 0: online,
    # 1: offline,
    # 2: not found,
    # 3: error
    url = 'https://api.twitch.tv/kraken/streams/' + username
    info = None
    status = 1
    try:
        r = requests.get(url, headers={"Client-ID": client_id}, timeout=15)
        r.raise_for_status()
        info = r.json()
        if info['stream'] == None:
            status = 1
        else:
            status = 0
    except requests.exceptions.RequestException as e:
        if e.response:
            if e.response.reason == 'Not Found' or e.response.reason == 'Unprocessable Entity':
                status = 2
    return status


while True:
    status = check_user()
    if status == 2:
        print("Channel not found")
        last_status = 2
        time.sleep(refresh)
    elif status == 3:
        print(datetime.datetime.now().strftime("%Hh%Mm%Ss"), " ","Erreur, nous retentons dans 5 minutes.")
        last_status = 3
        time.sleep(300)
    elif (status == 1) & (last_status != 1):
        print(username, "Hors ligne, vérification dans", refresh, "seconds.")
        webhook = Webhook.partial(WEBHOOK_ID_VOD, WEBHOOK_TOKEN_VOD, adapter=RequestsWebhookAdapter())
        webhook.send("Le live est terminé, retrouvez les lives à : https://twitch.tv//videos")
        last_status = 1
        time.sleep(refresh)
    elif (status == 0) & (last_status != 0):
        print(username, "Online")
        last_status = 0
        webhook = Webhook.partial(WEBHOOK_ID_LIVE, WEBHOOK_TOKEN_LIVE,adapter=RequestsWebhookAdapter())
        webhook.send("Live en cours : https://twitch.tv/")
        time.sleep(refresh)
