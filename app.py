# if you editing this and de copailing it u cud break somting
import tkinter as tk
from tkinter import Canvas
from tkinter import *
import time
import uuid
import sys

main = tk.Tk()
main.title("Password Manager 2.0.1")
canvas = Canvas(main, width=650, height=450)
canvas.pack()
main.resizable(False,False)
username = "0"
password = "0"
file = "0"
boxx = 10
boxy= 100
linese = 1

box =  canvas.create_rectangle(boxx,boxy, 250 + boxx,250 + boxy)
box = tk.Scrollbar(main)
box.place(x=100,y=100, width=180)
label = Label(main, text='Username:')
label.place(relx=0.7, rely=0.45, anchor='s')
user = tk.Entry(main, width = 50)
user.place(relx=0.7, rely=0.45, anchor='n')
passss = Label(main, text='Password:')
passss.place(relx=0.7, rely=0.55, anchor='s')
passs = tk.Entry(main, width = 50)
passs.place(relx=0.7, rely=0.55, anchor='n')
def load():
           linese = 1
           load = open("corapted data", "r")
           lines = load.readlines()
           for line in lines:
                      linese = linese + 1
                      filelist = ""
                      print("{}".format(line, line.strip()))
                      filelist = (line)
def file():
           global user
           string= user.get()
           global passs
           pase= passs.get()
           username = string
           password = pase
           time.sleep(0.1)
           filename = str(uuid.uuid4())
           die = str(uuid.uuid4())
           file = str(uuid.uuid4())

           open(filename, 'w+')
           with open(file, 'w+')as omg:
                      omg.writelines("\n" + username)
                      omg.writelines("\n"+ password)
                      omg.close()
                      
                           
           open(die, 'w+')
           time.sleep(0.5)
           with open("corapted data", "a") as data:
                      data.writelines("\n" + file)
                      data.close()
btn = Button(main, text ="Save", command = file)
pen = Button(main, text ="Load", command = load)
pen.place(x=500, y=400)
btn.place(x=560, y=400)

time.sleep(0.0001)
main.mainloop()

