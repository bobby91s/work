from datetime import datetime
import requests
import lxml
from lxml import html
from subprocess import call
import urllib
from bs4 import BeautifulSoup
from dateutil import parser


total_links = []
link_pages = []
checkers = []


def get_links(soup):
    for link in soup.find_all('a'):
        if 'https' in str(link) and 'page' not in str(link):
            if 'geographical' not in str(link):
                total_links.append(link.get('href'))


def get_data(total_links):
    for link in total_links:
        xx = requests.get(link)
        r = xx.text
        soup = BeautifulSoup(r, 'lxml')

        title = ((soup.title).text).strip("- Download")

        info = (soup.find('p', {'class':'PDFPerFullMagazineMeta'})).text

        last_modified = xx.headers['Last-Modified']
        last_modified = last_modified.split('+0300')
        last_modified = last_modified[0] + last_modified[1]
        last_modified = parser.parse(last_modified)

        image = soup.find('img')
        image_path = image['src']
        image_link = 'https://pdf-magazine-download.com' + str(image_path)

        download_tag = soup.find('p', {'class':'PDFPerFullBlockDownload'})
        x = download_tag.find('a')
        download_link = x.get('href')




        with open('collections.txt', 'a+') as outfile:
            outfile.write(title.encode('utf-8') + '\n' + info.encode('utf-8') +
                            '\n' + image_link.encode('utf-8') + '\n' +
                            download_link.encode('utf-8') + '\n' + '\n')


def update(total_links):
    for link in total_links:
        xx = requests.get(link)

        last_modified = xx.headers['Last-Modified']
        last_modified = last_modified.split('+0300')
        last_modified = last_modified[0] + last_modified[1]
        last_modified = parser.parse(last_modified)

        with open('collections.txt', 'a+') as outfile:
            if last_modified > checkers[0]:
                outfile.write(title.encode('utf-8') + '\n' + info.encode('utf-8') +
                                '\n' + image_link.encode('utf-8') + '\n' +
                                download_link.encode('utf-8') + '\n' + '\n')
            else:
                pass

r  = requests.get('https://pdf-magazine-download.com/geographical/')
data = r.text
soup = BeautifulSoup(data, 'lxml')
get_links(soup)


for link in soup.find_all('a'):
    if 'page' in str(link) and link.get('href') not in link_pages:
        link_pages.append(link.get('href'))


for link in link_pages:
    req  = requests.get(link)
    data = req.text
    soup2 = BeautifulSoup(data, 'lxml')
    get_links(soup2)


for link in total_links:
    url = requests.get(link)
    checker = url.headers['Last-Modified']
    checker = checker.split('+0300')
    checker = checker[0] + checker[1]
    checker = parser.parse(checker)
    checkers.append(checker)
    checkers.sort(reverse=True)


with open('collections.txt', 'a+') as outfile:
    outfile.seek(0)
    if not outfile.read(1):
        get_data(total_links)
    else:
        update(total_links)
