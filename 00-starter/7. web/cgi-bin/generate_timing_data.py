import glob
import os
import json
import athletemodel
from athletelist import sanitize

query_string = os.getenv('QUERY_STRING')
data_split = query_string.split('=')
dob_data = data_split[1]

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'data/*.txt'))
data_files = glob.glob(data_path)
athletemodel.put_to_store(data_files)
athletes = athletemodel.get_from_store()
athlete_data = []
for each_athlete in athletes:
    if dob_data == athletes[each_athlete].dob:
        athlete_data.append({"name" : athletes[each_athlete].name, "dob" : athletes[each_athlete].dob, 
                            "times" : sorted(set([sanitize(each_record) for each_record in athletes[each_athlete].times]))[0:3]})
print('Content-type: text/html \n\n')
print(json.dumps(athlete_data))
