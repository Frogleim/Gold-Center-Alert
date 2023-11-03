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
                  '25264213',
                  'cbcd2efa0b73666b48af032714d86a73',
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
    chat_id = -4086530854
    client.send_message(chat_id, 'Starting to send messages!')
    while True:
        goldandsilver_am_difference, goldandsilver_am_current = goldandsilver_am.go_am()
        world_price_difference, world_current = world_price.get_price()
        gold_one_price_difference, gold_one_current = goldone.get_price()
        world_price_bool = False
        gold_and_silver_bool = False
        gold_am_bool = False
        gold_center_difference, gold_center_price = gc_price.get_prices()

        print(f'World prices is: {world_current} {world_price_difference}'
              f'Gold and Silver prices is: {goldandsilver_am_current} {goldandsilver_am_difference}'
              f'GoldOne price is: {gold_one_current} {gold_one_price_difference}')

        # World price alert
        # if world_price_difference >= 0.1:
        #     print('World price changed!')
        #     world_price_bool = True
        #     client.send_message(
        #         chat_id,
        #         f'🌎{round(world_current, 1)}(✅ +{round(world_price_difference, 1)}$)'
        #
        #     )
        #
        # elif world_price_difference < -0.1:
        #     print('World price goes down')
        #     world_price_bool = True
        #     client.send_message(
        #         chat_id,
        #         f'🌎{round(world_current, 1)}(🔻 -{round(world_price_difference, 1)}$)'
        #     )
        #
        # else:
        #     print('World Prices doesnt changed')
        # # GoldONE price alert

        if gold_one_price_difference >= 0.1:
            print('GoldOne price changed!')
            gold_am_bool = True
            client.send_message(
                chat_id,
                f'🐸{round(float(gold_one_current), 1)}(✅ +{round(float(gold_one_price_difference), 1)}$)'
            )

        elif gold_one_price_difference < -0.1:
            print('GoldOne price goes down')
            gold_am_bool = True
            client.send_message(
                chat_id,
                f'🐸{round(float(gold_one_current), 1)}(🔻 -{round(float(gold_one_price_difference), 1)}$)'
            )

        else:
            print('GoldOne Prices doesnt changed')
        # Gold and Silver price alert

        if goldandsilver_am_difference >= 0.1:
            print('Gold and Silver price changed!')
            gold_and_silver_bool = True
            client.send_message(
                chat_id,
                f'💩{round(float(goldandsilver_am_current), 1)}(✅ +{round(float(goldandsilver_am_difference), 1)}$)'
            )

        elif goldandsilver_am_difference < -0.1:
            print('Gold and Silver price goes down')
            gold_and_silver_bool = True
            client.send_message(
                chat_id,
                f'💩{round(float(goldandsilver_am_current), 1)}(🔻 -{round(float(goldandsilver_am_difference), 1)}$)'
            )

        else:
            print('Gold and Silver doesnt changed')

        # Gold Center
        if gold_center_difference >= 0.1:
            print('Gold and Silver price changed!')
            gold_and_silver_bool = True
            client.send_message(
                chat_id,
                f'😎{round(float(gold_center_price), 1)}(✅ +{round(float(gold_center_difference), 1)}$)'
            )

        elif gold_center_difference < -0.1:
            print('Gold and Silver price goes down')
            gold_and_silver_bool = True
            client.send_message(
                chat_id,
                f'😎{gold_center_price} (🔻 -{round(float(gold_center_difference), 1)}$)'
            )

        else:
            print('Gold and Silver doesnt changed')

        time.sleep(10)


if __name__ == '__main__':
    app.run()
