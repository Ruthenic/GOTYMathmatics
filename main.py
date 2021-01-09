from howlongtobeatpy import HowLongToBeat
import requests
gamename = input("What game would you like to calculate the BDGs for? ")
results = HowLongToBeat().search(gamename)
print(results[0].game_name, results[0].gameplay_main + ' ' + results[0].gameplay_main_unit)
