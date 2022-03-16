import PyPDF2
import re
import os


def search_document(document, query) -> list:
    """
    Search a pdf file for a query.
    :param document: The file to search in.
    :param query: The query to search for.
    :return: True if the query was found, False otherwise.
    """
    results = []

    print(f"Searching {document}...")

    # Create the document reader
    pdf_reader = PyPDF2.PdfFileReader(open(document, "rb"), strict=False)
    num_pages = pdf_reader.numPages

    for page in range(num_pages):
        page_content = pdf_reader.getPage(page).extractText()
        if query in page_content:
            results.append(page)
            print("\tFound match on page " + str(page + 1))
    
    return (document, results)

def search_all(query, folder="temp"):
    """
    Search all pdf files in folder and return a list of all files that contain the query.
    :param query: The query to search for.
    :param folder: The folder to search in.
    :return: A list of all files that contain the query.
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        files.extend(filenames)
        break
    
    # Search all files
    results = []
    for file in files:
        results.append(search_document(f"{folder}/{file}", query))
    return results
