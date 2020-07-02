import string
import random 

print("Password generator")

forwhich=input("Enter the application to generate password: \n")
length=int(input("Enter the lenght of your password(max-94)\n "))
if length>=94:
    print("Max length crossed")
    quit()

pass1=list(string.ascii_lowercase)
pass2=list(string.ascii_uppercase)
pass3=list(string.digits)
pass4=list(string.punctuation)

elements=pass1+pass2+pass3+pass4

random.shuffle(elements)
password="".join(elements[0:length])
print("The password generated is :",password,"\n")
saveyn=input("Do you want to save the password ? ?\n Enter Yes or No \n ")
if saveyn=="yes":
    f=open("generatedpassword.txt","a")
    f.write(forwhich + "  -  "+password+"\n")
    f.close()
    print("Your password is generared succesfully ")

print("Thank you")