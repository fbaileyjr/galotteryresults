# -*- coding: utf-8 -*-
"""Models for API requests & responses."""
import dataclasses
import datetime
import re
from datetime import date
from time import sleep

import json1
import requests
from bs4 import BeautifulSoup, SoupStrainer

fantasy_5_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=fantasy5&size=20&status=PAYABLE"
mega_million_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=mega&size=20&status=PAYABLE"
powerball_url = "https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names=powerball&size=20&status=PAYABLE"

# response.json()['draws'][0]['results'][0]['primary'] = list of results
# response.json().get('draws')[0].get('results')[0].get('primary') = list of results
#
# time = response.json().get('draws')[0].get('drawTime')
# date = datetime.datetime.fromtimestamp(basetime/1000)
# results_list = response.json().get('draws')[0].get('results')[0].get('primary')
# f"{date.month:02d}"
#for x in testlist:
#    for key in x:
#        for x in x[key]:
#            print(x)

# dict of game keys
game_dict = { "Fantasy 5" : "fantasy5", "Mega Millions" : "mega", "PowerBall" : "poweball"}

# might have to paginate 
# dict_keys(['nextPageUrl', 'pageUrls', 'nextItems', 'previousItems', 'draws'])

def get_search_results(game, size):
    url = f"https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names={game}&size={size}&status=PAYABLE"
    response = requests.request("GET", url)
    return response

def parse_fantasy_5(response):
    results_list = []
    for draw in response.json().get('draws'):
        time = draw.get('drawTime')
        temp_date = datetime.datetime.fromtimestamp(time/1000)
        date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
        draw_results = { date : draw.get('results')[0].get('primary')}
        results_list.append(draw_results)
    return results_list[::-1]


def jdump(obj):
    print(json.dumps(obj, indent=2))
