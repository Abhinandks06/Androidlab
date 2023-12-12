import requests
def simple_scrapper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Content:")
        print(response.text)
    else:
        print("Failed to fetch the page,Status code.",response.status_code)
url_to_scrape="https://www.geeksforgeeks.org/"
simple_scrapper(url_to_scrape)
