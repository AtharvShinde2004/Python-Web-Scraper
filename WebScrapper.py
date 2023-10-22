import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Extract all the links on the page
            links = soup.find_all('a')
            for link in links:
                print(link.get('href'))

            # You can modify this code to extract other data as needed

        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the web page you want to scrape: ")
    simple_web_scraper(url)
