import os, time
import glob
print "Click on each button to control the printer(s).\nOnce you click on a button, be patient. The command will take a moment. \nYou will be notified once finished (~10 seconds)."
print "Images to print:"
l = 0
z = 0
ip = "192.168.1.9"
path_to_watch = "/var/www/html/uploads/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
#  if added: print "Added: ", ", ".join (added)
  if added:
    x=0
    while x != len(added):
	    z = z+1
	    print added[x]
#	    name = added[x].split('_')[1]
            name = added[x]
	    if "pi" in name:
	#	    os.system('echo "'+added[x]+'" > files/'+str(z*3)+'_'+name+'.txt')
		    os.system('cp "/var/www/html/uploads/'+added[x]+'"  files/'+str(z*3)+'-'+name+'-.png')
		    save = added[x]
	#            os.system('mv "Downloads/'+added[x]+'" Downloads/print.png')
	            added[x] = 'print.png'
	            added[x] = added[x].replace (" ", "\ ")
	    if "photo" in name:
	#	    os.system('echo "'+added[x]+'" > files/'+str(z*3)+'_'+name+'.txt')
		    os.system('echo raspberry | sudo -S convert /var/www/html/uploads/'+added[x]+' -rotate 90 /var/www/html/uploads/'+added[x])
		    os.system('cp "/var/www/html/uploads/'+added[x]+'"  files/'+str(z*3)+'-'+name+'-.png')
		    save = added[x]
	#            os.system('mv "Downloads/'+added[x]+'" Downloads/print.png')
	            added[x] = 'print.png'
	            added[x] = added[x].replace (" ", "\ ")
	    if "color" in name:
        #           os.system('echo "'+added[x]+'" > files/'+str(z*3)+'_'+name+'.txt')
                    os.system('cp "/var/www/html/uploads/'+added[x]+'"  color/'+str(z*3)+'-'+name+'-.png')
                    save = added[x]
        #            os.system('mv "Downloads/'+added[x]+'" Downloads/print.png')
                    added[x] = 'print.png'
                    added[x] = added[x].replace (" ", "\ ")
	    x = x + 1
  before = after
