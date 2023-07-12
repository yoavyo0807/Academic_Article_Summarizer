from curses import pair_number
import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.reader.pages[pair_number].extractText()
        return text

# Example of usage
pdf_file_path = r"C:\Users\Yoav\OneDrive\Projects\Academic_Article_Summarizer\myenv\Corpora\Example\Profile.pdf"
text = extract_text_from_pdf(pdf_file_path)

print(text)

