import requests
from bs4 import BeautifulSoup
import csv

CSV = 'sanmiGadgets3.csv'
HOST = 'https://sanmi.kz/'
URL = 'https://sanmi.kz/catalog/smartfony/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', {'class': 'item-parent'})
    cards = []

    for item in items:
        link = item.find('a', class_='dark_link').get('href')
        details = get_details(get_html(HOST + link).text)
        initDetails = {
            'name':item.find('a', class_='dark_link').get_text(strip=True),
            'cost':item.find('span', class_='price_value').get_text(strip=True).replace('\xa0', '')
        }
        initDetails.update(details)
        cards.append(initDetails)
    return cards

def get_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    props = soup.findAll('tr', {'itemprop': 'additionalProperty'})
    details = {}
    for prop in props:
        name = prop.find('span', {'itemprop': 'name'}).getText(strip=True)
        value = prop.find('span', {'itemprop': 'value'}).getText(strip=True)
        if 'Операционная система' == name:
            details.update({'os':value})
        elif 'Цвет' == name:
            details.update({'color':value})
        elif 'Материал' == name:
            details.update({'material':value})
        elif '5G' == name:
            details.update({'fiveG':value})
        elif 'Диагональ' == name:
            details.update({'diagonal':value})
        elif 'Разрешение дисплея' == name:
            details.update({'screen':value})
        elif 'Модель процессора' == name:
            details.update({'processor':value})
        elif 'Частота процессора' == name:
            details.update({'frequency':value})
        elif 'Объем оперативной памяти' == name:
            details.update({'opstorage':value})
        elif 'Объем встроенной памяти' == name:
            details.update({'storage':value})
        elif 'Фотокамера' in name:
            details.update({'camera':value})
        elif 'Фронтальная камера' in name:
            details.update({'frontCamera':value})
        elif 'Емкость аккумулятора' in name:
            details.update({'battery':value})
        elif 'Вес' == name:
            details.update({'weight':value})
    return details

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Gadget name', 'Cost', 'Operation system', 'Color', 'Material type', 'Have 5G', 'Diagonal',
                         'Screen resolution', 'Processor Model', 'Processor frequency', 'The amount of RAM',
                         'The amount of internal memory', 'Camera', 'Front camera', 'Battery capacity', 'Weight'])
        for item in items:
            print(item)
            writer.writerow([check(item, 'name'), check(item, 'cost'), check(item, 'os'), check(item, 'color'), check(item, 'material'), check(item, 'fiveG'),
                             check(item, 'diagonal'), check(item, 'screen').replace('\xd7', 'x'), check(item, 'processor'), check(item, 'frequency'), check(item, 'opstorage'),
                             check(item, 'storage'), check(item, 'camera'), check(item, 'frontCamera'), check(item, 'battery'), check(item, 'weight')])

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
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            print(get_content(html.text))
            save_doc(cards, CSV)
    else:
        print('Error')

parser()