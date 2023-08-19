import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip as tooltips
from ttkwidgets.autocomplete import AutocompleteEntry
from zonedict import allzone as ct
from datetime import datetime
from PIL import Image, ImageTk
import random
import pytz
import threading as thrd
from tkhtmlview import HTMLText, RenderHTML

# world time beta ver 0.8 by: luiscx99


class App(ttk.Window):
    # windows
    def __init__(self, title, size):
        super().__init__()
        ttk.Style('cerculean')
        self.title(title)
        global screen_math_w, screen_math_h
        scre_wdth, scre_hgth = self.winfo_screenwidth(), self.winfo_screenheight()
        screen_math_w, screen_math_h = scre_wdth / 2 - 250, scre_hgth / 2 - 290

        self.geometry(
            f'{size[0]}x{size[1]}+{int(screen_math_w)}+{int(screen_math_h)}')
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
            self, 'Calibri 11 bold', 'Calibri 15 bold')
        # time frame
        self.timeframe = Time_frame(
            self, 'Calibri 50 bold')
        # Setting app icon
        icon = get_styleimg('GUI/world_time_icon.ico', 256, 256)
        self.wm_iconphoto(False, icon)

        self.mainloop()


class Info_window(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        msize = [365, 450]
        self.geometry("%dx%d+%d+%d" %
                      (msize[0], msize[1], screen_math_w + 150, screen_math_h + 40))
        self.title("Info")
        self.maxsize(msize[0], msize[1])
        icon = get_styleimg('GUI/lightmode/infolight.png', 256, 256)
        self.wm_iconphoto(False, icon)

        # grid config
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # scrollbar frame
        scrollbar_frame = ScrollbarFrame(self)
        scrollbar_frame.grid(row=0, column=0, sticky='nsew')

        # heml frame
        html_frame = scrollbar_frame.scrolled_frame
        html_window = HTMLText(
            html_frame, html=RenderHTML('GUI/info.html'), width=57)
        html_window.grid()
        html_window.fit_height()

        # disable info button
        info_window_btn.config(state='disable')
        self.protocol("WM_DELETE_WINDOW", self.btn_state)

    def btn_state(self):
        self.destroy()
        info_window_btn.config(state='normal')

# scrollbar layout to the right


class ScrollbarFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        scrollbar = tk.Scrollbar(self, orient="vertical", width=12)
        scrollbar.pack(side="right", fill="y")

        # canvas
        self.canvas = tk.Canvas(self, borderwidth='0')
        self.canvas.pack(side="left", fill="both", expand=True)

        # bind the scrollbar to the self.canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.canvas.yview)

        # frame to be scrolled
        self.scrolled_frame = tk.Frame(self.canvas, borderwidth='0')
        self.canvas.create_window(
            (4, 4), window=self.scrolled_frame, anchor="nw")

        # configures the scrollregion
        self.scrolled_frame.bind("<Configure>", self.on_configure)
        self.scrolled_frame.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# import time zone dictionary
all_zone = ct.zone_dict()
TXT_T = 'This is the current time in:'
backup_country = {}

# convert user input to title case


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

# on start display a random country or time zone


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

# select light mode or dark mode


def change_theme():
    App.style = ttk.Style()
    current_theme = App.style.theme_use()
    global output_label1
    tips_txt = ['Select Light Mode', 'Select Dark Mode']
    fg = ['#ffffff', '#287CA9']
    if current_theme != 'darkly':
        current_theme = 'darkly'
        tool_tip.text = tips_txt[0]
        output_label1.config(foreground=fg[0])
        setup_theme(False)
    else:
        current_theme = 'cerculean'
        tool_tip.text = tips_txt[1]
        output_label1.config(foreground=fg[1])
        setup_theme(True)

    App.style.theme_use(current_theme)

# setup theme images


def setup_theme(val: bool):
    global setimg
    inv_image = {output_label1: ['GUI/darkmode/invertworldmap1.png', 450, 190, 'GUI/lightmode/worldmap1.png'],
                 output_lable2: ['GUI/darkmode/invertworldmap2.png', 450, 23, 'GUI/lightmode/worldmap2.png'],
                 output_label3: ['GUI/darkmode/invertworldmap3.png', 450, 23, 'GUI/lightmode/worldmap3.png'],
                 change_theme_btn: ['GUI/darkmode/themesdark.png', 18, 18, 'GUI/lightmode/themeslight.png'],
                 info_window_btn: ['GUI/darkmode/infodark.png', 18, 18, 'GUI/lightmode/infolight.png']}
    for invimgkey, invimgval in inv_image.items():
        setimgval = invimgval[3]
        if not val:
            setimgval = invimgval[0]
        setimg = get_styleimg(setimgval, invimgval[1], invimgval[2])
        invimgkey.config(image=setimg)
        invimgkey.imagerf = setimg

# get and return the time


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

# main top frame


class Title_frame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        global tool_tip, change_theme_btn, info_window_btn
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text='World Time',
                  font='Calibri 24 bold').grid(column=1, row=0)
        ttk.Label(self, text='Get the time from any country in the world',
                  font='Calibri 10 bold').grid(column=1, row=1)

        # images
        self.theme_image = get_styleimg(
            "GUI/lightmode/themeslight.png", 18, 18)
        self.info_image = get_styleimg("GUI/lightmode/infolight.png", 18, 18)

        # change theme button
        change_theme_btn = ttk.Button(
            self, image=self.theme_image, command=lambda: change_theme(), bootstyle='info_link', cursor='hand2')
        change_theme_btn.grid(column=0, row=0, padx=15)

        # about window button
        info_window_btn = ttk.Button(
            self, image=self.info_image, state='normal', command=lambda: Info_window(), bootstyle='info_link', cursor='hand2')
        info_window_btn.grid(column=2, row=0, padx=15)

        # tool tips
        tool_tip = tooltips(
            change_theme_btn, text="Select Dark Mode", bootstyle='info_inverse')
        tooltips(info_window_btn, text="App Info", bootstyle='info_inverse')

        self.pack(fill='x', pady=5)

# input frame to type the conutry or time zone


class Input_aframe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=250, height=80)
        self.pack_propagate(False)
        self.pack(padx=50)
        global entry_str, input_entry, error_lable
        complete_zone = list(all_zone.keys())
        entry_str = tk.StringVar()
        # auto complete entry
        input_entry = AutocompleteEntry(
            self, textvariable=entry_str, completevalues=complete_zone, font='Calibri 10 bold')
        input_entry.bind('<Return>', lambda event: get_time())
        input_button = ttk.Button(self, text='Get Time', command=get_time)
        # error frame
        errorframe = ttk.Frame(self, width=30, height=19)
        error_lable = ttk.Label(
            errorframe, text='Type the correct timezone or country', font='Calibri 10 bold', foreground='red')
        errorframe.pack()

        input_entry.pack(padx=5, side='left')
        input_button.pack(padx=5, side='left')

# local time middle frame
# display the current local time


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

# country text


class Output_txtframe(ttk.Frame):
    def __init__(self, master, fontstr: str, fonttxt: str):
        super().__init__(master, width=450, height=46)
        self.pack_propagate(False)
        global output_txt, output_str, output_label3, output_lable2
        output_txt = tk.StringVar()
        output_str = tk.StringVar()
        self.image = get_styleimg("GUI/lightmode/worldmap3.png", 450, 23)
        self.image2 = get_styleimg("GUI/lightmode/worldmap2.png", 450, 23)

        output_label3 = ttk.Label(self, border='0', image=self.image,
                                  textvariable=output_txt, font=fontstr, compound='center')
        output_label3.pack(expand=True, side='top')
        output_lable2 = ttk.Label(self, border='0', image=self.image2, textvariable=output_str,
                                  font=fonttxt, compound='center')
        output_lable2.pack(expand=True, side='top')
        self.pack()

# main time bottom frame


class Time_frame(ttk.Frame):
    def __init__(self, master, tfont: str):
        super().__init__(master, width=450, height=190)
        self.pack_propagate(False)
        global output_timestr, output_label1
        self.image = get_styleimg("GUI/lightmode/worldmap1.png", 450, 190)

        output_timestr = tk.StringVar()
        output_label1 = ttk.Label(self, border='0', image=self.image, textvariable=output_timestr,
                                  font=tfont,  compound='center', foreground='#287CA9')
        output_label1.pack(ipadx='5', side='top')
        self.pack()
        self.after(500, self.update_time_frame)
        # update time

    def update_time_frame(self):

        if backup_country == {}:
            # fix to prevent the app from hanged at startup
            thread1 = thrd.Thread(target=default_time)
            thread1.start()
        else:
            get_timeIn = The_time(backup_country[1])
            update_time_in = get_timeIn.day_time("%I:%M %p")
            output_timestr.set(update_time_in)
            output_local_time_str.set(upd_localtime())

        self.after(60000, self.update_time_frame)


App('World Time', (450, 427))
