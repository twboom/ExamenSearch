from msilib import sequence
import os
import shutil
import requests

from examenblad import get_assignments_from_year_for_subject
from pdf_search import search_all


def downloadFile(url, file_name):
    with open(f"temp/{file_name}", "wb") as file:
        response = requests.get(url)
        file.write(response.content)


def search():
    query = input("\nPlease enter your search query: ")
    print(f"Searching for {query}...")
    print("This might take a while...")
    search_results = search_all(query)
    print("\nPress ctrl+c (or command+c) to stop the program.")
    search()


if __name__ == "__main__":
    if not os.path.exists('temp'):
        os.mkdir('temp')

    print("ExamenSearch")
    subject = input("Subject: ")
    print(f"Getting exams for {subject}...")
    print("This might take a while...")

    # Start search
    print("Gathering links...")
    links = []
    for year in range(2002, 2022):
        link_list = get_assignments_from_year_for_subject(subject, year)
        print(f"\tFound {len(link_list)} exams for year {year}")
        links += link_list
    
    print(f"Found {len(links)} exams in total")

    print("\nDownloading the exams...")
    for link in links:
        file_name = link.split('/')[-1]
        if os.path.isfile(f"temp/{file_name}"):
            print(f"\tSkipping {file_name}")
        else:
            downloadFile(link, file_name)
            print(f"\tDownloaded {file_name}")
    print("Downloaded all exams")

    print("\nStarting your searching journey!")
    search()

    # Delete temp folder
    # shutil.rmtree('temp')