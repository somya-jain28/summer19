#!/usr/bin/python3

import socket

target_ip="52.66.50.22"
target_port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM )
while true:
    msg=input("enter your msg: ")
    n=msg.encode('ascii')
    s.sendto(n,(target_ip,target_port))

