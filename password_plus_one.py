#!/usr/bin/python
import re
import sys
import os
lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')

def increment(s):
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
    return s

print "[*]Description: This tool takes the output generated from oclHashcat and"
print "increments the digits by one value."
print "[*]To create the input file from cracking: oclHashcat64.exe -m 1000 hashes\hashes.lst --show > ocl_password_list.txt"
print "[*]Example Format: test1:509019:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b::::Password1"


user_input = raw_input("Location of Password List in oclHashcat Format: ")
assert os.path.exists(user_input), "No File Found at , "+str(user_input)


passlist = open(user_input,'r')
newpasslist = open('new_password_list.txt','w')
newpasslist.write('username,newpassword' + "\n")
for line in passlist:
    try:
        ar_split = line.strip().split(":")
        print "User:"+ar_split[0]+",Old Password:"+ar_split[-1] + ",New Password:" + increment(ar_split[-1])
        newpasslist.write(ar_split[0]+","+increment(ar_split[-1]) + "\n")
    except:
        pass
print "[*]Finished"
print "[*]Username/Password list saved to new_password_list.txt"
passlist.close()
newpasslist.close()
