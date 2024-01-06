# 4. Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address.
# Hint: You need to get the HTTP response code.
# Another Hint: StackOverflow is your friend


import requests
import sys

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        print(f"The website at {url} is working. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"The website at {url} is not working. Error: {e}")

# Check if the command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python Q_4.py <url>")
else:
    url = sys.argv[1]
    check_website(url)