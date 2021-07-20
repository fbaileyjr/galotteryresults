# -*- coding: utf-8 -*-
"""Models for API requests & responses."""
import dataclasses
import json
import re
from datetime import date
from time import sleep

import ga_api_endpoints
import requests
from bs4 import BeautifulSoup, SoupStrainer

prefix_url = ""
fantasy_5_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=fantasy5&size=20&status=PAYABLE"
mega_million_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=mega&size=20&status=PAYABLE"

fantasy_5 = {
    "method": "POST",
    "url": "api/v1",
    "headers" : "",
}

# might have to paginate 
# dict_keys(['nextPageUrl', 'pageUrls', 'nextItems', 'previousItems', 'draws'])

def get_search_results(response):
    response = requests.request("GET", "https://atlanta.craigslist.org/search/jjj?query=office")
    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find(id="search-results")
    list_results = search_results.find_all(search_results, class_="result-row")
    list_results[1].find("time").string
    today = date.today()
    today_craigslist = f"{day_dict[today.month]} {today.day}"
    final_results = []
    for result in list_results:
        if result.find("time").string == today_craigslist:
            final_results.append(result)
