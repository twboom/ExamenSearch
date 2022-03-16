import json
import requests
from bs4 import BeautifulSoup

data = json.load(open("data.json", "r"))


def get_subjects(year, level):
    categories = data["categories"]
    subjects_urls = []
    for category in categories:
        url = f"https://www.examenblad.nl/item/{category}/{year}/{level}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        subject_list = soup.find("ul", {"class": "seriekeuze"})
        if subject_list is None:
            continue
        links = [link for link in subject_list.find_all("a")]
        for link in links:
            name = link.text.replace("\n", "").strip().replace(level, "")
            if "*" in name:
                continue
            url = f"https://www.examenblad.nl{link.get('href')}"
            subjects_urls.append((name, url))
    return subjects_urls


def get_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        for item in data["ignore"]:
            if item in href:
                break
        for keyword in data["keywords"]:
            if keyword in href and ".pdf" in href:
                href = link.get("href")
                links.append(f"https://www.examenblad.nl{href}")
    return links
    

if __name__ == "__main__":
    complete_files = []
    for year in range(2002, 2020):
        urls = get_subjects(year, "vwo")
        files = []
        for url in urls:
            files.extend(get_files(url))
        complete_files.extend(files)
        print(f"{year}: {len(files)}")
    with open("files.json", "w") as f:
        json.dump(complete_files, f)