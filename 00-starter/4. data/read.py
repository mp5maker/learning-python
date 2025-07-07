def sanitize(string_data):
    if '-' in string_data:
        splitter = '-'
    elif ':' in string_data:
        splitter = ':'
    else:
        return string_data
    (mins, secs) = string_data.split(splitter)
    return(mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as data:
            data = data.readline()
            return data.strip().split(',')
    except IOError as ioerr:
        print("Pickle Error: " + str(ioerr))
        return(None)

james = get_data('james.txt')
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
sarah = get_data('sarah.txt')

james = sorted(set([sanitize(each_record) for each_record in james]))
julie = sorted(set([sanitize(each_record) for each_record in julie]))
mikey = sorted(set([sanitize(each_record) for each_record in mikey]))
sarah = sorted(set([sanitize(each_record) for each_record in sarah]))

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])