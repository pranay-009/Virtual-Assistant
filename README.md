# Virtual-Assistant
This is a virtual assistant project created using python. Just like virtual assistants like Siri, Alexa we have "Alex" our own virtual assistant. The virtual assistant can do many tasks like introducing self, It can tell you the time, open social media sites (Facebook, Instagram) in your web browser, open music, photos all by using voice command, it can also send WhatsApp messages, and search about anything on google, Wikipedia. 
I used Microsoft Sapi5 API to convert text to voice, and google speech recognizer to recognize the voice commands, we used other libraries like datetime, pyttsx3,pyaudio, os,wikipedia,webrowser,pywhatkit,sys,speech_recognition.
Each of the above libraries was used to perform some particular tasks like recognizing voice or opening a browser or to search something on Google (example: Wikipedia was used to perform Wikipedia search and give 2 sentences as the output). 
For this project, I did not use any real-world data but used some words as features which would help to identify which task to perform, example If you want to search something on google just use the “search” word in your voice command if you want Wikipedia search make sure you use “Wikipedia search” at the starting of your sentence, we used exceptional handling to handle exception like if the program cannot understand what you want.
Let me explain the different actions that took place in this particular program, as we know for a virtual assistant like Siri or Alexa it’s important to convert text to speech, so we use Microsoft sapi5 API, we set voice[1].id for the female voice you could change it into a male by changing the value to 0.
Another vital objective of a virtual assistant is to recognize the speech or voice command, we used a google speech recognizer to recognize it, you can choose any other speech recognizing API /engine(Google cloud speech API, Microsoft Bing voice recognition, etc) 
Libraries used:
➤googlesearch
➤pyttsx3
➤wikipedia
➤os
➤pyaudio
➤speech_recognition
➤webbrowser
➤pywhatkit
