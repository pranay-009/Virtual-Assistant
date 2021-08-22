#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googlesearch import search
import os
import wikipedia
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import pyaudio
import sys
import pywhatkit as py
engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour=(datetime.datetime.now().hour)
    if hour<12:
        speak("good morning!")
    if hour>=12 and hour<=19:
        speak("good afternoon!")
    if hour>19:
        speak("good evening!")
    speak("Hey! I am Alex your virtual assistant, tell me how may i help you?")    
def commandlisten():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("recognising....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}\n")

    except Exception as e:
        speak("did not understand can you please repeat?")
        return "None"
    return query    
def audio_content():
    a=sr.Recognizer()
    
    with sr.Microphone() as s:
        #listening using the mic
        print("please tell your message")
        hear=a.listen(s)   
        print("recognizing.......")
        try:
            print("recognizing....")  
            message=a.recognize_google(hear,language="en-in")
            print(message)
        except Exception as e:
              print("sorry! there might have been a problem")
    return(message)    
greet() 

contact={"mother":"+91974******","arup":"+9170*******8"}
# diffent command instruction begins
while True:
    test=commandlisten().lower()
    if "siri" in test:
        speak("yes! i know siri she is a virtual assistant just like me ")
#open wikipedia search and open youtube or google or stackoverflow
    elif "wikipedia search" in test :
        test=test.replace("wikipedia","")
        test=test.replace("search","")
        try:
            search_result=wikipedia.summary(test,sentences=2)
            speak("According to wikipedia ")
            print(search_result)
            speak(search_result)
        except Exception as e:
            speak("sorry the above page cannot be found please try again")
            print("sorry the above page cannot be found please try again")
    elif "open youtube" in test:
        webbrowser.open("youtube.com")
        speak("open youtube")
    elif "open wikipedia" in test:
        webbrowser.open("wikipedia.com") 
        speak("opening wikipedia")
    elif "open google" in test:
        webbrowser.open("google.com")
        speak("opening google")
#play anything in youtube the key words should be 'play youtube'        
    elif "play" and "youtube" in test:
        rep_test=test.replace("play","")
        rep_test=test.replace("youtube","")
        rep_test=test.replace("on","")
        try:
            py.playonyt(rep_test)
        except:
            print("sorry i could not find any")
            speak("sorry i could not find any")
#google search            
    elif "search" in test:
        test=test.replace("search","")
        test=test.replace("Alex","") 
        test=test.replace("google","")
        try:
            speak("here are your search reasult!")
            py.search(test)
        except:
            speak("search not found")
#web search stackoverflow            
    elif "open stackoverflow" in test:
        webbrowser.open("stackoverflow.com")  
        speak("opening stackoverflow")
    elif "open facebook" in test:
        webbrowser.open("facebook.com")  
        speak("opening facebook")
    elif "open instagram" in test:
        webbrowser.open("instagram.com")
        
    elif "thank you" in test:
        speak("you are welcome")
#introduce the user
    elif "introduce" in test:
        speak("you are pranay saha , first year student in Institute of engineering and mangement")
#time presently        
    elif "time" in test:
        t=datetime.datetime.now()
        speak("time is " + str(abs(12-t.hour))+" "+ str(t.minute)+ t.strftime("%p"))
#favourite photo of user        
    elif "favourite photo" in test:
        speak("opening ")
        
        photo=r"C:\Users\user\Pictures\spider2.jpg"
        os.startfile(photo)
#whatsapp open command        
    elif "open whatsapp" in test:
        speak("opening whatsapp")
        os.startfile(r"C:\Users\user\AppData\Local\WhatsApp\WhatsApp.exe")
#send message in whatsapp        
    elif "message" in test:
        test=test.replace("message ","")
        if test in contact.keys():
            print("contact found")
            t=datetime.datetime.now()
            try:
                speak("please say the message") 
                py.sendwhatmsg(contact[test],audio_content().lower(),t.hour,t.minute+1)
                print("sending the message")   
            except:
                print("sorry could not send the text!")
                speak("sorry i cannot send the message")
        else:
            print("sorry contact not found")
    elif "open photos" in test or "open pictures" in test:
        try:
            os.startfile(r"C:\Users\user\Pictures")
        except Exception as e:
            speak("sorry!file not found")
    elif "open music" in test:
        try:
            os.startfile(r"C:\Users\user\Music")
        except Exception as e:
            speak("sorry!file not found")
#exit the programme command    
    elif "close" in test or "stop" in test:
        sys.exit()
    else:
        speak("sorry thats beyond my capabilities at this moment!")
        


# In[ ]:




