import time

import requests


def get_prices():
    url = "https://api.goldcenter.am/v1/rate/local"

    try:
        r = requests.get(url)
        price = r.json()['data'][0]['buy']
        return price
    except Exception:
        return 'Something went wrong'


if __name__ == '__main__':
    while True:
        price = get_prices()
        print(price)
        time.sleep(10)
