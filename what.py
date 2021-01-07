##imports
import tkinter as tk
from tkinter import *
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import sys
import mainfunc
from mainfunc import main_function


##Starts validation
validation = main_function()
##takes number
ph = validation.get_num()
##should continue?
exited = validation.get_should_message()
if exited == False:
    sys.exit()


##initialize
master = Tk()
master.geometry("700x450")
master.title("Send whatssap messages")
#master.iconbitmap('C:\studies\python\Whatssap Automation\devil.ico')


##Screen Settings
windowWidth = 1000
windowHeight = 500
positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/2 - windowHeight/2)
master.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))


##variables for entries
mes_var = tk.StringVar()
count_var = tk.IntVar()
wait_time_var = tk.IntVar()


##Entries and labels
l1 = Label(master,text ="Let's start messaging",font = ('Comic Sans MS',18),bd = 1).grid(row = 0, column =0)
l2 = Label(master,text = "\nEnter your message",font = ('Comic Sans MS',12),bd = 1).grid(row=1, column =0)
Entry(master,textvariable = mes_var,font = ('Comic Sans MS',12),bd = 1).grid(row=1 , column = 1)
l3 = Label(master, text = "\nEnter the number of messages",font = ('Comic Sans MS',12),bd = 1).grid(row=2,column=0)
Entry(master,textvariable = count_var,font = ('Comic Sans MS',12),bd = 1).grid(row=2,column=1)
l4 = Label(master, text = "\nEnter wait time\nPrefer atleast 1 sec to reduce internet data loss.",font = ('Comic Sans MS',12),bd = 1).grid(row=3, column = 0)
Entry(master, textvariable=wait_time_var,font = ('Comic Sans MS',12),bd = 1).grid(row=3,column = 1)


##Class
class whatmess():

    def what_func():
        
        
        ##Extract info
        my_message = mes_var.get()
        count = int(count_var.get())
        wait_time = int(wait_time_var.get())


        ##Deploy Selenium
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        driver = webdriver.Chrome('C:\studies\misc\chromedriver',chrome_options=chrome_options)
        driver.get("https://web.whatsapp.com/")


        ##Disable keep me signed in
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/label/input').click()
            except:
                continue
            else:
                break

        wait = WebDriverWait(driver,20)

        wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]')))


        ##find phone number
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(ph)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
        
        
        ##Start loop messaging
        for i in range(count):
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(my_message)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
            time.sleep(wait_time)


    ##Last buttons
    Label(master, text = "\n").grid(row=4)
    Button(master,text = "Deploy",command = what_func,font = ('Comic Sans MS',12),bd = 1).grid(row=5)
    Label(master, text = "\n").grid(row=6)
    Button(master,text = "Quit",command = master.destroy,font = ('Comic Sans MS',12),bd = 1).grid(row=7)
    mainloop()