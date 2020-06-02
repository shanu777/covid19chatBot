import bs4
import requests
from bs4 import BeautifulSoup
import PyPDF2

class TestingGuidelines:
    def __init__(self):
        pass

    def testing_guidelines(self):
        url = 'https://www.mohfw.gov.in/'
        source = requests.get(url).content
        soup = BeautifulSoup(source, 'lxml')
        link_for_domestic_guidelines = soup.find('div', class_='tab-content').ul.li.a.get('href')
        with open('guidlines.pdf', 'wb') as file:
            res = requests.get(link_for_domestic_guidelines).content
            file.write(res)
            pass
        pdffileobj = open('guidlines.pdf', 'rb')
        pdfreader = PyPDF2.PdfFileReader(pdffileobj)
        x = pdfreader.numPages
        pageobj = pdfreader.getPage(0)
        text = pageobj.extractText()
        text = text.replace('\n', "")
        text = text.replace('Page | 1', '')
        return {
            'fulfillmentText': text,
            'source': text
        }