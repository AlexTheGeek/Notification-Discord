#!/usr/bin/env python3
import json
import time
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

#Discord configuration
WEBHOOK_ID = ""
WEBHOOK_TOKEN = ""

# global configuration
client_id = ""
oauth_token = ""

# user configuration
username = ""
user_id = ""


refresh = 15
last_status = 1 #set the first status to offline when the script start


def check_user():
    url = 'https://api.twitch.tv/helix/streams?user_id='+user_id
    info = None
    status = 1
    try:
        r = requests.get(url, headers={"Client-ID": client_id, "Authorization": oauth_token}, timeout=15)
        r.raise_for_status()
        info = r.json()
        if info['data'] == []:
            status = 1 #the streamer is offline
        else:
            status = 0 #the streamer is online
    except requests.exceptions.RequestException as e:
        if e.response:
            if e.response.reason == 'Not Found' or e.response.reason == 'Unprocessable Entity':
                status = 2 #the streamer is not found
    return status

def recup_from_twitch():
    url = 'https://api.twitch.tv/helix/streams?user_id='+user_id
    try:
        r = requests.get(url, headers={"Client-ID": client_id, "Authorization": oauth_token}, timeout=15)
        r.raise_for_status()
        info = r.json()
        tab = [" ", " ", "0"]
        stream = info['data']
        channel = stream[0]
    except:
        print('Error')
        tab[2] = 3
        return tab
    tab[0] = channel['title'] #Get the title of the live.
    #Get the id of the game that is playing during the live.
    m = requests.get('https://api.twitch.tv/helix/games?id='+channel['game_id'], headers={"Client-ID": client_id, "Authorization": oauth_token}, timeout=15)
    m.raise_for_status()
    game = m.json()
    game_data = game['data']
    game_data_data = game_data[0]
    tab[1] = game_data_data['name'] #Get the name of the game that appear on the Twitch live.
    return tab

while True:
    status = check_user()
    if status == 2:
        #print(username+"est une chaine non trouvee")
        last_status = 2
        time.sleep(refresh)
    elif status == 3:
        #print("Erreur, nous retentons dans 15 seoncdes.")
        last_status = 3
        time.sleep(refresh)
    elif (status == 1):
        #print(username, "Hors ligne, verification dans", refresh, "seconds.")
        last_status = 1
        time.sleep(refresh)
    elif (status == 0) & (last_status != 0):
        #print(username, "En ligne")
        valeur = recup_from_twitch()
        if valeur[2] == 3:
            last_status = 3
            time.sleep(refresh)
        else:
            webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
            webhook.send("Live en cours : https://twitch.tv/"+username +"\nTitre du live : "+valeur[0]+"\nJeu : "+valeur[1])
            last_status = 0
            #print("Message envoye")
            time.sleep(refresh)
