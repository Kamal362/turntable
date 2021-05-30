import os
from datetime import datetime

def upadateConteact():
    pass

def viewContact():
    with open("contacts.txt", "r") as fileInfo:
       # if os.path.exists("contacts.txt"):
           print(fileInfo.read())
        ##else:
           ##print("contact does not exist") 
    

def deleteContact():
    pass

def createContact():
    name = input("=>Name of the person: ")
    contact = input("=>Phone Number: ")
    with open("contacts.txt","a") as fileInfo:
        fileInfo.write(name)
        fileInfo.write(contact)
        fileInfo.write(datetime.now())
        print("contact successfully created! ")

def display():
    print("1. view contact \n2. create contact \n3. delete contact ")
    choice = input("=> choose: ")
    if choice == 1:
        viewContact()
    elif choice == 2:
        createContact()
    elif choice == 3:
        deleteContact() 
    else:
        print("Choice incorrect!")     
    


print(display())

