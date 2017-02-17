#!/usr/bin/python
##########
# A python script to take an old puppet 2 groups file
# and convert it into yaml for a hiera database
# in Puppet Enterprose 4
##########
import sys,re

ppfile = sys.argv[1]

with open(ppfile, 'r') as f:
  lines = f.readlines()
  for i in range(0, len(lines)):
   if "#" not in lines[i]:
      if "group " in lines[i]:
        x = re.findall(r'"([^"]*)"', lines[i])
        y = lines[i+1].split()
        print "  %s:" % x[0]
        print "    ensure: 'present'"
        print "    gid: %s" % y[2].replace(",", "")
