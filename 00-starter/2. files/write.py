try:
    write = open('random_write.txt', 'w')
    print('I am just writing bro!', file=write)
except IOError:
    print("File Error")
finally:
    write.close()