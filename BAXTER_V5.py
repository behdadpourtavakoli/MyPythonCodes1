#-------------------------------------------------------------------------------------
#                                  Imports
#-------------------------------------------------------------------------------------
import json
import random
import datetime
import operator
import os
import subprocess
import time
import sys
from unittest import result
import webbrowser
import requests
from bs4 import BeautifulSoup
import wikipedia
import wolframalpha
import pywhatkit
import threading

from BX_Intents import (greetings, farewell, thanks, noAnswer, youChoose)
from BX_External_Functions import (autoTypeAnimation, StartupText, ShutdownText, 
                                    UserInput, listen, speak, getRandomJoke, getFunFacts,
                                    setReminders, terminateTimers)
 
from pairs import chat
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#                           Commander Name (You) and A.I Name
#-------------------------------------------------------------------------------------
Commander = "Commander"
AI_Name = 'Baxter'
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                  WishMe Function
#-------------------------------------------------------------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + Commander)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + Commander)   
    else:
        speak("Good Evening" + Commander) 
#-------------------------------------------------------------------------------------
 
 
#-------------------------------------------------------------------------------------
#                                       Main
#-------------------------------------------------------------------------------------
def BAXTER():
    command = UserInput()
    command=str(command).lower()
 
    #-------------------------------------------------------------------------------------
    #                       General Conversation (From Intents.py) 
    #-------------------------------------------------------------------------------------
    #Greetings
    patterns, responses = greetings()
    if (command in patterns):
        results = (random.choice(responses))
        autoTypeAnimation(results)
        speak(results)
 
    #Farewell
    patterns, responses = farewell()
    if (command in patterns):
        results = (random.choice(responses))
        autoTypeAnimation(results)
        speak(results)
     
    #Thanks
    patterns, responses = thanks()
    if (command in patterns):
        results = (random.choice(responses))
        autoTypeAnimation(results)
        speak(results)
     
    #No Response
    patterns, responses = noAnswer()
    if (command in patterns):
        results = (random.choice(responses))
        autoTypeAnimation(results)
        speak(results)
 
    #-------------------------
    #       Tell a Joke
    #-------------------------
    if ('joke' in command):
        joke = getRandomJoke()
        autoTypeAnimation(joke)
        speak(joke)
    #-------------------------
    #-------------------------
    #     Tell a Fun Fact
    #-------------------------
    if ('fact' in command):
        funFact = getFunFacts()
        autoTypeAnimation(funFact)
        speak(funFact)
    #-------------------------
     
    #-------------------------------------------------------------------------------------
    #                       Search Wikipedia (General Info)
    #-------------------------------------------------------------------------------------
    if ('weather' not in command):
        if ('who is' in command) or ('what is the' in command) or ('what is a' in command) or ("what is" in command):
            if ('time' not in command):
                if ('news' not in command):
                    speak('Searching...')
                    command = command.replace("who is","")
                    command = command.replace("what is the","")
                    command = command.replace("what is a","")
                    command = command.replace("what is","")
                    results = wikipedia.summary(command, sentences = 2)
                    autoTypeAnimation(results)
                    speak(results) 
                     
    #-------------------------------------------------------------------------------------
    #               Search Wolfram Alpha (Math/Conversions, Definitions)
    #-------------------------------------------------------------------------------------
    if ('news' not in command):
        if ('weather' in command) or ('calculate' in command) or ("what's" in command) or ('define' in command) or ("what" in command):
                speak('Searching...')
                command = command.replace("calculate","")
                command = command.replace("what's","")
                command = command.replace("define","")
                # Wolframalpha App Id
                appId = 'JH9XHR-W9J76L7H5A'
                # Wolfram Instance
                client = wolframalpha.Client(appId)
                res = client.query(''.join(command))
                results = next(res.results).text
                autoTypeAnimation(results)
                speak(results)
 
    #-------------------------------------------------------------------------------------
    #                       Open Stuff on the Internet
    #-------------------------------------------------------------------------------------
    #Open Youtube Videos (Ex: 'Play __ on youtube')
    if ('youtube' in command):
        autoTypeAnimation("Launching Youtube...")
        speak('Launching Youtube')
        command = command.replace("youtube","")
        pywhatkit.playonyt(command)
 
    #Open Google Maps and Find The Location of A You Want
    if ('where is' in command):
        command = command.replace("where is","")
        autoTypeAnimation("Locating" + command + "...")
        speak('Locating' + command)
        webbrowser.open_new_tab("https://www.google.com/maps/place/" + command)
 
    #Search Stuff on Google
    if ('search' in command):
        command = command.replace("search", "")
        autoTypeAnimation("Searching" + command + " on Google")
        speak('Searching' + command)
        pywhatkit.search(command)
     
    #Close Firefox
    if ('close firefox' in command):
        autoTypeAnimation("Terminating Firefox...")
        speak('Closing Firefox')
        command = command.replace("close firefox", "")
        browser = "firefox.exe"
        os.system("taskkill /f /im " + browser)   
 
    #-------------------------------------------------------------------------------------
    #                       Open Stuff on the Computer
    #-------------------------------------------------------------------------------------
    #Open Windows Media Player and Auto Play the Playlist Called Music
    if ('play music' in command) or ('media player' in command) or ('drop the needle' in command):
        autoTypeAnimation("Launching music...")
        speak("Launching Music")
        command = command.replace("play music", "")
        command = command.replace("media player", "")
        command = command.replace("drop the needle", "") 
        subprocess.Popen("C:\Program Files (x86)\Windows Media Player\wmplayer.exe /Playlist Music")
 
    #Close Windows Media Player
    if ('stop music' in command):
        autoTypeAnimation("Terminating music...")
        speak('Closing Music')
        command = command.replace("stop music", "")
        mediaPlayer = "wmplayer.exe"
        os.system("taskkill /f /im " + mediaPlayer)   
 
    #-------------------------------------------------------------------------------------
    #                               Set Reminders
    #-------------------------------------------------------------------------------------
    if ('remind me' in command):
        command = command.replace("remind me", "")
        setReminders(command) #Call setReminders() from External Functions
     
    #-------------------------------------------------------------------------------------
    #                       Stop Program/Script Command
    #-------------------------------------------------------------------------------------
    if ('stop' in command) or ('shutdown' in command) or ('quit' in command):
        speak("Shutting Down...")
        results = "Terminating program..."
        autoTypeAnimation(results)
        ShutdownText()
        terminateTimers()
        exit()
    #-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
       
 
#------------------------------------------------------------------------------------------
#                                   Run The Program
#------------------------------------------------------------------------------------------
StartupText()
wishMe()
speak("How may I be of service?") 
 
while True:
    BAXTER()
#------------------------------------------------------------------------------------------
