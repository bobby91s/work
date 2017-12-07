import requests
import lxml
from lxml import html
from subprocess import call
import urllib
from bs4 import BeautifulSoup

total_links = []


r  = requests.get('https://pdf-magazine-download.com/geographical/')
data = r.text
soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
    if 'https' in str(link):
        total_links.append(link.get('href'))


def get_data(total_links):
    for link in total_links:
        xx = requests.get(link)
        r = xx.text
        soup = BeautifulSoup(r, 'lxml')

        title = ((soup.title).text).strip("- Download")

        info = (soup.find('p', {'class':'PDFPerFullMagazineMeta'})).text

        image = soup.find('img')
        image_path = image['src']
        image_link = 'https://pdf-magazine-download.com' + str(image_path)

        download_tag = soup.find('p', {'class':'PDFPerFullBlockDownload'})
        x = download_tag.find('a')
        download_link = x.get('href')

        print {"title":title, 'info':info, 'image':image_link,
                        'download_link':download_link}

get_data(total_links)
"""
am preluat toate informatiile cerute de pe prima pagina a site-ului, mai trebuie adaugate si celelalte linkuri de pe cele 
2 pagini si scrierea in fisier cu Last Modified ca si 'semn de carte'
"""
