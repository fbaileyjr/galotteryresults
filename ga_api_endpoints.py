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
# time = response.json().get('draws')[0].get('drawTime')
# date = datetime.datetime.fromtimestamp(basetime/1000)
# results_list = response.json().get('draws')[0].get('results')[0].get('primary')
# f"{date.month:02d}"
# for x in testlist:
#    for key in x:
#        for x in x[key]:
#            print(x)

# dict of game keys
game_dict = {"Fantasy 5": "fantasy5",
             "Mega Millions": "mega", "PowerBall": "powerball"}

# might have to paginate
# dict_keys(['nextPageUrl', 'pageUrls', 'nextItems', 'previousItems', 'draws'])


def get_search_results(game, size):
    url = f"https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=180&game-names={game}&size={size}&status=PAYABLE"
    response = requests.request("GET", url)
    return response


def parse_fantasy_5(response):
    first_list,second_list,third_list,fourth_list,fifth_list = [],[],[],[],[]
    for draw in response.json().get('draws'):
        #time = draw.get('drawTime')
        #temp_date = datetime.datetime.fromtimestamp(time / 1000)
        #date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
        if draw.get('results')[0].get('primary'):
             first_list.append(draw.get('results')[0].get('primary')[0])
             second_list.append(draw.get('results')[0].get('primary')[1])
             third_list.append(draw.get('results')[0].get('primary')[2])
             fourth_list.append(draw.get('results')[0].get('primary')[3])
             fifth_list.append(draw.get('results')[0].get('primary')[4])
        draw_results = {"first" : first_list, "second" : second_list, "third" : third_list, "fourth" : fourth_list, "fifth" : fifth_list}
    return draw_results


def parse_mega(response):
    first_list,second_list,third_list,fourth_list,fifth_list,mega_list = [],[],[],[],[],[]
    for draw in response.json().get('draws'):
        # time = draw.get('drawTime')
        # temp_date = datetime.datetime.fromtimestamp(time / 1000)
        # date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
        if draw.get('results')[0].get('primary'):
            first_list.append(draw.get('results')[0].get('primary')[0])
            second_list.append(draw.get('results')[0].get('primary')[1])
            third_list.append(draw.get('results')[0].get('primary')[2])
            fourth_list.append(draw.get('results')[0].get('primary')[3])
            fifth_list.append(draw.get('results')[0].get('primary')[4])
        if draw.get('results')[0].get('secondary')[0]:
            mega_list.append(draw.get('results')[0].get('secondary')[0])
        draw_results = {
            "first" : first_list, "second" : second_list,"third" : third_list, 
            "fourth" : fourth_list, "fifth" : fifth_list, "mega" : mega_list
        }
    return draw_results



def parse_powerball(response):
    first_list,second_list,third_list,fourth_list,fifth_list,pb_list = [],[],[],[],[],[]
    for draw in response.json().get('draws'):
        # time = draw.get('drawTime')
        # temp_date = datetime.datetime.fromtimestamp(time / 1000)
        # date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
        if draw.get('results')[0].get('primary'):
            first_list.append(draw.get('results')[0].get('primary')[0])
            second_list.append(draw.get('results')[0].get('primary')[1])
            third_list.append(draw.get('results')[0].get('primary')[2])
            fourth_list.append(draw.get('results')[0].get('primary')[3])
            fifth_list.append(draw.get('results')[0].get('primary')[4])
        if draw.get('results')[0].get('secondary')[0]:
            pb_list.append(draw.get('results')[0].get('secondary')[0])
        draw_results = {
            "first" : first_list, "second" : second_list,"third" : third_list, 
            "fourth" : fourth_list, "fifth" : fifth_list, "powerball" : pb_list
        }
    return draw_results

def jdump(obj):
    print(json.dumps(obj, indent=2))
