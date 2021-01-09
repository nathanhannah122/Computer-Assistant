import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import time
import requests
from bs4 import BeautifulSoup
from datetime import date

# sets and initialises with variables
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# sets the type of voice- To change
engine.setProperty('voice', voices[1].id)

# Temp Data
URL = 'https://weather.com/en-GB/weather/today/l/53.90,-1.99?par=google&temp=c'
css_class = "CurrentConditions--tempValue--3KcTQ"
file_name = "weather"


# Function for getting temp with BeautifulSoup
def get_temp():
    page = requests.get(URL)                                                    # gets the URL (weather.com)
    soup = BeautifulSoup(page.content, 'html.parser')
    span = soup.select_one(".CurrentConditions--tempValue--3KcTQ")               # selects the class
    span = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")       # finds the class
    temp = (span.text.strip())                                                     # strips all other data
    print("The current Temperature is", temp)                                      # outputs needed data
    talk('The current temperature is')
    talk(temp)
    soup2 = BeautifulSoup(page.content, 'html.parser')
    span2 = soup2.select_one(".TodayDetailsCard--feelsLikeTempValue--2aogo")       # selects the class
    span2 = soup2.find("span", class_="TodayDetailsCard--feelsLikeTempValue--2aogo")    # finds the class
    temp2 = (span2.text.strip())                                                       # strips all other data
    print("It Feels like ", temp2)
    talk('it feels like')
    talk(temp2)
    return temp, temp2


# function for the speech using pyttsx3
def talk(text):
    engine.say(text)
    engine.runAndWait()


# function takes the command spoken
def take_command():
    try:
        with sr.Microphone() as source:                         # uses the mic to detect input
            print('...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)      # uses google recogniser
            command = command.lower()
            if 'computer' in command:                       # only inputs data if key word is spoken (computer)
                command = command.replace('computer', '')      # removes key word from request
                return command
            else:
                command = '@@@'
                return command
    except:
        print('Failed to detect input')                 # runs if no input detected
        command = '///'
        return command


# function that writes all unrecognised commands into a txt file
def fail(time, speech):
    fh = open("fail_log", "a")
    fh.write(time)
    fh.write(speech)
    fh.write('\n')
    fh.close()
    return time, speech


# function that allows certain commands to be written when run
def run_computer():
    # initialises count so that the code can re-run with while loop, depending on the command
    count = 1
    while count > 0:
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')                      # removes 'play' so that key term is used to search
            pywhatkit.playonyt(song)                                # uses pywhatkit to play what is requested on Youtube
            talk('Playing' + song)
            print('Now playing-', song)
            count = 0                                               # ends loop
        elif 'date' in command:
            today = date.today()                                    # uses datetime to get current date
            d2 = today.strftime("%B %d, %Y")                        # formats the date
            print(d2)
            talk(d2)                                                 # uses talk function to output
        elif 'help' in command:
            print()
            print('- Computer HELP -')
            print('     You Can Ask:')
            print('- what time is it? ')
            print('- What is the current temperature?')
            print('- Tell me a joke')
            print('- Play...')
            print('- Who/what is...')
            print('- And more')
            time.sleep(5)                                   # uses time to wait until next voice input
        elif 'hello' in command:
            talk('Hello, nice to meet you!')
        elif 'time' in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')         # uses datetime to say current time
            print(time_now)
            talk('Current time is ' + time_now)
        elif 'temperature' in command:
            get_temp()                                      # uses get_temp function to find the temperature
        elif 'who is' in command:
            person = command.replace('who is', '')         # removes pat of command other than key words
            info = wikipedia.summary(person, 1)            # uses wikipedia api to search what is input
            print(info)
            talk(info)
        elif 'what is' in command:
            thing = command.replace('what is', '')         # uses wikipedia api to search what is input
            info = wikipedia.summary(thing, 1)          # uses wikipedia api to search what is input
            print(info)
            talk(info)
        elif 'joke' in command:
            joke = pyjokes.get_joke()                  # uses pyjokes library to say a joke
            print(joke)
            talk(joke)
        elif 'red alert' in command:
            print('RED ALERT!')                         # star trek ee
            time.sleep(.5)
            pywhatkit.playonyt('Red Alert sound effect')
            count = 0                                       # ends loop
        elif 'access main program' in command:                  # Jurassic park ee
            print('PERMISSION DENIED....and....')
            for x in range(10):
                print("YOU DIDN'T SAY THE MAGIC WORD!")
                time.sleep(.3)
                count = 0                                          # ends loop
            pywhatkit.playonyt('Ah Ah Ah, you did not say the magic word')          # uses pywhatkit to play yt video
        elif '@@@' in command:                                                 # command input when computer not heard
            talk('To activate me say - computer')
        elif '///' in command:                                              # command used to end when no input is detected
            print()
            count = 0                                                   # ends loop
        elif 'log' in command:
            f = open("fail_log", "r")                                   # opens log to show previous unknown commands
            print('-Undetectable commands-')
            print(f.read())
            f.close()
        else:
            talk("Sorry I Don't know that one yet")                       # else when it cannot detect a valid command
            talk("to see what I can do, say Computer Help")
            timestamp = datetime.datetime.now()
            timestamp = timestamp.strftime("%d-%m-%y %H:%M:%S")
            fail(timestamp, command)                                    # writes to txt what is said


#   Main Program
print('Computer')
talk('to activate me say, Computer, then a phrase')
run_computer()
