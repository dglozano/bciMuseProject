from tkinter import *
from ExampleOSCServer import MuseServer
import time

green_l = '#e3eadb'
green_lm = '#d0ddba'
green_m = '#b2cca2'
green_dm = '#9eb47e'
green_d = '#9dae6d'

form_label_config = {
    "fg": green_l,
    "bg": green_dm,
    "font": ("Arial", 30)
}

form_label_position = {
    "relwidth": 0.20,
    "relx":0.15,
    "relheight":0.07
}

form_entry_config = {
    "fg": green_dm,
    "bg": green_l,
    "font": ("Arial", 30),
    "relief": FLAT,
}

form_entry_position = {
    "relwidth": 0.50,
    "relx":0.35,
    "relheight":0.07
}

radio_button_config = {
    "font":("Arial",30),
    "bg":green_d,
    "fg":green_l,
    "relief":RAISED,
    "anchor":CENTER,
    "cursor":"mouse",
    "borderwidth":0,
    "activeforeground":green_l,
    "activebackground":green_m,
    "selectcolor":green_m,
    "indicatoron":0,
}

class MainGui():
    def __init__(self):
        self.root = Tk()
        self.root.configure(background=green_lm)
        self.fullscreen()
        self.display_form()
        self.root.mainloop()

    def fullscreen(self):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-fullscreen', True)
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: e.widget.quit())

    def continue_form_cback(self):
        #gather data
        self.form.destroy()
        self.root.configure(background="white")
        self.display_instructions()

    def display_instructions(self):
        # load instructions 
        # display nicer the horseshoe
        self.horseshoe = StringVar()
        self.good_connection = False
        label = Label(self.root, textvariable=self.horseshoe, **form_label_config)
        label.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
        try:
            self.server = MuseServer(self)
        except (ServerError, err) as e:
            print(e)
            sys.exit()
        else:
            self.server.start()

    def set_horseshoe(self, l_ear, l_forehead, r_forehead, r_ear):
        if l_ear == 1 and l_forehead == 1 and r_forehead == 1 and r_ear == 1:
            if self.good_connection == False:
                self.good_connection = True
                self.time_good_connection_started = time.time()
                self.horseshoe.set("start LE %i LF %i RF %i RE %i" % (l_ear,l_forehead,r_forehead,r_ear))
            elif time.time() - self.time_good_connection_started >= 5:
                self.horseshoe.set("5seco LE %i LF %i RF %i RE %i" % (l_ear,l_forehead,r_forehead,r_ear))
            else:
                self.horseshoe.set("%i LE %i LF %i RF %i RE %i" % (time.time() - self.time_good_connection_started,l_ear,l_forehead,r_forehead,r_ear))
        else:
            self.good_connection = False
            self.horseshoe.set("stopp LE %i LF %i RF %i RE %i" % (l_ear,l_forehead,r_forehead,r_ear))

    #TODO 01: fix fonts
    def display_form(self):
        self.form = Frame(self.root, bg=green_d)
        title = Label(self.form, text="Subject's Data Form", fg=green_l, bg=green_dm, font=("Arial", 52))

        first_name_label = Label(self.form, text="First Name", **form_label_config)
        self.first_name_entry = Entry(self.form,  **form_entry_config)

        last_name_label = Label(self.form, text="Last Name", **form_label_config)
        self.last_name_entry = Entry(self.form,  **form_entry_config)

        age_label = Label(self.form, text="Age", **form_label_config)
        self.age_entry = Entry(self.form,  **form_entry_config)

        gender_label = Label(self.form, text="Gender", **form_label_config)
        gender_frame = Frame(self.form, bg=green_d)
        self.gender_choice = IntVar()
        radio_male = Radiobutton(gender_frame,text="Male",value=1,variable=self.gender_choice,**radio_button_config)
        radio_female = Radiobutton(gender_frame,text="Female",value=2,variable=self.gender_choice,**radio_button_config)
        radio_other = Radiobutton(gender_frame,text="Other",value=3,variable=self.gender_choice,**radio_button_config)

        nationality_label = Label(self.form, text="Nationality", **form_label_config)
        nationality_frame = Frame(self.form, bg=green_d)
        self.nationality = IntVar()
        radio_arg = Radiobutton(nationality_frame,text="Argentina",value=1,variable=self.nationality,**radio_button_config)
        radio_cad = Radiobutton(nationality_frame,text="Canada",value=2,variable=self.nationality,**radio_button_config)

        continue_button = Button(self.form,text="Continue",
                                    font=("Arial", 30),
                                    bg=green_dm, fg=green_l,
                                    activebackground=green_m,
                                    activeforeground=green_l,
                                    command = self.continue_form_cback)

        ### Place ### 

        self.form.place(relwidth=0.7, relx=0.15, relheight=1.0, rely=0.0)
        title.place(relwidth=0.7, relx=0.15, relheight=0.15, rely=0.05)

        first_name_label.place(rely=0.25, **form_label_position)
        self.first_name_entry.place(rely=0.25, **form_entry_position)

        last_name_label.place(rely=0.37, **form_label_position)
        self.last_name_entry.place(rely=0.37, **form_entry_position)

        age_label.place(rely=0.49, **form_label_position)
        self.age_entry.place(rely=0.49, **form_entry_position)

        gender_label.place(rely=0.61, **form_label_position)
        gender_frame.place(rely=0.61, **form_entry_position)
        radio_male.place(relx=0, rely=0, relheight=1, relwidth=0.33)
        radio_female.place(relx=0.33, rely=0, relheight=1, relwidth=0.33)
        radio_other.place(relx=0.66, rely=0, relheight=1, relwidth=0.34)

        nationality_label.place(rely=0.73, **form_label_position)
        nationality_frame.place(rely=0.73, **form_entry_position)
        radio_arg.place(relx=0, rely=0, relheight=1,relwidth=0.5)
        radio_cad.place(relx=0.5, rely=0, relheight=1,relwidth=0.5)

        continue_button.place(relx=0.325, rely=0.88, relwidth=0.35, relheight=0.07)

if __name__ == '__main__':
    MainGui() 