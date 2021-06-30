#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def getcommands():
    usercommands = []
    while True:
        userinput = input('Please provide a command: ')
        usercommands.append(userinput)
        cont = input("Would you like to add another command? Y\N")
        if cont.lower() != "y":
            break
    return usercommands

def hostcollector():
    hostlist = []
    while True:
        ip = input('What is the ip address of this machine?')
        un = input('What is the username of this machine?')
        host = {"ip": ip, "un": un}
        hostlist.append(host)
        usercommands.append(userinput)
        cont = input("Would you like to add another host? Y\N")
        if cont.lower() != "y":
            break
    return hostlist

def main():

   credz = hostcollecter()

   our_commands = usercommands

   mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## create session object
  for cred in credz:
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
    ## create SSH connection
    sshsession.connect(hostname=cred["ip"], username=cred["un"], pkey=mykey)
    #our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    for x in our_commands: 
      ## call our imported function and save the value returned
      resp = cmdissue(x, sshsession)
      ## if returned response is not null, print it out
      if resp != "":
         with open("results.log", "a") as logger:
             print(cred["un"], "\n", resp, file=logger)
  
      ## end the SSH connection
      sshsession.close()

if __name__ == '__main__':
  main()

