import requests
from bs4 import BeautifulSoup as BS
import time

# Initialize the previous price and alert status

previous_price = None
alert_status = False
return_response = ''
current_price = None
price_difference = 0.0
price_threshold = 0.1

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

                if previous_price is not None:
                    price_difference = float(current_price) - float(previous_price)
                    if price_difference >= price_threshold:
                        return_response = "Price goes up"
                        alert_status = True
                    elif price_difference < -price_threshold:
                        return_response = "Price goes down"
                        alert_status = True
                    else:
                        return_response = "Price is stable"
                        alert_status = False

                previous_price = current_price
            else:
                print("Table not found on the webpage.")

    else:
        print("Failed to retrieve the webpage.")
        alert_status = False  # Reset alert status on error


    return price_difference, current_price


if __name__ == '__main__':
    while True:
        alert = go_am()
        if alert:
            print("Alert: Price change detected.")
        time.sleep(10)
