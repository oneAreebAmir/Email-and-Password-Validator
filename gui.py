"""
Created by Areeb Amir
Date : 21/06/2022
Created a program where email and password are taken as two inputs and process them in such algorithm that both is valid and correct and give output correction if there is something wrong. Its contain tkinter which is graphical user interface GUI. 
"""

from tkinter import *
import random

def pass_generator():
    length = random.randint(9,19)
    characters ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passwords = "".join(random.sample(characters,length))
    generate_pass_label.config(text=passwords) 

window = Tk()
window.title('Email & Password')
window.geometry('400x250')
window.minsize(400,250)
window.maxsize(400,250)

text = Label(window, text='Made by Areeb Amir').place(x=0,y=0)

valid_email = Label(window, text='')
valid_email.place(x=80, y=30)

valid_pass = Label(window, text='')
valid_pass.place(x=80, y=90)

label_email = Label(window, text='Email : ')
label_email.place(x=60, y=60)

label_pass = Label(window, text='Password : ')
label_pass.place(x=60, y=120)

input_email = Entry(window)
input_email.place(x= 160, y=60)

input_pass = Entry(window)
input_pass.place(x=160, y=120)

generate_pass_button = Button(window, text='Generate Passwords', command=pass_generator)
generate_pass_button.place(x=60, y=200)

generate_pass_label = Label(window, text='')
generate_pass_label.place(x=230, y=200)

def validation():
    email = input_email.get()
    password = input_pass.get()
    check_email(email)
    check_pass(password)

def check_email(email):
    domain = ['gmail','outlook','yahoo']
    domainCase = any(c in email for c in domain)
    k,j,d = 0,0,0
    if len(email)>=6 and len(email) <= 24:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if domainCase:
                    if (email[-4] == ".") ^ (email[-3] == "."):
                        for i in email:
                            if i == i.isspace():
                                k = 1
                            elif i.isalpha():
                                if i == i.upper():
                                    j = 1
                            elif i.isdigit():
                                continue
                            elif i == "_" or i == "." or i == "@":
                                continue
                            else:
                                d = 1
                        if k == 1 or j == 1 or d==1:
                            valid_email.config(text='Email is invalid')
                        elif k ==0 or j ==0 or d==0:
                            valid_email.config(text='Email is valid')
                    else:
                        valid_email.config(text='Email should contain . or com')
                else:
                    valid_email.config(text='Email should contain domain')
            else:
                valid_email.config(text='Email should contain @')            
        else:
            valid_email.config(text='The first index should started with alphabet')
    else:
        valid_email.config(text='Email is less than 6 or greater than 24')

def check_pass(password):
    lowerCase = any(c.islower() for c in password)
    UpperCase = any(c.isupper() for c in password)
    DigitCase = any(c.isdigit() for c in password)
    SpaceCase = any(c.isspace() for c in password)
    SpecialChar = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',';','<',',','>','.','?','/']
    CharCase = any(c in password for c in SpecialChar)
    if len(password) >= 8 and len(password) <= 20:
        if lowerCase and UpperCase and DigitCase and CharCase and (not SpaceCase):
            valid_pass.config(text='Password is valid') 
        elif not lowerCase:
            valid_pass.config(text='You didnt use Lower case letter')
        elif not UpperCase:
            valid_pass.config(text='You didnt use upper case letter')
        elif not DigitCase:
            valid_pass.config(text='You didnt use digits')
        elif not CharCase:
            valid_pass.config(text='You didnt use special character')
        elif SpaceCase:
            valid_pass.config(text='You use space')
    else:
        valid_pass.config(text='Password is less than 8 or greater than 20 ')

Generate_valid = Button(window, text='Generate Validation', command=validation)
Generate_valid.place(x=120, y=150)

window.mainloop()
