import pyttsx3
import PyPDF2

book = open('book.pdf', 'rb')
Reader = PyPDF2.PdfFileReader(book)


Read = pyttsx3.init()
for num in range(10, 12):
    page = Reader.getPage(num)
    text = page.extractText()
    Read.say(text)
    Read.runAndWait()