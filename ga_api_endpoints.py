# -*- coding: utf-8 -*-
"""Models for API requests & responses."""
import dataclasses
import datetime
import json
import re
from datetime import date
from time import sleep

import requests
from bs4 import BeautifulSoup, SoupStrainer

fantasy_5_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=fantasy5&size=20&status=PAYABLE"
mega_million_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=mega&size=20&status=PAYABLE"
powerball_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=powerball&size=20&status=PAYABLE"

# response.json()['draws'][0]['results'][0]['primary'] = list of results
# response.json().get('draws')[0].get('results')[0].get('primary') = list of results
#
#time = response.json().get('draws')[0].get('drawTime')
#date = datetime.datetime.fromtimestamp(basetime/1000)


# might have to paginate 
# dict_keys(['nextPageUrl', 'pageUrls', 'nextItems', 'previousItems', 'draws'])

def get_search_results(game, size):
    url = f"https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names={game}&size={size}&status=PAYABLE"
    response = requests.request("GET", url)
