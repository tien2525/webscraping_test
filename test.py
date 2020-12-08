from bs4 import BeautifulSoup
import requests

url = "http://www.twitter.com"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

if __name__ == "__main__":
    print(content)