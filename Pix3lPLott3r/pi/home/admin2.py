from tkinter import *
import socket,os,time
from tkinter import messagebox as tkMessageBox
os.system('cd ~/; rm lock/*')
os.system('irxevent &')
def hostname_resolves(hostname):
#    try:
#        socket.gethostbyname(hostname)
#        return 1
#    except socket.error:
#        return 0
	response = os.system('ping -i 0.2 -c 1 '+ hostname)
	if response == 0:
		return 1
	else:
		return 0

x = 0
y = 0
z = 0
a = 0

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="Start Hotspot", fg="red",
                         command=self.hotspot)
    self.button.pack(side=LEFT)

    self.button = Button(frame,
                         text="Printer Status", fg="black",
                         command=self.check)
    self.button.pack(side=LEFT)
    self.button = Button(frame,
                         text="Activate 1", fg="black",
                         command=self.start1)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Activate 2",
                         command=self.start2)
    self.slogan.pack(side=LEFT)
    self.btn = Button(frame,
                         text="Activate 3",
                         command=self.start3)
    self.btn.pack(side=LEFT)

    self.button = Button(frame, 
                         text="Cancel Print 1", fg="black",
                         command=self.end1)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Cancel Print 2",
                         command=self.end2)
    self.slogan.pack(side=LEFT)
    self.btn = Button(frame,
                         text="Cancel Print 3",
                         command=self.end3)
    self.btn.pack(side=LEFT)
    termf = Frame(root, width = 400, height = 200)

    termf.pack(fill=BOTH, expand=YES)
    wid = termf.winfo_id()
    os.system('xterm -into %d -geometry 80x20 -sb -e python2 printer3.py &' % wid)
    termf = Frame(root, width = 400, height = 150)

    termf.pack(fill=BOTH, expand=YES)
    wid = termf.winfo_id()
    os.system('xterm -into %d -geometry 80x20 -sb -e python2 out.py &' % wid)

    b = Button(master, text="End all printers", command=self.end)
    b.pack()


  def check(self):
      printer1 = hostname_resolves('192.168.150.2') 
#      printer1 = hostname_resolves('google.com') 
      printer2 = hostname_resolves('192.168.150.3') 
      printer3 = hostname_resolves('192.168.150.4')
      if printer1 == 0:
          text1 = "Printer 1 Offline\n"
      else:
          text1 = "Printer 1 Online\n"
      if printer2 == 0:
          text2 = "Printer 2 Offline\n"
      else:
          text2 = "Printer 2 Online\n"
      if printer3 == 0:
          text3 = "Printer 3 Offline\n"
      else:
          text3 = "Printer 3 Online\n"
      print(printer1)
      print(printer2)
      text = text1 + text2 + text3
      print(text)
      tkMessageBox.showinfo( "Status", text)
  def hotspot(self):
    print("Hotspot Starting")
    global a
    if a != 1:
#       os.system('echo seshan | sudo -S ifconfig wlan0 down')
       os.system('echo raspberry | sudo -S hotspot start &')
       a = 1
    else :
            os.system('echo raspberry | sudo -S hotspot stop ; echo raspberry | sudo -S killall hotspot')
            a = 0
    tkMessageBox.showinfo( "Done", "Done")
  def end1(self):
    print("Ending1")
    os.system('sshpass -p mindstorms ssh robot@192.168.150.2 "echo mindstorms | sudo -S killall python" ; sshpass -p seshan ssh robot@192.168.150.2 "echo mindstorms | sudo -S python ~/reset.py"')
    tkMessageBox.showinfo( "Done", "Done")
  def end2(self):
    print("Ending2")
    os.system('sshpass -p seshan ssh sanjay@192.168.150.3 "echo seshan | sudo -S killall python"')
    tkMessageBox.showinfo( "Done", "Done")
  def end3(self):
    print("Ending3")
    os.system('sshpass -p seshan ssh robot@192.168.150.4 "echo seshan | sudo -S killall python"')
    tkMessageBox.showinfo( "Done", "Done")
  def start1(self):
    print("start1")
    global x
    if x != 1:
      os.system('cd ~/; python sendcolorp1.py &')
      time.sleep(1)
      os.system('cd ~/; python sendp1.py &') 
      tkMessageBox.showinfo( "Done", "Done")
    x = 1
  def start2(self):
    print("start2")
    global y
    if y != 1:
       os.system('cd ~/; python sendp2.py &')
       tkMessageBox.showinfo( "Done", "Done")
    y = 1
  def start3(self):
    print("start3")
    global z
    if z != 1:
        os.system('cd ~/; python sendp3.py &')
        tkMessageBox.showinfo( "Done", "Done")
    z = 1
  def end(self):
    os.system('killall python')
    global x
    global y
    global z
    x = 0
    y = 0
    z = 0
root = Tk()
root.wm_title('PIX3L PLOTT3R Control Panel')
text = Text(root)
app = App(root)
root.mainloop()


#import tkinter as Tkinter
#from tkinter import messagebox as tkMessageBox
#top = Tkinter.Tk()
#
#def helloCallBack():
#   tkMessageBox.showinfo( "Hello Python", "Hello World")
#
#B = Tkinter.Button(top, text ="Cancel Print 1", command = helloCallBack)
#B = Tkinter.Button(top, text ="Cancel Print 2", command = helloCallBack)
#B = Tkinter.Button(top, text ="Cancel Print 3", command = helloCallBack)

#B.pack()
#top.mainloop()


