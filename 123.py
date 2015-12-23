#usr/bin/python

#import pxssh
#import except

host="{115.160.137.166,183.60.203.30,183.60.203.12,183.60.203.58,122.226.189.5,115.160.137.167,103.42.178.2,23.226.48.122,23.226.48.114,43.226.48.106,43.229.115.250,43.229.115.10}"
user='root'
passwd='123QWE'
#x="input_raw"

x=input("Enter you want to conncetion IP:")

#def main(user,passwd,x):
   # if x in host:
   #    try:
           s = pxssh.pxssh()
           s.login(host,user,passwd)
           return s
          
  #  main()
 #       
