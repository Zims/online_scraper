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
json_name = ''
business_title_list = []
def output_file(*args):
    def get_result():
        search_url = args[0]
        global file_name
        file_name = args[1]
        res = requests.get(search_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        organic_pane = soup.find_all(lambda tag: tag.name == 'div' and 
                               tag.get('class') == ['result'])

        for business in organic_pane:
            global title
            global address_location
            global phone_num
            global url_address
            for business_title in business.select('.business-name'):
                title = business_title.text
                # print(title)
            for address in business.select('.locality'):
                address_location = address.text
                # print(address_location)
            for phone in business.select('.phones.phone.primary'):
                phone_num = phone.text
                # print(phone_num)
            for site in business.find_all("a", string="Website"):
                url_address = site['href']
                print(url_address)
            yield {
                "title": title,
                "address": address_location,
                "number": phone_num,
                "website": url_address 
                }


    get_result()
    top_30 = list(get_result())
    now = datetime.now()
    current_time = now.strftime("%H:%M_%m-%y")
    global file_name
    if "/" in file_name:
        file_name = args[1].replace('/', '_')
    if " " in file_name:
        file_name = file_name.replace(' ', '_')
    print('DONE')
    # app_json = json.dumps(appDict)

    with open(f'output/{file_name}-{current_time}.json', 'w') as json_file:
        global json_name
        json_name = f'{file_name}-{current_time}.json'
        print(json_name)
        json.dump(top_30, json_file)

# output_file(str('https://www.yellowpages.com/search?search_terms=makeup+artist&geo_location_terms=New+York%2C+FL'))
# output_file()