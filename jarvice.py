import PyPDF2
import string
import re
from tkinter import *
import PIL
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import inflect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import filedialog, Text
import os
import PyPDF2
client = wolframalpha.Client('7K53TX-WY9YKL68RX')

# folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# b_music = ['Edison', 'Micro', 'Lucid_Dreamer']
# pygame.mixer.init()
# pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
# pygame.mixer.music.set_volume(0.05)
# pygame.mixer.music.play(-1)

def pupup():
    ImageAddress = '0516red_RedView.jpg'
    ImageItself = Image.open(ImageAddress)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.draw()
    plt.pause(5) # pause how many seconds
    plt.close()

def speak(audio):
    print('Nandan:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        return query
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
       COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
       root = Tk()
       root.title('NANDAN')
       root.config(background='Red')
       root.geometry('350x600')
       root.resizable(0, 0)
       root.iconbitmap(r'favicon.ico')
       img = ImageTk.PhotoImage(Image.open(r"271020.jpg"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg=random.choice(COLORS), fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Nandan", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg=random.choice(COLORS),fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
       speak('Hello, I am Nandan! What should I do for You?')
       self.compText.set('Hello, I am Nandan! What should I do for You?')

       root.bind("<Return>", self.clicked) 
       root.mainloop()
    
    def clicked(self):
        print('Working')
        
        for i in range(1,1000) :
            try:
                self.userText.set('Listening...')
                query = myCommand()
                self.userText.set(query)
                
                query = query.lower()

                if 'open word' in query:
                    self.compText.set('okay')
                    speak('okay')
                    subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')

                elif 'open google chrome' in query:
                    self.compText.set('okay')
                    speak('okay')
                    subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

                elif 'open powerpoint' in query:
                    self.compText.set('okay')
                    speak('okay')
                    subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE')

                elif 'open youtube' in query:
                    self.compText.set('okay')
                    speak('okay')
                    webbrowser.open('www.youtube.com')
                elif 'open calculator' in query:
                    self.compText.set('okay')
                    speak('okay')
                    import cal

                elif 'open google' in query:
                    self.compText.set('okay')
                    speak('okay')
                    webbrowser.open('www.google.co.in')

                elif 'open gmail' in query:
                    self.compText.set('okay')
                    speak('okay')
                    webbrowser.open('www.gmail.com')

                elif 'shutdown' in query:
                    self.compText.set('okay')
                    speak('okay')
                    os.system('shutdown -s')

                elif "what\'s up" in query or 'how are you' in query:
                    stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                    self.compText.set(random.choice(stMsgs))
                    speak(random.choice(stMsgs))
                
                elif "who are you" in query:
                    self.compText.set("i am Nandan! your virtual assistant")
                    speak("i am Nandan! your virtual assistant")
                
                elif 'email' in query:
                    self.compText.set('Who is the recipient? ')
                    speak('Who is the recipient? ')
                    recipient = myCommand()
                    self.userText.set(recipient)
                    recipient = recipient.lower()

                    
                    try:
                        # self.compText.set('What should be the subject? ')
                        # speak('What should be the subject? ')
                        # subject = myCommand()
                        # self.userText.set(subject)
                        self.compText.set('What should I say? ')
                        speak('What should I say? ')
                        contents = myCommand()
                        # self.userText.set(contents)
                        # massage = MIMEMultipart()

                        Your_password = "********"
                        Your_Username = "**************"
                        recipients = '**********'
                        # # massage['From'] = Your_Username
                        # # massage['To'] = recipients
                        # massage['Subject'] = subject
                        # massage.attach(MIMEText(contents,'plain'))
                        # content = massage.as_string()
                        

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login(Your_Username, Your_password)
                        server.sendmail(Your_Username, recipients, contents)
                        server.close()
                        self.compText.set('Email sent!')
                        speak('Email sent!')

                    except:
                        self.compText.set('Email not sent!')
                        speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



                elif 'nothing' in query or 'abort' in query or 'stop' in query:
                    self.compText.set('Okay')
                    speak('okay')
                    self.compText.set('Bye Sir, have a good day.')
                    speak('Bye Sir, have a good day.')
                    sys.exit()
                
                elif 'hello' in query:
                    self.compText.set('Hello Sir')
                    speak('Hello Sir')


                elif 'bye' in query:
                    self.compText.set('Bye ' + 'Sir' + ', have a good day.')
                    speak('Bye ' + 'Sir' + ', have a good day.')
                    sys.exit()
                                            
                elif 'play music' in query:
                    music_folder = 'C:\\Users\\skt\\Music\\YouTube\\'
                    music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
                    random_music = music_folder + random.choice(music) + '.mp3'
                    os.system(random_music)
                    
                    self.compText.set('Okay, here is your music! Enjoy!')
                    speak('Okay, here is your music! Enjoy!')


                elif 'show me threads' in query or 'show me thread' in query or 'show me threats' in query:
                    import gui
                    



                    
                else:
                    try:
                        try:
                            res = client.query(query)
                            results = next(res.results).text
                            self.compText.set(results)
                            speak(results)
                        except:
                            results = wikipedia.summary(query, sentences=2)
                            self.compText.set(results)
                            speak(results)
                
                    except:
                        speak('I don\'t know Sir! Google is smarter than me!')
                        self.compText.set('I don\'t know Sir! Google is smarter than me!')
                        webbrowser.open('www.google.com')
            except:
                
                pass
if __name__ == '__main__':
    pupup() 
    greetMe()
    widget = Widget()
