# Hotel Cast
A Chromecast alternative that works on hotel WiFi.  
[Live Demo](https://gsiders.app/demo)
## Why?? 
Since I travel for work I never can use my chromecast since most hotel networks isolate clients or require a sign in page. Both of these cause the chromecast not to work. So I took it into my own hands to write and application to fix this. Yes I could have just bought a travel router or a Roku, but I like a good challenge!

I normally just plug my laptop into the TV and watch whatever I need. That is fine and all but playing, pausing, changing videos requires me to get up and interact with my computer. I tried using TeamViewer on my phone to control it but it just didn't work well. So I took things into my own hands and wrote an app I call it HotelCast!


## How it works: 
It consists of three parts:

#### CLIENT:

- Client uses a front facing web app that servers as control for the local server.
- Client selects the show/movie/Youtube video they want to watch the link is written to the command file 

#### CLOUD SERVER: 
- Serves frontend
- Servers and hosts the command file of what to "cast" (play) on local computer
- Django webapp

#### Local Server: 

- Local server pulls from the cloud server the commands to run via a python script. 
- The script is constantly querying the cloud server for changes to the command file.
### EXAMPLE:

#### Client:
- Client selects a episode of a show on netflix (pakrs and rec, season 1, episode 7)
- WebApp writes to cloud server file (command.txt) the direct URL to play (the Netflix video)
#### Cloud Server :
- Serves command file containing Netflix watch URL (command.txt)
#### Local server:
- Using python I query the cloud server for the command.txt(command.txt)
- I then use python to play the url (doesn't matter if its netflix, hulu, youtube, ect) in chrome (Selenium ChromeDriver) in full screen
## Requirements
- Python 2.7 
- Django 1.11.16
- [Guidebox](http://guidebox.com)
- Python Requests 
- Selnium

## About
Idea and code was writen by: 
[Grant Siders](http://grantsiders.com). Feel free to contriube by forking the repo and opening a pull request! 

