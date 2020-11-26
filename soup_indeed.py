import pprint
import json
import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

# https://de.indeed.com/jobs?q=Python&l=&ts=1604567228298&rq=1&rsIdx=1&fromage=last&newcount=3020
file_name = ''
json_name = ''
def output_file():
    def get_result():
        search_url = 'https://de.indeed.com/jobs?q=Python&l=&ts=1604567228298&rq=1&rsIdx=1&fromage=last&newcount=3020'        
        global file_name
        file_name = 'opo'

        res = requests.get(search_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        job_name_list = []

        result_card = soup.select('.jobsearch-SerpJobCard.unifiedRow.result.row.unifiedRow')
        for job_offer in result_card:
            for job in job_offer.select('.title'):
                job_name = job.text
                job_name_list.append(job_name.strip())

        for i in job_name_list:
            print(i)
        print(len(job_name_list))
        
    get_result()
        # for business in result_card:
        #     global title
        #     global address_location
        #     global phone_num
        #     for business_title in business.select('.business-name'):
        #         title = business_title.find('span').text
        #     for address in business.select('.locality'):
        #         address_location = address.text
        #     for phone in business.select('.phones.phone.primary'):
        #         phone_num = phone.text
        #     yield {
        #         "title": title,
        #         "address": address_location,
        #         "number": phone_num
        #         }


    # get_result()
    # top_30 = list(get_result())
    # now = datetime.now()
    # current_time = now.strftime("%H:%M_%m-%y")
    # global file_name
    # if "/" in file_name:
    #     file_name = args[1].replace('/', '_')
    # if " " in file_name:
    #     file_name = file_name.replace(' ', '_')
    # print('DONE')

    # with open(f'output/{file_name}-{current_time}.json', 'w') as json_file:
    #     global json_name
    #     json_name = f'{file_name}-{current_time}.json'
    #     print(json_name)
    #     json.dump(top_30, json_file)

output_file()