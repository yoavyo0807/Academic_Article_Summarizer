import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Example usage
pdf_file_path = r"C:\Users\Yoav\OneDrive\Projects\Academic_Article_Summarizer\myenv\Corpora\Example\Profile.pdf"
text = extract_text_from_pdf(pdf_file_path)
print(text)


