import pickle
import os
from athletelist import AthleteList

def get_data(filename):
    try:
        with open(filename) as data:
            data = data.readline()
            data = data.strip().split(',')
            data = {"name": data.pop(0), "dob": data.pop(0), "times": data}
            return AthleteList(data)
    except IOError as ioerr:
        print("IOError: " + ioerr)
        return(None)

def put_to_store(filelist):
    all_athletes = {}
    for each_file in filelist:
        data = get_data(each_file)
        all_athletes[data.name] = data
    try:
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'data/athlete.pickle'))
        with open(data_path, 'wb') as savefile:
            pickle.dump(all_athletes, savefile)
    except IOError as ioerr:
        print("Input/Output Error: " + str(ioerr)) 

def get_from_store():
    all_athletes = {}
    try:
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'data/athlete.pickle'))
        with open(data_path, 'rb') as readfile:
            all_athletes = pickle.load(readfile)
    except IOError as ioerr:
        print("Input/Output Error: " + str(ioerr))
    return all_athletes      
