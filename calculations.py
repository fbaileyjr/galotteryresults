import re
import statistics


def cold_numbers(game, list):
	game_list = {
	    "fantasy5" : 45,
	    "mega" : 56,
	    "megaball" : 72,
	    "pb" : 60,
	    "powerball" : 65,
	}


def count_even(list):
	count = 0
	for num in list:
        if num // 2 == 0:
        	count += 1
    return count

def count_odd(list):
	count = 0
	for num in list:
        if num // 2 != 0:
        	count += 1
    return count

def parse_fantasy5_results(dict):
	pass


def parse_megaball_results(dict):
	pass


def parse_powerball_results(dict):
	pass

def popular_numbers(list)
    pass


# what do we need to calculate? median, max, min, odd, evens
# function to calculate the next possible numbers?
# more than once, numbers that have not been drawn
# there will be { position : [list_of_numbers]}
