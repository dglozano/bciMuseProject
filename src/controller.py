#!/usr/bin/env python3

from OSCServer import MuseServer

import subprocess
import time
import csv


class Controller():
    def __init__(self, gui):
        self.view = gui; 
        self.started = False
        self.stopped = False
        self.video_playing = 0
        self.experiments_path = "experiments/"
        self.resources_path = "res/"
        self.videos = ["37s - Canada WWII.avi", "30s - Maradona.mp4", "30s - Trump.mp4", "37s - Crosby.mp4", "40s - Malvinas.mp4"]
        self.subtitles = ["Canada WWII.srt", "Maradona.srt", "Trump.srt", "Crosby.srt", "Malvinas.srt"]

    def continue_to_instructions(self, event = None):
        self.user_data = self.view.gather_data()
        if self.is_complete() == False:
                self.view.show_error()
        else:
            self.enable_button = False
            self.good_connection = False
            self.muse_connected = False
            self.view.instructions()
            self.start_muse_server()

    def start_muse_server(self):
        try:
            self.server = MuseServer(self, self.user_data)
        except (ServerError, err) as e:
            print(e)
            sys.exit()
        else:
            self.server.start()

    def set_horseshoe(self, l_ear, l_forehead, r_forehead, r_ear):
        self.muse_connected = True
        if l_ear == 1 and l_forehead == 1 and r_forehead == 1 and r_ear == 1:
            if self.good_connection == False:
                self.good_connection = True
                self.enable_button = False
                self.time_good_connection_started = time.time()
                self.view.update_horseshoe(l_ear,l_forehead,r_forehead,r_ear)
            elif time.time() - self.time_good_connection_started >= 5:
                self.enable_button = True
                self.view.update_horseshoe(l_ear, l_forehead, r_forehead, r_ear, 0)
            else:
                time_remaining = 6 - time.time() + self.time_good_connection_started
                self.enable_button = False
                self.view.update_horseshoe(l_ear, l_forehead, r_forehead, r_ear, time_remaining)
        else:
            self.good_connection = False
            self.enable_button = False
            self.view.update_horseshoe(l_ear,l_forehead,r_forehead,r_ear)

    def is_complete(self):
        for val in self.user_data:
            if val is None or val == '':
                return False
        return True

    def start(self):
        self.started = True
        self.next = False
        self.view.play_videos(videos = self.videos, countdown_length = 10, subtitles = self.subtitles)

    def stop(self):
        self.stopped = True
        self.view.final_form()

    def exit_form_submit(self):
        answers = self.view.get_answers()
        with open(self.experiments_path + "/%s-%s.csv" % (self.user_data[3], self.user_data[0]), 'a', newline='') as csvfile:
            eegwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            eegwriter.writerow(answers) 
        self.view.goodbye_message()

if __name__ == '__main__':
    Controller() 