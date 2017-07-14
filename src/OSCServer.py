#!/usr/bin/env python3

from liblo import *

import sys
import time
import csv

class MuseServer(ServerThread):
    # Creates the CSV file filled with the form's data and start listening on port 5000
    def __init__(self, app, args):
        self.app = app
        self.subject_number, age, gender, self.nationality = args
        with open("../experiments/%s-%s.csv" % (self.nationality, self.subject_number), 'a', newline='') as csvfile:
            eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            eegwriter.writerow([self.subject_number, age, gender, self.nationality])  
        ServerThread.__init__(self, 5000)

    # Receives EEG and current time data. Saves it in the CSV file along with a boolean flag
    # that indicates if the countdown is being shown (0) or a video is being played (1)
    @make_method('/muse/eeg', 'ffffii')
    def eeg_callback(self, path, args):
        if self.app.started == True and self.app.stopped == False:
            l_ear, l_forehead, r_forehead, r_ear, sec, microsec = args
            with open("../experiments/%s-%s.csv" % (self.nationality, self.subject_number), 'a', newline='') as csvfile:
                eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                eegwriter.writerow([l_ear, l_forehead, r_forehead, r_ear, sec, microsec, self.app.video_playing])

    # Receives horseshoe data
    @make_method('/muse/elements/horseshoe', 'iiii')
    def horseshoe_callback(self, path, args):
        if self.app.started == False:
            l_ear, l_forehead, r_forehead, r_ear = args
            self.app.set_horseshoe(l_ear, l_forehead, r_forehead, r_ear)
