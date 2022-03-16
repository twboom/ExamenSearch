from distutils.log import error
from django.forms import TypedChoiceField
import requests
from bs4 import BeautifulSoup


def get_assignments_from_year_for_subject(subject, year):
    subject = subject.lower()
    url = f"https://www.examenblad.nl/examen/biologie-vwo-2/{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a", href=True):
        if "opgaven" in link.get("href") and subject in link.get("href"):
            href = link.get("href")
            links.append(f"https://www.examenblad.nl{href}")
    return links


if __name__ == "__main__":
    print(get_assignments_from_year_for_subject('biologie', 2020))