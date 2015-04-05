#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
	print "Usage: vrfy.py <target> <users.txt>"
	sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a Socket
connect=s.connect((sys.argv[1],25)) # Connect to the Server
banner=s.recv(1024)		    # Receive the banner
print banner
f = open(sys.argv[2], 'r')	    # open file, read only
for user in f:			    # loop over list
	s.send('VRFY ' + user) #VRFY a user
	result=s.recv(1024)
	print result
s.close()			    # Close the socket
