from tkinter import *
from tkinter import messagebox
from ExampleOSCServer import MuseServer
import subprocess
import time

#run this before muse-io --device 00:06:66:78:45:25 --osc osc.udp://localhost:5000

green_l = '#e3eadb'
green_lm = '#d0ddba'
green_m = '#b2cca2'
green_dm = '#9eb47e'
green_d = '#9dae6d'
red_disabled = "#ff3d3d"

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

button_config = {
    "font": ("Arial", 30),
    "bg": green_dm,
    "fg": green_l,
    "activebackground": green_m,
    "activeforeground": green_l,
    "disabledforeground": red_disabled
}

button_place = {
    "relx": 0.50,
    "rely": 0.915,
    "anchor": CENTER,
    "relwidth": 0.35,
    "relheight": 0.07
}

container_place = {
    "relwidth":0.7,
    "relx":0.15,
    "relheight":1.0,
    "rely":0.0
}

title_place = {
    "relwidth":0.7,
    "relx":0.15,
    "relheight":0.15,
    "rely":0.05
}

instructions_text_config = {
    "font": ("Arial", 25),
    "fg": green_d,
    "bg": "white",
    "bd": 0,
    "justify":CENTER,
    "width":800
}

class MainGui():
    def __init__(self):
        self.root = Tk()
        self.root.configure(background=green_lm)
        self.fullscreen()
        self.started = False
        self.stop = False
        self.video_playing = 0
        self.display_form()
        self.root.mainloop()

    def fullscreen(self):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-fullscreen', True)
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: e.widget.quit())

    def continue_form_cback(self, event = None):
        self.user_data = self.gather_data()
        if self.is_complete() == False:
            messagebox.showerror("Error", "You must complete the form to proccede. Try Again.")
        else:
            self.form.destroy()
            self.root.configure(background="white")
            self.display_instructions()

    def display_instructions(self):
        # load instructions 
        # display nicer the horseshoe
        self.instructions = Frame(self.root, bg="white")
        self.instructions.place(**container_place)

        title = Label(self.instructions, text="Instructions", fg=green_d, bg="white", font=("Arial", 52))
        title.place(**title_place)

        instructions_text = Message(self.instructions, text = "BlabldslkafajslkfdsdafjsakdasfdjlksaBlabldslkafajslkfdsdafjsakdasfdjlksafjldsakfdsafsjdalfksakladfjaksdfjsaldfjfjldsakfdsafsjdalfksakladfjaksdfjsaldfj", **instructions_text_config)
        instructions_text.place(relx=0.15, rely=0.25, relwidth=0.7)

        self.horseshoe = StringVar()
        self.horseshoe.set("Muse is not connected")
        self.good_connection = False
        self.enable_button = False

        label = Label(self.instructions, textvariable=self.horseshoe, fg = green_d, bg = "white", font=("Arial",30))
        label.place(relx=0.5, rely=0.75, anchor = CENTER)

        self.start_button = Button(self.instructions,text="Start", state=DISABLED, command = self.start, **button_config)
        self.start_button.place(**button_place)
        
        try:
            self.server = MuseServer(self, self.user_data)
        except (ServerError, err) as e:
            print(e)
            sys.exit()
        else:
            self.server.start()
        self.check_enable()

    def set_horseshoe(self, l_ear, l_forehead, r_forehead, r_ear):
        if l_ear == 1 and l_forehead == 1 and r_forehead == 1 and r_ear == 1:
            if self.good_connection == False:
                self.good_connection = True
                self.time_good_connection_started = time.time()
                self.horseshoe.set("LE %i LF %i RF %i RE %i" % (l_ear,l_forehead,r_forehead,r_ear))
            elif time.time() - self.time_good_connection_started >= 5:
                self.enable_button = True
                self.horseshoe.set("Good Connection acquired!")
            else:
                self.horseshoe.set("LE %i LF %i RF %i RE %i\n%i Seconds left" 
                % (l_ear,l_forehead,r_forehead,r_ear,6 - time.time() + self.time_good_connection_started))
        else:
            self.good_connection = False
            self.enable_button = False
            self.horseshoe.set("LE %i LF %i RF %i RE %i" % (l_ear,l_forehead,r_forehead,r_ear))

    def check_enable(self):
        if self.enable_button == True:
            self.start_button.config(state=NORMAL)
        else:
            self.start_button.config(state=DISABLED)
            self.start_button.after(100, self.check_enable)

    def gather_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_choice.get()
        nationality = self.nationality.get()
        return (first_name, last_name, age, gender, nationality)

    def is_complete(self):
        for val in self.user_data:
            if val is None or val == '':
                return False
        return True

    def start(self):
        self.instructions.destroy()
        self.countdown_label = Label(self.root, text="", fg = green_d, bg = "white", font=("Arial",200))
        self.countdown_label.place(relx=0.5, rely=0.5, anchor = CENTER)
        self.started = True
        self.next = False
        self.countdown(10)
        videos = ["30s - Trump.mp4", "30s - Maradona.mp4", "30s - Gretzky.mp4", "30s - Malvinas.mp4", "40s - Malvinas.mp4"]
        self.wait_and_play(videos)

    def countdown(self, secs):
        if secs > 0:
            self.countdown_label.config(text=secs)
            self.root.after(1000, self.countdown, secs-1)
        else:
            self.next = True

    def wait_and_play(self, videos):
        if self.next == True:
            video = videos.pop()
            play_subprocess = subprocess.Popen(['vlc','--play-and-exit','-f','--no-video-title', '../res/' + video])
            self.video_playing = 1
            play_subprocess.wait()
            self.video_playing = 0
            self.next = False
            self.countdown(10)
            if len(videos) > 0:
                self.wait_and_play(videos)
            else:
                self.exit()
        else:
            self.root.after(50, self.wait_and_play, videos)

    def exit(self):
        if self.next == True:
            self.stop = True
            self.countdown_label.config(text = "Thank you for collaborating!\nPress <Escape> to Exit.", font=("Arial",80))
        else:
            self.root.after(50, self.exit)

    #TODO 01: fix fonts
    def display_form(self):
        self.form = Frame(self.root, bg=green_d)
        title = Label(self.form, text="Subject's Data Form", fg=green_l, bg=green_dm, font=("Arial", 52))

        first_name_label = Label(self.form, text="First Name", **form_label_config)
        self.first_name_entry = Entry(self.form,  **form_entry_config)
        self.first_name_entry.focus_set()

        last_name_label = Label(self.form, text="Last Name", **form_label_config)
        self.last_name_entry = Entry(self.form,  **form_entry_config)

        age_label = Label(self.form, text="Age", **form_label_config)
        self.age_entry = Entry(self.form,  **form_entry_config)

        gender_label = Label(self.form, text="Gender", **form_label_config)
        gender_frame = Frame(self.form, bg=green_d)
        self.gender_choice = StringVar()
        radio_male = Radiobutton(gender_frame,text="Male",value="Male",variable=self.gender_choice,**radio_button_config)
        radio_female = Radiobutton(gender_frame,text="Female",value="Female",variable=self.gender_choice,**radio_button_config)
        radio_other = Radiobutton(gender_frame,text="Other",value="Other",variable=self.gender_choice,**radio_button_config)

        nationality_label = Label(self.form, text="Nationality", **form_label_config)
        nationality_frame = Frame(self.form, bg=green_d)
        self.nationality = StringVar()
        radio_arg = Radiobutton(nationality_frame,text="Argentina",value="Argentina",variable=self.nationality,**radio_button_config)
        radio_cad = Radiobutton(nationality_frame,text="Canada",value="Canada",variable=self.nationality,**radio_button_config)

        continue_button = Button(self.form,text="Continue", command = self.continue_form_cback, **button_config)
        continue_button.bind("<Return>", self.continue_form_cback)

        ### Place ### 

        self.form.place(**container_place)
        title.place(**title_place)

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

        continue_button.place(**button_place)

if __name__ == '__main__':
    MainGui() 