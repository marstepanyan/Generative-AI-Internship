import requests
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import urljoin

url = 'https://ai.picsart.com/whisper/swagger#/'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    json_url_match = re.search(r"url:\s+'([^']+/openapi\.json)'", response.text)

    if json_url_match:
        json_url = json_url_match.group(1)

        absolute_json_url = urljoin(url, json_url)

        # Send a new request to the JSON URL to get the JSON content
        json_response = requests.get(absolute_json_url)

        # Check if the request to the JSON URL was successful
        if json_response.status_code == 200:
            # Parse the JSON content
            parsed_json = json.loads(json_response.text)

            # print(parsed_json)

        else:
            print(f"Failed to retrieve JSON content. Status code: {json_response.status_code}")

    else:
        print("JSON URL not found in the page.")

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
