#!/usr/bin/env python3

from tkinter import *
from tkinter import font

# ----- Colors ----- #

green_l = '#e3eadb'
green_lm = '#d0ddba'
green_m = '#b2cca2'
green_dm = '#9eb47e'
green_d = '#9dae6d'
red_disabled = "#ff3d3d"
green_active = "#50ff35"
yellow_almost = "#ff9d34"

# ----- Choose Language ----- #

# Position

lang_btn_position = {
    "relx": 0.50,
    "relwidth": 0.30,
    "relheight": 0.10,
    "anchor": CENTER,
}

# ----- Initial Form ----- #

# Config 

inital_title_config = {
    "fg": green_l,
    "bg": green_dm,
    "font": ("Arial", 52)
}

initial_gender_radio_config = {
    "relheight": 1,
    "relwidth": 0.333,
    "rely": 0,
}

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
    "relwidth":0.8,
    "relx":0.10,
    "relheight":0.15,
    "rely":0.05
}

instructions_text_config = {
    "font": ("Arial", 25),
    "fg": green_d,
    "bg": "white",
    "bd": 0,
    "justify":CENTER,
    "width":850
}

question_position = {
    "relwidth": 0.8,
    "relx": 0.10,
    "relheight": 0.07
}