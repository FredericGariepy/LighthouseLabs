#!/usr/bin/python3

# LHL script
# https://web.compass.lighthouselabs.ca/p/cyber/days/w03d5/activities/2945

# system
import sys

# regex
import re

# this regex (raw string) will create keys   P?<key_name> and the matching capture groups will be value of the keys.
LOG_LINE_RegEx = r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<timestamp>.*)\]\s"(?P<verb>[A-Z]+)\s(?P<path>[\w\/]+)\s+(?P<protocol>[\w\/\.]+)"\s(?P<status_code>\d+)\s(?P<response_size>\d+).*'

# compiling, is an internal way for the regex library (re) to optimize the regex expression
pattern = re.compile(LOG_LINE_RegEx)

# for loop on  sys.stdin
# wtf is sys.stdin? system standard input: basic meaning; sys.stdin = the file that is passed to the python script
for line in sys.stdin:

  # m is just whatever line matches the pattern 
  m = pattern.match(line)

  # if m, meaning: if there is a match (m)
  if m:
      # groupdic() this is going to turn the matched line into a dictionary, with keys and values 
      # what's a dictionary ? dictionary tutorial: https://www.w3schools.com/python/python_dictionaries.asp
      print(m.groupdict())

# Why use dictionary?
# Actually makes life easier, we can now access specific parts of our lines
# Example print(m.IP)  or m.status_code == 400 do something...
