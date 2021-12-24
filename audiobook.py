import pyttsx3
import PyPDF2

book = open(input('Enter the name of the book you want to be read: \n'), 'rb')
Reader = PyPDF2.PdfFileReader(book)

print("Am reading from the book you chose, \n relax and enjoy")
Read = pyttsx3.init()
for num in range(10, 12):
    page = Reader.getPage(num)
    text = page.extractText()
    Read.say(text)
    Read.runAndWait()


print("We are reading from " + book + " " + num)