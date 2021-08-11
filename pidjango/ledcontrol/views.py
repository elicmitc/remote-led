from django.shortcuts import render
from django.http import HttpResponse
import time
import os,signal
from threading import Thread
# Create your views here.

def killproc():
    print("---------------------- Process Information --------------------");
    for lines in os.popen('ps ax | grep /home/pi/Desktop/Led-Server/pidjango/ledcontrol/server.py'):
        fields = lines.split('\n')
        for line in fields:
            pid_str = line.split(' pts/',1)
            pid = pid_str[0].replace(' ','', 1)
            if(len(pid) != 0 ):
                tokill = 'sudo kill -9 ' + pid
                #print(f'tokill: {tokill}')
                os.system(tokill)
                print(f'process({pid}): terminated')
    return
def startcolor(output):
    os.system(output)
    return
def index(request):
    return HttpResponse("Hello, welcome to the API for changing the LED colors.")
def rgb(request, r, g, b):
    color = f"\"{r} {g} {b}\""
    statement = f"You're color is {r} {g} {b}"
    output = "sudo python3 /home/pi/Desktop/Led-Server/pidjango/ledcontrol/server.py " + color
    killproc()
    startcolor(output)
    return HttpResponse(statement)

