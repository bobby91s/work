import requests
import lxml
from lxml import html
from subprocess import call
import urllib
from bs4 import BeautifulSoup


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

        image = soup.find('img')
        image_path = image['src']
        image_link = 'https://pdf-magazine-download.com' + str(image_path)

        download_tag = soup.find('p', {'class':'PDFPerFullBlockDownload'})
        x = download_tag.find('a')
        download_link = x.get('href')
        # print download_link


        
        with open('collections.txt', 'a+') as outfile:
            outfile.write(title.encode('utf-8') + '\n' + info.encode('utf-8') +
                            '\n' + image_link.encode('utf-8') + '\n' +
                            download_link.encode('utf-8') + '\n' + '\n')


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
    checkers.append(checker)

get_data(total_links)
