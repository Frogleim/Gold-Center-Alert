import requests
import time

# Initialize the previous price, alert status, and return response
previous_price = None
alert_status = False
return_response = None
current_price = None


def get_price():
    global previous_price, alert_status, return_response, current_price

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
        current_price = data['rates'][0]['amount_buy_1']
        print(f"Current GolOne Gold Price: ${current_price}")

        if previous_price is not None:
            price_difference = float(current_price) - float(previous_price)
            if abs(price_difference) >= 0.1:
                if price_difference > 0:
                    print("Gold GolOne price increased by 0.1 or more.")
                    alert_status = True
                    return_response = 'Up'
                else:
                    print("Gold GolOne price decreased by 0.1 or more.")
                    alert_status = True
                    return_response = 'Down'
            else:
                alert_status = False
                return_response = None
        else:
            alert_status = False
            return_response = None
        previous_price = current_price

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        alert_status = False
        return_response = None

    return return_response, current_price


if __name__ == '__main__':
    while True:
        alert, response = get_price()
        print(response)
        if alert:
            print(f"Alert: Price change detected ({response}).")
        time.sleep(10)
