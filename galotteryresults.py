import json
import re
from datetime import date
from time import sleep

from bs4 import BeautifulSoup, SoupStrainer

import ga_api_endpoints as endpoints
import requests


def jdump(obj):
    print(json.dumps(obj, indent=2))


if __name__ == "__main__":
    while True:
        choice = input(f'Which game do you want? Fantasy 5, Mega Millions, or Powerball? ')
        if choice.lower() in ['fantasy 5', 'mega millions', 'powerball']:
            break
        else:
            print(f'Please provide a valid game selection.')

    response = endpoints.get_search_results(choice, 20)

    game_choice = {'fantasy 5' : 'parse_fantasy_5', 'mega millions': 'parse_mega', 'powerball' : 'parse_powerball'}

    if choice.lower() == 'fantasy 5':
        results = endpoints.parse_fantasy_5(response)
    elif choice.lower() == 'mega millions':
        results = endpoints.parse_mega(response)
    else:
        results = endpoints.parse_powerball(response)   
