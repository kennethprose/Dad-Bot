# Dad Bot - A GroupMe Bot

DadBot is a GroupMe bot designed to reply to messages with the oldest dad joke in the book.

For example,

    Son: "Dad i'm hungry"
    Dad: "Hi hungry, I'm Dad"

## Getting Started

These instructions will get the bot up and running on your local machine. These instructions are written for a Linux machine.

### Prerequisites

You need to know your public IP address, the local IP address of the machine you will run the script on, and the port number you wish to use.
Set up port forwarding on your router to forward all packets aimed at your chosen port number to the IP of the machine you will use.

[Create a new bot](https://dev.groupme.com/bots/new) - The callback URL must be in the following form: http://[Public IP]:[Port Number]
Take note of the Bot ID generated after you create the bot.

### Installing

What you need to install on your system.

You must have python3 installed

```
sudo apt install python3.8
```

Install dateutil

```
pip install python-dateutil
```

Finally, download the dadBot.py file. The file location does not matter.

### Configure

Open the dadBot.py file in a text editor.

You must change the variables in the section beggining on line 22.
* botID - The ID that was generated after creating the bot
* botName - What you named your bot when creating the bot
* machineIP - Your machines local IP address
* portNumber - The port number you want to use.

Once you have changed the four variables, save and close the file.

### Starting the bot

Open a terminal and navigate to the directory where you downloaded the dadBot.py file.

Run the following command
```
python3 dadBot.py
```

## Authors

* **Kenneth Rose**

## Veriosn

1.0
