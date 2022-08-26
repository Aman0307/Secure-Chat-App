# Secure-Chat-App
**INTRODUCTION**


Security issues have an important place in today's communication 
technologies. Since mutual communication must be done through secure 
channels that don’t allow third people to intervene, it is very important 
to make the security levels of these channels as high as possible.
Encryption algorithms can be utilized to provide secure messaging 
environment. Thus, messages will circulate as encrypted form in 
transmission medium, not as clear text. Somebody who has seized 
encrypted data does not obtain original message from the encrypted data 
unless they possess the necessary method or a key.

There are many ways to encrypt and decrypt messages in a messaging 
application. In this project I have used a python module called fernet 
to perform the encryption and decryption of data. The fernet module 
guarantees that data encrypted using it cannot be further manipulated or 
read without the key.

To enhance the user experience, a python module called tkinter is used. 
Python with tkinter is the fastest and easiest way to create the GUI 
applications.

Finally, this application has two main components – A server side and A 
client side. The server-side code will run on a server and each client will 
have a client-side code running on their device. Each client can connect 
to server through a specified port.







**PROPOSED METHOD WITH ARCHITECTURE**


This is a simple GUI (Graphical User Interface) chat application where 
multiple users can connect with each other in a client-server architecture 
i.e the clients will interact with the help of the server.
A pair of two simple network application programs on server and client 
machines has been written. Both machines will communicate with each 
other by writing to and reading from their sockets. One can understand 
socket as an entry door to a machine. It is the interface between the 
transport layer of the network and the application residing on the 
machine.

Server program has all the logic to control and regulate the Chat, so most 
of the chat logic is implemented with a server program. So, first step of 
communication is to identify the users, how server do this? In network 
communication, users are identified by a socket which is nothing but a 
combination of IP address and port address. Since only the clients will 
interact the server script, it does not have a GUI.

The main aim of this project was to build a secure messaging application. 
This is achieved using python cryptography module called fernet. The 
fernet module of the cryptography package has inbuilt functions for the 
generation of the key, encryption of plaintext into ciphertext, and 
decryption of ciphertext into plaintext using the encrypt and decrypt 
methods respectively. The fernet module guarantees that data encrypted 
using it cannot be further manipulated or read without the key.

Fernet is built on top of a number of standard cryptographic primitives. 
Specifically, it uses:
➢ AES in CBC mode with a 128-bit key for encryption; using PKCS7 
padding.
➢ HMAC using SHA256 for authentication.
➢ Initialization vectors are generated using os.urandom()







**IMPLEMENTATION**


The project uses tkinter for user interface. This provides basic layouts 
and some feature like buttons etc. We can add more feature to enhance 
user experience.

At first the server script is run. This sets up the server that will connect 
hosts and also act as a channel to send and receive messages.
Each user will run the client-side code on his system this will result in a 
window getting popped up. This will ask for username, email-id and 
password to verify the identity of the user. If the user enters a valid 
email-id and password and if the user has an existing Gmail account 
whose email and password are given, the user will join the chatroom 
otherwise he/she will be redirected to the same login page again with an 
error message.

Once a user has entered the chatroom and wants to send a message, he 
will generate a key using fernet module. Then this key will be stored in a 
file from where the server can access it. The user will encrypt messages 
with this key and send it to the server.
The server will use the key to decrypt the messages and broadcast it in 
the chatroom. Once there are no users in the chatroom, the chatroom 
window will terminate and the program will end.
