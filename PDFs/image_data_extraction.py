from pdfminer.high_level import extract_text

text = extract_text("PDFs/output.pdf")
print(text)