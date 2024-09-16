from pdfminer.high_level import extract_text

# test commit
text = extract_text("PDFs/output.pdf")
print(text)
