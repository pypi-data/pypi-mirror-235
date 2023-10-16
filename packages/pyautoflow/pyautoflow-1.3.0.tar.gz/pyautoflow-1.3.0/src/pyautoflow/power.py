import os

def shutdown():
    os.system("shutdown /s /t 1")

def reboot():
    os.system("shutdown /r /t 1")