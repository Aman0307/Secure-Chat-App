# import all the required  modules
# import all functions /
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os
from cryptography.fernet import Fernet
import re 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

  

#Function to generate Fernet key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

generate_key()



#function to load key into a file
def load_key():
    return open("secret.key","rb").read()


#function to encrypt messages
def encrypt_message(msg):
    key=load_key()
    encoded_msg = msg.encode()
    f= Fernet(key)
    encrypted_msg=f.encrypt(encoded_msg)
    return encrypted_msg

#Check if email format is correct
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
 
    # pass the regular expression
    # and the string in search() method
    if(re.match(regex, email)):
        return "Valid Email"
 
    else:
        return "Invalid Email"


#Function to check if it is a valid email id from google
def gmail_val(email,password):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)
    
        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(email)
    
        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()
    
        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(password)

       
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()
        driver.implicitly_wait(5)


   
        element = driver.find_element_by_class_name("gb_uc").click()
        
        print(driver.execute_script('return document.title'))
        if driver.execute_script('return document.title')!= 'Gmail':
            return 'Login Successful!!'
        else:
            return 'Login Failed'
    
        
    except:
        return 'Login Failed'


  
PORT = 4
SERVER = "192.168.56.1"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
  
# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM)
client.connect(ADDRESS)
  
  
# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self):
        
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
          
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width = False, 
                             height = False)
        self.login.configure(width = 470,
                             height = 550)
        # create a Label
        self.pls = Label(self.login, 
                       text = "Please login to continue",
                       justify = CENTER, 
                       font = "Helvetica 14 bold")
          
        self.pls.place(relheight = 0.15,
                       relx = 0.2, 
                       rely = 0.07)
        # create a Label for Name
        self.labelName = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
          
        self.labelName.place(relheight = 0.1,
                             relx = 0.1, 
                             rely =  0.2)
          
        # create a entry box for 
        # typing the Name
        self.entryName = Entry(self.login, 
                             font = "Helvetica 14")
          
        self.entryName.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)

       # create a Label for Email address
        self.labelEmail = Label(self.login,
                               text = "Email: ",
                               font = "Helvetica 12")
          
        self.labelEmail.place(relheight = 0.3,
                             relx = 0.1, 
                             rely = 0.3)
          
        # create a entry box for 
        # typing the Email
        self.entryEmail = Entry(self.login, 
                             font = "Helvetica 14")
          
        self.entryEmail.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.4)

        # create a Label for Password
        self.labelPassword = Label(self.login,
                               text = "Password: ",
                               font = "Helvetica 12")
          
        self.labelPassword.place(relheight = 0.3,
                             relx = 0.1, 
                             rely = 0.5)
          
        # create a entry box for 
        # typing the Password
        self.entryPassword = Entry(self.login, 
                             font = "Helvetica 14",
                             show = '*')
          
        self.entryPassword.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.6)
        

        # set the focus of the curser
        self.entryName.focus()
          
        # create a Continue Button 
        # along with action
        self.go = Button(self.login,
                         text = "CONTINUE", 
                         font = "Helvetica 14 bold", 
                         command = lambda: self.goAhead(self.entryName.get(),self.entryEmail.get(),self.entryPassword.get()))
          
        self.go.place(relx = 0.4,
                      rely = 0.80)
    
        self.Window.mainloop()
  
    def goAhead(self, name,email,password):
        #Check if entered email and password are correct and if they exist

        if check(email)=="Valid Email":
            messagebox.showinfo("Email Verification", "Valid Email")
            s = gmail_val(email,password)
            if s=="Login Failed":
                messagebox.showinfo("Email Login", "Login Failed")
                self.login.destroy()
                g=GUI()
            else:
                messagebox.showinfo("Email Login", "Login Successful!!")
                
        
        if check(email)=="Invalid Email":
            messagebox.askretrycancel("Email Verification", "Invalid Email")
            self.login.destroy()
            g= GUI()
        self.login.destroy()
        
        self.layout(name)
          
        # the thread to receive messages
        rcv = threading.Thread(target=self.receive)

        rcv.start()
  
    # The main layout of the chat
    def layout(self,name):
        
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 470,
                              height = 550,
                              bg = "#17202A")
        self.labelHead = Label(self.Window,
                             bg = "#17202A", 
                              fg = "#EAECEE",
                              text = self.name ,
                               font = "Helvetica 13 bold",
                               pady = 5)
          
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 450,
                          bg = "#ABB2B9")
          
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
          
        self.textCons = Text(self.Window,
                             width = 20, 
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14", 
                             padx = 5,
                             pady = 5)
          
        self.textCons.place(relheight = 0.745,
                            relwidth = 1, 
                            rely = 0.08)
          
        self.labelBottom = Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 80)
          
        self.labelBottom.place(relwidth = 1,
                               rely = 0.825)
          
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
          
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
          
        self.entryMsg.focus()
          
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
          
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.06, 
                             relwidth = 0.22)
          
        self.textCons.config(cursor = "arrow")
          
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
          
        # place the scroll bar 
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
          
        scrollbar.config(command = self.textCons.yview)
          
        self.textCons.config(state = DISABLED)
  
    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        
        self.msg=msg

        self.entryMsg.delete(0, END)
        snd= threading.Thread(target = self.sendMessage)
        snd.start()
  
    # function to receive messages
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
  
                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END,
                                         message+"\n\n")
                      
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break 
          
    # function to send messages 
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}:{self.msg}")
            print(message)
            message = encrypt_message(message)
            print(message)
            client.send(message)
#            client.send(message.encode(FORMAT))    
            break    
  
# create a GUI class object
g = GUI()