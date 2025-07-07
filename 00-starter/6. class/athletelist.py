class AthleteList(list):
    def __init__(self, athlete):
        self.name = athlete['name']
        self.dob = athlete['dob']
        self.times = athlete['times']
    def best(self):
        return(sorted(set([sanitize(each_record) for each_record in self.times]))[0:3])

def sanitize(data):
    if '-' in data:
        splitter = '-'
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (mins, secs) = data.split(splitter)
    return (mins + "." + secs)

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

james = get_data('james.txt')
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
sarah = get_data('sarah.txt')

print("Athlete Name: " + james.name + ", DOB: " + james.dob + ", Top 3:" + str(james.best()))
