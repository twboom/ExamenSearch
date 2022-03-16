from ast import Sub
import json
import requests
from bs4 import BeautifulSoup

def get_subjects(year, level):
    categories = ["talen", "exacte-vakken", "maatschappijvakken", "kunstvakken-en-lo"]
    subjects_urls = []
    for category in categories:
        url = f"https://www.examenblad.nl/item/{category}/{year}/{level}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        subject_list = soup.find("ul", {"class": "seriekeuze"})
        links = [link for link in subject_list.find_all("a")]
        for link in links:
            url = f"https://www.examenblad.nl{link.get('href')}"
            subjects_urls.append(url)
    return subjects_urls

def get_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if "opgaven" in href and ".pdf" in href:
            href = link.get("href")
            links.append(f"https://www.examenblad.nl{href}")
    return links
    

if __name__ == "__main__":
    for year in range(2002, 2020):
        urls = get_subjects(year, "vwo")
        files = []
        for url in urls:
            files.extend(get_files(url))
        print(f"{year}: {len(files)}")