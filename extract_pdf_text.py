import pdfplumber

pdf_path = "Python Programming.pdf"

with pdfplumber.open(pdf_path) as pdf:
    all_text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            all_text += page_text + "\n"

with open("extracted_questions.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Text extraction complete. Check 'extracted_questions.txt' for the content.")
