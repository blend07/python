import requests

url = "https://www.wikipedia.org"

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occured: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occured: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occured: {req_err}")