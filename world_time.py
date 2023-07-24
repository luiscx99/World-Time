import tkinter as tk
import ttkbootstrap as ttk
from ttkwidgets.autocomplete import AutocompleteEntry
from zonedict import allzone as ct
from datetime import datetime
from PIL import Image, ImageTk
import random
import pytz


# world time version 0.6 by: luiscx99

class App(ttk.Window):
    # windows
    def __init__(self, title, size):
        super().__init__()
        ttk.Style("yeti")
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.maxsize(size[0], size[1])

        # title_frame
        self.titlelable = Title_frame(self)
        # input_fram
        self.inputframe = Input_aframe(self)
        # output local
        self.outputlocal = Local_time(
            self, 'The local time is:', 'Calibri 9 bold', 'Calibri 10 bold')
        # output txt
        self.outputalltext = Output_txtframe(
            self, 'info', 'inverse-info', 'Calibri 11 bold', 'Calibri 15 bold', '#258fac')
        # time frame
        self.timeframe = Time_frame(
            self, 'info', 'inverse-info', 'Calibri 50 bold')
        # Setting app icon
        icon = get_styleimg('GUI/world_time_icon.ico', 256, 256)
        self.wm_iconphoto(False, icon)

        self.mainloop()


# import time zone dictionary
all_zone = ct.zone_dict()

TXT_T = 'This is the current time in:'
backup_country = {}

# fix country input to title case


def country_title_c():
    inputstr = entry_str.get()
    if inputstr in all_zone:
        strinput = inputstr
    else:
        strinput = inputstr.title()
    return strinput

# Get country time


def get_time():
    global country_tz, current_time_in
    check_error(0)
    gettime_zone = all_zone[country_title_c()]
    timeIn = The_time(gettime_zone)
    backup_country[1] = gettime_zone
    current_time_in = timeIn.day_time('%I:%M %p')
    check_error(1)

    output_ctime()

# set country time


def output_ctime():
    output_str.set(country_title_c())
    output_txt.set(TXT_T)
    output_timestr.set(current_time_in)
    entry_str.set('')
    upd_localtime()

# local time


def upd_localtime():
    global current_day
    current_day = The_time(False).day_time("%m/%d/%Y, %I:%M %p")
    output_local_time_str.set(current_day)
    return current_day

# set default time


def default_time():
    default_zone, country_zone = random.choice(list(all_zone.items()))
    save_time = The_time(country_zone)
    backup_country[1] = country_zone
    output_str.set(default_zone)
    default_time_in = save_time.day_time('%I:%M %p')
    output_timestr.set(default_time_in)
    output_txt.set(TXT_T)

# setup error frame


def setup_error_frame():
    error_lable.pack()
    entry_str.set('')
    error_lable.after(5000, error_lable.pack_forget)

# check for empty or wrong country


def check_error(val: bool):
    if not entry_str.get() and not val:
        setup_error_frame()
    elif entry_str.get() and not val:
        strinput = country_title_c()
        if strinput not in all_zone:
            setup_error_frame()

# get images


def get_styleimg(img: str, wdth: int, hght: int):
    image = Image.open(img)
    image = image.resize((wdth, hght))
    image = ImageTk.PhotoImage(image)
    return image


class The_time:
    def __init__(self, zone):
        if zone:
            self.pytime = pytz.timezone(zone)
            self.pydatetime = datetime.now(self.pytime)
        elif not zone:
            self.pydatetime = datetime.now()

    def day_time(self, local: str):
        timein = self.pydatetime.strftime(local)
        return timein


class Title_frame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text='World Time',
                  font='Calibri 24 bold').pack(pady=10)
        ttk.Label(self, text='Get the time from any country in the world',
                  font='Calibri 10 bold').pack()
        self.pack()


class Input_aframe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=250, height=80)
        self.pack_propagate(False)
        self.pack(padx=50)
        self.input_all()

    def input_all(self):
        global entry_str, input_entry, error_lable
        complete_zone = list(all_zone.keys())
        entry_str = tk.StringVar()
        # auto complete entry
        input_entry = AutocompleteEntry(
            self, textvariable=entry_str, completevalues=complete_zone, font='Calibri 10 bold')
        input_entry.bind('<Return>', lambda event: get_time())
        input_button = ttk.Button(self, text='Get Time', command=get_time)
        errorframe = ttk.Frame(self, width=30, height=19)
        error_lable = ttk.Label(
            errorframe, text='Type the correct timezone or country', font='Calibri 10 bold', foreground='red')
        errorframe.pack()
        input_entry.pack(padx=5, side='left')
        input_button.pack(padx=5, side='left')


class Local_time(ttk.Frame):
    def __init__(self, master, Ltext: str, Lfont: str, timef: str):
        super().__init__(master, width=540, height=40)
        self.pack_propagate(False)
        global output_local_time_str
        output_local_time_str = tk.StringVar()
        output_local_time_str.set(upd_localtime())
        localttx = ttk.Label(self, text=Ltext, font=Lfont)
        localtimetxt = ttk.Label(
            self, textvariable=output_local_time_str, font=timef)
        localttx.pack(side='top', fill='x')
        localtimetxt.pack(side='top', fill='x')
        self.pack(padx=7)


class Output_txtframe(ttk.Frame):
    def __init__(self, master, style: str, invstyle: str, fontstr: str, fonttxt: str, fg: str):
        super().__init__(master, bootstyle=style, width=450, height=46)
        self.pack_propagate(False)
        global output_txt, output_str
        output_txt = tk.StringVar()
        output_str = tk.StringVar()

        self.image = get_styleimg("GUI/outputtext.png", 450, 23)
        self.image2 = get_styleimg("GUI/outputtext2.png", 450, 23)

        ttk.Label(self, border='0', image=self.image, foreground=fg,
                  textvariable=output_txt, font=fontstr, compound='center').pack(expand=True, side='top')
        ttk.Label(self, border='0', image=self.image2, textvariable=output_str,
                  font=fonttxt, foreground=fg, compound='center').pack(expand=True, side='top')
        self.pack()


class Time_frame(ttk.Frame):
    def __init__(self, master, stylet: str, invtext: str, tfont: str):
        super().__init__(master, bootstyle=stylet, width=450, height=190)
        self.pack_propagate(False)
        global output_timestr
        self.image = get_styleimg("GUI/timezone.png", 450, 190)

        output_timestr = tk.StringVar()
        ttk.Label(self, border='0', image=self.image, textvariable=output_timestr,
                  font=tfont, compound='center', foreground='#126D90').pack(ipadx='5', side='top')
        self.pack()
        self.after(600, self.update_time_frame)
        # update time

    def update_time_frame(self):
        if backup_country == {}:
            # default time
            default_time()
        else:
            get_timeIn = The_time(backup_country[1])
            update_time_in = get_timeIn.day_time("%I:%M %p")
            output_timestr.set(update_time_in)
            output_local_time_str.set(upd_localtime())

        self.after(60000, self.update_time_frame)


App('World Time', (450, 437))
