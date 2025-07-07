import os

try:
    if os.path.exists('random.txt'):
        data = open('random.txt')
        # print(data.readline(), end='')
        for each_line in data:
            try:
                if not each_line.find(":") == -1:
                    (role, line_spoken) = each_line.split(":", 1)
                    print(role, end='')
                    print(' said: ', end='')
                    print(line_spoken, end='')
            except ValueError:
                pass
        data.close()
    else:
        print('The data file is missing!')
except IOError:
    print('The data file is missing!')