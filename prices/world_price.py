import yfinance as yf
import time
from dataclasses import dataclass

previous_price = None
alert_status = False
return_response = ''
current_price = None
price_difference = 0.0
price_threshold = 0.1


def get_price():
    global previous_price, alert_status, return_response, current_price, price_difference

    gold_ticker = yf.Ticker("GC=F")
    gold_data = gold_ticker.history(period="1d")

    if not gold_data.empty:
        gold_price = round(float(gold_data['Close'].iloc[-1]), 1)
        gold_price = gold_price / 31.1

        if previous_price is not None:

            price_difference = gold_price - previous_price

            print(f'Prices difference: {price_difference}')
            if price_difference >= price_threshold:
                return_response = "Price goes up"
                alert_status = True
            elif price_difference < -price_threshold:
                return_response = "Price goes down"
                alert_status = True
            else:
                return_response = "Price is stable"
                alert_status = False

        previous_price = gold_price

    else:
        print("Could not fetch live gold price data.")
        alert_status = False  # Reset alert status on error
    return price_difference, gold_price




if __name__ == '__main__':
    while True:
        cur, diff = get_price()
        print(diff)
        time.sleep(10)
