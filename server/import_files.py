import json
from examenblad import get_subjects, get_files
from db import new_file, fetch_files
from pdf_reader import import_document


data = json.load(open("data.json", "r"))


def import_content(start_year=data["year"]["start"], end_year=data["year"]["end"]):
    files = fetch_files(start_year, end_year)
    for file in files:
        import_document(file[0], file[1])


def import_files():
    start_year = data["year"]["start"]
    end_year = data["year"]["end"]
    levels = data["levels"]

    for year in range(start_year, end_year + 1):
        for level in levels:
            subjects = get_subjects(year, level)
            for subject in subjects:
                files = get_files(subject[1])
                for file in files:
                    period = file.split("/")[5].split("-")
                    if len(period) == 2:
                        period = period[1]
                    else:
                        period = period[0]
                    document_type = file.split("/")[7].split("-")[0]
                    new_file(file, year, subject[0], level, period, document_type)
                    print(f"Imported {year} {level} {subject[0]} {period} {document_type}")



if __name__ == "__main__":
    # import_files()
    import_content(start_year=2007)