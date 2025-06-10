#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import os
import sys
import re
import time
import math
from datetime import datetime
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import threading
from threading import Thread
from openpyexcel import load_workbook
from openpyexcel.styles import PatternFill
import pyvisa
import serial

sem = threading.Semaphore()

class MeasControlGUI():
    """class GUI"""
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.close_app)
        self.folder_1 = os.getcwd()
        self.ser = 0
        self.count = 1
        self.varcap = 0
        self.tdiv_2 = 0

        self.varlist_str = ['name_protokol','temp','humi','press','custom','pover','var_spb1','var_spb2']
        self.vardict_str = {self.var: tk.StringVar() for self.var in self.varlist_str}

        self.varlist_boo = ['dcv_var','acv_var','f_var','dci_var','aci_var','r2_var','r4_var','tr_var','per_var','c_var','gost']
        self.vardict_boo = {self.var: tk.BooleanVar() for self.var in self.varlist_boo}
        for self.var in self.varlist_boo[:10]:
            self.vardict_boo[self.var].set(1)

        self.ar10b = ('arial', 10, 'bold')
        self.ar12b = ('arial', 12, 'bold')
        self.colour_cell = PatternFill(start_color='FFFFDAB9', end_color='FFFFDAB9', fill_type='solid')

        self.img1 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\pan1.gif')
        self.img2 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\check.gif')
        self.img3 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\error.png')
        self.img4 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\refresh.png')
        self.img5 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\doc.png')
        self.img6 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\connect.png')

        with open(f'{self.folder_1}\\setting.json','r', encoding='utf-8') as file_json:
            self.sett_json = json.load(file_json)
        with open(f'{self.folder_1}\\theme.json','r', encoding='utf-8') as file_json:
            self.theme_json = json.load(file_json)
        with open(f'{self.folder_1}\\language.json','r', encoding='utf-8') as file_json:
            self.lang_json = json.load(file_json)

        self.lang = self.lang_json[self.sett_json['language']]
        self.theme = self.theme_json[self.sett_json['theme']]
        self.sign_pribor = self.sett_json['sign_pribor']

        self.bg_colour = self.theme['.']['bg_colour']
        self.fg_colour = self.theme['.']['fg_colour']
        self.bg_button = self.theme['.']['bg_button']

        self.style = ttk.Style()
        self.style.theme_create('theme', settings=self.theme)
        self.style.theme_use('theme')

        parent.title('MEASControl')
        parent.geometry('1000x495')
        parent.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        parent.resizable(width=False, height=False)

        main_menu = tk.Menu(self.parent)
        self.parent.config(menu=main_menu)
        fmenu = tk.Menu(main_menu, tearoff=False)
        fmenu.add_separator()
        fmenu.add_command(label=self.lang['fmenu_close'], command=self.close_app)

        fsetting = tk.Menu(main_menu, tearoff=False)
        fsetting.add_command(label=self.lang['fset_1'], command=self.setting_win)
        fsetting.add_command(label=self.lang['fset_2'], command=self.set_style_win)
        fsetting.add_command(label=self.lang['fset_3'], command=self.virt_dmm)

        main_menu.add_cascade(label=self.lang['add_cascade_1'], menu=fmenu)
        main_menu.add_cascade(label=self.lang['add_cascade_2'], command=self.protokol)
        main_menu.add_cascade(label=self.lang['add_cascade_3'], menu=fsetting)
        main_menu.add_cascade(label=self.lang['add_cascade_4'], command=self.about_win)

        tabframe = tk.Frame(self.parent)
        rightframe = tk.Frame(self.parent)
        statusframe = tk.Frame(self.parent)

        tabframe.grid(row=1, column=0, ipadx=185, ipady=210,sticky="nsew")
        rightframe.grid(row=1, column=1, sticky="ns")
        statusframe.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.sb = tk.Scrollbar(rightframe, orient='vertical')
        self.lb = tk.Listbox(rightframe, selectmode='extended', width=39, height=20, relief='ridge')
        self.sb['command'] = self.lb.yview
        self.lb['yscroll'] = self.sb.set
        self.sb.pack(side=tk.RIGHT, fill='y')
        self.lb.pack(side=tk.RIGHT, fill='y')

        tab_control = ttk.Notebook(tabframe)
        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text=self.lang['tab_control_1'])
        tab_control.add(self.tab2, text=self.lang['tab_control_2'])
        tab_control.pack(expand=1, fill='both')

        self.statusbar = tk.Label(statusframe, text=self.lang['statusbar_1'], background="gray80", anchor='w')
        self.statusbar.pack(side='left', fill='x', expand=True)
        self.statusbar_1 = tk.Label(statusframe, text="I T L ©", background="gray80", anchor='e')
        self.statusbar_1.pack(side='right', fill='x')

        self.tree = ttk.Treeview(self.tab1, columns=['1', '2', '3', '4'], height=5)
        self.tree.heading('#0', text="", anchor='center')
        self.tree.heading('1', text=self.lang['tree_head_1'], anchor='center')
        self.tree.heading('2', text=self.lang['tree_head_2'], anchor='center')
        self.tree.heading('3', text=self.lang['tree_head_3'], anchor='center')
        self.tree.heading('4', text=self.lang['tree_head_4'], anchor='center')
        self.tree.column('#0', stretch=False, anchor='center', minwidth=30, width=30)
        self.tree.column('1', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('2', stretch=False, anchor='center', minwidth=100, width=100)
        self.tree.column('3', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('4', stretch=False, anchor='center', minwidth=360, width=360)
        self.tree.place(x=5, y=290)

        self.tree2 = ttk.Treeview(self.tab2, columns=['1', '2', '3', '4'], height=11)
        self.tree2.heading('#0', text="", anchor='center')
        self.tree2.heading('1', text=self.lang['tree2_head_1'], anchor='center')
        self.tree2.heading('2', text=self.lang['tree2_head_2'], anchor='center')
        self.tree2.heading('3', text=self.lang['tree2_head_3'], anchor='center')
        self.tree2.heading('4', text=self.lang['tree2_head_4'], anchor='center')
        self.tree2.column('#0', stretch=False, anchor='center', minwidth=40, width=40)
        self.tree2.column('1', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree2.column('2', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree2.column('3', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree2.column('4', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree2.place(x=210, y=140)

        self.lbf1 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_1'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf1.place(x=5, y=5)
        self.lbf2 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_2'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf2.place(x=205, y=5)
        self.lbf3 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_3'], width=200, height=100, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        #self.lbf3.place(x=405, y=505)
        self.lbf33 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_33'], width=200, height=100, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        #self.lbf33.place(x=405, y=105)
        lbf4 = tk.LabelFrame(self.tab2, text=self.lang['LabelFrame_4'], width=200, height=390, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        lbf4.place(x=5, y=5)

        self.dmm_on = tk.Button(self.lbf1, image=self.img6, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_dmm)
        self.dmm_on.place(x=150, y=135)
        self.fluk_on = tk.Button(self.lbf2, image=self.img6, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_fluke_5500)
        self.fluk_on.place(x=150, y=135)
        self.dmm_on2 = tk.Button(self.lbf3, image=self.img6, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_dmm2)
        self.dmm_on2.place(x=150, y=35)
        self.power_on = tk.Button(self.lbf33, image=self.img6, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_power)
        self.power_on.place(x=150, y=35)
        self.fresh = tk.Button(self.tab1, image=self.img4, fg='#fff', bg=self.bg_button, font=self.ar12b, command=lambda: self.pribor(''))
        self.fresh.place(x=690, y=240)
        self.start_on = tk.Button(self.tab2, text=self.lang['Button_5'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.start)
        self.start_on.place(x=210, y=20)
        self.protocol_open = tk.Button(self.tab2, image=self.img5, state='disable', fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.prot_open)
        self.protocol_open.place(x=685, y=10)
        #self.paus_on = tk.Button(self.tab2, text=self.lang['Button_6'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b)
        #self.paus_on.place(x=350, y=20)

        self.combo_dmm = ttk.Combobox(self.lbf1, state='readonly', height=5, width=25)
        self.combo_dmm.place(x=15, y=10)
        self.combo_flu = ttk.Combobox(self.lbf2, state='readonly', height=5, width=25)
        self.combo_flu.place(x=15, y=10)
        self.combo_dmm2 = ttk.Combobox(self.lbf3, state='readonly', height=5, width=25)
        self.combo_dmm2.place(x=15, y=10)
        self.combo_power = ttk.Combobox(self.lbf33, state='readonly', height=5, width=25)
        self.combo_power.place(x=15, y=10)

        self.lab1 = tk.Label(self.lbf2, text=self.lang['Label_1'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab2 = tk.Label(self.lbf2, text=self.lang['Label_2'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab3 = tk.Label(lbf4, text=self.lang['Label_3'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab3.place(x=5,y=5)
        self.lab4 = tk.Label(lbf4, text=self.lang['Label_4'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab4.place(x=5,y=35)
        self.lab5 = tk.Label(lbf4, text=self.lang['Label_5'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab5.place(x=5,y=85)
        self.lab6 = tk.Label(lbf4, text=self.lang['Label_6'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab6.place(x=5,y=115)
        self.lab7 = tk.Label(lbf4, text=self.lang['Label_7'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab7.place(x=5,y=145)
        self.lab8 = tk.Label(lbf4, text=self.lang['Label_8'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab8.place(x=5,y=175)
        self.lab9 = tk.Label(lbf4, text=self.lang['Label_9'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab9.place(x=5,y=205)
        self.lab10 = tk.Label(self.tab1, text=self.lang['Label_10'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab10.place(x=20,y=230)

        self.entry1 = ttk.Entry(self.tab1, textvariable=self.vardict_str['name_protokol'], width=50, font=self.ar10b)
        self.entry1.place(x=170, y=230)
        self.entry2 = ttk.Entry(lbf4, textvariable=self.vardict_str['temp'], width=10, font=self.ar10b)
        self.entry2.place(x=120, y=85)
        self.entry3 = ttk.Entry(lbf4, textvariable=self.vardict_str['humi'], width=10, font=self.ar10b)
        self.entry3.place(x=120, y=115)
        self.entry4 = ttk.Entry(lbf4, textvariable=self.vardict_str['press'], width=10, font=self.ar10b)
        self.entry4.place(x=120, y=145)
        self.entry5 = ttk.Entry(lbf4, textvariable=self.vardict_str['custom'], width=10, font=self.ar10b)
        self.entry5.place(x=120, y=175)
        self.entry6 = ttk.Entry(lbf4, textvariable=self.vardict_str['pover'], width=10, font=self.ar10b)
        self.entry6.place(x=120, y=205)

        self.spinbox1 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb1'], from_=0, to=30, width=6)
        self.spinbox2 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb2'], from_=0, to=30, width=6)
        self.chkbtn_1 = tk.Checkbutton(self.lbf1, bg="#848a98", activebackground="#848a98", text="МИ 1202-86, ГОСТ 8.366-79", variable=self.vardict_boo['gost'], onvalue=1, offvalue=0, font=self.ar10b)

        self.lb2 = tk.Listbox(self.tab2, selectmode='extended', width=47, height=2, relief='ridge', fg='blue', font=("Arial", 15, 'bold'))
        self.lb2.place(x=210, y=70)

        self.progress1 = ttk.Progressbar(self.tab2, orient='horizontal', mode='determinate', length=730, value=0)
        self.progress1.place(x=5, y=395)

    def close_app(self):
        self.parent.quit()
        self.parent.destroy()
        sys.exit()

    def prot_open(self):
        os.system('start excel {}\\Protocol\\{}'.format(self.folder_1, self.vardict_str['name_protokol'].get()))

    def date_time(self):
        today = datetime.today()
        self.data_today = today.strftime('%Y-%m-%d,%H-%M-%S')

    def protokol(self):
        rep = filedialog.askopenfilenames(parent=self.parent, initialdir=f'{self.folder_1}\\Protocol\\', initialfile='',
                                          filetypes=[("xlsx", "*.xlsx"),("All files", "*")])
        try:
            os.startfile(rep[0])
        except IndexError:
            pass

    def win_one(self, name_win, size_win):
        self.top = tk.Toplevel(self.parent)
        self.top.title(name_win)
        self.top.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        self.top.resizable(0, 0)
        win_width = self.top.winfo_screenwidth()
        win_high = self.top.winfo_screenheight()
        win_width = win_width // 3
        win_high = win_high // 2
        win_width = win_width - 200
        win_high = win_high - 200
        self.top.geometry(size_win.format(win_width, win_high))

    def about_win(self):
        self.win_one(self.lang['add_cascade_4'], '700x450+{}+{}')
        text1 = ('MEASControl\rVersion: 1.12a\rDate: 2025-04-15\rAutor: g1enden (I T L)')
        text2 = ('Agilent/Keysight:\r34401A\r34410A\r34411A\r34420A\r34460A\r34461A\r34465A\r34470A\r\r\r\r\r\r')
        text3 = ('AKIP:\rV7-78/1\r\r\r\r\r\r\r\r\r\r\r\r\r')
        text4 = ('Lecroy:\rWJ312A\rWJ324A\rHDO8108A\r\r\r\r\r\r\r\r\r\r\r')
        text5 = ('Tektronix:\rTDS2002\rTDS2012B\rTDS2014(B,C)\rTDS2024(B,C)\rTPS2024\r\r\r\r\r\r\r\r\r')
        text6 = ('Agilent/Keysight:\rMSO-X3032T\rMSO-X3104(A,T)\rMSO-X3034A\rMSO-X3054A\rMSO-X4104A\rMSO-X4154A\rDSO-X4034A\rDSO-X92004A\rDSO6102A\rMSO6012A\rDSO7034B\rMSO7104B\rDSO9104A\rMSO9404A\r')
        text7 = ('Siglent:\rAKIP-4119/1\rAKIP-4131/1A\rAKIP-4131/2A\r\r\r\r\r\r\r\r\r\r\r')
        text8 = ('R&S:\rRTO1024\rRTO1044\r\r\r\r\r\r\r\r\r\r\r\r')
        text9 = ('Agilent/Keysight:\r33622A\r\r\r\r\r\r\r\r\r\r\r\r\r')

        top_1 = tk.Frame(self.top, height=70, relief="raise")
        top_1.pack(side='top', fill='x')
        top_2 = tk.Frame(self.top, height=30, relief="raise")
        top_2.pack(side='top', fill='x')
        top_3 = tk.Frame(self.top, height=30, relief="raise")
        top_3.pack(side='top', fill='x')
        bottom_1 = tk.Frame(self.top, height=40, relief="raise", bg='grey88')
        bottom_1.pack(side='bottom', fill='x')
        img_about = tk.Label(top_1, image=self.img1)
        img_about.place(x=10,y=10)
        autor = tk.Label(top_1, justify='left', text=text1, font=self.ar10b, foreground='deepskyblue4')
        autor.place(x=260,y=0)
        lbf5 = tk.LabelFrame(top_2, text='Мультиметры', width=200, height=300, font=self.ar10b, foreground='deepskyblue4')
        lbf5.grid(row=0, column=0)
        lbf6 = tk.LabelFrame(top_2, text='Осциллографы', width=500, height=300, font=self.ar10b, foreground='deepskyblue4')
        lbf6.grid(row=0, column=1)
        lbf7 = tk.LabelFrame(top_2, text='Генераторы', width=500, height=300, font=self.ar10b, foreground='deepskyblue4')
        lbf7.grid(row=0, column=2)
        support_2 = tk.Label(lbf5, text=text2, font=('arial', 10), foreground='deepskyblue4')
        support_2.grid(row=0, column=0)
        support_3 = tk.Label(lbf5, text=text3, font=('arial', 10), foreground='deepskyblue4')
        support_3.grid(row=0, column=1)
        support_4 = tk.Label(lbf6, text=text4, font=('arial', 10), foreground='deepskyblue4')
        support_4.grid(row=0, column=0)
        support_5 = tk.Label(lbf6, text=text5, font=('arial', 10), foreground='deepskyblue4')
        support_5.grid(row=0, column=1)
        support_6 = tk.Label(lbf6, text=text6, font=('arial', 10), foreground='deepskyblue4')
        support_6.grid(row=0, column=2)
        support_7 = tk.Label(lbf6, text=text7, font=('arial', 10), foreground='deepskyblue4')
        support_7.grid(row=0, column=3)
        support_8 = tk.Label(lbf6, text=text8, font=('arial', 10), foreground='deepskyblue4')
        support_8.grid(row=0, column=4)
        support_9 = tk.Label(lbf7, text=text9, font=('arial', 10), foreground='deepskyblue4')
        support_9.grid(row=0, column=1)

        _button = tk.Button(bottom_1, text=self.lang['Button_7'], width=10, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=250,y=2)

    def checkbut_widget(self, rng_i, ch_text, ch_var):
        for i in range(rng_i):
            tk.Checkbutton(self.top, text=ch_text[i], variable=ch_var[i], onvalue=1, offvalue=0).pack(anchor='w')

    def setting_win(self):
        self.win_one(self.lang['add_cascade_3'], '220x250+{}+{}')
        try:
            if self.a1[1] == '34420A':
                self.checkbut_widget(3, ["Заглушка","Постоянное напряжение","Сопротивление 4-провода"], [self.vardict_boo['acv_var'],self.vardict_boo['dcv_var'],self.vardict_boo['r4_var']])
            elif self.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78-1'):
                self.checkbut_widget(8, ["Постоянное напряжение","Переменное напряжение","Частота","Постоянный ток",
                "Переменный ток","Ёмкость","Сопротивление 2-провода","Сопротивление 4-провода"], [self.vardict_boo['dcv_var'],self.vardict_boo['acv_var'],
                self.vardict_boo['f_var'],self.vardict_boo['dci_var'],self.vardict_boo['aci_var'],self.vardict_boo['c_var'],self.vardict_boo['r2_var'],self.vardict_boo['r4_var']])
            elif self.a1[1] == 'WJ312A':
                self.checkbut_widget(3, ["Постоянное напряжение","Время нарастания","Период"], [self.vardict_boo['dcv_var'],self.vardict_boo['tr_var'],self.vardict_boo['per_var']])
            elif self.a1[1] in ('TDS2014B', 'TDS2014C', 'TDS2024C'):
                self.checkbut_widget(3, ["Постоянное напряжение","Временной интервал","Время нарастания"], [self.vardict_boo['dcv_var'],self.vardict_boo['per_var'],self.vardict_boo['tr_var']])
        except AttributeError:
            clab = tk.Label(self.top, text='Прибор не определён', font='arial 13', foreground='deepskyblue4')
            clab.pack(anchor='w')

        _button = tk.Button(self.top, text=self.lang['Button_7'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=40,y=210)

    def set_style_win(self):
        self.win_one(self.lang['fset_2'], '350x300+{}+{}')
        lab_style = tk.Label(self.top, text=self.lang['set_style_win_2'], font=self.ar10b)
        lab_style.place(x=20,y=15)
        combo_style = ttk.Combobox(self.top, state='readonly', values=['Dark', 'Light'], height=5, width=25)
        combo_style.current(0)
        combo_style.place(x=150, y=15)
        lab_lang = tk.Label(self.top, text=self.lang['set_style_win_3'], font=self.ar10b)
        lab_lang.place(x=20,y=45)
        combo_lang = ttk.Combobox(self.top, state='readonly', values=['Russia', 'English'], height=5, width=25)
        combo_lang.current(0)
        combo_lang.place(x=150, y=45)

        def set_ok():
            if combo_lang.get() == self.sett_json['language'] and combo_style.get() == self.sett_json['theme']:
                self.top.destroy()
            else:
                self.sett_json['language'] = combo_lang.get()
                self.sett_json['theme'] = combo_style.get()
                with open(f'{self.folder_1}\\setting.json', 'w', encoding='utf-8') as file_json:
                    json.dump(self.sett_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)
                self.parent.destroy()
                try:
                    self.inst_dmm.close()
                    self.inst_fluke.close()
                except AttributeError:
                    print (self.lang['set_style_win_4'])
                os.system(f'{self.folder_1}\\MEASControl.py')

        _button = tk.Button(self.top, text=self.lang['Button_7'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=set_ok)
        _button.place(x=120,y=250)

    def cnt(self):
        cnt_dict = {}
        cnt_dict0 = {'34401A':1, '34401A_gost':1, '34420A':1, '34410A':1, '34411A':1, '34460A':1, '34461A':1, '34465A':1, '34470A':1, 'V7-78-1':1, '33622A':2,
                    'WJ312A':2, 'WJ324A':4, 'TDS2002':2, 'TDS2012B':2, 'TDS2014':4, 'TDS2014C':4, 'TDS2014B':4, 'TDS2024':4, 'TDS2024B':4, 'TDS2024C':4, 'TPS2024':4, 'MSO-X3032T':2, 'MSO-X3034A':4, 
                    'MSO-X3054A':4, 'MSO-X3104T':4, 'MSO-X3104A':4, 'DSO-X4034A':4, 'MSO-X4104A':4, 'MSO-X4154A':4, 'DSO6102A':2, 'MSO6012A':2, 'DSO9104A':4, 'MSO9404A':4,
                    'DSO7034B':4, 'MSO7104B':4, 'AKIP-4119-1':4, 'AKIP-4131-1A':4, 'AKIP-4131-2A':4, 'HDO8108A':8, 'RTO1024':4, 'RTO1044':4, 'DSOX92004A':4}
        
        for item_0 in ['Call(', 'Call_oscill(', 'Call_DSO9000', 'Call_generator(']:
            for item_i in list(cnt_dict0.keys()):
                osc_item = sum(1 for line in open(f'{self.folder_1}\\file_py\\{item_i}.py', encoding='utf-8') if line.lstrip().startswith(item_0))
                if osc_item > 0:
                    cnt_dict[item_i] = osc_item * cnt_dict0[item_i]

        return cnt_dict

    def virt_dmm(self):
        self.pribor(f'{self.folder_1}\\virt_pribor.yaml@sim')

    def visa_search(self, param):
        #self.rm = pyvisa.ResourceManager(visa_library='C:/Program Files/IVI Foundation/VISA/Win64/agvisa/agbin/visa32.dll')
        self.rm = pyvisa.ResourceManager(param)
        self.rm_list = list(self.rm.list_resources())
        return self.rm_list

    def decay_cycle(self, rm):
        for j, _ in enumerate(self.sign_pribor):
            if re.search(list(self.sign_pribor.keys())[j], rm):
                rm = list(self.sign_pribor.values())[j]
        return rm

    def adres_cycle(self, combo_dmm, rm):
        for j, _ in enumerate(self.sign_pribor):
            if combo_dmm == list(self.sign_pribor.values())[j]:
                adres = list(filter(lambda rmt: list(self.sign_pribor.keys())[j] in rmt, rm))
                if len(adres) > 0:
                    return adres

        if combo_dmm[:4] in ('ASRL', 'USB0', 'TCPI'):
            return [combo_dmm]

    def pribor(self, par):
        self.lb.delete(0, 'end')
        self.lb.insert('end', self.lang['pribor_1'])
        self.lb.itemconfig('end', bg='light cyan')
        self.visa_search(par)
        decay_list = list(map(self.decay_cycle, self.rm_list))
        self.lb.insert('end', *decay_list)
        self.combo_dmm.configure(values=decay_list)
        self.combo_flu.configure(values=decay_list)
        self.combo_dmm2.configure(values=decay_list)
        self.combo_power.configure(values=decay_list)
        self.vardict_str['var_spb1'].set('10')
        self.vardict_str['var_spb2'].set('3')
        self.tree.delete(*self.tree.get_children())
        self.tree2.delete(*self.tree2.get_children())
        self.fluk_on.configure(command=self.connect_fluke_5500)
        self.lbf3.place(x=405, y=505)
        self.lbf33.place(x=405, y=505)
        self.lab1.place(x=40,y=255)
        self.lab2.place(x=15,y=285)
        self.spinbox1.place(x=133, y=255)
        self.spinbox2.place(x=133, y=285)
        self.chkbtn_1.place(x=0,y=240)

    def connect_dmm(self):
        try:
            self.date_time()
            self.inst_dmm = self.rm.open_resource(self.adres_cycle(self.combo_dmm.get(), self.rm_list)[0], timeout=1000, write_termination='\n', read_termination='\n')
            if self.combo_dmm.get()[:4] in ('ASRL', 'USB0'):
                self.inst_dmm.write('SYST:REM')
                time.sleep(1)
            self.data_1 = self.inst_dmm.query("*IDN?")
            self.a1 = self.data_1.split(',')
            self.a1[1] = self.a1[1].replace('/', '-').replace(' ', '')
            if self.a1[1] == '34401A':
                self.chkbtn_1.place(x=0,y=40)
            elif self.a1[1] in ('WJ312A', 'WJ324A', 'TDS2002', 'TDS2012B', 'TDS2014', 'TDS2014C', 'TDS2014B', 'TDS2024', 'TDS2024B', 'TDS2024C', 'TPS2024', 'MSO-X3032T',
                                'MSO-X3034A', 'DSO-X4034A', 'MSO-X3104T', 'MSO-X3054A', 'MSO-X3104A', 'MSO-X4104A', 'MSO-X4154A', 'DSO6102A', 'MSO6012A', 'DSO9104A',
                                'MSO9404A', 'DSO7034B', 'MSO7104B', 'AKIP-4119-1', 'AKIP-4131-1A', 'AKIP-4131-2A','HDO8108A', 'RTO'):
                self.fluk_on.configure(command=self.connect_fluke_9500)
                self.lab1.place(x=40,y=55)
                self.lab2.place(x=15,y=85)
                self.spinbox1.place(x=133, y=55)
                self.spinbox2.place(x=133, y=85)
            if self.a1[1] in ('DSO9104A', 'MSO9404A', 'DSOX92004A', '33622A'):
                self.lbf3.place(x=405, y=5)
                if self.a1[1] == 'DSOX92004A':
                    self.lab1.configure(text='Внутренний калибратор\nCal Out')
                    self.lab1.place(x=10,y=55)
                elif self.a1[1] == '33622A':
                    self.lbf33.place(x=405, y=105)
                    self.lbf2.configure(text='Частотомер')
                    self.fluk_on.configure(command=self.connect_counter)
            if self.a1[1] == 'RTO':
                self.a1[1] = self.a1[1]+self.data_1.split(',')[2].split('/')[0].split('.')[1].replace('00k','')
                self.a1[2] = self.a1[2].split('/')[1]

            self.a10 = f'{self.a1[1]} подключен'
            self.vardict_str['name_protokol'].set(f'{self.data_today},{self.a1[1]},{self.a1[2]}.xlsx')
            self.lab3['text'] = f'Тип: {self.a1[1]}'
            self.lab4['text'] = f'Зав.№: {self.a1[2]}'
            try:
                self.lb.insert('end', self.a10)
                self.tree.insert('', 'end', text='', image=self.img2, values=(self.a10.split(' ')[0], self.a1[1], self.a1[2], self.data_1))
            except AttributeError:
                self.lb.insert('end', self.data_1)
            self.lb.see('end')
            self.lb.itemconfig('end', bg='light cyan')
        except TypeError:
            self.lb.insert('end', 'Ошибка! Прибор не определён')
            self.lb.itemconfig('end', bg='salmon')

    def connect_dmm2(self):
        try:
            self.inst_dmm2 = self.rm.open_resource(self.adres_cycle(self.combo_dmm2.get(), self.rm_list)[0], timeout=1000)
            if self.combo_dmm2.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
                self.inst_dmm2.write('SYST:REM')
                time.sleep(1)

            self.data_3 = self.inst_dmm2.query("*IDN?")
            self.c1 = self.data_3.split(',')
            self.c10 = f'Мультиметр {self.c1[1]} подключен'
            try:
                self.lb.insert('end', self.c10)
                self.tree.insert('', 'end', text='', image=self.img2, values=(self.c10.split(' ')[0], self.c1[1], self.c1[2], self.data_3))
            except AttributeError:
                self.lb.insert('end', self.data_3)
            self.lb.see('end')
            self.lb.itemconfig('end', bg='light cyan')
        except TypeError:
            self.lb.insert('end', 'Ошибка! Мультиметр не определён')
            self.lb.itemconfig('end', bg='salmon')

    def connect_power(self):
        try:
            self.inst_power = self.rm.open_resource(self.adres_cycle(self.combo_power.get(), self.rm_list)[0], timeout=1000)
            if self.combo_power.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
                self.inst_power.write('SYST:REM')
                time.sleep(1)

            self.data_p = self.inst_power.query("*IDN?")
            self.cp = self.data_p.split(',')
            self.c10_p = f'{self.cp[1]} подключен'
            try:
                self.lb.insert('end', self.c10_p)
                self.tree.insert('', 'end', text='', image=self.img2, values=(self.c10_p.split(' ')[0], self.cp[1], self.cp[2], self.data_p))
            except AttributeError:
                self.lb.insert('end', self.data_p)
            self.lb.see('end')
            self.lb.itemconfig('end', bg='light cyan')
        except TypeError:
            self.lb.insert('end', 'Ошибка! Мультиметр не определён')
            self.lb.itemconfig('end', bg='salmon')

    def connect_fluke_set(self):
        self.b1 = self.data_2.split(',')
        self.b10 = f'Калибратор {self.b1[0]} {self.b1[1]} подключен'
        self.lb.insert('end', self.b10)
        self.lb.see('end')
        self.lb.itemconfig('end', bg='light cyan')
        self.tree.insert('', 'end', text='', image=self.img2, values=(self.b10.split(' ')[0], self.b1[1], self.b1[2], self.data_2))

    def connect_fluke_5500(self):
        try:
            self.inst_fluke = self.rm.open_resource(self.combo_flu.get(), baud_rate=9600, data_bits=8, write_termination='\r', read_termination='\r')
            time.sleep(1)
            self.inst_fluke.write('*IDN?')
            self.data_2 = self.inst_fluke.read()
            self.connect_fluke_set()
            if self.b1[1] == 'N4-56':
                self.calbr = self.sett_json['N4-56']
            elif self.b1[1] in ('5522A', '5500E'):
                self.calbr = self.sett_json['5522A']
        except:
            self.lb.insert('end', 'Ошибка! Калибратор не определён')
            self.lb.itemconfig('end', bg='salmon')

    def write(self, message):
        self.ser.write(f'{message}\r'.encode('UTF-8'))

    def read(self):
        return self.ser.readline().decode('ASCII')

    def query(self, message):
        self.write(message)
        return self.read()

    def connect_fluke_9500(self):
        self.ser = serial.Serial(port='COM{}'.format(self.combo_flu.get().split('::')[0][4:]), baudrate=115200, timeout=1)
        time.sleep(0.5)
        self.ser.readline().decode('UTF-8')
        self.query("++auto 1")
        self.query(f"++addr {self.spinbox1.get()}")
        self.data_2 = self.query("*IDN?")
        self.connect_fluke_set()
        try:
            if self.b1[0] == 'Fluke':
                self.query(f"ROUT:SIGN:PATH CH{self.spinbox2.get()}")
                self.active_head = self.query(f"ROUT:FITT? CH{self.spinbox2.get()}")
                self.lb.insert('end', self.active_head)
                self.lb.see('end')
        except:
            self.lb.insert('end', 'Формирователь не обнаружен')

    def connect_fluke_9500_(self): # протестировать в следующий раз
        self.inst_fluke_9500 = self.rm.open_resource(self.combo_flu.get(), baud_rate=115200, data_bits=8, timeout=1, write_termination='\r', read_termination='\n')
        time.sleep(2)
        self.inst_fluke_9500.write('++auto 1')
        self.inst_fluke_9500.write(f'++addr {self.spinbox1.get()}')
        self.data_2 = self.inst_fluke_9500.query('*IDN?')
        self.connect_fluke_set()
        try:
            if self.b1[0] == 'Fluke':
                self.inst_fluke_9500.write(f"ROUT:SIGN:PATH CH{self.spinbox2.get()}")
                self.active_head = self.inst_fluke_9500.query(f"ROUT:FITT? CH{self.spinbox2.get()}")
                self.lb.insert('end', self.active_head)
                self.lb.see('end')
        except:
            self.lb.insert('end', 'Формирователь не обнаружен')

    def connect_counter(self):
        try:
            self.inst_count = self.rm.open_resource(self.adres_cycle(self.combo_flu.get(), self.rm_list)[0], timeout=1000, write_termination='\n', read_termination='\n')
            if self.combo_flu.get()[:4] in ('ASRL', 'USB0'):
                self.inst_count.write('SYST:REM')
                time.sleep(1)
            self.data_4 = self.inst_count.query("*IDN?")
            self.c1 = self.data_4.split(',')
            self.c1[1] = self.c1[1].replace('/', '-').replace(' ', '')
            self.c11 = f'{self.c1[1]} подключен'
            try:
                self.lb.insert('end', self.c11)
                self.tree.insert('', 'end', text='', image=self.img2, values=(self.c11.split(' ')[0], self.c1[1], self.c1[2], self.data_4))
            except AttributeError:
                self.lb.insert('end', self.data_4)
                self.lb.see('end')
                self.lb.itemconfig('end', bg='light cyan')
        except TypeError:
            self.lb.insert('end', 'Ошибка! Прибор не определён')
            self.lb.itemconfig('end', bg='salmon')

    def entry_in_cell(self):
        for row in self.ws.rows:
            for cell in row:
                if cell.value == '_type':
                    cell.value = self.a1[1].split('_')[0]
                elif cell.value == '_numb':
                    cell.value = self.a1[2]
                elif cell.value == '_customer':
                    cell.value = self.vardict_str['custom'].get()
                elif cell.value == '_temp':
                    cell.value = self.vardict_str['temp'].get()
                elif cell.value == '_hum':
                    cell.value = self.vardict_str['humi'].get()
                elif cell.value == '_pres':
                    cell.value = self.vardict_str['press'].get()
                elif cell.value == '_pov':
                    cell.value = self.vardict_str['pover'].get()
                elif cell.value == '_date':
                    cell.value = self.data_today[:10]

    def start(self):
        try:
            self.start_time = datetime.today()
            if self.vardict_boo['gost'].get() == 1:
                self.a1[1] = '34401A_gost'
            self.progress1.configure(maximum=self.cnt()[self.a1[1]])
            self.lb.insert('end', f'Время начала: {self.data_today[11:]}')
            self.wb = load_workbook(f'{self.folder_1}\\shablon\\{self.a1[1]}.xlsx')
            self.ws = self.wb.active
            exec(open(f'{self.folder_1}\\file_py\\{self.a1[1]}.py', encoding='utf-8').read())
        except AttributeError:
            self.lb.insert('end', 'Ошибка! Приборы не определены')
            self.lb.itemconfig('end', bg='salmon')

# ====================================== Multimetrs ======================================
class Call(Thread):
    """class callibration multimeters"""
    def __init__(self, name, vfluke, confdmm, cell1, cell2, vary1, vary2, accur):
        Thread.__init__(self)
        self.name = name
        self.vfluke = vfluke
        self.confdmm = confdmm
        self.cell1 = cell1
        self.cell2 = cell2
        self.vary1 = vary1
        self.vary2 = vary2
        self.accur = accur
        self.set_fluk = None
        self.data_true = None
        self.data_err = None
        self.data_error = None
        self.start()

    def v7_78_agilent(self):
        my_gui.inst_dmm.write(self.confdmm)
        my_gui.inst_dmm.write(self.vary1)
        time.sleep(1)
        if self.confdmm.split(' ', 1)[0] == 'CONF:FRES':
            my_gui.inst_fluke.write(my_gui.calbr[self.name]+self.vfluke+my_gui.calbr['res4'])
        else:
            my_gui.inst_fluke.write(my_gui.calbr[self.name]+self.vfluke)
        time.sleep(1)
        my_gui.inst_fluke.write(my_gui.calbr['ON'])
        time.sleep(self.vary2)
        my_gui.inst_dmm.write('READ?')
        if self.vary1 == 'DET:BAND 3':
            time.sleep(10)
        else:
            time.sleep(4)
        data_0 = float(my_gui.inst_dmm.read())
        self.set_fluk = float(self.vfluke.split(' ')[0])
        self.data_true = data_0
        if self.vfluke.split(' ')[1] in ('mV', 'mV,', 'mA', 'mA,'):
            self.data_true = data_0 * 1E+3
        elif self.vfluke.split(' ')[1] in ('uA', 'uA,'):
            self.data_true = data_0 * 1E+6
        elif self.vfluke.split(' ')[1] in ('kOHM', 'kOHM;'):
            self.data_true = data_0 / 1E+3
        elif self.vfluke.split(' ')[1] in ('MOHM', 'MOHM;'):
            self.data_true = data_0 / 1E+6
        elif self.vfluke.split(' ')[1] in ('GOHM', 'GOHM;'):
            self.data_true = data_0 / 1E+9
        elif self.vfluke.split(' ')[1] == 'NF':
            self.data_true = (data_0 - my_gui.varcap) * 1E+9
        elif self.vfluke.split(' ')[1] == 'UF':
            self.data_true = (data_0 - my_gui.varcap) * 1E+6

        if self.name == 'fr':
            self.set_fluk = float(self.vfluke.split(' ')[2])
            if self.vfluke.split(' ')[3] == 'kHz':
                self.data_true = data_0 / 1E+3

        self.data_err = round(self.data_true - self.set_fluk, 6)

    def agilent_34420A(self):
        my_gui.inst_dmm.write(self.confdmm)
        my_gui.inst_dmm.write(self.vary1)
        my_gui.inst_dmm.write(self.vary2)
        time.sleep(1)
        if len(self.vfluke) > 0:
            if self.confdmm == 'CONF:FRES':
                my_gui.inst_fluke.write(my_gui.calbr[self.name]+self.vfluke+my_gui.calbr['res4'])
            else:
                my_gui.inst_fluke.write(my_gui.calbr[self.name] + self.vfluke)
            my_gui.inst_fluke.write(my_gui.calbr['ON'])
        time.sleep(5)
        my_gui.inst_dmm.write('READ?')
        time.sleep(2)
        data_0 = float(my_gui.inst_dmm.read())
        self.data_true = data_0
        if self.name == 'dcv':
            if self.vfluke.split(' ')[1] == 'mV':
                self.data_true = data_0 * 1E+3
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[0])) * 1E+3
            else:
                if self.accur.split(' ')[1] == 'u':
                    self.data_error = (self.data_true - float(self.vfluke.split(' ')[0])) * 1E+6
                elif self.accur.split(' ')[1] == 'm':
                    self.data_error = (self.data_true - float(self.vfluke.split(' ')[0])) * 1E+3
        elif self.name == 'r':
            if self.vfluke.split(' ')[1] == 'kOHM;':
                self.data_true = data_0 / 1E+3
            elif self.vfluke.split(' ')[1] == 'MOHM;':
                self.data_true = data_0 / 1E+6
            if self.accur in ('72 u', '620 u', '62 m', '620 m', '74 Ohm'):
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[0])) * 1E+6
            elif self.accur in ('6.2 m', '6.4 Ohm'):
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[0])) * 1E+3
        elif self.name in ('dcv0', 'r0'):
            if self.accur.split(' ')[1] == 'n':
                self.data_true = data_0 * 1E+3
            elif self.accur.split(' ')[1] == 'm':
                self.data_true = data_0 / 1E+3
            elif self.accur.split(' ')[1] == 'Ohm':
                self.data_true = data_0 / 1E+6
            self.data_error = self.data_true * 1E+6

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f'Режим измерения: {self.name.upper()}')
        my_gui.lb2.insert('end', 'Установлено: ' + self.vfluke)
        my_gui.lb2.see('end')

        if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78-1'):
            self.v7_78_agilent()
        elif my_gui.a1[1] == '34420A':
            self.agilent_34420A()

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cell1:
                    cell.value = self.data_true
                    tree2_img = my_gui.img2
                    if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78-1'):
                        if self.data_true > self.set_fluk+self.accur or self.data_true < self.set_fluk-self.accur:
                            cell.fill = my_gui.colour_cell
                            tree2_img = my_gui.img3

                if my_gui.a1[1] == '34420A':
                    if cell.value == self.cell2:
                        cell.value = self.data_error
                        if self.data_error > float(self.accur.split(' ')[0]) or self.data_error < -float(self.accur.split(' ')[0]):
                            cell.fill = my_gui.colour_cell
                            tree2_img = my_gui.img3

        my_gui.tree2.insert('', 0, text='', image=tree2_img, values=(self.vfluke,round(self.data_true,4),self.data_err,f'±{self.accur}'))
        my_gui.wb.save('{}\\Protocol\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.inst_fluke.write(my_gui.calbr['OFF'])
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()
# ====================================== Oscilloscop ======================================
class Param_osc(Thread):
    """Class setting parammetrs oscilloscopes"""
    def __init__(self, name, imp, rezfluke, tdiv, ffluke):
        Thread.__init__(self)
        self.name = name
        self.imp = imp
        self.rezfluke = rezfluke
        self.tdiv = tdiv
        self.ffluke = ffluke
        self.start()

    def chanel_select(self, ch, numb_ch, on, off):
        a = on.split('_')
        b = off.split('_')
        for i in range(1, numb_ch+1, 1):
            time.sleep(1)
            if i == int(ch):
                my_gui.inst_dmm.write(f'{a[0]}{i}{a[1]}')
            else:
                my_gui.inst_dmm.write(f'{b[0]}{i}{b[1]}')

    def default_agilent(self):
        if my_gui.a1[1] in ('DSO9104A', 'MSO9404A'):
            my_gui.inst_dmm.write(f':TRIG:EDGE1:SOUR CHAN{self.name}')
        else:
            my_gui.inst_dmm.write(f':TRIG:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f':MEAS:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f'CHAN{self.name}:COUP DC')
        my_gui.inst_dmm.write(f'CHAN{self.name}:PROB 1')
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)

    def agilent_band(self, fvolt, oscal):
        global data_band
        my_gui.query(f'VOLT {fvolt}')
        my_gui.inst_dmm.write(f'CHAN{self.name}:IMP FIFT')
        my_gui.inst_dmm.write(f'CHAN{self.name}:SCAL {oscal}')
        my_gui.query("OUTP:STAT ON")
        time.sleep(1)
        data_band = float(my_gui.inst_dmm.query(':MEAS:VRMS?'))
        my_gui.query("OUTP:STAT OFF")

    def param_msox3(self):
        self.chanel_select(self.name, 4, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        self.default_agilent()
        if self.rezfluke == 'SCOP:SHAP DC':
            my_gui.inst_dmm.write(f'CHAN{self.name}:OFFS 17.5')  # смещение сигнала
            my_gui.inst_dmm.write('TRIG:LEV 0')                  # уровень запуска
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.inst_dmm.write(f'CHAN{self.name}:SCAL 0.05')
            my_gui.inst_dmm.write(f'CHAN{self.name}:OFFS -0.1')
            #my_gui.inst_dmm.write('TRIG:LEV -0.2')
        elif self.rezfluke == 'SCOP:SHAP MARK':
            my_gui.query(self.ffluke)
        elif self.ffluke == 'band':
            self.agilent_band(0.12, 0.02)

    def param_dso6(self):
        if my_gui.a1[1] in ('DSO7034B', 'MSO7104B'):
            self.chanel_select(self.name, 4, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        else:
            self.chanel_select(self.name, 2, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        self.default_agilent()
        if self.rezfluke == 'SCOP:SHAP DC':
            my_gui.inst_dmm.write('TRIG:LEV 0')                  # уровень запуска
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 150E-12")
            my_gui.inst_dmm.write(f'CHAN{self.name}:IMP FIFT')
            my_gui.inst_dmm.write(f'CHAN{self.name}:SCAL 0.05')
            my_gui.inst_dmm.write(f'CHAN{self.name}:OFFS -0.1')
            my_gui.inst_dmm.write('TRIG:LEV -0.1')
        elif self.ffluke == 'band':
            self.agilent_band(1.2, 0.2)

    def param_dso9(self):
        self.chanel_select(self.name, 4, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        self.default_agilent()
        if self.rezfluke == 'SCOP:SHAP DC':
            my_gui.inst_dmm.write(f'CHAN{self.name}:INP {self.ffluke}')

    def param_dsox90000(self):
        self.chanel_select(self.name, 4, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        my_gui.inst_dmm.write(f':TRIG:EDGE1:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f':MEAS:SOUR CHAN{self.name}')

    def param_tds2(self):
        self.chanel_select(self.name, 4, 'SEL:CH_ ON', 'SEL:CH_ OFF')
        my_gui.inst_dmm.write(f'CH{self.name}:COUP DC')
        my_gui.inst_dmm.write(f'CH{self.name}:PRObe 1')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        if my_gui.a1[1] == 'TPS2024':
            my_gui.inst_dmm.write(f'CH{self.name}:POS -3')
        else:
            my_gui.inst_dmm.write(f'CH{self.name}:POS 0')  # смещение сигнала
        my_gui.inst_dmm.write('TRIG:MAI:LEV 0')        # уровень запуска
        if self.rezfluke == 'SCOP:SHAP MARK':
            my_gui.query(self.ffluke)
            my_gui.tdiv_2 = self.ffluke.split(' ')[1]
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.inst_dmm.write(f'CH{self.name}:POS 3')
            my_gui.tdiv_2 = self.tdiv.split(' ')[1]
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write('TRIG:MAI:MOD AUTO')
        my_gui.inst_dmm.write(f'TRIG:MAI:EDGE:SOU CH{self.name}')
        my_gui.inst_dmm.write(f'MEASU:MEAS1:SOU CH{self.name}')
        if my_gui.a1[1] in ('TDS2014C', 'TDS2024C'):
            my_gui.inst_dmm.write('MEASU:MEAS1:TYP PK2pk')
        else:
            my_gui.inst_dmm.write('MEASU:MEAS1:TYP MEAN')
        my_gui.inst_dmm.write(f'MEASU:MEAS2:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS2:TYP RMS')
        my_gui.inst_dmm.write(f'MEASU:MEAS3:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS3:TYP PERIod')
        my_gui.inst_dmm.write(f'MEASU:MEAS4:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS4:TYP RIS')

    def param_akip4131(self):
        self.chanel_select(self.name, 4, 'C_:TRA ON', 'C_:TRA OFF')
        my_gui.inst_dmm.write(f'C{self.name}:CPL D1M')
        my_gui.inst_dmm.write(f'TRSE EDGE,SR,C{self.name},HT,OFF')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        my_gui.inst_dmm.write(f'C{self.name}:OFST 0')       # смещение сигнала
        my_gui.inst_dmm.write(f'C{self.name}:TRig_LeVel 0') # уровень запуска
        if self.rezfluke == 'SCOP:SHAP DC':
            my_gui.inst_dmm.write(f'BWL C{self.name}, ON')  # ограниечение полосы
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.tdiv_2 = self.tdiv.split(' ')[1]
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write(f'PACU MEAN, C{self.name}')
        my_gui.inst_dmm.write(f'PACU RMS, C{self.name}')
        my_gui.inst_dmm.write(f'PACU RISE, C{self.name}')

    def param_wj312(self):
        self.chanel_select(self.name, int(my_gui.a1[1][4]), 'C_:TRA ON', 'C_:TRA OFF')
        my_gui.inst_dmm.write('TRMD AUTO')
        my_gui.inst_dmm.write(f'C{self.name}:CPL DC1M')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        my_gui.inst_dmm.write(self.ffluke)
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write(f'C{self.name}:OFST 0')
        my_gui.inst_dmm.write(f'TSRC CH{self.name}')
        my_gui.inst_dmm.write('TLVL 0')
        if self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.inst_dmm.write(f'C{self.name}:VDIV 200mv')
            my_gui.inst_dmm.write(f'C{self.name}:OFST 200mv')
            my_gui.inst_dmm.write('TLVL -200mv')
        elif self.rezfluke == 'SCOP:SHAP SIN':
            my_gui.query('FREQ:FIX 10E+06')

        my_gui.inst_dmm.write('MDSP ON')
        my_gui.inst_dmm.write('DIRM A')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},TOP')
        my_gui.inst_dmm.write('DIRM B')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},BASE')
        my_gui.inst_dmm.write('DIRM C')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},TR10-90')
        my_gui.inst_dmm.write('DIRM D')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},FREQ')
        time.sleep(1)

    def param_hdo8108(self):
        self.chanel_select(self.name, 8, 'C_:TRA ON', 'C_:TRA OFF')
        my_gui.inst_dmm.write('TRMD AUTO')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        my_gui.inst_dmm.write(self.ffluke)
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write(f'TRSE EDGE,SR,C{self.name},HT,OFF')
        if self.rezfluke == 'SCOP:SHAP DC':
            my_gui.inst_dmm.write(f'BWL C{self.name},20MHZ')
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 150E-12")
            my_gui.inst_dmm.write(f'C{self.name}:TRLV -50mv')
        elif self.rezfluke.split(';')[0] == 'SCOP:SHAP SQU':
            my_gui.query('PAR:SQU:POL SYMM')

    def param_rto(self):
        self.chanel_select(self.name, 4, 'CHAN_:STAT ON', 'CHAN_:STAT OFF')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        my_gui.inst_dmm.write(self.ffluke)
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write(f'TRIG1:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f'CHAN{self.name}:WAV1:TYPE HRES')
        my_gui.inst_dmm.write(f'CHAN{self.name}:WAV1:ARIT AVER')

        if self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            if my_gui.a1[1] == 'RTO1024':
                my_gui.query("PAR:EDGE:SPE 150E-12")
            elif my_gui.a1[1] == 'RTO1044':
                my_gui.query("PAR:EDGE:SPE 25E-12")
            my_gui.inst_dmm.write(f'CHAN{self.name}:POS 4')
            my_gui.inst_dmm.write(f'TRIG1:LEV{self.name} -0.15')

        my_gui.inst_dmm.write('MEAS1 ON')
        my_gui.inst_dmm.write(f'MEAS1:SOUR C{self.name}W1')
        my_gui.inst_dmm.write('MEAS1:MAIN MEAN')
        my_gui.inst_dmm.write('MEAS2 ON')
        my_gui.inst_dmm.write(f'MEAS2:SOUR C{self.name}W1')
        my_gui.inst_dmm.write('MEAS2:MAIN RTIM')

    def run(self):
        sem.acquire()
        if my_gui.a1[1] in ('WJ312A', 'WJ324A'):
            self.param_wj312()
        elif my_gui.a1[1] == 'HDO8108A':
            self.param_hdo8108()
        elif my_gui.a1[1] in ('DSO-X4034A', 'MSO-X4104A', 'MSO-X4154A', 'MSO-X3034A', 'MSO-X3054A','MSO-X3104A','MSO-X3104T', 'MSO-X3032T'):
            self.param_msox3()
        elif my_gui.a1[1] in ('DSO6102A', 'MSO6012A', 'DSO7034B', 'MSO7104B'):
            self.param_dso6()
        elif my_gui.a1[1] in ('DSO9104A', 'MSO9404A'):
            self.param_dso9()
        elif my_gui.a1[1] == 'DSOX92004A':
            self.param_dsox90000()
        elif my_gui.a1[1] in ('TDS2002', 'TDS2012B', 'TDS2014', 'TDS2014C', 'TDS2014B', 'TDS2024', 'TDS2024B', 'TDS2024C', 'TPS2024'):
            self.param_tds2()
        elif my_gui.a1[1] in ('AKIP-4119-1', 'AKIP-4131-1A', 'AKIP-4131-2A'):
            self.param_akip4131()
        elif my_gui.a1[1] in ('RTO1024', 'RTO1044'):
            self.param_rto()
        sem.release()
# ========================================================================================
class Call_oscill(Thread):
    """Class callibration oscilloscopes"""
    def __init__(self, vfluk, vosc1, vosc2, cel1, cel2, accur):
        Thread.__init__(self)
        self.vfluk = vfluk
        self.vosc1 = vosc1
        self.vosc2 = vosc2
        self.cel1 = cel1
        self.cel2 = cel2
        self.accur = accur
        self.start()

    '''def excel_colour(self, func):
        global cell
        for row in my_gui.ws.rows:
            for cell in row:
                def colour_cell():
                    cell.fill = my_gui.colour_cell
                    self.tree2_img = my_gui.img3
                
                def colour_cell_accur():
                    if self.data_error > self.accur or self.data_error < -self.accur:
                        colour_cell()
                
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    func()
                    
                if cell.value == self.cel2:
                    cell.value = self.data_error
                    colour_cell_accur()'''

    def call_wj312(self):
        time.sleep(1)
        my_gui.inst_dmm.write('ACQ AVERAGE; AVGCNT 4')
        time.sleep(2)
        self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.vosc2 == 'MSRC?':
            self.data_true = self.data_true * 1E+9
        if self.vosc2 in ('MSRC?', 'MSRD?'):
            self.data_error = self.data_true
        else:
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1]))*1000

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                if cell.value == self.cel2:
                    cell.value = self.data_error
                    if self.data_error > self.accur or self.data_error < -self.accur:
                        cell.fill = my_gui.colour_cell
                        self.tree2_img = my_gui.img3

        my_gui.inst_dmm.write('ACQ NORMAL')

    def call_tds2(self):
        time.sleep(1)
        my_gui.inst_dmm.write('ACQ:MOD AVE; NUMAV 16')
        time.sleep(3)
        #if my_gui.a1[1] == 'TDS2014':
        #    self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(' ')[1]) # :MEASUREMENT:MEAS1:VALUE 9.9E37 TDS2014?
        #else:
        self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.vosc2 in ('MEASU:MEAS1:VAL?'):
            if my_gui.a1[1] == 'TPS2024':
                self.data_error = (self.data_true - float(self.vfluk.split(' ')[1])) * 1000
            else:
                self.data_error = ((self.data_true - float(self.vfluk.split(' ')[1])) / float(self.vfluk.split(' ')[1])) * 100
        elif self.vosc2 == 'MEASU:MEAS3:VAL?':
            self.data_true = self.data_true * float(f'1E+{my_gui.tdiv_2[-1:]}')
            self.data_error = self.data_true - float(my_gui.tdiv_2.split('E')[0])
        elif self.vosc2 == 'MEASU:MEAS4:VAL?':
            self.data_true = self.data_true * 1E+9
            self.data_error = self.data_true
        elif self.vosc2 == 'MEASU:MEAS2:VAL?':
            self.data_true = self.data_true * 1E+3
            self.data_error = (float(self.vfluk.split(' ')[1]) / (2 * math.sqrt(2))) * 1E+3

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2  == 'MEASU:MEAS4:VAL?':
                        if self.data_true > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    elif self.vosc2 == 'MEASU:MEAS3:VAL?':
                        if self.data_error > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                if cell.value == self.cel2:
                    cell.value = self.data_error
                    if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

        '''@self.excel_colour
        def excel_tds(self):
            if self.vosc2  == 'MEASU:MEAS4:VAL?':
                if self.data_true > self.accur:
                    cell.fill = my_gui.colour_cell
                    self.tree2_img = my_gui.img3
            elif self.vosc2 == 'MEASU:MEAS3:VAL?':
                if self.data_error > self.accur:
                    cell.fill = my_gui.colour_cell
                    self.tree2_img = my_gui.img3'''

        my_gui.inst_dmm.write('ACQ:MOD SAM')

    def call_msox_3(self):
        time.sleep(1)
        my_gui.inst_dmm.write(':ACQ:TYPE AVER; :ACQ:COUN 64')
        time.sleep(2)
        if my_gui.a1[1] == 'MSO-X3104A':
            my_gui.inst_dmm.write(self.cel2) # offset for view signal
            time.sleep(1)
        if self.vosc2 == ':MARK:Y1P?':
            my_gui.inst_dmm.write(':MARK:MODE WAV') # курсоры-слежение
            time.sleep(1)
        self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.vosc2 in (':MEAS:VAV?', ':MARK:Y1P?'):
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1]))
            if abs(float(self.vfluk.split(' ')[1])) < 1:
                self.data_error = self.data_true - float(self.vfluk.split(' ')[1])
                self.data_true = self.data_true * 1000
        elif self.vosc2 == ':MEAS:RIS?':
            self.data_true_1 = self.data_true / 1E-9
            self.data_true = (0.35 / self.data_true) * 1E-6
            self.data_error = self.data_true
        elif self.vosc2 == ':MEAS:VRMS?':
            self.data_band2 = float(my_gui.inst_dmm.query(self.vosc2))
            self.data_true = round(20 * math.log(data_band / self.data_band2, 10), 2)
            self.data_error = self.data_true
        elif self.vosc2 == ':MEAS:VPP?':
            self.data_true = self.data_true * 1E+3
            self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2 in (':MEAS:RIS?', ':MEAS:VPP?'):
                        if self.data_true < self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    else:
                        if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

                if self.vosc2 == ':MEAS:RIS?':
                    if cell.value == self.cel2:
                        cell.value = self.data_true_1

        my_gui.inst_dmm.write(':ACQ:TYPE NORM')

    def call_dso_6(self):
        time.sleep(1)
        my_gui.inst_dmm.write(':ACQ:TYPE AVER; :ACQ:COUN 64')
        time.sleep(3)
        if self.vosc2 in (':MEAS:VAV?'):
            my_gui.inst_dmm.write('CHAN{}:OFFS {}'.format(self.vosc1[4], float(self.vfluk.split(' ')[1]) / 2))  # смещение сигнала для периодической поверки
            time.sleep(1)
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1])) * 1000
            self.data_true = self.data_true * 1000

        if self.cel1.split('_')[0][:4] == 'vofs':
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS {self.vosc2}')
            self.data_true = float(my_gui.inst_dmm.query('MEAS:VMAX?'))
            self.data_error = (float(self.vosc2) - self.data_true) * 1000
            self.data_true = self.data_true * 1000
            time.sleep(1)

        elif self.vosc2 in (':MEAS:RIS?'):
            if my_gui.a1[1] in ('DSO7034B', 'MSO6012A'):
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2)) * 1E+9
            else:
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2)) * 1E+12
            self.data_error = self.data_true

        elif self.vosc2 in (':MEAS:VRMS?'):
            self.data_band2 = float(my_gui.inst_dmm.query(self.vosc2))
            if my_gui.a1[1] == 'MSO6012A':
                self.data_true = 20 * math.log(self.data_band2 / (0.001 * 50)**0.5, 10) # Vrms to dBm
            else:
                self.data_true = 20 * math.log(data_band / self.data_band2, 10) # dB
            self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2 in (':MEAS:RIS?', ':MEAN:VRMS?'):
                        if self.data_true > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    if self.vosc2 == ':MEAS:VAV?':
                        if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                if cell.value == self.cel2:
                    cell.value = self.data_error
                    if self.data_error > self.accur or self.data_error < -self.accur:
                        cell.fill = my_gui.colour_cell
                        self.tree2_img = my_gui.img3

        my_gui.inst_dmm.write(':ACQ:TYPE NORM')

    def call_akip4131(self):
        time.sleep(1)
        my_gui.inst_dmm.write('ACQW AVERAGE,16')
        time.sleep(2)

        if self.cel1[0:4] == 'odcv' or self.vosc2.split(' ')[-1] == 'RISE':
            my_gui.inst_dmm.write('{}:OFST {}V'.format(self.vosc1.split(':')[0], self.cel2))
            time.sleep(2)

        if self.vosc2.split(' ')[-1] == 'MEAN':
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1]))
            if float(self.vosc1.split(' ')[1]) < 1 and self.cel1[0:3] == 'dcv': # mV
                self.data_error = (self.data_true - float(self.vfluk.split(' ')[1])) * 1000
                self.data_true = self.data_true * 1000

        if self.vosc2.split(' ')[-1] == 'RISE':
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('S')[0]) * 1E+9
            self.data_error = self.data_true

        if self.vosc2.split(' ')[-1] == 'RMS':
            my_gui.inst_dmm.write('ACQW SAMPLING')
            my_gui.inst_dmm.write('TDIV 10US')
            my_gui.query(self.cel2)
            time.sleep(1)
            self.data_true50 = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
            my_gui.inst_dmm.write('TDIV 5NS')
            if my_gui.a1[1] == 'AKIP-4119-1':
                start_bw = 66
            else:
                start_bw = 98
            for k in range(start_bw, 130): # increasing the freq to a 0.708 level
                my_gui.query(f'FREQ:FIX {k}E+06')
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
                if self.data_true < (self.data_true50 * 0.708):
                    break

            self.data_true = k
            self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2.split(' ')[-1] == 'MEAN':
                        if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    if self.vosc2.split(' ')[-1] == 'RISE':
                        if self.data_true > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    elif self.vosc2.split(' ')[-1] == 'RMS':
                        if self.data_true < self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

        my_gui.inst_dmm.write('ACQW SAMPLING')

    def call_hdo8108(self):
        time.sleep(2)
        if self.cel1[0:4] == 'odcv' or self.vosc2.split(' ')[-1] == 'RISE':
            my_gui.inst_dmm.write('{}:OFST {}v'.format(self.vosc1.split(':')[0], self.cel2))
            time.sleep(2)

        if self.vosc2.split(' ')[-1] == 'MEAN':
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1]))

        if self.vosc2.split(' ')[-1] == 'RISE':
            my_gui.inst_dmm.write('PARM CUST,STAT') #для усреднения
            my_gui.inst_dmm.write(f'PACU 1,RISE,{self.vosc2[0:2]}')
            self.data_true = float(my_gui.inst_dmm.query('PAST? CUST,AVG').split(',')[2].split('S')[0]) * 1E+12
            self.data_true = math.sqrt(self.data_true**2 - 140**2)
            self.data_error = self.data_true

        if self.vosc2.split(' ')[-1] == 'PKPK':
            my_gui.inst_dmm.write('TDIV 100US')
            my_gui.query(self.cel2)
            time.sleep(1)
            self.data_true50 = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
            my_gui.inst_dmm.write('TDIV 10NS')
            for k in range(1070, 1250, 10): # increasing the freq to a 0.708 level
                my_gui.query(f'FREQ:FIX {k}E+06')
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
                if self.data_true < (self.data_true50 * 0.708):
                    break
            self.data_true = k
            self.data_error = self.data_true

        if self.vosc2.split(' ')[-1] == 'PERIOD':
            time.sleep(1)
            my_gui.inst_dmm.write('PARM CUST,STAT')
            my_gui.inst_dmm.write(f'PACU 1,PER,{self.vosc2[0:2]}')
            self.data_true = float(my_gui.inst_dmm.query('PAST? CUST,AVG').split(',')[2].split('S')[0])
            self.data_error = self.data_true - (1 / float(self.cel2))
            self.data_true = self.data_true * 10**(int(self.cel2.split('+')[1]))

        if self.vosc2 == 'READ?':
            while True:
                self.data_true = my_gui.query(self.vosc2)
                if self.data_true != '':
                    break
            if self.vfluk.split(' ')[1] == '1E+06':
                self.data_true = float(self.data_true) / 1E+6
                self.data_error = (self.data_true - 1) * 1E+6
            else:
                self.data_true = float(self.data_true)
                self.data_error = self.data_true - 50

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2.split(' ')[-1] == 'MEAN' or self.vosc2 == 'READ?':
                        if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    if self.vosc2.split(' ')[-1] == 'RISE':
                        if self.data_true > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    if self.vosc2.split(' ')[-1] == 'PKPK':
                        if self.data_true < self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    if self.vosc2.split(' ')[-1] == 'PERIOD':
                        if self.data_error > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

    def call_rto(self):
        time.sleep(1)
        if self.cel1[0:4] == 'odcv':
            my_gui.inst_dmm.write('{}:OFFS {}'.format(self.vosc1.split(':')[0], self.vfluk.split(' ')[1]))
            time.sleep(2)

        my_gui.inst_dmm.write('ACQ:COUN 1000')
        time.sleep(2)
        self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.cel1[0:3] == 'dcv':
            self.data_error = ((self.data_true - float(self.vfluk.split(' ')[1])) / float(self.vfluk.split(' ')[1])) * 100
            self.data_true = self.data_true * 1000
        if self.cel1[0:4] == 'odcv':
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1])) * 1000
        if self.cel1[0:2] == 'tr':
            self.data_true = self.data_true * 1E+12
            self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.cel1[0:4] == 'odcv' or self.cel1[0:2] == 'tr':
                        if self.data_error > self.accur or self.data_error < -self.accur:
                                cell.fill = my_gui.colour_cell
                                self.tree2_img = my_gui.img3

        my_gui.inst_dmm.write('ACQ:COUN 1')

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', 'Канал №{}'.format(self.vosc1.split(':')[0][-1]))
        my_gui.lb2.insert('end', f'Установлено: {self.vfluk}')
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2
        my_gui.query(self.vfluk)
        my_gui.inst_dmm.write(self.vosc1)
        my_gui.query("OUTP:STAT ON")

        if my_gui.a1[1] in ('WJ312A', 'WJ324A'):
            self.call_wj312()
        elif my_gui.a1[1] == 'HDO8108A':
            self.call_hdo8108()
        elif my_gui.a1[1] in ('TDS2002', 'TDS2012B', 'TDS2014', 'TDS2014C', 'TDS2014B', 'TDS2024', 'TDS2024B', 'TDS2024C', 'TPS2024'):
            self.call_tds2()
        elif my_gui.a1[1] in ('DSO-X4034A', 'MSO-X4104A', 'MSO-X4154A', 'MSO-X3034A', 'MSO-X3054A','MSO-X3104A','MSO-X3104T', 'MSO-X3032T'):
            self.call_msox_3()
        elif my_gui.a1[1] in ('DSO6102A', 'MSO6012A', 'DSO7034B', 'MSO7104B'):
            self.call_dso_6()
        elif my_gui.a1[1] in ('AKIP-4119-1', 'AKIP-4131-1A', 'AKIP-4131-2A'):
            self.call_akip4131()
        elif my_gui.a1[1] in ('RTO1024', 'RTO1044'):
            self.call_rto()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.vfluk.split(' ')[1],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save('{}\\Protocol\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()

class Call_DSO9000(Thread):
    """Class callibration oscilloscope DSO9104, MSO9404A, DSOX92004A"""
    def __init__(self, vfluk, vosc1, vosc2, vdmm, cel1, cel2, cel3, cel4, accur):
        Thread.__init__(self)
        self.vfluk = vfluk
        self.vosc1 = vosc1
        self.vosc2 = vosc2
        self.vdmm = vdmm
        self.cel1 = cel1
        self.cel2 = cel2
        self.cel3 = cel3
        self.cel4 = cel4
        self.accur = accur
        self.data_true_dmm = None
        self.data_true_dmm0 = None
        self.data_true0 = None
        self.start()

    def meas_aver(self):
        my_gui.inst_dmm2.write(self.vdmm)
        time.sleep(1)
        my_gui.inst_dmm2.write('MEAS:VOLT:DC?')
        self.data_true_dmm = float(my_gui.inst_dmm2.read()) * 1000
        self.data_true = float(my_gui.inst_dmm.query(':MEAS:VAV?')) * 1000

    def call_dso_9(self):
        time.sleep(1)
        my_gui.inst_dmm.write(':ACQ:AVER ON; :ACQ:COUN 64')
        time.sleep(2)
        if self.vosc2 == ':MEAS:VAV?':
            self.meas_aver()

        if self.cel1[0:4] == 'vofs':
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS {self.vosc2}')
            self.meas_aver()
            time.sleep(1)
            my_gui.inst_dmm.write(':ACQ:AVER OFF') # измерения с 0 смещением и выкл выходом
            time.sleep(1)
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS 0')
            if my_gui.a1[1] == 'DSOX92004A':
                my_gui.inst_dmm.write(':CAL:OUTP DC,0')
            else:
                my_gui.query('OUTP:STAT OFF')
            time.sleep(1)
            my_gui.inst_dmm.write(':ACQ:AVER ON; :ACQ:COUN 64')
            time.sleep(2)
            my_gui.inst_dmm2.write('MEAS:VOLT:DC?')
            self.data_true_dmm0 = float(my_gui.inst_dmm2.read()) * 1000
            self.data_true0 = float(my_gui.inst_dmm.query(':MEAS:VAV?')) * 1000

        if self.cel2[0:3] == 'nul':
            self.data_true = float(my_gui.inst_dmm.query(':MEAS:VAV?')) * 1000

        if self.vosc2[:11] == (':MEAS:VRMS?'):
            self.data_true_dmm = (float(self.vfluk.split(' ')[1])* 1000) / (2* math.sqrt(2))
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2)) * 1000

        self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true_dmm
                if cell.value == self.cel2:
                    cell.value = self.data_true
                if cell.value == self.cel3:
                    cell.value = self.data_true_dmm0
                if cell.value == self.cel4:
                    cell.value = self.data_true0

        my_gui.inst_dmm.write(':ACQ:AVER OFF')

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', 'Канал №{}'.format(self.vosc1.split(':')[0][-1]))
        my_gui.lb2.insert('end', f'Установлено: {self.vfluk}')
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2
        if my_gui.a1[1] == 'DSOX92004A':
            my_gui.inst_dmm.write(self.vfluk) # выход Cal out
        else:
            my_gui.query(self.vfluk)
            if self.vosc2 == ':MEAS:VAV?' or self.cel1[0:4] == 'vofs' or self.vosc2[:11] == (':MEAS:VRMS?'):
                my_gui.query("OUTP:STAT ON")
        my_gui.inst_dmm.write(self.vosc1)

        if my_gui.a1[1] in ('DSO9104A', 'MSO9404A', 'DSOX92004A'):
            self.call_dso_9()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.vfluk.split(' ')[1],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save('{}\\Protocol\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        if my_gui.a1[1] == 'DSOX92004A':
            my_gui.inst_dmm.write(':CAL:OUTP DC,0')
        else:
            my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()

class Call_generator(Thread):
    """Class callibration generators"""
    def __init__(self, form, load, cel, accur):
        Thread.__init__(self)
        self.form = form
        self.load = load
        self.cel = cel
        self.accur = accur
        self.start()

    def call_33622a(self):
        my_gui.inst_dmm.write('OUTP{}:LOAD {}'.format(self.form.split(':')[0][-1], self.load))
        my_gui.inst_dmm.write(self.form)
        my_gui.inst_dmm.write('OUTP{} ON'.format(self.form.split(':')[0][-1]))
        time.sleep(2)
        if self.cel[0] == 'f':
            my_gui.inst_count.write(':MEAS:FREQ?')
            time.sleep(3)
            self.data_true = float(my_gui.inst_count.read())
            self.data_error = self.data_true - float(self.form.split(',')[0].split(' ')[-1])
        elif self.cel[:3] == 'vac':
            my_gui.inst_dmm2.write('MEAS:VOLT:AC?')
            time.sleep(1)
            self.data_true = float(my_gui.inst_dmm2.read())
            self.data_error = self.data_true - float(self.form.split(',')[1].split(' ')[0])
            if self.cel[:7] == 'vac_dbm':
                self.data_true = 10* math.log(20*self.data_true**2, 10)
                self.data_error = self.data_true
        elif self.cel[:3] == 'vdc':
            my_gui.inst_dmm2.write('MEAS:VOLT:DC?')
            time.sleep(1)
            self.data_true = float(my_gui.inst_dmm2.read())
            self.data_error = self.data_true - float(self.form.split(',')[2].split(' ')[0])
        elif self.cel[:3] == 'dbm':
            self.data_true = float(my_gui.inst_power.query('MEAS1:POW:AC?'))
            self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel:
                    cell.value = self.data_true
                    if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', 'Канал №{}'.format(self.form.split(':')[0][-1]))
        my_gui.lb2.insert('end', 'Установлено: {}'.format(self.form.split(',')[-2]))
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2

        if my_gui.a1[1] == '33622A':
            self.call_33622a()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.form.split(',')[-2],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save('{}\\Protocol\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()
# ===============================================================================
class Supportfunc(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.start()

    def message(self):
        messagebox.showinfo('ВНИМАНИЕ!', self.name.split('-')[1])

    def reset_common(self):
        my_gui.inst_dmm.write('*RST')
        my_gui.inst_dmm.write('*CLS')

    def resetdmm(self):
        self.reset_common()
        my_gui.inst_fluke.write('*RST')
        my_gui.inst_fluke.write('*CLS')
        if my_gui.b1[1] == 'N4-56':
            my_gui.inst_fluke.write('RES:MODE:HD ON')

    def resetoscil(self):
        self.reset_common()
        my_gui.query('*RST')
        my_gui.query('*CLS')
        if my_gui.a1[1][:3] == 'TDS':
            my_gui.inst_dmm.write('ACQuire:STATE RUN')
        time.sleep(5)
    
    def reset_gener(self):
        self.reset_common()
        my_gui.inst_power.write('*RST')
        my_gui.inst_power.write('*CLS')

    def capacitorcomp(self):
        my_gui.inst_dmm.write('CONF:CAP')
        time.sleep(5)
        my_gui.inst_dmm.write('READ?')
        time.sleep(5)
        my_gui.varcap = float(my_gui.inst_dmm.read())
        time.sleep(1)
        my_gui.progress1.step(1)

    def return_support(self):
        if self.name.split('-')[0] == 'message':
            self.message()
        elif self.name.split('-')[0] == 'reset_common':
            self.reset_common()
        elif self.name.split('-')[0] == 'resetdmm':
            self.resetdmm()
        elif self.name.split('-')[0] == 'resetoscil':
            self.resetoscil()
        elif self.name.split('-')[0] == 'reset_gener':
            self.reset_gener()
        elif self.name.split('-')[0] == 'capacitorcomp':
            self.capacitorcomp()

    def run(self):
        sem.acquire()
        time.sleep(2)
        self.return_support()
        time.sleep(2)
        sem.release()
# ============================================================================
class Clear_merge(Thread):
    """Class clear merge and row in excel"""
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def merged_cells(self):
        for merged_cells in my_gui.ws.merged_cells.ranges:
            style = my_gui.ws.cell(merged_cells.min_row, merged_cells.min_col)._style
            for col in range(merged_cells.min_col, merged_cells.max_col + 1):
                for row in range(merged_cells.min_row, merged_cells.max_row + 1):
                    my_gui.ws.cell(row, col)._style = style

    def clear_rows(self):
        for i in range (1, my_gui.ws.max_row + 1):
            for j in range(1, my_gui.ws.max_column + 1):
                if str(my_gui.ws.cell(i, j).value).find('_') != -1:
                    my_gui.ws.cell(i, j).value = '-'

    def run(self):
        sem.acquire()
        my_gui.protocol_open.configure(state='normal')
        my_gui.entry_in_cell()
        my_gui.date_time()
        stop_time = datetime.today()
        self.clear_rows()
        time.sleep(1)
        self.merged_cells()
        time.sleep(1)
        my_gui.wb.save('{}\\Protocol\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.lb.insert('end', f'Время окончания: {my_gui.data_today[11:]}')
        my_gui.lb.insert('end', f'Время поверки: {stop_time - my_gui.start_time}')
        sem.release()

root = tk.Tk()
my_gui = MeasControlGUI(root)
if __name__ == '__main__':
    my_gui.cnt()
    my_gui.pribor('')
    root.mainloop()
