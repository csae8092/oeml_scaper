import requests
import string
from bs4 import BeautifulSoup
from tqdm import tqdm

from config import BASE_URL

letters = string.ascii_uppercase
page_links = []
for x in tqdm(letters, total=len(letters)):
    url = f"{BASE_URL}/ml/musik_{x}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode("utf-8"), "html.parser")
    for a in soup.find_all('a'):
        link = a.get('href')
        if f"_{x}_" in link:
            new_url = f"{BASE_URL}{link}"
            r = requests.get(new_url)
            nsoup = BeautifulSoup(r.content.decode("utf-8"), "html.parser")
            for na in nsoup.find_all('a'):
                nlink = na.get('href')
                if nlink.endswith('.xml'):
                    page_links.append(nlink)

with open('urls.txt', 'w') as f:
    for line in page_links:
        f.write(f"{line}\n")
