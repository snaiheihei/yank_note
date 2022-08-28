from pdf2docx import Converter

cv = Converter("3.pdf")
cv.convert("3.docx", start=0, end=None)

cv.close()