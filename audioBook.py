import pyttsx3
import PyPDF2

nameBook = input("Sach can doc: ")
book=open(nameBook, "rb")       #rb:read binary

pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
bot=pyttsx3.init()

voices=bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)
bot.setProperty('rate', 125)        #set up a new voice rate

for num in range(8, pages):
    page=pdfReader.getPage(24)
    text=page.extractText()
    bot.say(text)
    bot.runAndWait()