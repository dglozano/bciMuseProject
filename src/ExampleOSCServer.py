from liblo import *

import sys
import time
import pickle
import csv

class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self, gui, args):
        self.gui = gui
        first_name, self.last_name, age, gender, self.nationality = args
        with open("%s-%s.csv" % (self.last_name, self.nationality), 'a', newline='') as csvfile:
            eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            eegwriter.writerow([first_name, self.last_name, age, gender, self.nationality])  
        ServerThread.__init__(self, 5000)

    #receive EEG data
    @make_method('/muse/eeg', 'ffffii')
    def eeg_callback(self, path, args):
        if self.gui.started == True and self.gui.stop == False:
            print(args)
            l_ear, l_forehead, r_forehead, r_ear, sec, microsec = args
            with open("%s-%s.csv" % (self.last_name, self.nationality), 'a', newline='') as csvfile:
                eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                eegwriter.writerow([l_ear, l_forehead, r_forehead, r_ear, sec, microsec, self.gui.video_playing])

    @make_method('/muse/elements/horseshoe', 'iiii')
    def horseshoe_callback(self, path, args):
        if self.gui.enable_button == False:
            l_ear, l_forehead, r_forehead, r_ear = args
            self.gui.set_horseshoe(l_ear, l_forehead, r_forehead, r_ear)
