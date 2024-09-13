import tabula

table = tabula.read_pdf("PDFs/weather.pdf", pages=1)

table[0].to_csv('PDFs/output.csv', index=None)
