import requests
import time

# Initialize the previous price, alert status, and return response
previous_price = None
alert_status = False
return_response = None
current_price = None
price_difference = 0.0
price_threshold = 0.1


def get_price():
    global previous_price, alert_status, return_response, current_price, price_difference

    url = 'https://goldone.am/get_rates'

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
        "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "your_xsrf_token_here",  # Replace with your XSRF token
        "cookie": "your_cookie_here",  # Replace with your cookie
        "Referer": "https://goldone.am/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        current_price = data['rates'][0]['amount_sell_1']
        current_price = round(current_price, 3)
        if previous_price is not None:
            price_difference = current_price - previous_price
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
        alert_status = False
        return_response = None
    return price_difference, current_price


if __name__ == '__main__':
    while True:
        curr, prev = get_price()
        print(curr)
        print(prev)
        time.sleep(10)