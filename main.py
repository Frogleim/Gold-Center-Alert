#!/usr/local/bin/python3
# coding: utf-8

__author__ = "Benny <benny.think@gmail.com>"

import logging
import os
import time
from pyrogram import Client, filters, types, raw
from prices import goldandsilver_am, world_price, goldone, gc_price, logs


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
    go_am_price_difference, current_go_am = goldandsilver_am.go_am()
    world_price_difference, world_current = world_price.get_price()
    gold_one_price_difference, gold_one_current = goldone.get_price()
    world_price_bool = False
    gold_and_silver_bool = False
    gold_am_bool = False
    gold_center = gc_price.get_prices()

    print(f'World prices is: {world_current} {world_price_difference}'
          f'Gold and Silver prices is: {current_go_am} {go_am_price_difference}'
          f'GoldOne price is: {gold_one_current} {gold_one_price_difference}')

    # World price alert
    if world_price_difference >= 0.1:
        print('World price changed!')
        world_price_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}\n'
            f'🐸{gold_one_current}\n😎{gold_center}\n🌎 '
            f'{world_current}✅{world_price_difference}'

        )

    elif world_price_difference < -0.1:
        print('World price goes down')
        world_price_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}\n'
            f'🐸{gold_one_current}\n😎{gold_center}\n🌎 '
            f'{world_current}🔻{world_price_difference}'
        )

    else:
        print('World Prices doesnt changed')
    # Gold and Silver price alert

    if gold_one_price_difference >= 0.1:
        print('GoldOne price changed!')
        gold_am_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}✅ {gold_one_price_difference}\n'
            f'🐸{gold_one_current}\n😎{gold_center}\n🌎 '
            f'{world_current}'
        )

    elif gold_one_price_difference < -0.1:
        print('GoldOne price goes down')
        gold_am_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}🔻{go_am_price_difference}\n'
            f'🐸{gold_one_current}\n😎{gold_center}\n🌎 '
            f'{world_current}'
        )

    else:
        print('GoldOne Prices doesnt changed')
    # Gold One price alert

    if go_am_price_difference >= 0.1:
        print('Gold and Silver price changed!')
        gold_and_silver_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}\n'
            f'🐸{gold_one_current}✅{gold_one_price_difference}\n😎{gold_center}\n🌎 '
            f'{world_current}'
        )

    elif go_am_price_difference < -0.1:
        print('Gold and Silver price goes down')
        gold_and_silver_bool = True
        client.send_message(
            chat_id,
            f'💩 {current_go_am}\n'
            f'🐸{gold_one_current}🔻{gold_one_price_difference}\n😎{gold_center}\n🌎 '
            f'{world_current}'
        )

    else:
        print('Gold and Silver doesnt changed')


if __name__ == '__main__':
    app.run()
