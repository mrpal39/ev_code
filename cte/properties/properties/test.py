from bs4 import BeautifulSoup
from  urllib import  url

html_doc = url('https: // djangopackages.org/categories')

soup = BeautifulSoup(html_doc, 'html.parser')


print(soup.prettify())
