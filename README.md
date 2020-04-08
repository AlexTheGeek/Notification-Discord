# Live-notification

It's a program that notify you when a specefic streamer is online.  
It's going to send you a message on your Discord channel and turn on your Philips Hue lights in a specific color.  

# Requirements:
- Discord.py : fint the documentation [here](https://discordpy.readthedocs.io/en/latest/index.html). Installation commmand: ```python3 -m pip install -U discord.py```
- phue : find the [Github project](https://github.com/studioimaginaire/phue). Installation command:  ```sudo pip install phue```

# Fonctions
## Check_user:
This fonction check if the specific streamer is online or not. 
This fonction return 4 different number :  
* 0 : online
* 1 : offline
* 2 : not found
* 3 : error

## Recup_from_twitch:
This function allows you to retrieve the various information that you want to display later.  
In this project, we recover the title of the live and also the game.  

# Credit:
Alexis Brunet : albrunet2000[at]gmail.com
