#!/usr/bin/env python3

from tkinter import *
from tkinter import font

# -------------- Colors -------------- #

green_l = '#e3eadb'
green_lm = '#d0ddba'
green_m = '#b2cca2'
green_dm = '#9eb47e'
green_d = '#9dae6d'
red_disabled = "#ff3d3d"
green_active = "#50ff35"
yellow_almost = "#ff9d34"

# -------------- Common -------------- #

# Config

form_label_config = {
    "fg": green_l,
    "bg": green_dm,
    "font": ("Arial", 30)
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

# Place

continue_button_place = {
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

# -------------- Choose Language -------------- #

# Place

lang_btn_place = {
    "relx": 0.50,
    "relwidth": 0.30,
    "relheight": 0.10,
    "anchor": CENTER,
}

# -------------- Initial Form -------------- #

# Config 

inital_title_config = {
    "fg": green_l,
    "bg": green_dm,
    "font": ("Arial", 52)
}

initial_entry_config = {
    "fg": green_dm,
    "bg": green_l,
    "font": ("Arial", 30),
    "relief": FLAT,
}

# Place

initial_gender_radio_place = {
    "relheight": 1,
    "relwidth": 0.333,
    "rely": 0,
}

initial_nation_radio_place = {
    "relheight": 1,
    "relwidth": 0.5,
    "rely": 0,
}

initial_label_place = {
    "relwidth": 0.20,
    "relx":0.15,
    "relheight":0.07
}

initial_entry_place = {
    "relwidth": 0.50,
    "relx":0.35,
    "relheight":0.07
}

# -------------- Instructions -------------- #

# Config

instr_title_config = {
    "fg": green_d,
    "bg": "white",
    "font": ("Arial", 52)
}

instr_text_config = {
    "font": ("Arial", 25),
    "fg": green_d,
    "bg": "white",
    "bd": 0,
    "justify":CENTER,
    "width":850
}

instr_horseshoe_config = {
    "text": "⬤",
    "fg": red_disabled,
    "bg": "white",
    "font": ("Arial",35),
}

instr_secs_left_config = {
    "fg": green_d,
    "bg": "white",
    "font": ("Arial",25)
}

# Place

instr_secs_left_place = {
    "relx": 0.5,
    "rely": 0.83,
    "anchor": CENTER
}

instr_text_place = {
    "relx": 0.05,
    "rely": 0.20,
    "relwidth": 0.9
}

# -------------- Countdown -------------- #

# Config

countdown_config = {
    "text": "",
    "fg": green_d,
    "bg": "white",
    "font": ("Arial",200)
}

# Place

countdown_place = {
    "relx": 0.5,
    "rely": 0.5,
    "anchor": CENTER
}

# -------------- Final Form -------------- #

# Place

question_place = {
    "relwidth": 0.8,
    "relx": 0.10,
    "relheight": 0.07
}

final_yes_place = {
    "relwidth": 0.15,
    "relx": 0.325,
    "relheight": 0.05
}

final_no_place = {
    "relwidth": 0.15,
    "relx": 0.525,
    "relheight": 0.05
}

# -------------- Goodbye Message -------------- #

# Config

goodbye_config = {
    "text":"",
    "fg": green_d,
    "bg": "white",
    "font": ("Arial",80)
}

# Place

goodbye_place = {
    "relx": 0.5,
    "rely": 0.5,
    "anchor": CENTER
}