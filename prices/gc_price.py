import time

import requests

previous_gold_center_price = None
price_threshold = 0.1
price_difference = 0.0


def get_prices():
    global previous_gold_center_price, price_difference

    url = "https://api.goldcenter.am/v1/rate/local"

    try:
        r = requests.get(url)
        price = r.json()['data'][0]['buy']

        if previous_gold_center_price is not None:
            price_difference = price - previous_gold_center_price
            if price_difference >= price_threshold:
                return_response = "Price goes up"
                alert_status = True
            elif price_difference < -price_threshold:
                return_response = "Price goes down"
                alert_status = True
            else:
                return_response = "Price is stable"
                alert_status = False
        previous_gold_center_price = price

    except Exception as e:
        return 0, 'Something went wrong', str(e)
    return price_difference, price


if __name__ == '__main__':
    while True:
        price = get_prices()
        print(price)
        time.sleep(10)
