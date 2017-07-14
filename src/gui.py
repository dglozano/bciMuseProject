#!/usr/bin/env python3

from tkinter import *
from tkinter import font
from tkinter import messagebox
from controller import Controller
from style import *
from lang import *
import subprocess
import time

class MainGui():
    def __init__(self):
        self.app = Controller(self)
        self.root = Tk()
        self.root.configure(background=green_lm)
        self.fullscreen()
        self.choose_language()
        self.root.mainloop()

    def fullscreen(self):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-fullscreen', True)
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: e.widget.quit())

    def show_error(self):
        messagebox.showerror("Error", str_initial_form[self.lang]['error'])

    def update_horseshoe(self, l_ear, l_forehead, r_forehead, r_ear, seconds_left=0):
        if seconds_left > 0:
            self.seconds_left.set("%i %s" % (seconds_left, str_instr[self.lang]['secs_left']))
        elif self.app.muse_connected == True:
            self.seconds_left.set(" ")

        self.l_ear.config(fg=self.choose_color(l_ear))
        self.l_forehead.config(fg=self.choose_color(l_forehead))
        self.r_forehead.config(fg=self.choose_color(r_forehead))
        self.r_ear.config(fg=self.choose_color(r_ear))

    def choose_color(self, quality):
        if quality == 4:
            return red_disabled
        elif quality == 1:
            return green_active
        else:
            return yellow_almost

    def check_enable(self):
        if self.app.enable_button == True:
            self.start_button.config(state=NORMAL)
            self.start_button.after(100, self.check_enable)
        else:
            self.start_button.config(state=DISABLED)
            self.start_button.after(100, self.check_enable)

    def gather_data(self):
        subject_number = self.number_entry.get()
        age = self.age_entry.get()
        gender = self.gender_choice.get()
        nationality = self.nationality.get()
        return (subject_number, age, gender, nationality)

    def play_videos(self, videos, countdown_length, subtitles):
        self.instructions.destroy()
        self.countdown_label = Label(self.root, **countdown_config)
        self.countdown_label.place(**countdown_place)
        self.next = False
        self.countdown(countdown_length)
        self.wait_and_play(videos, countdown_length, subtitles)

    def countdown(self, secs):
        if secs > 0:
            self.countdown_label.config(text=secs)
            self.root.after(1000, self.countdown, secs-1)
        else:
            self.next = True

    def wait_and_play(self, videos, countdown_length, subtitles):
        if self.next == True:
            video = videos.pop()
            subtitle = subtitles.pop()
            play_subprocess = subprocess.Popen(['vlc','--play-and-exit','-f',
                                                '--sub-file=' + self.app.resources_path + 'subtitles/'+ self.lang + '-' + subtitle,
                                                '--no-video-title', self.app.resources_path + 'videos/' + video])
            self.app.video_playing = 1
            play_subprocess.wait()
            self.app.video_playing = 0
            self.next = False
            self.countdown(countdown_length)
            if len(videos) > 0:
                self.wait_and_play(videos, countdown_length, subtitles)
            else:
                self.wait_and_final_form()
        else:
            self.root.after(50, self.wait_and_play, videos, countdown_length, subtitles)

    def wait_and_final_form(self):
        if self.next == True:
            self.app.stop()
        else:
            self.root.after(50, self.wait_and_final_form)

    def get_answers(self):
        self.form.destroy()
        canadaWWII =  self.ww2.get()
        malvinas = self.falkland.get()
        maradona = self.maradona.get()
        crosby = self.crosby.get()
        trump = self.trump.get()
        return [canadaWWII, malvinas, maradona, crosby, trump]

    def choose_language(self):
        self.form = Frame(self.root, bg=green_lm)
        self.form.place(**container_place)

        # ----- Config ----- #

        english_button = Button(self.form,text="English", command = self.english, **button_config)
        english_button.bind("<Return>", self.english)
        spanish_button = Button(self.form,text="Español", command = self.spanish, **button_config)
        spanish_button.bind("<Return>", self.spanish)

        # ----- Place ----- #

        english_button.place(rely=0.425, **lang_btn_place)
        spanish_button.place(rely=0.575, **lang_btn_place)

    def spanish(self):
        self.lang = 'esp'
        self.initial_form()

    def english(self):
        self.lang = 'eng'
        self.initial_form()

    def initial_form(self):
        self.form.destroy()

        # ----- Config ----- #

        self.form = Frame(self.root, bg=green_d)
        
        title = Label(self.form, text = str_initial_form[self.lang]['title'], **inital_title_config)

        number_label = Label(self.form, text=str_initial_form[self.lang]['number'], **form_label_config)
        self.number_entry = Entry(self.form,  **initial_entry_config)
        self.number_entry.focus_set()

        age_label = Label(self.form, text=str_initial_form[self.lang]['age'], **form_label_config)
        self.age_entry = Entry(self.form,  **initial_entry_config)

        gender_label = Label(self.form, text=str_initial_form[self.lang]['gender'], **form_label_config)
        gender_frame = Frame(self.form, bg=green_d)
        self.gender_choice = StringVar()
        radio_male = Radiobutton(gender_frame,text=str_initial_form[self.lang]['male'],value="Male",variable=self.gender_choice,**radio_button_config)
        radio_female = Radiobutton(gender_frame,text=str_initial_form[self.lang]['female'],value="Female",variable=self.gender_choice,**radio_button_config)
        radio_other = Radiobutton(gender_frame,text=str_initial_form[self.lang]['other'],value="Other",variable=self.gender_choice,**radio_button_config)

        nationality_label = Label(self.form, text=str_initial_form[self.lang]['nationality'], **form_label_config)
        nationality_frame = Frame(self.form, bg=green_d)
        self.nationality = StringVar()
        radio_arg = Radiobutton(nationality_frame,text=str_initial_form[self.lang]['arg'],value="Argentina",variable=self.nationality,**radio_button_config)
        radio_cad = Radiobutton(nationality_frame,text=str_initial_form[self.lang]['cad'],value="Canada",variable=self.nationality,**radio_button_config)

        continue_button = Button(self.form,text=str_initial_form[self.lang]['continue'], command = self.app.continue_to_instructions, **button_config)
        continue_button.bind("<Return>", self.app.continue_to_instructions)

        # ----- Place ----- #

        self.form.place(**container_place)
        title.place(**title_place)

        number_label.place(rely=0.25, **initial_label_place)
        self.number_entry.place(rely=0.25, **initial_entry_place)

        age_label.place(rely=0.37, **initial_label_place)
        self.age_entry.place(rely=0.37, **initial_entry_place)

        gender_label.place(rely=0.49, **initial_label_place)
        gender_frame.place(rely=0.49, **initial_entry_place)
        radio_male.place(relx=0, **initial_gender_radio_place)
        radio_female.place(relx=0.33, **initial_gender_radio_place)
        radio_other.place(relx=0.66, **initial_gender_radio_place)

        nationality_label.place(rely=0.61, **initial_label_place)
        nationality_frame.place(rely=0.61, **initial_entry_place)
        radio_arg.place(relx=0, **initial_nation_radio_place)
        radio_cad.place(relx=0.5, **initial_nation_radio_place)

        continue_button.place(**continue_button_place)

    def instructions(self):
        self.form.destroy()
        self.root.configure(background="white")
        self.seconds_left = StringVar()
        self.instructions = Frame(self.root, bg="white")
        self.instructions.place(**container_place)

        # ----- Config ----- #

        title = Label(self.instructions, text=str_instr[self.lang]['title'], **instr_title_config)
        instructions_text = Message(self.instructions, text = str_instr[self.lang]['content'], **instr_text_config)
        label_seconds = Label(self.instructions, textvariable=self.seconds_left, **instr_secs_left_config)
        self.l_ear = Label(self.instructions, **instr_horseshoe_config)
        self.l_forehead = Label(self.instructions, **instr_horseshoe_config)
        self.r_forehead = Label(self.instructions, **instr_horseshoe_config)
        self.r_ear = Label(self.instructions, **instr_horseshoe_config)
        self.start_button = Button(self.instructions,text=str_instr[self.lang]['start'],
                                        state=DISABLED, command = self.app.start, **button_config)

        # ----- Place ----- #
        
        title.place(**title_place)
        instructions_text.place(**instr_text_place)
        label_seconds.place(**instr_secs_left_place)
        self.l_ear.place(relx=0.425, rely=0.75, anchor = CENTER)
        self.l_forehead.place(relx=0.475, rely=0.72, anchor = CENTER)
        self.r_forehead.place(relx=0.525, rely=0.72, anchor = CENTER)
        self.r_ear.place(relx=0.575, rely=0.75, anchor = CENTER)
        self.start_button.place(**continue_button_place)
    
        self.check_enable()

    def final_form(self):
        self.countdown_label.destroy()
        self.form = Frame(self.root, bg=green_d)
        self.form.place(**container_place)

        # ----- Vars ----- #

        self.ww2 = IntVar()
        self.falkland = IntVar()
        self.maradona = IntVar()
        self.crosby = IntVar()
        self.trump = IntVar()

        # ----- Config/Place ----- #
        
        self.create_yes_no_question(self.form, 'ww2', self.ww2, 0.05)
        self.create_yes_no_question(self.form, 'falkland', self.falkland, 0.21)
        self.create_yes_no_question(self.form, 'maradona', self.maradona, 0.37)
        self.create_yes_no_question(self.form, 'crosby', self.crosby, 0.53)
        self.create_yes_no_question(self.form, 'trump', self.trump, 0.69)

        continue_button = Button(self.form,text=str_final_form[self.lang]['continue'],
                                    command = self.app.exit_form_submit, **button_config)
        continue_button.bind("<Return>", self.app.exit_form_submit)

        continue_button.place(**continue_button_place)

    def create_yes_no_question(self, parent, q_key, str_var, rely_place):
        yes = str_final_form[self.lang]['yes']
        no = str_final_form[self.lang]['no']

        # ----- Config ----- #

        question_label = Label(parent, text = str_final_form[self.lang][q_key], **form_label_config)
        answer_yes = Radiobutton(parent, text = yes, value=1, variable = str_var, **radio_button_config)
        answer_no = Radiobutton(parent, text = no, value=0, variable = str_var, **radio_button_config)

        # ----- Place ----- #

        question_label.place(rely = rely_place, **question_place)
        answer_yes.place(rely = rely_place + 0.09, **final_yes_place)
        answer_no.place(rely = rely_place + 0.09, **final_no_place)
    
    def goodbye_message(self):
        label = Label(self.root, **goodbye_config)
        label.config(text = str_final_form[self.lang]['goodbye'])
        label.place(**goodbye_place)


if __name__ == '__main__':
    MainGui() 