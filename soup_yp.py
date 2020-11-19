import pprint
import json
import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

# https://www.yellowpages.com/search?search_terms=hairstylist&geo_location_terms=New+York%2C+NY
# https://www.yellowpages.com/search?search_terms=hairstylist&geo_location_terms=New+York%2C+FL
# https://www.yellowpages.com/search?search_terms=makeup+artist&geo_location_terms=New+York%2C+FL
file_name = ''

def output_file(*args):
    def get_result():
        search_url = args[0]
        global file_name
        file_name = args[1]
        # if "/" in args[1]:
        #     file_name = args[1].replace('/', '_')
        # search_url = str(input("Paste the Yellowpages address to scrape (copy the the address of Yellowpages search results): "))
        # print(search_url)
        res = requests.get(search_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # links = soup.select('.storylink')
        # subtext = soup.select('.subtext')
        result_card = soup.select('.result')
        for business in result_card:
            global title
            global address_location
            global phone_num
            for business_title in business.select('.business-name'):
                title = business_title.find('span').text
            for address in business.select('.locality'):
                address_location = address.text
            for phone in business.select('.phones.phone.primary'):
                phone_num = phone.text
            yield {
                "title": title,
                "address": address_location,
                "number": phone_num
                }


    get_result()
    top_30 = list(get_result())
    now = datetime.now()
    current_time = now.strftime("%H:%M_%m-%y")
    global file_name
    if "/" in file_name:
        file_name = args[1].replace('/', '_')
    print('DONE')
    # app_json = json.dumps(appDict)
    with open(f'output/{file_name}-{current_time}.json', 'w') as json_file:
        json.dump(top_30, json_file)

# output_file(str('https://www.yellowpages.com/search?search_terms=makeup+artist&geo_location_terms=New+York%2C+FL'))