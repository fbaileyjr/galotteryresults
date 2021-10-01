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

#https://www.galottery.com/api/v2/draw-games/draws/?game-names=FANTASY+5&status=OPEN&next-draws=96


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
game_dict = {'fantasy 5': 'FANTASY+5',
             'mega millions': 'MEGA+MILLIONS', 'powerball': 'POWERBALL'}

# might have to paginate
# dict_keys(['nextPageUrl', 'pageUrls', 'nextItems', 'previousItems', 'draws'])

#class Endpoints():          
def get_search_results(game, size):
    if game == 'fantasy 5':
        url = f'https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws={size}&game-names={game}&size={size}&status=CLOSED'
        response = requests.request("GET", url)
        return response
    elif game == 'mega millions':
        pass
    elif game == 'powerball':
        url = f'https://www.galottery.com/api/v2/draw-games/draws/page?order=desc&previous-draws=100&game-names=POWERBALL&size={size}&status=CLOSED'
        response = requests.request("GET", url)
        return response
    else:
        return ''

def parse_fantasy_5(response):
    first_list,second_list,third_list,fourth_list,fifth_list = [],[],[],[],[]
    if isinstance(response.json().get('draws'), list):
        for draw in response.json().get('draws'):
            #time = draw.get('drawTime')
            #temp_date = datetime.datetime.fromtimestamp(time / 1000)
            #date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
            if draw.get('results')[0].get('primary'):
                 first_list.append(int(draw.get('results')[0].get('primary')[0]))
                 second_list.append(int(draw.get('results')[0].get('primary')[1]))
                 third_list.append(int(draw.get('results')[0].get('primary')[2]))
                 fourth_list.append(int(draw.get('results')[0].get('primary')[3]))
                 fifth_list.append(int(draw.get('results')[0].get('primary')[4]))
        draw_results = {"first" : first_list, "second" : second_list, "third" : third_list, "fourth" : fourth_list, "fifth" : fifth_list}
        return draw_results

def parse_mega(response):
    first_list,second_list,third_list,fourth_list,fifth_list,mega_list = [],[],[],[],[],[]
    if isinstance(response.json().get('draws'), list): 
        for draw in response.json().get('draws'):
            # time = draw.get('drawTime')
            # temp_date = datetime.datetime.fromtimestamp(time / 1000)
            # date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
            if draw.get('results')[0].get('primary'):
                first_list.append(int(draw.get('results')[0].get('primary')[0]))
                second_list.append(int(draw.get('results')[0].get('primary')[1]))
                third_list.append(int(draw.get('results')[0].get('primary')[2]))
                fourth_list.append(int(draw.get('results')[0].get('primary')[3]))
                fifth_list.append(int(draw.get('results')[0].get('primary')[4]))
                # need to remove MB-
                mega_list.append(int(draw.get('results')[0].get('primary')[6]))
        draw_results = {
            "first" : first_list, "second" : second_list,"third" : third_list, 
            "fourth" : fourth_list, "fifth" : fifth_list, "mega" : mega_list
        }
    return draw_results

def parse_powerball(response):
    first_list,second_list,third_list,fourth_list,fifth_list,pb_list,date_list = [],[],[],[],[],[],[]
    for draw in response.json().get('draws'):
        # time = draw.get('drawTime')
        # temp_date = datetime.datetime.fromtimestamp(time / 1000)
        # date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
        if draw.get('results')[0].get('primary'):
            first_list.append(int(draw.get('results')[0].get('primary')[0]))
            second_list.append(int(draw.get('results')[0].get('primary')[1]))
            third_list.append(int(draw.get('results')[0].get('primary')[2]))
            fourth_list.append(int(draw.get('results')[0].get('primary')[3]))
            fifth_list.append(int(draw.get('results')[0].get('primary')[4]))
            pball = re.search('\d+$',draw.get('results')[0].get('primary')[6])
            if pball.group(0):
                pb_list.append(int(pball.group(0)))
            time = draw.get('drawTime')
            temp_date = datetime.datetime.fromtimestamp(time / 1000)
            date = f"{temp_date.year}-{temp_date.month:02d}-{temp_date.day:02d}"
            date_list.append(date)
    draw_results = {
        'first' : first_list[::-1], 'second' : second_list[::-1],'third' : third_list[::-1], 
        'fourth' : fourth_list[::-1], 'fifth' : fifth_list[::-1], 'powerball' : pb_list[::-1],
        'date' : date_list[::-1]
    }
    return draw_results

def jdump(obj):
    print(json.dumps(obj, indent=2))


def choose_game():
    while True:
        choice = input(f'Which game do you want? Fantasy 5, Mega Millions, or Powerball? ')
        if choice.lower() in ['fantasy 5', 'mega millions', 'powerball']:
            break
        else:
            print(f'Please provide a valid game selection.')

    response = get_search_results(choice.lower() , 20)

    if choice.lower() == 'fantasy 5':
        results = parse_fantasy_5(response)
    elif choice.lower() == 'mega millions':
        results = parse_mega(response)
    elif choice.lower() == 'powerball':
        results = parse_powerball(response)
    return results 
