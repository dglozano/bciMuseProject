from liblo import *

import sys
import time
import pickle
import csv

PATHS = pickle.load(open("paths.p","rb"))

class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print("%s %f %f %f %f" % (path,l_ear,l_forehead,r_forehead,r_ear))
        with open('muse.csv', 'a', newline='') as csvfile:
            eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            eegwriter.writerow([path, l_ear, l_forehead, r_forehead, r_ear])

try:
    server = MuseServer()
except (ServerError, err) as e:
    print(e)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)