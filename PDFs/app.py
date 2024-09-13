from fpdf import FPDF

pdf = FPDF(orientation="p", unit="pt", format="A4")
pdf.add_page()

pdf.image('PDFs/sample.png')

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=50, txt="Hello", align="C", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=20, txt="more description", ln=1)

pdf.set_font(family="Times", style="B", size=12)
txt1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.output("PDFs/output.pdf")