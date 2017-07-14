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

    def instructions(self):
        self.form.destroy()
        self.root.configure(background="white")
        self.instructions = Frame(self.root, bg="white")
        self.instructions.place(**container_place)

        title = Label(self.instructions, text=str_instr[self.lang]['title'], fg=green_d, bg="white", font=("Arial", 52))
        title.place(**title_place)
        
        instructions_text = Message(self.instructions, text = str_instr[self.lang]['content'], **instructions_text_config)
        instructions_text.place(relx=0.05, rely=0.20, relwidth=0.9)

        self.seconds_left = StringVar()
        label_seconds = Label(self.instructions, textvariable=self.seconds_left,
                                    fg = green_d, bg = "white", font=("Arial",25))
        label_seconds.place(relx=0.5, rely=0.83, anchor = CENTER)

        self.l_ear = Label(self.instructions, text="⬤",fg=red_disabled, bg = "white", font=("Arial",35))
        self.l_forehead = Label(self.instructions, text="⬤",fg=red_disabled, bg = "white", font=("Arial",35))
        self.r_forehead = Label(self.instructions, text="⬤",fg=red_disabled, bg = "white", font=("Arial",35))
        self.r_ear = Label(self.instructions, text="⬤",fg=red_disabled, bg = "white", font=("Arial",35))
        self.l_ear.place(relx=0.425, rely=0.75, anchor = CENTER)
        self.l_forehead.place(relx=0.475, rely=0.72, anchor = CENTER)
        self.r_forehead.place(relx=0.525, rely=0.72, anchor = CENTER)
        self.r_ear.place(relx=0.575, rely=0.75, anchor = CENTER)

        self.start_button = Button(self.instructions,text=str_instr[self.lang]['start'],
                                    state=DISABLED, command = self.app.start, **button_config)
        self.start_button.place(**button_place)
    
        self.check_enable()

    def update_horseshoe(self, l_ear, l_forehead, r_forehead, r_ear, seconds_left=0):
        if seconds_left > 0:
            self.seconds_left.set("%i Seconds left" % (seconds_left))
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
        self.countdown_label = Label(self.root, text="", fg = green_d, bg = "white", font=("Arial",200))
        self.countdown_label.place(relx=0.5, rely=0.5, anchor = CENTER)
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
                                                '--sub-file=../res/subtitles/'+ self.lang + '-' + subtitle,
                                                '--no-video-title', '../res/videos/' + video])
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
        canadaWWII =  self.canadaWWII.get()
        malvinas = self.malvinas.get()
        maradona = self.maradona.get()
        crosby = self.crosby.get()
        trump = self.trump.get()
        return [canadaWWII, malvinas, maradona, crosby, trump]

    def choose_language(self):
        self.form = Frame(self.root, bg=green_lm)
        self.form.place(**container_place)

        english_button = Button(self.form,text="English", command = self.english, **button_config)
        english_button.bind("<Return>", self.english)
        spanish_button = Button(self.form,text="Español", command = self.spanish, **button_config)
        spanish_button.bind("<Return>", self.spanish)

        english_button.place(rely=0.425, **lang_btn_position)
        spanish_button.place(rely=0.575, **lang_btn_position)

    def spanish(self):
        self.lang = 'esp'
        self.initial_form()

    def english(self):
        self.lang = 'eng'
        self.initial_form()

    def initial_form(self):
        self.form.destroy()
        self.form = Frame(self.root, bg=green_d)
        
        title = Label(self.form, text = str_initial_form[self.lang]['title'], **inital_title_config)

        number_label = Label(self.form, text=str_initial_form[self.lang]['number'], **form_label_config)
        self.number_entry = Entry(self.form,  **form_entry_config)
        self.number_entry.focus_set()

        age_label = Label(self.form, text=str_initial_form[self.lang]['age'], **form_label_config)
        self.age_entry = Entry(self.form,  **form_entry_config)

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

        ### Place ### 

        self.form.place(**container_place)
        title.place(**title_place)

        number_label.place(rely=0.25, **form_label_position)
        self.number_entry.place(rely=0.25, **form_entry_position)

        age_label.place(rely=0.37, **form_label_position)
        self.age_entry.place(rely=0.37, **form_entry_position)

        gender_label.place(rely=0.49, **form_label_position)
        gender_frame.place(rely=0.49, **form_entry_position)
        radio_male.place(relx=0, **initial_gender_radio_config)
        radio_female.place(relx=0.33, **initial_gender_radio_config)
        radio_other.place(relx=0.66, **initial_gender_radio_config)

        nationality_label.place(rely=0.61, **form_label_position)
        nationality_frame.place(rely=0.61, **form_entry_position)
        radio_arg.place(relx=0, rely=0, relheight=1,relwidth=0.5)
        radio_cad.place(relx=0.5, rely=0, relheight=1,relwidth=0.5)

        continue_button.place(**button_place)

    def final_form(self):
        self.countdown_label.destroy()
        self.form = Frame(self.root, bg=green_d)

        self.form.place(**container_place)

        yes = str_final_form[self.lang]['yes']
        no = str_final_form[self.lang]['no']

        canadaWWII_label = Label(self.form, text=str_final_form[self.lang]['ww2'], **form_label_config)
        canadaWWII_label.place(rely = 0.05, **question_position)
        self.canadaWWII = IntVar()
        yes_canadaWWII = Radiobutton(self.form,text=yes,value=1,variable=self.canadaWWII,**radio_button_config)
        no_canadaWWII = Radiobutton(self.form,text=no,value=0,variable=self.canadaWWII,**radio_button_config)
        yes_canadaWWII.place(rely=0.14, relwidth = 0.15, relx = 0.325, relheight = 0.05)
        no_canadaWWII.place(rely=0.14, relwidth = 0.15, relx = 0.525, relheight = 0.05)

        malvinas_label = Label(self.form, text=str_final_form[self.lang]['falkland'], **form_label_config)
        malvinas_label.place(rely=0.21, **question_position)
        self.malvinas = IntVar()
        yes_malvinas = Radiobutton(self.form,text=yes,value=1,variable=self.malvinas,**radio_button_config)
        no_malvinas = Radiobutton(self.form,text=no,value=0,variable=self.malvinas,**radio_button_config)
        yes_malvinas.place(rely=0.30, relwidth = 0.15, relx = 0.325, relheight = 0.05)
        no_malvinas.place(rely=0.30, relwidth = 0.15, relx = 0.525, relheight = 0.05)

        maradona_label = Label(self.form, text=str_final_form[self.lang]['maradona'], **form_label_config)
        maradona_label.place(rely=0.37, **question_position)
        self.maradona = IntVar()
        yes_maradona = Radiobutton(self.form,text=yes,value=1,variable=self.maradona,**radio_button_config)
        no_maradona = Radiobutton(self.form,text=no,value=0,variable=self.maradona,**radio_button_config)
        yes_maradona.place(rely=0.46, relwidth = 0.15, relx = 0.325, relheight = 0.05)
        no_maradona.place(rely=0.46, relwidth = 0.15, relx = 0.525, relheight = 0.05)

        crosby_label = Label(self.form, text=str_final_form[self.lang]['crosby'], **form_label_config)
        crosby_label.place(rely=0.53, **question_position)
        self.crosby = IntVar()
        yes_crosby = Radiobutton(self.form,text=yes,value=1,variable=self.crosby,**radio_button_config)
        no_crosby = Radiobutton(self.form,text=no,value=0,variable=self.crosby,**radio_button_config)
        yes_crosby.place(rely=0.62, relwidth = 0.15, relx = 0.325, relheight = 0.05)
        no_crosby.place(rely=0.62, relwidth = 0.15, relx = 0.525, relheight = 0.05)

        trump_label = Label(self.form, text=str_final_form[self.lang]['trump'], **form_label_config)
        trump_label.place(rely=0.69, **question_position)
        self.trump = IntVar()
        yes_trump = Radiobutton(self.form,text=yes,value=1,variable=self.trump,**radio_button_config)
        no_trump = Radiobutton(self.form,text=no,value=0,variable=self.trump,**radio_button_config)
        yes_trump.place(rely=0.78, relwidth = 0.15, relx = 0.325, relheight = 0.05)
        no_trump.place(rely=0.78, relwidth = 0.15, relx = 0.525, relheight = 0.05)

        continue_button = Button(self.form,text=str_final_form[self.lang]['continue'], command = self.app.exit_form_submit, **button_config)
        continue_button.bind("<Return>", self.app.exit_form_submit)
        continue_button.place(**button_place)

    def goodbye_message(self):
        label = Label(self.root, text="", fg = green_d, bg = "white", font=("Arial",80))
        label.config(text = str_final_form[self.lang]['goodbye'])
        label.place(relx=0.5, rely=0.5, anchor = CENTER)

if __name__ == '__main__':
    MainGui() 