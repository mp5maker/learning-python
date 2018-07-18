import pickle

try:
    with open('mydata.pickle', 'wb') as mysaveddata:
        pickle.dump([1, 2, 'three'], mysaveddata)
    with open('mydata.pickle', 'rb') as myrestoredata:
        retrieve = pickle.load(myrestoredata)
    print(retrieve)
except pickle.PickleError as perr:
    print("Pickling error: " + str(perr))