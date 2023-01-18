'''
CAPP 121: PA #4 Polling Places

NAME: Xiomara Salazar, Jonathan Juarez

File to process precinct data
'''

import csv
import json

def precincts_to_json(filename, output_directory):
    """
    Load the princint data from a CSV file to JSON files,
        one JSON file per CSV dic

    Input:
        filename (string): Name of the CSV file
        output_directory (string): The name of the directory to write the 
            JSON files

    Returns (None): Nothing, creates JSON files
    """
    clean_precincts_dict_list = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for dic in reader:
            clean_precincts_dict_list.append(dic)

    for i, dic in enumerate(clean_precincts_dict_list):
        new_dic = {}
        new_dic["seed"] = int(dic.pop("seed"))
        dic["name"] = "Unknown" if dic["name"] == '' else dic['name']
        dic["num_booths"] = 1 if dic["num_booths"] == '' else dic['num_booths']
        dic["hours_open"] = int(dic["hours_open"])
        dic["num_voters"] = int(dic["num_voters"])
        dic["num_booths"] = int(dic["num_booths"])
        dic["voting_duration_rate"] = float(dic["voting_duration_rate"])
        dic["arrival_rate"] = float(dic["arrival_rate"])
        dic["large_precinct"] = True 
        if dic["num_voters"] > 100:
            dic["large_precinct"]
        else: dic["large_precinct"] = False
        dic.pop("pop")
        new_dic["precinct"] = dic

        with open("{data}/precinct-{number}.json".format(data = output_directory, number = i), "w") as f:
            json.dump(new_dic, f)

