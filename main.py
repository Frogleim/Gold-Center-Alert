#!/usr/local/bin/python3
# coding: utf-8

__author__ = "Benny <benny.think@gmail.com>"

import logging
import os
import time
from pyrogram import Client, filters, types, raw
from prices import goldandsilver_am, world_price, goldone, gc_price

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s [%(levelname)s]: %(message)s')

PROXY = os.getenv("PROXY")
TOKEN = os.getenv("TOKEN")
APP_ID = os.getenv("APP_ID")
APP_HASH = os.getenv("APP_HASH")

DC_MAP = {
    1: "Miami",
    2: "Amsterdam",
    3: "Miami",
    4: "Amsterdam",
    5: "Singapore"
}


def create_app():
    _app = Client("redirect_bot",
                  bot_token='6676961848:AAHfGFa7QCjt4hZB-QlD6PtkZVEPomQnt7M')
    if PROXY:
        _app.proxy = dict(
            scheme="socks5",
            hostname=PROXY.split(":")[0],
            port=int(PROXY.split(":")[1])
        )

    return _app


app = create_app()
service_count = 0


@app.on_message(filters.command(["start"]))
def start_handler(client: "Client", message: "types.Message"):
    chat_id = 5517438705
    client.send_message(chat_id, 'Starting to send messages!')
    previous_go_am_alert = None  # Initialize previous alerts to None
    previous_world_price_alert = None
    previous_gold_one_alert = None

    while True:
        go_am_alert, go_am_current_price, price_difference = goldandsilver_am.go_am()
        world_price_alert, world_current_price, price_difference = world_price.get_price()
        gold_one_alert, gold_one_current_price, price_difference = goldone.get_price()
        print(gold_one_current_price)
        gold_center = gc_price.get_prices()

        if go_am_alert != previous_go_am_alert:  # Check if the alert has changed
            if go_am_alert == 'Up':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}✅ {price_difference}\n'
                                             f'🐸GO - {gold_one_current_price}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}')
            elif go_am_alert == 'Down':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}🔻 {price_difference}\n'
                                             f'🐸GO - {gold_one_current_price}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}')
            previous_go_am_alert = go_am_alert  # Update previous alert

        if world_price_alert != previous_world_price_alert:
            if world_price_alert == 'Up':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}\n'
                                             f'🐸GO - {gold_one_current_price}✅ {price_difference}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}')
            elif world_price_alert == 'Down':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}\n'
                                             f'🐸GO - {gold_one_current_price}🔻 {price_difference}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}')
            previous_world_price_alert = world_price_alert

        if gold_one_alert != previous_gold_one_alert:
            if gold_one_alert == 'Up':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}\n'
                                             f'🐸GO - {gold_one_current_price}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}✅ {price_difference}')
            elif gold_one_alert == 'Down':
                client.send_message(chat_id, f'💩G&S - {go_am_current_price}\n'
                                             f'🐸GO - {gold_one_current_price}\n😎GC-{gold_center}\n🌎 '
                                             f'Price - {world_current_price}🔻 {price_difference}')
            previous_gold_one_alert = gold_one_alert

        time.sleep(10)


if __name__ == '__main__':
    app.run()
