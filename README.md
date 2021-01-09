# Computer - Assistant 
Using python speech recognition and various libraries to allow commands to be fulfilled
----------------------------------------------------------------------
**Required -**
- Python 3.0 
- import speech_recognition
- import pyttsx3
- import pywhatkit
- import wikipedia
- import pyjokes
- import datetime
- import time
- import requests
- bs4
- pyaudio
- datetime
----------------------------------------------------------------------

**Adding another command**

To add a new command: 
- under def_runcomputer()
- navigate to if/else statements
- follow the same format and add an 'elif' statement anywhere prior to the 'else' statemet

**Changing name**

To change activation word from computer
- navigate to line 59 - if 'computer' in command
- replace inside '' with word chosen
- change all referred text from computer to chosen activation word 


**Installing using Pycharm**

- Create a new project
- Navigate to file> settings> Project:project_name> Python interpreter
- On the top right corner a click on the '+' to install the package
- Search package
- Select version needed (latest)
- Select 'install package' at bottom left of the screen


**Installing using terminal** 

pip install (insert package name)
repeat for all libraries

e.g `pip install pyaudio`
