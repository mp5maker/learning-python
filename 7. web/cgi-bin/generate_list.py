import glob
import os
import athletemodel
import json

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'data/*.txt'))
data_files = glob.glob(data_path)
athletemodel.put_to_store(data_files)
athletes = athletemodel.get_from_store()
get_all_data = []
for each_athlete in athletes:
    get_all_data.append({"name": athletes[each_athlete].name, "dob": athletes[each_athlete].dob})
print('Content-type: text/html \n\n')
print(json.dumps(get_all_data)) 