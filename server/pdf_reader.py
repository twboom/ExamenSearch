import PyPDF2
import io
from urllib.request import Request, urlopen

from db import new_pages


def import_document(file_id, document_url):
    """
    Read a pdf file and return the text content.
    :param document: The file to read.
    :return: The text content of the file.
    """
    try:
        remote_file = urlopen(Request(document_url)).read()
    except:
        print(f"Error importing {document_url}")
        return
    memory_file = io.BytesIO(remote_file)
    
    try:
        pdf_reader = PyPDF2.PdfFileReader(memory_file, strict=False)
        num_pages = pdf_reader.numPages

        print(f"Importing {document_url}...")

        page_numbers = []
        text_contents = []

        for page in range(num_pages):
            page_content = pdf_reader.getPage(page).extractText()
            page_numbers.append(page)
            text_contents.append(page_content)
            print(f"\tImported page {page + 1}")

        new_pages(file_id, page_numbers, text_contents)
    except Exception as e:
        print(f"\tError importing {document_url}")