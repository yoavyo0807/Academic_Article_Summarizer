import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text

# Example of usage
pdf_file_path = ''
text = extract_text_from_pdf(pdf_file_path)

print(text)

