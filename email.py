email = str(input("please enter email: "))
username = email.split("@")[0]
domain = email.split("@")[1]
print("Your username is "+username+"\nand your domain is "+domain)