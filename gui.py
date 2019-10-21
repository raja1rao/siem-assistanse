import tkinter as tk
from tkinter import filedialog, Text
import os
import PyPDF2
import string
import re
from tkinter import *
import PIL
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import wikipedia
import wolframalpha
import os
import smtplib
import random
import webbrowser
import pygame
import subprocess
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
    plt.pause(5)  # pause how many seconds
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
        r.pause_threshold = 1
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

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

pdf=[]

def addpdf():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="D:\siem assistance\siem-assistanse",
                                          title="select file", filetypes=(('pdf file', '*.pdf'), ("all files", "*.*")))
    pdf.append(filename)
    print(filename)
    for pdfs in pdf:
        label = tk.Label(frame, text=pdfs,bg="gray")
        label.pack() 

def tell():
    for widget in frame.winfo_children():
        widget.destroy()
    for pdfs in pdf:
                    pdfFileObj = open(pdfs, 'rb')

                    # creating a pdf reader object
                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                    # printing number of pages in pdf file
                    # print(pdfReader.numPages)

                    # creating a page object
                    pageObj = pdfReader.getPage(1)

                    # extracting text from page
                    txt = pageObj.extractText()


                    x = re.sub('['+string.punctuation+']', '', txt).split()


                    if 'Threats' in x:
                        print('threats are there')
                        for page in range(int(x[-1])+4):

                            pageObj = pdfReader.getPage(page)

                            # extracting text from page
                            txt1 = pageObj.extractText()

                            convlist = txt1.split()

                            if convlist[0] == 'Threats':
                        
                                findoccs = convlist.index('Occurrence')
                                findocc = findoccs+1

                                # print(findocc)
                                findVictims = convlist.index('Victims')
                                # print(findVictims)
                                findVictim = findVictims-1
                                mainlist = convlist[findocc:findVictim]
                                # print(mainlist)
                                values = len(mainlist)
                                value = values-4

                                ip = txt1.split()
                                # print(ip)
                                victimsipi = ip.index('Victims')+3
                                # print(ip[victimsipi])
                                victimsipe = ip.index('Sources')-2
                                # print(ip[victimsipe])

                                for i in range(0, values):
                                    if i % 4 == 0:

                                        gui=[]
                                    
                                        for g in range(victimsipi, victimsipe):
                                            if g % 3 == 0:
                                                vip = ip[g]
                                                vocc = ip[g+1]
                                                p = inflect.engine()
                                                # print(vip+"and"+vocc)
                                                # print(mainlist[i])
                                                if vocc == mainlist[i+3]:
                                                    xx = mainlist[i]+"."+mainlist[i+1] + " is a  " + mainlist[i+2] + \
                                                        " whose Occurrence is " + \
                                                        mainlist[i+3] + \
                                                        " and the victim is "+vip
                                                    
                                                    speak(mainlist[i]+"."+mainlist[i+1] + " is a  " + mainlist[i+2] +
                                                          " whose Occurrence is " +
                                                          mainlist[i+3] +
                                                          " and the victim is "+p.number_to_words(vip))
                                                    gui.append(xx)
                                        for pdfs in gui:
                                            label = tk.Label(frame, text=pdfs,bg="gray")
                                            label.pack()
                                                   
                                                   
                    else:
                        print("there is no threats of give the right pdf")


root1 = tk.Tk()

canvas = tk.Canvas(root1, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root1,bg="white")
frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)

openfile = tk.Button(root1, text="opentfile",padx=10,pady=5,fg="white",bg="#263D42" ,command=addpdf)
openfile.pack()

tellme = tk.Button(root1, text="tellme", padx=10, pady=5, fg="white", bg="#263D42",command=tell)
tellme.pack()

root1.mainloop()
