import requests
import csv

#main class for parsing
class MechtaParsing():

    URL_PHONES = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=smartfony&filter=true'
    URL_PHONES_DATA ='https://www.mechta.kz/api/main/catalog_new/index.php?section=smartfony&catalog=true' 

    URL_TV = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=televizory&filter=true'
    URL_TV_DATA ='https://www.mechta.kz/api/main/catalog_new/index.php?section=televizory&page_num=15&catalog=true' 

    URL_FRIDGE = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=holodilniki&filter=true' 
    URL_FRIDGE_DATA = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=holodilniki&page_num=5&catalog=true' 

    URL_WATCH = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=smart-chasy&filter=true'
    URL_WATCH_DATA ='https://www.mechta.kz/api/main/catalog_new/index.php?section=smart-chasy&page_num=2&catalog=true'

    URL_CLEANER = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=pylesosy&filter=true'
    URL_CLEANER_DATA = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=pylesosy&page_num=2&catalog=true'

    URL_TABLETS = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=planshety&filter=true'
    URL_TABLETS_DATA = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=planshety&page_num=2&catalog=true'

    URL_DISHWASHER = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=posudomoechnye-mashiny&filter=true'
    URL_DISHWASHER_DATA = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=posudomoechnye-mashiny&filter=true'


    urls = {'phones': (URL_PHONES, URL_PHONES_DATA), 'TV': (URL_TV, URL_TV_DATA), 'fridge': (URL_FRIDGE, URL_FRIDGE_DATA),
            'Watches': (URL_WATCH, URL_WATCH_DATA), 'Cleaners': (URL_CLEANER, URL_CLEANER_DATA), 'Tablets': URL_TABLETS, 'Dishwashers': (URL_DISHWASHER, URL_DISHWASHER_DATA)}


    def parseFridge(self, category):
        for pageNum in range(1, 20):
            url, url_data = self.urls[category][0],'https://www.mechta.kz/api/main/catalog_new/index.php?section=holodilniki&page_num=' +  str(pageNum) + '&catalog=true'

            html = requests.get(url).json()

            url_get = url_data + str(html['data']['all'])
            data = requests.get(url_get).json()
            with open('fridges1.csv', 'a', encoding = 'utf-8') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(('title', 'price', 'type', 'volume', 'system', 'brand', 'rating'))
                for i in data['data']['ITEMS']:
                    try:
                        wr.writerow(
                            (
                               i['NAME'],
                               i['PRICE']['PRICE'],
                               i['MAIN_PROPERTIES'][0]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][1]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][2]['PROP_VALUE'],
                               i['METRICS']['BRAND'],
                               i['RATING']

                            )
                        )

                    except KeyError:
                        continue


    def parseTV(self,category):
        for pageNum in range(1,30):
            url, url_data = self.urls[category][0], 'https://www.mechta.kz/api/main/catalog_new/index.php?section=televizory&page_num='+str(pageNum)+'&catalog=true'
            html = requests.get(url).json()

            url_get = url_data + str(html['data']['all'])
            data = requests.get(url_get).json()
            with open('TV1.csv', 'a', encoding = 'utf-8') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(('title', 'price', 'size', 'resolution', 'brand', 'rating'))
                for i in data['data']['ITEMS']:
                    try:
                        wr.writerow(
                            (
                               i['NAME'],
                               i['PRICE']['PRICE'],
                               i['MAIN_PROPERTIES'][0]['PROP_VALUE'].split(' ')[0],
                               i['MAIN_PROPERTIES'][1]['PROP_VALUE'],
                               i['METRICS']['BRAND'],
                               i['RATING']
                            )
                        )

                    except KeyError:
                        continue


    def parseWatches(self, category):
        for pageNum in range(1, 20):
            url, url_data = self.urls[category][0],'https://www.mechta.kz/api/main/catalog_new/index.php?section=smart-chasy&page_num=' +  str(pageNum) + '&catalog=true'

            html = requests.get(url).json()

            url_get = url_data + str(html['data']['all'])
            data = requests.get(url_get).json()
            with open('watches1.csv', 'a', encoding = 'utf-8') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(('title', 'price', 'wi-fi', 'weight', '4G', 'brand', 'rating'))
                for i in data['data']['ITEMS']:
                    try:
                        wr.writerow(
                            (
                               i['NAME'],
                               i['PRICE']['PRICE'],
                               i['MAIN_PROPERTIES'][0]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][1]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][2]['PROP_VALUE'],
                               i['METRICS']['BRAND'],
                               i['RATING']

                            )
                        )

                    except KeyError:
                        continue


    def parseCleaner(self, category):
        for pageNum in range(1, 20):
            url, url_data = self.urls[category][0],'https://www.mechta.kz/api/main/catalog_new/index.php?section=pylesosy&page_num=' +  str(pageNum) + '&catalog=true'

            #url,url_data = self.urls[category][0],self.urls[category][1]
            html = requests.get(url).json()

            url_get = url_data + str(html['data']['all'])
            data = requests.get(url_get).json()
            with open('cleaners1.csv', 'a', encoding = 'utf-8') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(('title', 'price', 'clean_type', 'container_volume', 'power', 'brand', 'rating'))
                for i in data['data']['ITEMS']:
                    try:
                        wr.writerow(
                            (
                               i['NAME'],
                               i['PRICE']['PRICE'],
                               i['MAIN_PROPERTIES'][0]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][1]['PROP_VALUE'],
                               i['MAIN_PROPERTIES'][2]['PROP_VALUE'].split(' ')[0],
                               i['METRICS']['BRAND'],
                               i['RATING']

                            )
                        )

                    except KeyError:
                        continue


    def parseDishwasher(self, category):
        for pageNum in range(1, 20):
            url, url_data = self.urls[category][0],'https://www.mechta.kz/api/main/catalog_new/index.php?section=posudomoechnye-mashiny&page_num=' +  str(pageNum) + '&catalog=true'

            html = requests.get(url).json()

            url_get = url_data + str(html['data']['all'])
            data = requests.get(url_get).json()
            with open('dishwashers1.csv', 'a', encoding='utf-8') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(('title', 'price', 'capacity', 'programs_number', 'water_consumption', 'brand', 'rating'))
                for i in data['data']['ITEMS']:
                    try:
                        wr.writerow(
                            (
                                i['NAME'],
                                i['PRICE']['PRICE'],
                                i['MAIN_PROPERTIES'][0]['PROP_VALUE'],
                                i['MAIN_PROPERTIES'][1]['PROP_VALUE'],
                                i['MAIN_PROPERTIES'][2]['PROP_VALUE'].split(' ')[0],
                                i['METRICS']['BRAND'],
                                i['RATING']

                            )
                        )

                    except KeyError:
                        continue

m = MechtaParsing()
#m.parseTV('TV')
#m.parseFridge('fridge')
#m.parseWatches('Watches')
#m.parseCleaner('Cleaners')
#m.parseDishwasher('Dishwashers')


# skip duplicate
with open('dishwashers1.csv','r', encoding = 'utf-8') as in_file, open('dishwashers.csv','w', encoding = 'utf-8') as out_file:
    seen = set()
    for line in in_file:
        if line in seen: continue

        seen.add(line)
        out_file.write(line)