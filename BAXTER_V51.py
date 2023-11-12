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
import sched
import webbrowser
import requests
from bs4 import BeautifulSoup
import wikipedia
import wolframalpha
 
 
from BX_Intents import (greetings, farewell, thanks, noAnswer, youChoose)
from BX_External_Functions import (autoTypeAnimation, StartupText, ShutdownText, 
                                    UserInput, listen, speak, getRandomJoke, getFunFacts,
                                    setReminders, setTodo, terminateTimers, sendEmail,
                                    wishMe, setRenewal, ErrorMsg, offlineWarningMsg,
                                    schedule_reminder)
 
# Print a warning msg if there is no internet to prevent pywhatkit 
# from crashing the program due to no connection 
try:
    import pywhatkit
except:
    offlineWarningMsg()
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
        try:
            joke = getRandomJoke()
            autoTypeAnimation(joke)
            speak(joke)
        except:
            ErrorMsg("get", "jokes")
    #-------------------------
    #-------------------------
    #     Tell a Fun Fact
    #-------------------------
    if ('fact' in command):
        try:
            funFact = getFunFacts()
            autoTypeAnimation(funFact)
            speak(funFact)
        except:
            ErrorMsg("get", "fun facts")
    #-------------------------
     
    #-------------------------------------------------------------------------------------
    #                       Search Wikipedia (General Info)
    #-------------------------------------------------------------------------------------
    if ('weather' not in command):
        if ('who is' in command) or ('what is the' in command) or ('what is a' in command) or ("what is" in command):
            if ('time' not in command):
                if ('news' not in command):
                    autoTypeAnimation('Searching Wikipedia...')
                    speak('Searching...')
                    command = command.replace("who is","")
                    command = command.replace("what is the","")
                    command = command.replace("what is a","")
                    command = command.replace("what is","")
                    try:
                        results = wikipedia.summary(command, sentences = 2)
                        autoTypeAnimation(results)
                        speak(results) 
                    except:
                        ErrorMsg("connect to", "Wikipedia")
                     
    #-------------------------------------------------------------------------------------
    #               Search Wolfram Alpha (Math/Conversions, Definitions)
    #-------------------------------------------------------------------------------------
    if ('news' not in command):
        if ('weather' in command) or ('calculate' in command) or ("what's" in command) or ('define' in command) or ("what" in command):
                autoTypeAnimation('Searching Wolfram Alpha...')
                speak('Searching...')
                command = command.replace("calculate","")
                command = command.replace("what's","")
                command = command.replace("define","")
                # Wolframalpha App Id
                appId = 'JH9XHR-W9J76L7H5A'
                try:
                    # Wolfram Instance
                    client = wolframalpha.Client(appId)
                    res = client.query(''.join(command))
                    results = next(res.results).text
                    autoTypeAnimation(results)
                    speak(results)
                except:
                    ErrorMsg("connect to", "Wolfram Alpha database")
 
    #-------------------------------------------------------------------------------------
    #                       Open Stuff on the Internet
    #-------------------------------------------------------------------------------------
    #Open Youtube Videos (Ex: 'Play __ on youtube')
    if ('youtube' in command):
        autoTypeAnimation("Launching Youtube...")
        speak('Launching Youtube')
        command = command.replace("youtube","")
        try:
            pywhatkit.playonyt(command)
        except:
            ErrorMsg("connect to", "Youtube")
 
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
        try:
            pywhatkit.search(command)
        except:
            ErrorMsg("connect to" , "Google")
     
    #Close Firefox
    if ('close firefox' in command):
        autoTypeAnimation("Terminating Firefox...")
        speak('Closing Firefox')
        command = command.replace("close firefox", "")
        browser = "firefox.exe"
        try:
            os.system("taskkill /f /im " + browser)   
        except:
            ErrorMsg("close", "Firefox")
 
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
        try: 
            subprocess.Popen("C:\Program Files (x86)\Windows Media Player\wmplayer.exe /Playlist Music")
        except:
            ErrorMsg("open","Windows Media Player")
 
    #Close Windows Media Player
    if ('stop music' in command):
        autoTypeAnimation("Terminating music...")
        speak('Closing Music')
        command = command.replace("stop music", "")
        mediaPlayer = "wmplayer.exe"
        try:
            os.system("taskkill /f /im " + mediaPlayer)
        except:
            ErrorMsg("close", "Windows Media Player")
 
    #-------------------------------------------------------------------------------------
    #                         Set Reminders & Renewals
    #-------------------------------------------------------------------------------------
    if ('remind me' in command) or ('reminder' in command) or ('renew' in command):
        command = command.replace("remind me to", "")
        #If renew is mentioned in the command call the setRenewal Function
        if ('renew' in command):
            setRenewal()
        #Else, call the setReminders Function
        else:
            setReminders() #Call setReminders() from External Functions
 
    #-------------------------------------------------------------------------------------
    #                               Set ToDo
    #-------------------------------------------------------------------------------------
    if ('todo' in command):
        command = command.replace("add", "")
        command = command.replace("to the todo list", "")
        setTodo(command) #Call setTodo() from External Functions
 
    #-------------------------------------------------------------------------------------
    #                               Send E-Mails
    #-------------------------------------------------------------------------------------
    if ('email' in command):
        command = command.replace("email", "")
        sendEmail() #Call send E-Mail function fro External Functions
     
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
def Main():
    scheduler = sched.scheduler(time.time, time.sleep) #Create Schedule
    schedule_reminder(scheduler) #Run Reminders
    StartupText()
    wishMe()
    speak("How may I be of service?") 
    while True:
        scheduler.run(False)
        BAXTER()
        # while not scheduler.empty():
            #scheduler.run(False)
#------------------------------------------------------------------------------------------
