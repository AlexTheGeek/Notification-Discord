# Notification Discord
There are 2 script, the first one is to know when a streamer is online and the second one is to know the last video of any YouTuber. This 2 script send notification to a specific channel of a Discord Server with a Webhooks.

## Requirements:
- Discord.py : fint the documentation [here](https://discordpy.readthedocs.io/en/latest/index.html). Installation commmand: ```python3 -m pip install -U discord.py```
- phue : find the [Github project](https://github.com/studioimaginaire/phue). Installation command:  ```sudo pip install phue```
- you need to create a webhook on a channel of your Discord Server. When you are going to generate a new webhook your are going to have a url to call the webhook ressembling https://discordapp.com/api/webhooks/999999999999999999/XXXXXXXXXXXXXXXXXXXX. The part of 9 referes to the variable WEBHOOK_ID and the part of X referes to the variable WEBHOOK_TOKEN.

## Twitch
It's a program that notify you when a specefic streamer is online.  
It's going to send you a message on your Discord channel and turn on your Philips Hue lights in a specific color.  
With the new api of Twitch we need to find the ID of the channel.

### Fonctions:
#### Check_user:
This fonction check if the specific streamer is online or not. 
This fonction return 4 different number :  
* 0 : online
* 1 : offline
* 2 : not found
* 3 : error

#### Recup_from_twitch:
This function allows you to retrieve the various information that you want to display later.  
In this project, we recover the title of the live and also the game.  

## Youtube
This script send a notification, when a new video has been published on YouTube.  
You need an API key from the [Google Console](https://console.developers.google.com/), add to the library of the API the YouTube Data API v3.  
And the ID of the YouTuber, you find it in the channel url. (e.g. https://www.youtube.com/channel/UCgijyWr61vIBPN-9ILflszA, the id is UCgijyWr61vIBPN-9ILflszA)

## Credit:
Alexis Brunet : alexbrcontact[at]gmail.com
