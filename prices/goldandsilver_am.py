import requests
from bs4 import BeautifulSoup as BS
import time

# Initialize the previous price and alert status
previous_price = None
alert_status = False
return_response = ''
current_price = None
price_difference = 0.0


def go_am():
    global previous_price, alert_status, return_response, price_difference, current_price

    url = 'http://goldandsilver.am/'
    r = requests.get(url)

    if r.status_code == 200:
        soup = BS(r.text, "html.parser")
        main_table = soup.find('table', {'class': 'gold-table goldtbl'})

        if main_table:
            td_elements = main_table.find_all('td')
            prices = [td.get_text() for i, td in enumerate(td_elements) if i < 3]

            if all(prices):
                current_price = prices[1]
                print(f"Current GoldandSilver Gold Price: ${current_price}")

                if previous_price is not None:
                    price_difference = float(current_price) - float(previous_price)
                    if abs(price_difference) >= 0.1:
                        if price_difference > 0:
                            print("Gold GoldandSilver price increased by 0.1 or more.")
                            alert_status = True
                            return_response = 'Up'

                        else:
                            print("Gold GoldandSilver price decreased by 0.1 or more.")
                            alert_status = True
                            return_response = 'Down'

                    else:
                        alert_status = False  # Reset alert status if no alert
                else:
                    alert_status = False

                previous_price = current_price

    else:
        print("Failed to retrieve the webpage.")
        alert_status = False  # Reset alert status on error

    return return_response, current_price, round(price_difference, 2)


if __name__ == '__main__':
    while True:
        alert = go_am()
        if alert:
            print("Alert: Price change detected.")
        time.sleep(10)
