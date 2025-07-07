def sanitize(each_record):
    if '-' in each_record:
        splitter = '-'
    elif ':' in each_record:
        splitter = ':'
    else:
        return each_record
    (mins, secs) = each_record.split(splitter)
    return (mins + "." + secs)

def get_data(filename):
    try:
        with open(filename) as data:
            data = data.readline()
            data = data.strip().split(',')
            return ({'Name': data.pop(0), 
                    'DOB': data.pop(0), 
                    'Times': str(sorted(set([each_record for each_record in data]))[0:3])})
    except IOError as ioerr:
        print("IOError: " + str(ioerr))
        return(None)

photon = get_data('photon.txt')
print('Name: ' + photon['Name'] + ' :: DOB: ' + photon['DOB'] + ' :: Fastest Times:' + photon['Times'])