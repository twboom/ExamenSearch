import json
from examenblad import get_subjects, get_files
from db import new_file


data = json.load(open("data.json", "r"))


def import_all():
    start_year = data["year"]["start"]
    end_year = data["year"]["end"]
    levels = data["levels"]

    for year in range(start_year, end_year + 1):
        for level in levels:
            subjects = get_subjects(year, level)
            for subject in subjects:
                files = get_files(subject[1])
                for file in files:
                    period = file.split("/")[5].split("-")[1]
                    document_type = file.split("/")[7].split("-")
                    if len(document_type) > 1:
                        document_type = document_type[0]
                    new_file(file, year, subject[0], level, period, document_type)
                    print(f"Imported {year} {level} {subject[0]} {period} {document_type}")



if __name__ == "__main__":
    # subjects = get_subjects(2021, "vwo")
    # files = get_files(subjects[0][1])
    # [print(file) for file in files]

    import_all()