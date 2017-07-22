#!/usr/bin/env python3

import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

import threading
import sys
import time
import csv

class MuseServer(threading.Thread):
    def __init__(self, app, args):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.app = app
        self.subject_number, age, gender, self.nationality = args
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
        parser.add_argument("--port", type=int, default=5000, help="The port to listen on")
        args = parser.parse_args()

        dispat = dispatcher.Dispatcher()
        dispat.map("/muse/eeg", self.eeg_callback, "EEG")
        dispat.map("/muse/elements/horseshoe", self.horseshoe_callback, "Horseshoe")

        self.server = osc_server.BlockingOSCUDPServer((args.ip, args.port), dispat)
        print("Serving on {}".format(self.server.server_address))

        with open(self.app.experiments_path + "%s-%s.csv" % (self.nationality, self.subject_number), 'a', newline='') as csvfile:
            eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            eegwriter.writerow([self.subject_number, age, gender, self.nationality])
        
        
    def run(self):
        self.server.serve_forever(poll_interval=0.5)

    def stop(self):
        self.server.shutdown()

    # Receives EEG and current time data. Saves it in the CSV file along with a boolean flag
    # that indicates if the countdown is being shown (0) or a video is being played (1)
    def eeg_callback(self, unused_addr, args, l_ear, l_forehead, r_forehead, r_ear, sec, microsec):
        if self.app.started == True and self.app.stopped == False:
            with open(self.app.experiments_path + "%s-%s.csv" % (self.nationality, self.subject_number), 'a', newline='') as csvfile:
                eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                eegwriter.writerow([l_ear, l_forehead, r_forehead, r_ear, sec, microsec, self.app.video_playing])

    # Receives horseshoe data
    def horseshoe_callback(self, unused_addr, args, l_ear, l_forehead, r_forehead, r_ear):
        if self.app.started == False:
            self.app.set_horseshoe(l_ear, l_forehead, r_forehead, r_ear)
