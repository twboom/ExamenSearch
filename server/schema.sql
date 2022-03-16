CREATE TABLE IF NOT EXISTS file (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    year INTEGER,
    subject TEXT,
    level TEXT,
    period INTEGER,
    document_type TEXT,
    UNIQUE(url, year, subject, level, period, document_type)
);

CREATE TABLE IF NOT EXISTS page (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    page_number INTEGER,
    text_content TEXT,
    FOREIGN KEY(file_id) REFERENCES file(id)
    UNIQUE(file_id, page_number)
);