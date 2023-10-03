import time

import yfinance as yf

# Create a ticker object for gold (XAU/USD)
previous_price = None
alert_status = False
return_response = ''
current_price = None


def get_price():
    global previous_price, alert_status, return_response, current_price

    gold_ticker = yf.Ticker("GC=F")
    gold_data = gold_ticker.history(period="1d")

    if not gold_data.empty:
        gold_price = round(float(gold_data['Close'].iloc[-1]), 1)
        gold_price = gold_price / 31.1

        if gold_price:
            current_price = round(gold_price, 1)
            print(f"Current World Gold Price: ${current_price}")

            if previous_price is not None:
                price_difference = float(current_price) - float(previous_price)
                if abs(price_difference) >= 0.1:
                    if price_difference > 0:
                        print("World Gold price increased by 0.1 or more.")
                        alert_status = True
                        return_response = 'Up'

                    else:
                        print("World Gold price decreased by 0.1 or more.")
                        alert_status = True
                        return_response = 'Down'

                else:
                    alert_status = False  # Reset alert status if no alert
            else:
                alert_status = False
            previous_price = current_price

    else:
        print("Could not fetch live gold price data.")
        alert_status = False  # Reset alert status on error

    return return_response, current_price


if __name__ == '__main__':
    while True:
        alert = get_price()
        if alert:
            print("Alert: Price change detected.")
        time.sleep(10)
