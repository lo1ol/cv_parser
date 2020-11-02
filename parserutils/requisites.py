import requests
import re

from bs4 import BeautifulSoup


REQUISITES_KEYWORDS = [
r'ИНН[\s\:0-9]+', 
r'БИК[\s\:0-9]+', 
r'КПП[\s\:0-9]+', 
r'[Рр]{1}асч[её]{1}тный сч[её]{1}т[\s\:0-9]+',
]


def find_requisites(domain):
    print("Finding requisites...")
    requisites_list = []
    response = requests.get(domain)
    soup = BeautifulSoup(response.text, 'html.parser')
    for word in REQUISITES_KEYWORDS:
        regex_result = re.search(re.compile(word), response.text)
        if regex_result:
            regex_result = regex_result.group(0)
            requisites_list.append(regex_result)
    return requisites_list