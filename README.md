# Dad Bot - A GroupMe Bot

DadBot is a GroupMe bot designed to reply to messages with the oldest dad joke in the book.

For example,

    Son: "Dad, I'm hungry"
    Dad: "Hi hungry, I'm Dad"

## Getting Started

These instructions will get the bot up and running on your local machine.

## Prerequisites

You'll need to know:

- Your public IP
- The local IP of the machine the bot will run on
- An unused port

You will also have to set up port forwarding on your router to direct all packets aimed at your chosen port number to the IP of your host machine.

[Create a new bot](https://dev.groupme.com/bots/new) - The callback URL must be in the following form:

```
http://[Public_IP]:[Port_Number]
```

Take note of the Bot ID generated after you create the bot.

## Installing

You must have [Python](https://www.python.org/) installed.

You will also need Python [Requests](https://docs.python-requests.org/en/latest/). You can install Requests using [pip](https://pypi.org/project/pip/).

Finally, download the source files. The location does not matter.

## Configure

Open the config.json file in a text editor.

You must set these values:

- bot_id - The ID that was generated after creating the bot. You can find it again [here](https://dev.groupme.com/bots).
- machine_ip - The host machine's local IP address. (Ex. 192.168.0.100)
- port_num - The port number you want to use. (Default: 1111)

Once you have changed these values, save and close the file.

## Starting the bot

Open a terminal and navigate to the directory where you downloaded the source files.

Run the following command:

```
python dadBot.py
```

or

```
python3 dadBot.py
```

## Help

If you have any issues installing or running the bot, feel free to reach out to me or create a new issue. I will do my best to reply.

## Authors

- **Kenneth Rose**

## Veriosn

1.3
