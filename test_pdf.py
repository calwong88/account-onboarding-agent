# test_pdf.py — delete this after testing
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("test.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = [Paragraph("Hello World", styles["Title"])]
doc.build(story)
print("Created test.pdf")