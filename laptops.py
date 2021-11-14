import requests
from bs4 import BeautifulSoup
import csv
from lxml import html

CSV = 'laptop.csv'
HOST = 'http://www.bestbuy.com'
URL = 'http://www.bestbuy.com'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', {'class': 'product-item'})
    print(len(items), "len of items")
    cards = []

    for item in items:
        link = item.find('a', class_='product-item__info_title').get('href')
        details = get_details(get_html(HOST + link).text)
        name = item.find('a', class_='product-item__info_title').get_text(strip=True).split('/')
        initDetails = {
            'id':item.id,
            'name':name,
            'size_of_n':str(len(name)),
            'cost':item.find('div', class_='price').get_text(strip=True),
            'mark':name[0].split(' '),
            'model':name[0].split(' '),
            'diagonal':name[0].split(' '), 
            'processor':name[0].split(' '), 
            'volume':name[2], 
            'videocard':name[3], 
            'ram':name[1]
        }
        initDetails.update(details)
        cards.append(initDetails)
    return cards

def get_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    props = soup.findAll('div', {'class': 'detail-specifications'})
    details = {}
    for prop in props:
        tree = html.fromstring(prop)
        name = prop.find('span', {'itemprop': 'name'}).getText(strip=True)
        value = prop.find('span', {'itemprop': 'value'}).getText(strip=True)
        if 'Screen size' == name:
            details.update({'diagonal':value})
        elif 'Model name' == name:
            details.update({'name':value})
        elif 'Manufacturer' == name:
            details.update({'mark':value})
        elif 'CPU' == name:
            details.update({'processor':value})
        elif 'RAM' == name:
            details.update({'ram':value})
        elif 'Storage' == name:
            details.update({'volume':value})
        elif 'GPU' == name:
            details.update({'videocard':value})
    return details

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID', 'Name', 'Prise', 'Mark', 'Model', 'Laptop code', 'Diagonal', 'Processor Model', 'Processor cpu',
                         'The amount of RAM', 'Videocard', 'The amount of internal memory'])
        for item in items:
            print(item)
            writer.writerow([
                'a'+str(c),
                datas['Manufacturer'][i]+" "+datas['Model Name'][i]+" "+datas['CPU'][i], 
                "%.2f" % (float(datas['Price (Euros)'][i].split(',')[0]+'.'+datas['Price (Euros)'][i].split(',')[1])*493.82), 
                datas['Manufacturer'][i], 
                datas['Model Name'][i], 
                datas['Screen Size'][i], 
                datas['CPU'][i], 
                datas['RAM'][i], 
                datas['GPU'][i],
                datas[' Storage'][i]
                                ])

def check(item, key):
    if key in item:
        return item[key]
    else:
        return ''

def parser():
    PAGENATION = input('Page size: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Parsing page: {page}')
            print(len(html.text), 'c')
            html = get_html(URL, params={'page': page})
            print(len(html.text), 2)
            print(get_content(html.text))
            cards.extend(get_content(html.text))
            print(get_content(html.text), 2)
            save_doc(cards, CSV)
    else:
        print('Error')

parser()
