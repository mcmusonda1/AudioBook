import pyttsx3
import PyPDF2

# Enter your pdf path
book = open(input('Enter the name of the book you want to be read: \n'), 'rb')
Reader = PyPDF2.PdfFileReader(book)

print("Am reading from the book you chose, \n relax and enjoy")
Read = pyttsx3.init()

# Input the range of where to start reading from and end on

for num in range(input('Please enter the number of the page I should start reading from: \n'), input('Please enter the page number of were I should end on reading: \n')):
    page = Reader.getPage(num)
    text = page.extractText()
    Read.say(text)
    Read.runAndWait()


print("We are reading from " + book + " " + num)