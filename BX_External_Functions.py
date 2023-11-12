#!/usr/bin/env python3
 
#-------------------------------------------------------------------------------------
#                               B.A.X.T.E.R Externalized Functions
#-------------------------------------------------------------------------------------
 
#----------------------------------------------------------------------------------------------
#                                  Table Of Contents/Overview
#----------------------------------------------------------------------------------------------
# Imports
# Define Variables
 
# Auto Type Function
# Jokes 
# Fun Facts
# Listen Function -> Uses Google API to Listen
# Reminder Function
# Startup & Shutdown Text Function
# Terminate Timers
# User Input Function
# Voice Settings
#----------------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                  Imports
#-------------------------------------------------------------------------------------
import time
import datetime
import random
import sys
import requests
import json
import threading
 
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
import keyboard
 
import speech_recognition as sr
import pyttsx3
 
from rich import print
from rich.console import Console
from rich.prompt import Prompt
 
from BX_Intents import (youChoose)
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                Define Variables
#-------------------------------------------------------------------------------------
console = Console(width=100) 
#-------------------------------------------------------------------------------------
 
 
#-------------------------------------------------------------------------------------
#                                Auto Type Function
#-------------------------------------------------------------------------------------
def autoTypeAnimation(results):
    #----------------------
    #Auto typing animation:
    print("[green]Baxter: [/green]", end="")
    for i in results:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    #---------------------- 
#-------------------------------------------------------------------------------------
 
 
#-------------------------------------------------------------------------------------
#                               Fun Facts Function
#-------------------------------------------------------------------------------------
def getFunFacts():
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
       
    # Use GET request
    response = requests.request("GET", url)  
       
    # Load the request in json file
    data = json.loads(response.text)
    result = data['text']
    return result
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                Joke Function
#-------------------------------------------------------------------------------------
def getRandomJoke():
    headers = {
        'Accept': 'application/json'
    }
    result = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return result["joke"]
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                Listen Function
#-------------------------------------------------------------------------------------
def listen():
    hear = sr.Recognizer()
    with sr.Microphone() as source:
        results = "Listening..."
        autoTypeAnimation(results)
        audio = hear.listen(source)  
    try:
        results = "Recognizing..."
        autoTypeAnimation(results)
        # Uses google API to listen
        command = hear.recognize_google(audio, language='en-in')
        print("[yellow]Commander: " + command)
 
    except:
            pass
 
    return command 
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                Reminder Function
#-------------------------------------------------------------------------------------
def setReminders(command):
    results = "Would you like to pick a time for me to remind you, or should I do it?"
    autoTypeAnimation(results)
    speak(results)
     
    #User enters choice and thier input gets converted to lowercase 
    choiceCommand = UserInput() #Take user's input
    choiceCommand=str(choiceCommand).lower() #Convert str cmd to lowercase
 
    #Scan through the youChoose() list to see if the user's input matches
    #If it does, have Baxter randomly choose a time to remind the user
    #Else, have the user enter the time they would like to be reminded 
    patterns = youChoose()
    if (choiceCommand in patterns):
        #Baxter picks a random time to remind you
        remindTimeHrs = random.uniform(0.5,5.0) #Range: 0.5hrs - 5hrs
        remindTimeHrs = round(remindTimeHrs,2) #Round RemindTimeHrs to 2 decimal places
        remindTimeSec = remindTimeHrs*3600 #Hrs->Sec
        results = "Ok, I will remind you" + command + " in " + str(remindTimeHrs) + " hours"
        autoTypeAnimation(results)
        speak(results)
        t = threading.Timer(remindTimeSec, reminderPopup, args=(command,))
        t.start() #Start the timer
         
    else:
        #User picks the time to be reminded
        results = "When should I remind you" + command +"?"
        autoTypeAnimation(results)
        speak(results)
        while True:
            autoTypeAnimation("Enter wait time (H:M:S) (Ex: 0:0:5 -> 5sec)")
            timestr = UserInput()
            if not timestr:
                break
            try:
                h,m,s = timestr.split(':')
                timestr = (int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()))
                t = threading.Timer(timestr, reminderPopup, args=(command,))
                results = "Ok, I will remind you" + command + " in " + h + " Hours "+ m + " minutes " + s + " seconds"
                autoTypeAnimation(results)
                speak(results)
                t.start() #Start the timer
                break
            except ValueError:
                print("[green]Baxter: [red]Not a valid time input")
 
 
def reminderPopup(command):
    print("\n")
    style = "bold"
    console.print("[green]Baxter:", style=style, justify="center")
    console.print("[cyan]Reminder Alert!", style=style, justify="center")
    console.print("[cyan]I was told to remind you" + command, style=style, justify="center")
    speak("I hate to interrupt, but I was told to remind you" + command)
    keyboard.press('ENTER') #'Press' Enter to crudely clear the user query
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                             Startup & Shutdown Function
#-------------------------------------------------------------------------------------
def StartupText():
    #----------------------
    #Auto typing animation:
    results = """
    Systems Started...
    Defaulting to Keyboard Input...
    B.A.X.T.E.R System Online
    """
    #Print Start Header
    style = "bold green on blue"
    console.print("[green]B.A.X.T.E.R A.I System", style=style, justify="center")
    #Print Text
    console.print("[green]"+ results, justify="center")
 
def ShutdownText():
    #----------------------
    #Auto typing animation:
    results = """
    Systems Terminated...
    B.A.X.T.E.R System Offline
    """
    #Print Text
    console.print("[red]"+ results, justify="center")
    #Print End Header
    style = "bold blue on red"
    console.print(" ", style=style, justify="center")
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                             Terminate Timers Function
#-------------------------------------------------------------------------------------
def terminateTimers():
    #Cancel all ongoing timers
    for timer in threading.enumerate():
        if isinstance(timer, threading.Timer):
            #print(timer)
            timer.cancel()
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                User Input Function
#-------------------------------------------------------------------------------------
def UserInput():
    command = str(Prompt.ask("[yellow]Commander[/yellow]"))
    # CommanderInput(command)
    return command 
#-------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------------------------
#                                  Voice Settings
#-------------------------------------------------------------------------------------
def speak(audio):
    speaker = pyttsx3.init ()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[2].id)
    speaker.setProperty ('rate', 180)
    speaker.say (audio)
    speaker.runAndWait () 
# # Test to see all avaliable voices
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()
#-------------------------------------------------------------------------------------
