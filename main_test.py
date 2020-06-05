import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import logging

from sccli.Socketcluster import socket


# const
channel0 = "market.bidoffer"


def on_connect(sock: socket):
    logging.warning("on_connect got called")
    sock.subscribeack(channel0, on_sub_ack)


def on_disconnect(sock: socket):
    logging.warning("on_disconnect got called")


def on_connect_error(sock: socket, err):
    logging.warning("on_connect_error got called: ", err)


def on_message(key, obj):
    logging.warning("got data " + obj + " from key " + key)


def on_sub_ack(channel, error, obj):
    if error is '':
        logging.warning("subscribed successfully to channel " + channel)


if __name__ == "__main__":
    svrAddr = "ws://10.100.50.100:8000/socketcluster/"
    logging.warning("about to connect: %s", svrAddr)
    s = socket(svrAddr)
    s.setBasicListener(on_connect, on_disconnect, on_connect_error)
    s.onchannel(channel0, on_message)
    s.connect()
