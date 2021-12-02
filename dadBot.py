"""
    DadBot is a GroupMe bot designed to reply to messages with the oldest dad joke in the book.

    For example,
    Son: "Dad, I'm hungry"
    Dad: "Hi hungry, I'm Dad"
"""

__author__ = "Kenneth Rose"
__date__ = "12/1/21"
__version__ = "1.3"

from socket import *
import _thread
import json
import requests

# Import data from config
configFile = open('config.json')
config = json.load(configFile)

botID = config['bot_id']
machineIP = config['machine_ip']
portNumber = int(config['port_num'])

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((machineIP, portNumber))
serverSocket.listen(5)


def reply(name):
    response = "Hi " + name + ", I'm Dad"
    data = {
        "bot_id": botID,
        "text": response
    }
    r = requests.post('https://api.groupme.com/v3/bots/post',
                      data=json.dumps(data))


def recieve(connectionSocket):
    # Recieve new message
    post = connectionSocket.recv(4096).decode()

    # Filter out the messages sent by the bot
    senderIndex = post.index('"sender_type":')
    if post[senderIndex+15:senderIndex+18] != "bot":

        # Determine the message that was sent
        textIndex = post.index('"text":') + 8
        userIdIndex = post.index(',"user_id"') - 1
        message = post[textIndex:userIdIndex]

        # Look for any formulation of the work "I'm"
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

        # Extract name when "I'm" is found
        if imIndex != -1 and (message[imIndex - 1] == " " or (imIndex - 1) == -1):
            name = message[imIndex + 3:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            reply(name)

        if i_mIndex != -1 and (message[i_mIndex - 1] == " " or (i_mIndex - 1) == -1):
            name = message[i_mIndex + 4:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            reply(name)

        if i_mIndexApple != -1 and (message[i_mIndexApple - 1] == " " or (i_mIndexApple - 1) == -1):
            name = message[i_mIndexApple + 4:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            reply(name)

        if i_amIndex != -1 and (message[i_amIndex - 1] == " " or (i_amIndex - 1) == -1):
            name = message[i_amIndex + 5:userIdIndex]
            if name[0] == " ":
                name = name[1:]
            if name[-1:] == " ":
                name = name[:-1]
            reply(name)


while True:
    # Accept incoming message and start a new thread to send reply
    connectionSocket, addr = serverSocket.accept()
    _thread.start_new_thread(recieve, (connectionSocket,))
