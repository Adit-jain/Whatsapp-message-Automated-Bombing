##imports
import tkinter as tk
from tkinter import *
import phonenumbers
from phonenumbers import timezone, carrier, geocoder


##Initialzie
number =""
should_message = False
master = Tk()
master.title("Validate the phone Number")
#master.iconbitmap('C:\studies\python\Whatssap Automation\devil.ico')

##Screen Settings
windowWidth = 1000
windowHeight = 500
positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)
master.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))


##Labels
l1 = Label(master, text = "What is the Country Code :                ",font = ('Comic Sans MS',14),bd = 1, relief = "sunken").grid(row=0)
l2 = Label(master, text = "What is the Phone number :                ",font = ('Comic Sans MS',14),bd = 1, relief = "sunken").grid(row=1)


##variables for entries
country_code_var = tk.StringVar()
original_number_var = tk.StringVar()
answer = tk.StringVar()

##Entries
country_code_entry = Entry(master, textvariable = country_code_var,font = ('Comic Sans MS',14),bd = 1, relief = "sunken")
original_number_entry = Entry(master, textvariable = original_number_var,font = ('Comic Sans MS',14),bd = 1, relief = "sunken")
country_code_entry.grid(row=0,column = 1)
original_number_entry.grid(row=1, column = 1)

def start_messaging():
        global should_message
        should_message = True
        master.destroy()


##Validation class
class main_function():

    def __init__(self):
        pass

    
    def Trace():

        ##Class gets number details from GUI
        country_code = country_code_var.get()
        original_number = original_number_var.get()
        global number
        number = "+" + country_code + original_number
        phonenumber = phonenumbers.parse(number)


        #Checks validation
        valid = phonenumbers.is_valid_number(phonenumber)
        possible = phonenumbers.is_possible_number(phonenumber)


        if valid == True and possible == True:

            ##Extracts details
            time_zone = timezone.time_zones_for_number(phonenumber)
            

            carrier_company = carrier.name_for_number(phonenumber,'en')
            

            location = geocoder.description_for_number(phonenumber,'en')
            
            ##Prints details
            ansstr =  "\n Details :- \n {} \n The Phone number belongs to the time zone of : {}  \n The phone number is provided by {} \n The phone number belongs to {}".format(phonenumber,time_zone,carrier_company,location.upper())
            answer.set(ansstr)


            ##Begin messaging
            Label(master, text = "\n").grid(row=6)
            Button(master,text = "Click here to start messaging", command = start_messaging ,font = ('Comic Sans MS',12),bd = 1).grid(row=7)
            

        elif valid == False and possible == True:
            answer.set("Invalid number")

        elif possible == False:
            answer.set("Enter in correct format")


    def get_num(self):
        
        return number[3:]

    def get_should_message(self):
        return should_message



    ##Buttons and Result Display
    Label(master, text="\n").grid(row=2)
    Button(master, text = "TRACE", command = Trace,font = ('Comic Sans MS',12),bd = 1).grid(row=3)
    Label(master, textvariable = answer,font = ('Comic Sans MS',12),bd = 1, relief = "sunken").grid(row = 5)
    Label(master, text = "\n").grid(row=8)
    Button(master,text = "Quit", command = master.destroy ,font = ('Comic Sans MS',12),bd = 1).grid(row=9)
    mainloop()




