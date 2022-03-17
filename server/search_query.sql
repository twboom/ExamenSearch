SELECT file_id
FROM page
WHERE CONTAINS(text_content, q)