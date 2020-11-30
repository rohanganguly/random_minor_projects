import os

print ("Press 1 to Shutdown Computer")
print ("Press 2 to Restart Computer")
print ("Press any other key to exit this menu")

keypress= int(input("\nEnter Your Choice: "))

if keypress==1:
    os.system("shutdown /s /t 1")
elif keypress==2:
    os.system("shutdown /r /t 1")
else:
    exit()

