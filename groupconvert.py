#!/usr/bin/python

import sys,re

ppfile = sys.argv[1]

with open(ppfile, 'r') as f:
  lines = f.readlines()
  for i in range(0, len(lines)):
   if "#" not in lines[i]:
      if "group " in lines[i]:
        x = re.findall(r'"([^"]*)"', lines[i])
        y = lines[i+1].split()
        print x[0]
        print y[2].replace(",", "")
