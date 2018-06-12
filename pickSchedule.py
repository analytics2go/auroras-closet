#!/usr/bin/python
##

with open('jobids.txt') as f:
 print f.read()
 
#get the inforamtion  for each job
 for pjob in f.read().split("\n"):
  print pjob 
 
 f.close()