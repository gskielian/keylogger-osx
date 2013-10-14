#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

################################################################################
# Requires Figlet 
################################################################################

import subprocess
import sys, serial
from time import sleep

def file_len(fname):
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
    f.close()
    return i + 1

def main():

  total_lines=file_len("/var/log/keystroke.log")
  aList=[]
  for i in range(0,1000):
    aList.append(total_lines)
  index=0;
  vel_lines=0;
  apm=0;
  while True:
    try:
      total_lines=file_len("/var/log/keystroke.log")
      aList.insert(0,total_lines)
      aList.pop()
      vel_lines = aList[0] - aList[99]
      apm = aList[0] - aList[599]
      subprocess.call("figlet APT = "  + str(vel_lines/10)  + '; figlet APM = ' + str(apm), shell=True)
      sleep(0.1)
      subprocess.call("clear",shell=True) 
    except KeyboardInterrupt:
      print 'exiting'
      break

if __name__ == '__main__':
  main()
