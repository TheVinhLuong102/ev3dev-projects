#!/usr/bin/python
import glob,os,time
import os.path
from lockfile import LockFile
ip = "192.168.150.7"
print('hi')
while True:
  lock = LockFile("lock/lock")
  print "waiting for lock"
  time.sleep(0.5)
  lock.acquire()
  print "got lock"
  time.sleep(5)
  array = sorted(glob.glob("files/*.png"))
  if array != []:
   print array[0]
#   txt = open(''+array[0])
#   txt = txt.read()
   os.system('rm '+array[0])
   lock.release()
   print "released and printing"
#   print(txt)
   time.sleep(0)
#   txt = txt.split('\n')[0]
   lock2 = LockFile("lockcolor/lock")
   print "waiting for COLOR"
   name = array[0].split('-')[1]
#   if name != "pic":
   print name
   lock2.acquire()
   print "MONOCHROME ACTIVATED"
   os.system('sshpass -p mindstorms scp "/var/www/html/uploads/'+name+'" robot@'+ip+':~/')
#   time.sleep(300)
#   myvar = input("release mo>")
   print "printmo"
   os.system('sshpass -p mindstorms ssh -t robot@'+ip+' "~/printer.sh \''+name+'\'"')
   lock2.release()
#   else:
#    os.system('sshpass -p seshan scp "/var/www/html/uploads/'+txt+'" robot@'+ip+':~/')
#    os.system('sshpass -p seshan ssh -t robot@'+ip+' "~/printercam.sh \''+txt+'\'"')
   print "done"
