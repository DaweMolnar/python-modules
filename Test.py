#!/usr/bin/env python2
from net import Network
import libxml2
import libssh2
import socket
import re

doc = libxml2.parseDoc(open('test.xml').read())
ssh_host = doc.xpathEval('//ssh/@host')[0].children
ssh_user = doc.xpathEval('//ssh/@user')[0].children
ssh_pass = doc.xpathEval('//ssh/@pass')[0].children

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((str(ssh_host),22))
session = libssh2.Session()
session.startup(sock)
session.userauth_password(str(ssh_user),str(ssh_pass))
channel = session.open_session()
channel.execute('ip addr')
while True:
    data = channel.read(1024)
    if data == '' or data is None: break
    linelist = data.split('\n')
    for line in linelist:
        if "inet" in line:
            ip = (' '.join(line.split())).split(' ')[1]
            if not(':' in ip):
                print ip.split('/')[0] + " can be pinged: " + str(Network.ping(ip.split('/')[0]))
