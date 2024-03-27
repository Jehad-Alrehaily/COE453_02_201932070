import requests


def call_api():
    url = "https://api-details-d37u9yt9.ew.gateway.dev/mul"
    payload = {
        "num1": 5,
        "num2": 3
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        # Process the data returned by the API
        # ...
        print(data)
    except requests.exceptions.RequestException as e:
        print("Error calling the API:", e)


call_api()
