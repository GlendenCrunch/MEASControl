#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import os
import sys
import re
import time
from datetime import datetime
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from openpyexcel import load_workbook
from openpyexcel.styles import PatternFill
import pyvisa
import serial
import usb.core
from calibration_oscil import *


class MeasControlGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.folder_1 = os.getcwd()
        self.title('MEASControl')
        self.geometry('1000x495')
        self.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.close_app)

        self.ser = 0
        self.count = 1
        self.varcap = 0
        self.tdiv_2 = 0

        self.varlist_str = ['name_proc','temp','humi','pres','custom','pover','var_spb1','var_spb2']
        self.vardict_str = {self.var: tk.StringVar() for self.var in self.varlist_str}

        self.varlist_boo = ['dcv_var','acv_var','f_var','dci_var','aci_var','r2_var','r4_var','tr_var','per_var','c_var','gost']
        self.vardict_boo = {self.var: tk.BooleanVar() for self.var in self.varlist_boo}
        for self.var in self.varlist_boo[:10]:
            self.vardict_boo[self.var].set(1)

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

        self.style = ttk.Style()
        self.style.theme_create('theme', settings=self.theme)
        self.style.theme_use('theme')
        self.create_widgets()

    def create_widgets(self):
        main_menu = tk.Menu()
        self.config(menu=main_menu)
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

        tabframe = tk.Frame()
        rightframe = tk.Frame()
        statusframe = tk.Frame()

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

        self.statusbar = tk.Label(statusframe, text=self.lang['statusbar_1'], background="#cccccc", anchor='w')
        self.statusbar.pack(side='left', fill='x', expand=True)
        self.statusbar_1 = tk.Label(statusframe, text="I T L ©", background="#cccccc", anchor='e')
        self.statusbar_1.pack(side='right', fill='x')

        self.tree = ttk.Treeview(self.tab1, columns=['1', '2', '3', '4'], height=5)
        self.tree.heading('#0', text="", anchor='center')
        self.tree.heading('1', text=self.lang['tree_head_1'], anchor='center')
        self.tree.heading('2', text=self.lang['tree_head_2'], anchor='center')
        self.tree.heading('3', text=self.lang['tree_head_3'], anchor='center')
        self.tree.heading('4', text=self.lang['tree_head_4'], anchor='center')
        self.tree.column('#0', stretch=False, anchor='center', minwidth=20, width=20)
        self.tree.column('1', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('2', stretch=False, anchor='center', minwidth=90, width=90)
        self.tree.column('3', stretch=False, anchor='center', minwidth=110, width=110)
        self.tree.column('4', stretch=False, anchor='center', minwidth=390, width=390)
        self.tree.place(x=0, y=290)

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

        self.lbf1 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_1'], width=200, height=200, fg=self.theme['.']['fg_colour'], bg=self.theme['.']['bg_colour'], font=self.sett_json['font_ar10b'])
        self.lbf1.place(x=5, y=5)
        self.lbf2 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_2'], width=200, height=200, fg=self.theme['.']['fg_colour'], bg=self.theme['.']['bg_colour'], font=self.sett_json['font_ar10b'])
        self.lbf2.place(x=205, y=5)
        self.lbf3 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_3'], width=200, height=100, fg=self.theme['.']['fg_colour'], bg=self.theme['.']['bg_colour'], font=self.sett_json['font_ar10b'])
        #self.lbf3.place(x=405, y=505)
        self.lbf33 = tk.LabelFrame(self.tab1, text=self.lang['LabelFrame_33'], width=200, height=100, fg=self.theme['.']['fg_colour'], bg=self.theme['.']['bg_colour'], font=self.sett_json['font_ar10b'])
        #self.lbf33.place(x=405, y=105)
        lbf4 = tk.LabelFrame(self.tab2, text=self.lang['LabelFrame_4'], width=200, height=390, fg=self.theme['.']['fg_colour'], bg=self.theme['.']['bg_colour'], font=self.sett_json['font_ar10b'])
        lbf4.place(x=5, y=5)

        self.dmm_on = tk.Button(self.lbf1, image=self.img6, bg=self.theme['.']['bg_button'], command=self.connect_dmm)
        self.dmm_on.place(x=150, y=135)
        self.fluk_on = tk.Button(self.lbf2, image=self.img6, bg=self.theme['.']['bg_button'], command=self.connect_fluke_5500)
        self.fluk_on.place(x=150, y=135)
        self.dmm_on2 = tk.Button(self.lbf3, image=self.img6, bg=self.theme['.']['bg_button'], command=self.connect_dmm2)
        self.dmm_on2.place(x=150, y=35)
        self.power_on = tk.Button(self.lbf33, image=self.img6, bg=self.theme['.']['bg_button'], command=self.connect_power)
        self.power_on.place(x=150, y=35)
        self.fresh = tk.Button(self.tab1, image=self.img4, bg=self.theme['.']['bg_button'], command=lambda: self.pribor(''))
        self.fresh.place(x=690, y=240)
        self.start_on = tk.Button(self.tab2, text=self.lang['Button_5'], width=12, fg='#ffffff', bg=self.theme['.']['bg_button'], font=self.sett_json['font_ar12b'], command=self.start)
        self.start_on.place(x=210, y=20)
        self.protocol_open = tk.Button(self.tab2, image=self.img5, state='disable', bg=self.theme['.']['bg_button'], command=self.prot_open)
        self.protocol_open.place(x=685, y=10)
        #self.paus_on = tk.Button(self.tab2, text=self.lang['Button_6'], width=12, fg='#ffffff', bg=self.theme['.']['bg_button'], font=self.sett_json['font_ar12b'])
        #self.paus_on.place(x=350, y=20)

        self.combo_dmm = ttk.Combobox(self.lbf1, state='readonly', postcommand= self.owon_get, height=5, width=25)
        self.combo_dmm.place(x=15, y=10)
        self.combo_flu = ttk.Combobox(self.lbf2, state='readonly', height=5, width=25)
        self.combo_flu.place(x=15, y=10)
        self.combo_dmm2 = ttk.Combobox(self.lbf3, state='readonly', height=5, width=25)
        self.combo_dmm2.place(x=15, y=10)
        self.combo_power = ttk.Combobox(self.lbf33, state='readonly', height=5, width=25)
        self.combo_power.place(x=15, y=10)

        self.lab1 = tk.Label(self.lbf2, text=self.lang['Label_1'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab2 = tk.Label(self.lbf2, text=self.lang['Label_2'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab3 = tk.Label(lbf4, text=self.lang['Label_3'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab3.place(x=5,y=5)
        self.lab4 = tk.Label(lbf4, text=self.lang['Label_4'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab4.place(x=5,y=35)
        self.lab5 = tk.Label(lbf4, text=self.lang['Label_5'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab5.place(x=5,y=85)
        self.lab6 = tk.Label(lbf4, text=self.lang['Label_6'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab6.place(x=5,y=115)
        self.lab7 = tk.Label(lbf4, text=self.lang['Label_7'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab7.place(x=5,y=145)
        self.lab8 = tk.Label(lbf4, text=self.lang['Label_8'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab8.place(x=5,y=175)
        self.lab9 = tk.Label(lbf4, text=self.lang['Label_9'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab9.place(x=5,y=205)
        self.lab10 = tk.Label(self.tab1, text=self.lang['Label_10'], bg=self.theme['.']['bg_colour'], fg=self.theme['.']['fg_colour'], font=self.sett_json['font_ar10b'])
        self.lab10.place(x=20,y=230)

        self.entry1 = ttk.Entry(self.tab1, textvariable=self.vardict_str['name_proc'], width=50, font=self.sett_json['font_ar10b'])
        self.entry1.place(x=170, y=230)
        self.entry2 = ttk.Entry(lbf4, textvariable=self.vardict_str['temp'], width=10, font=self.sett_json['font_ar10b'])
        self.entry2.place(x=120, y=85)
        self.entry3 = ttk.Entry(lbf4, textvariable=self.vardict_str['humi'], width=10, font=self.sett_json['font_ar10b'])
        self.entry3.place(x=120, y=115)
        self.entry4 = ttk.Entry(lbf4, textvariable=self.vardict_str['pres'], width=10, font=self.sett_json['font_ar10b'])
        self.entry4.place(x=120, y=145)
        self.entry5 = ttk.Entry(lbf4, textvariable=self.vardict_str['custom'], width=10, font=self.sett_json['font_ar10b'])
        self.entry5.place(x=120, y=175)
        self.entry6 = ttk.Entry(lbf4, textvariable=self.vardict_str['pover'], width=10, font=self.sett_json['font_ar10b'])
        self.entry6.place(x=120, y=205)

        self.spinbox1 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb1'], from_=0, to=30, width=6)
        self.spinbox2 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb2'], from_=0, to=30, width=6)
        self.chkbtn_1 = tk.Checkbutton(self.lbf1, bg="#848a98", activebackground="#848a98", text="МИ 1202-86, ГОСТ 8.366-79", variable=self.vardict_boo['gost'], onvalue=1, offvalue=0, font=self.sett_json['font_ar10b'])

        self.lb2 = tk.Listbox(self.tab2, selectmode='extended', width=47, height=2, relief='ridge', fg='blue', font=("Arial", 15, 'bold'))
        self.lb2.place(x=210, y=70)

        self.progress1 = ttk.Progressbar(self.tab2, orient='horizontal', mode='determinate', length=730, value=0)
        self.progress1.place(x=5, y=395)

    def close_app(self):
        self.quit()
        self.destroy()
        sys.exit()

    def prot_open(self):
        os.system(f"start excel {self.folder_1}\\Protocol\\{self.vardict_str['name_proc'].get()}")

    def date_time(self):
        today = datetime.today()
        self.data_today = today.strftime('%Y-%m-%d,%H-%M-%S')

    def protokol(self):
        rep = filedialog.askopenfilenames(initialdir=f'{self.folder_1}\\Protocol\\', initialfile='',
                                          filetypes=[("xlsx", "*.xlsx"),("All files", "*")])
        try:
            os.startfile(rep[0])
        except IndexError:
            pass

    def win_one(self, name_win, size_win):
        self.top = tk.Toplevel()
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
        self.win_one(self.lang['add_cascade_4'], '880x450+{}+{}')
        text1 = 'MEASControl\rVersion: 1.13a\rDate: 2025-09-24\rAutor: g1enden (I T L)'
        text2 = 'Agilent/Keysight:\r34401A\r34410A\r34411A\r34420A\r34460A\r34461A\r34465A\r34470A\r\r\r\r\r\r\r\r\r'
        text3 = 'AKIP:\rV7-78/1\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text4 = 'Lecroy:\rWJ312A\rWJ324A\rHDO8108A\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text5 = 'Tektronix:\rTDS2002\rTDS2012B\rTDS2014(B,C)\rTDS2024(B,C)\rTPS2024\r\r\r\r\r\r\r\r\r\r\r\r'
        text6 = 'Agilent/Keysight:\rMSO-X3032T\rMSO-X3104(A,T)\rMSO-X3034A\rMSO-X3054A\rMSO-X4104A\rMSO-X4154A\rDSO-X4034A\rMSO-X6004A\rDSO-X92004A\rDSO6102A\rMSO6012A\rDSO7034B\rMSO7104B\rDSO9104A\rMSO9404A\rDSOZ594A\r'
        text7 = 'Siglent(AKIP):\rAKIP-4119/1\rAKIP-4131/1A\rAKIP-4131/2A\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text8 = 'R&S:\rRTO1024\rRTO1044\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text9 = 'OWON(AKTAKOM):\rADS-222\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text10 = 'Rigol:\rMSO5204\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r'
        text11 = 'Agilent/Keysight:\r33622A\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r'

        top_1 = tk.Frame(self.top, height=70, relief="raise")
        top_1.pack(side='top', fill='x')
        top_2 = tk.Frame(self.top, height=30, relief="raise")
        top_2.pack(side='top', fill='x')
        top_3 = tk.Frame(self.top, height=30, relief="raise")
        top_3.pack(side='top', fill='x')
        top_4 = tk.Frame(self.top, height=30, relief="raise", bg='grey88')
        top_4.pack(side='bottom', fill='x')
        img_about = tk.Label(top_1, image=self.img1)
        img_about.place(x=10,y=10)
        autor = tk.Label(top_1, justify='left', text=text1, font=self.sett_json['font_ar10b'], foreground='deepskyblue4')
        autor.place(x=260,y=0)
        lbf5 = tk.LabelFrame(top_2, text='Мультиметры', width=200, height=300, font=self.sett_json['font_ar10b'], foreground='deepskyblue4')
        lbf5.grid(row=0, column=0)
        lbf6 = tk.LabelFrame(top_2, text='Осциллографы', width=500, height=300, font=self.sett_json['font_ar10b'], foreground='deepskyblue4')
        lbf6.grid(row=0, column=1)
        lbf7 = tk.LabelFrame(top_2, text='Генераторы', width=500, height=300, font=self.sett_json['font_ar10b'], foreground='deepskyblue4')
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
        support_9 = tk.Label(lbf6, text=text9, font=('arial', 10), foreground='deepskyblue4')
        support_9.grid(row=0, column=5)
        support_10 = tk.Label(lbf6, text=text10, font=('arial', 10), foreground='deepskyblue4')
        support_10.grid(row=0, column=6)
        support_11 = tk.Label(lbf7, text=text11, font=('arial', 10), foreground='deepskyblue4')
        support_11.grid(row=0, column=1)

        _button = tk.Button(top_4, text=self.lang['Button_7'], width=10, fg='#ffffff', bg=self.theme['.']['bg_button'], font=self.sett_json['font_ar12b'], command=self.top.destroy)
        _button.pack(side='top')

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

        _button = tk.Button(self.top, text=self.lang['Button_7'], width=12, fg='#ffffff', bg=self.theme['.']['bg_button'], font=self.sett_json['font_ar12b'], command=self.top.destroy)
        _button.place(x=40,y=210)

    def set_style_win(self):
        self.win_one(self.lang['fset_2'], '350x300+{}+{}')
        lab_style = tk.Label(self.top, text=self.lang['set_style_win_2'], font=self.sett_json['font_ar10b'])
        lab_style.place(x=20,y=15)
        combo_style = ttk.Combobox(self.top, state='readonly', values=['Dark', 'Light'], height=5, width=25)
        combo_style.current(0)
        combo_style.place(x=150, y=15)
        lab_lang = tk.Label(self.top, text=self.lang['set_style_win_3'], font=self.sett_json['font_ar10b'])
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
                self.destroy()
                try:
                    self.inst_dmm.close()
                    self.inst_fluke.close()
                except AttributeError:
                    print (self.lang['set_style_win_4'])
                os.system(f'{self.folder_1}\\MEASControl.py')

        _button = tk.Button(self.top, text=self.lang['Button_7'], width=12, fg='#ffffff', bg=self.theme['.']['bg_button'], font=self.sett_json['font_ar12b'], command=set_ok)
        _button.place(x=120,y=250)

    def cnt(self):
        cnt_dict = {}
        for item_0 in ['Call(', 'Call_oscill(', 'Call_DSO9000', 'Call_generator(']:
            for item_j in ('DMM', 'Generator', 'Oscilloscope'):
                for item_i in self.sett_json['ch_pribor'][item_j]:
                    osc_item = sum(1 for line in open(f'{self.folder_1}\\file_py\\{item_i}.py', encoding='utf-8') if line.lstrip().startswith(item_0))
                    if osc_item > 0:
                        cnt_dict[item_i] = osc_item * self.sett_json['ch_pribor'][item_j][item_i]

        return cnt_dict

    def virt_dmm(self):
        self.pribor(f'{self.folder_1}\\virt_pribor.yaml@sim')

    def visa_search(self, param):
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
                adres = [n for n in rm if list(self.sign_pribor.keys())[j] in n]
                if len(adres) > 0:
                    return adres

        if combo_dmm[:4] in ('ASRL', 'USB0', 'TCPI'):
            return [combo_dmm]

    def pribor(self, par):
        self.lb.delete(0, 'end')
        self.lb.insert('end', self.lang['pribor_1'])
        self.lb.itemconfig('end', bg='light cyan')
        self.visa_search(par)
        decay_list = [self.decay_cycle(n) for n in self.rm_list]
        decay_list.append('OWON(AKTAKOM)')
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

    def owon_get(self):
        if self.combo_dmm.get() == 'OWON(AKTAKOM)':
            self.dmm_on.configure(command=self.conect_owon)

    def conect_owon(self):
        self.date_time()
        self.dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)
        self.dev.set_configuration()
        msg = ':SDSLSCPI#\n' # включить общение по SCPI
        print("Write:", msg, self.dev.write(0x3,msg,1000))
        self.data_1 = self.send_owon('*IDN?').tobytes().decode('utf-8')
        self.connect_param()

    def send_owon(self, cmd):
        self.dev.write(3,cmd,1000)
        result = (self.dev.read(0x81,100000,1000))
        return result

    def connect_dmm(self):
        self.date_time()
        try:
            self.inst_dmm = self.rm.open_resource(self.adres_cycle(self.combo_dmm.get(), self.rm_list)[0], timeout=1000, write_termination='\n', read_termination='\n')
            if self.combo_dmm.get()[:4] in ('ASRL', 'USB0'):
                self.inst_dmm.write('SYST:REM')
                time.sleep(1)
            self.data_1 = self.inst_dmm.query("*IDN?")
            self.connect_param()
        except:
            self.lb.insert('end', 'Ошибка! Прибор не определён')
            self.lb.itemconfig('end', bg='salmon')

    def connect_param(self):
        self.a1 = self.data_1.split(',')
        self.a1[1] = self.a1[1].replace('/', '-').replace(' ', '')
        self.a1[2] = self.a1[2].replace('/', '-').replace(' ', '')
        if self.a1[1] == '34401A':
            self.chkbtn_1.place(x=0,y=40)
        elif self.a1[1] in list(self.sett_json['ch_pribor']['Oscilloscope'].keys()):
            self.fluk_on.configure(command=self.connect_fluke_9500)
            self.lab1.place(x=40,y=55)
            self.lab2.place(x=15,y=85)
            self.spinbox1.place(x=133, y=55)
            self.spinbox2.place(x=133, y=85)
        if self.a1[1] in ('MSO-X6004A', 'DSO9104A', 'MSO9404A', 'DSOX92004A', 'DSOZ594A', '33622A'):
            self.lbf3.place(x=405, y=5)
            if self.a1[1] in ('DSOX92004A', 'DSOZ594A'):
                self.lab2.configure(text='Внутренний калибратор\nCal Out')
                self.lab1.place(x=10,y=550)
                self.spinbox1.place(x=133, y=550)
                self.spinbox2.place(x=133, y=850)
            elif self.a1[1] == '33622A':
                self.lbf33.place(x=405, y=105)
                self.lbf2.configure(text='Частотомер')
                self.fluk_on.configure(command=self.connect_counter)
        if self.a1[1] == 'RTO':
            self.a1[1] = self.a1[1]+self.data_1.split(',')[2].split('/')[0].split('.')[1].replace('00k','')
            self.a1[2] = self.a1[2].split('/')[1]

        for item_j in ('DMM', 'Generator', 'Oscilloscope'):
            for item_i in self.sett_json['ch_pribor'][item_j]:
                if item_i == self.a1[1]:
                    self.a10 = f'{item_j} {self.a1[1]} подключен'

        self.vardict_str['name_proc'].set(f'{self.data_today},{self.a1[1]},{self.a1[2]}.xlsx')
        self.lab3['text'] = f'Тип: {self.a1[1]}'
        self.lab4['text'] = f'Зав.№: {self.a1[2]}'
        try:
            self.lb.insert('end', self.a10)
            self.tree.insert('', 'end', text='', image=self.img2, values=(self.a10.split(' ')[0], self.a1[1], self.a1[2], self.data_1))
        except AttributeError:
            self.lb.insert('end', self.data_1)
        self.lb.see('end')
        self.lb.itemconfig('end', bg='light cyan')

    def connect_dmm2(self):
        self.inst_dmm2 = self.rm.open_resource(self.adres_cycle(self.combo_dmm2.get(), self.rm_list)[0], timeout=1000)
        self.additional_device(self.inst_dmm2, self.combo_dmm2)

    def connect_power(self):
        self.inst_power = self.rm.open_resource(self.adres_cycle(self.combo_power.get(), self.rm_list)[0], timeout=1000)
        self.additional_device(self.inst_power, self.combo_power)

    def connect_counter(self):
        self.inst_count = self.rm.open_resource(self.adres_cycle(self.combo_flu.get(), self.rm_list)[0], timeout=1000)
        self.additional_device(self.inst_count, self.combo_flu)

    def additional_device(self, insrument, combo):
        try:
            if combo.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
                insrument.write('SYST:REM')
                time.sleep(1)

            identif = insrument.query("*IDN?")
            self.c1 = identif.split(',')
            #self.c1[1] = self.c1[1].replace('/', '-').replace(' ', '')
            c10 = f'{self.c1[1]} подключен'
            try:
                self.lb.insert('end', c10)
                self.tree.insert('', 'end', text='', image=self.img2, values=('', self.c1[1], self.c1[2], identif))
            except AttributeError:
                self.lb.insert('end', identif)
            self.lb.see('end')
            self.lb.itemconfig('end', bg='light cyan')
        except:
            self.lb.insert('end', 'Ошибка! Прибор не определён')
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

    def write_9500(self, message):
        self.ser.write(f'{message}\r'.encode('UTF-8'))

    def read_9500(self):
        return self.ser.readline().decode('ASCII')

    def query(self, message):
        self.write_9500(message)
        return self.read_9500()

    def connect_fluke_9500(self):
        self.ser = serial.Serial(port=f"COM{self.combo_flu.get().split('::')[0][4:]}", baudrate=115200, timeout=1)
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

    '''def connect_fluke_9500(self): # протестировать в следующий раз
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
            self.lb.insert('end', 'Формирователь не обнаружен')'''

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
                    cell.value = self.vardict_str['pres'].get()
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

#my_gui = MeasControlGUI()
if __name__ == '__main__':
    my_gui.cnt()
    my_gui.pribor('')
    my_gui.mainloop()
