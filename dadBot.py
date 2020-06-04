"""
    DadBot is a GroupMe bot designed to reply to messages with the oldest dad joke in the book.

    For example,
    Son: "Dad i'm hungry"
    Dad: "Hi hungry, I'm Dad"
"""

__author__ = "Kenneth Rose"
__date__ = "6/4/20"
__version__ = "1.2"

from socket import *
import sys
import _thread
import json
import requests

#
# FILL THIS OUT
#
botID = "[Replace with Bot ID]"
machineIP = "[Replace with your local machine IP address]" # Ex. "192.168.0.1"
portNumber = 1111 # You can change this
#
# FILL THIS OUT
#

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((machineIP, portNumber))
serverSocket.listen(5)

def reply(connectionSocket):
    post = connectionSocket.recv(4096).decode()
    senderIndex = post.index('"sender_type":')
    if post[senderIndex+15:senderIndex+18] != "bot":
        textIndex = post.index('"text":') + 8
        userIdIndex = post.index(',"user_id"') - 1
        message = post[textIndex:userIdIndex]
        try:
            imIndex = message.casefold().index("im ")
        except:
            imIndex = -1
        try:
            i_mIndex = message.casefold().index("i'm ")
        except:
            i_mIndex = -1
        try:
            i_mIndexApple = message.casefold().index("i’m ")
        except:
            i_mIndexApple = -1
        try:
            i_amIndex = message.casefold().index("i am ")
        except:
            i_amIndex = -1
            
        if imIndex != -1 and (message[imIndex - 1] == " " or (imIndex - 1) == -1):
            name = message[imIndex + 3:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            response = "Hi " + name + ", I'm Dad"
            data = {
                "bot_id": botID,
                "text": response
            }
            r = requests.post('https://api.groupme.com/v3/bots/post', data)
            print(response)

        if i_mIndex != -1 and (message[i_mIndex - 1] == " " or (i_mIndex - 1) == -1):
            name = message[i_mIndex + 4:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            response = "Hi " + name + ", I'm Dad"
            data = {
                "bot_id": botID,
                "text": response
            }
            r = requests.post('https://api.groupme.com/v3/bots/post', data)
            print(response)

        if i_mIndexApple != -1 and (message[i_mIndexApple - 1] == " " or (i_mIndexApple - 1) == -1):
            name = message[i_mIndexApple + 4:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            response = "Hi " + name + ", I'm Dad"
            data = {
                "bot_id": botID,
                "text": response
            }
            r = requests.post('https://api.groupme.com/v3/bots/post', data)
            print(response)
            
        if i_amIndex != -1 and (message[i_amIndex - 1] == " " or (i_amIndex - 1) == -1):
            name = message[i_amIndex + 5:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            response = "Hi " + name + ", I'm Adam"
            data = {
                "bot_id": botID,
                "text": response
            }
            r = requests.post('https://api.groupme.com/v3/bots/post', data)
            print(response)

while True:
    connectionSocket, addr = serverSocket.accept()
    _thread.start_new_thread(reply, (connectionSocket,))
