import re
import statistics

import ga_api_endpoints
import keras
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator

# https://towardsdatascience.com/time-series-forecasting-with-recurrent-neural-networks-74674e289816s

# statistics: https://www.galottery.com/api/v1/draw-games/statistics/?game-names=POWERBALL&draw-count=10
# {"drawStatistics":[{"drawnResults":[{"gameName":"POWERBALL","period":"DRAW-COUNT","mostDrawnResults":["22","20","37","40","63","39","47","54","60","61","62","1"],"leastDrawnResults":["69","68","67","66","65","64","59","56","53","52","48","43"],"statistics":[{"result":"22","frequency":0.08},{"result":"20","frequency":0.06},{"result":"37","frequency":0.06},{"result":"40","frequency":0.06},{"result":"63","frequency":0.06},{"result":"39","frequency":0.04},{"result":"47","frequency":0.04},{"result":"54","frequency":0.04},{"result":"60","frequency":0.04},{"result":"61","frequency":0.04},{"result":"62","frequency":0.04},{"result":"1","frequency":0.02},{"result":"4","frequency":0.02},{"result":"5","frequency":0.02},{"result":"9","frequency":0.02},{"result":"11","frequency":0.02},{"result":"18","frequency":0.02},{"result":"21","frequency":0.02},{"result":"23","frequency":0.02},{"result":"31","frequency":0.02},{"result":"33","frequency":0.02},{"result":"36","frequency":0.02},{"result":"38","frequency":0.02},{"result":"41","frequency":0.02},{"result":"44","frequency":0.02},{"result":"45","frequency":0.02},{"result":"46","frequency":0.02},{"result":"49","frequency":0.02},{"result":"50","frequency":0.02},{"result":"51","frequency":0.02},{"result":"55","frequency":0.02},{"result":"57","frequency":0.02},{"result":"58","frequency":0.02},{"result":"2","frequency":0.0},{"result":"3","frequency":0.0},{"result":"6","frequency":0.0},{"result":"7","frequency":0.0},{"result":"8","frequency":0.0},{"result":"10","frequency":0.0},{"result":"12","frequency":0.0},{"result":"13","frequency":0.0},{"result":"14","frequency":0.0},{"result":"15","frequency":0.0},{"result":"16","frequency":0.0},{"result":"17","frequency":0.0},{"result":"19","frequency":0.0},{"result":"24","frequency":0.0},{"result":"25","frequency":0.0},{"result":"26","frequency":0.0},{"result":"27","frequency":0.0},{"result":"28","frequency":0.0},{"result":"29","frequency":0.0},{"result":"30","frequency":0.0},{"result":"32","frequency":0.0},{"result":"34","frequency":0.0},{"result":"35","frequency":0.0},{"result":"42","frequency":0.0},{"result":"43","frequency":0.0},{"result":"48","frequency":0.0},{"result":"52","frequency":0.0},{"result":"53","frequency":0.0},{"result":"56","frequency":0.0},{"result":"59","frequency":0.0},{"result":"64","frequency":0.0},{"result":"65","frequency":0.0},{"result":"66","frequency":0.0},{"result":"67","frequency":0.0},{"result":"68","frequency":0.0},{"result":"69","frequency":0.0}],"drawCount":10,"selectionType":"PRIMARY"},{"gameName":"POWERBALL","period":"DRAW-COUNT","mostDrawnResults":["21","19","5","11","12","24","25","1","2","3","4","6"],"leastDrawnResults":["26","23","22","20","18","17","16","15","14","13","10","9"],"statistics":[{"result":"21","frequency":0.3},{"result":"19","frequency":0.2},{"result":"5","frequency":0.1},{"result":"11","frequency":0.1},{"result":"12","frequency":0.1},{"result":"24","frequency":0.1},{"result":"25","frequency":0.1},{"result":"1","frequency":0.0},{"result":"2","frequency":0.0},{"result":"3","frequency":0.0},{"result":"4","frequency":0.0},{"result":"6","frequency":0.0},{"result":"7","frequency":0.0},{"result":"8","frequency":0.0},{"result":"9","frequency":0.0},{"result":"10","frequency":0.0},{"result":"13","frequency":0.0},{"result":"14","frequency":0.0},{"result":"15","frequency":0.0},{"result":"16","frequency":0.0},{"result":"17","frequency":0.0},{"result":"18","frequency":0.0},{"result":"20","frequency":0.0},{"result":"22","frequency":0.0},{"result":"23","frequency":0.0},{"result":"26","frequency":0.0}],"drawCount":10,"selectionType":"SECONDARY"}]}]}
def cold_numbers(game, list):
	game_list = {
	    "fantasy5" : 42,
	    "megaball" : 70,
	    "mb" : 25,
	    "powerball" : 69,
	    "pb" : 26,
	}


# def count_even(list):
# 	count = 0
# 	#for num in list:
#     #    if num // 2 == 0:
#      #       count += 1
#     #return count

# def count_odd(list):
# 	# count = 0
# 	# for num in list:
#  #        if num // 2 != 0:
#  #        	count += 1
#  #    return count

# def parse_fantasy5_results(dict):
# 	pass


# def parse_megaball_results(dict):
# 	pass


# def parse_powerball_results(dict):
# 	pass

# def popular_numbers(list)
#     pass


# what do we need to calculate? median, max, min, odd, evens
# function to calculate the next possible numbers?
# more than once, numbers that have not been drawn
# there will be { position : [list_of_numbers]}

results = ga_api_endpoints.choose_game()
