from django.shortcuts import render
from django.http import HttpResponse
import time
import os,signal
from threading import Thread
# Create your views here.

def killproc():
    path = os.getcwd() + '/ledcontrol/server.py' 
    path_list = f'ps ax | grep {path}'
    print("---------------------- Process Information --------------------");
    #for lines in os.popen('ps ax | grep /home/pi/Desktop/pidjango/ledcontrol/server.py'):
    for lines in os.popen(path_list):
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
def startcolorserver(output):
    os.system(output)
    return
def index(request):
    return HttpResponse("Hello, welcome to the API for changing the LED colors.")
def rgb(request, r, g, b):
    directory_path = os.getcwd()
    directory_path = directory_path + "/ledcontrol/server.py " # make it the path to the server listening to mcu
    color = f"\"{r} {g} {b}\"" # string that gets sent to mcu 
    statement = f"You're color is {r} {g} {b}.\npwd: {directory_path}"
    output = "sudo python3 " + directory_path + color
    print(f"command: {output}")
    killproc()
    startcolorserver(output)
    return HttpResponse(statement)

