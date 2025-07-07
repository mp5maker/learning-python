def sanitize(data):
    if '-' in data:
        splitter = '-'
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (mins, secs) = data.split(splitter)
    return (mins + "." + secs)

class AthleteList(list):
    def __init__(self, athlete):
        self.name = athlete['name']
        self.dob = athlete['dob']
        self.times = athlete['times']
    def best(self):
        return(sorted(set([sanitize(each_record) for each_record in self.times]))[0:3])
