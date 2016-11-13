import glob,os,time
import os.path
from lockfile import LockFile
ip = "192.168.150.3"
while True:
  lock = LockFile("lock/lock")
  print "waiting for lock"
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
   name = array[0].split('-')[1]
#   if name != "pic":
   os.system('sshpass -p seshan scp "/var/www/html/uploads/'+name+'" robot@'+ip+':~/')
   os.system('sshpass -p seshan ssh -t robot@'+ip+' "~/printer.sh \''+name+'\'"')
#   else:
#    os.system('sshpass -p seshan scp "/var/www/html/uploads/'+txt+'" robot@'+ip+':~/')
#    os.system('sshpass -p seshan ssh -t robot@'+ip+' "~/printercam.sh \''+txt+'\'"')
   print "done"
