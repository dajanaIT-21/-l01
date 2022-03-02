###################
#    ülesnne10    #
#  Dajana Mähdi   #
#   02.03.2022    #
###################
import re

#IP'd

ip = " "
with open('ül10_asi.txt', 'r') as fail:
    for line in fail:
        if re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line):
            print(line,end="")
            
#Paroolid
with open('ül10_asi.txt', 'r') as fail:
    for line in fail:
        if re.match("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$",line):
            print(line,end="")
        