#merge all txt files into one txt files, named with the time down to the milisecond
#1. open a file, read lines, store lines
#2. do that for every file.
#3. store every reading in a variable
# 4. get the time, change it to str
#4. write lines into new file
#5

import glob
import datetime
now = datetime.datetime.now()
nows = now.strftime("%y-%m-%d-%H-%M-%S-%f")+".txt"
files = glob.glob("file*.txt")

master = open(nows, "w")

for file in files:
    with open(file, "r") as f:
        x = f.read()
        master.write(x + "\n")
