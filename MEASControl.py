#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import os
import re
import time
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
varcap = 0
count = 1
colour_cell = PatternFill(start_color='FFFFDAB9', end_color='FFFFDAB9', fill_type='solid')


class MeasControlGUI():
    """class GUI"""
    def __init__(self, parent):
        self.parent = parent
        self.folder_1 = os.getcwd()
        self.rg6 = {'0A07': '34411A', '1A07': '34461A', '1301': '34461A', '1401': '34461A',
                    '0101': '34465A', '0DAD':'V7-78/1', '1F01': 'N5183A', '5707': '33622A',
                    '5418': 'N1913A', '0090': 'CNT-90XL', '0368': 'TDS 2014B',
                    '17A4': 'MSO-X 3034A', '1770': 'MSO-X 3104T'}
        self.ser = 0
        self.name_protokol = tk.StringVar()
        self.temp = tk.StringVar()
        self.humi = tk.StringVar()
        self.press = tk.StringVar()
        self.custom = tk.StringVar()
        self.pover = tk.StringVar()
        self.var_spb1 = tk.StringVar()
        self.var_spb2 = tk.StringVar()
        self.dcv_var = tk.BooleanVar()
        self.acv_var = tk.BooleanVar()
        self.f_var = tk.BooleanVar()
        self.dci_var = tk.BooleanVar()
        self.aci_var = tk.BooleanVar()
        self.c_var = tk.BooleanVar()
        self.r2_var = tk.BooleanVar()
        self.r4_var = tk.BooleanVar()
        self.tr_var = tk.BooleanVar()
        self.per_var = tk.BooleanVar()
        self.gost = tk.BooleanVar()
        self.dcv_var.set(1)
        self.acv_var.set(1)
        self.f_var.set(1)
        self.dci_var.set(1)
        self.aci_var.set(1)
        self.c_var.set(0)   # временно отключил
        self.r2_var.set(1)
        self.r4_var.set(1)
        self.tr_var.set(1)
        self.per_var.set(1)
        self.gost.set(0)

        self.img1 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\pan1.gif')
        self.img2 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\check.gif')

        with open(f'{self.folder_1}\\setting.json','r', encoding='utf-8') as file_json:
            self.sett_json = json.load(file_json)
        with open(f'{self.folder_1}\\theme.json','r', encoding='utf-8') as file_json:
            self.theme_json = json.load(file_json)
        with open(f'{self.folder_1}\\language.json','r', encoding='utf-8') as file_json:
            self.lang_json = json.load(file_json)

        if self.sett_json['language'] == '0':
            self.lang_set = 'rus'
        elif self.sett_json['language'] == '1':
            self.lang_set = 'eng'

        self.bg_colour = self.theme_json['bg_colour']
        self.fg_colour = self.theme_json['fg_colour']
        self.bg_button = self.theme_json['bg_button']
        self.pastel_setting = self.theme_json["pastel_setting"]
        self.style = ttk.Style()
        self.style.theme_create('pastel', settings=self.pastel_setting)

        self.style.theme_use('pastel')

        parent.title('MEASControl')
        parent.geometry('1000x490')
        parent.iconbitmap(f'{self.folder_1}\\icon\\icon.ico')
        parent.resizable(width=False, height=False)

        main_menu = tk.Menu(self.parent)
        self.parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu, tearoff=False)
        file_menu.add_separator()
        file_menu.add_command(label=self.lang_json[self.lang_set]['file_menu_close'], command=self.parent.destroy)

        file_setting = tk.Menu(main_menu, tearoff=False)
        file_setting.add_command(label=self.lang_json[self.lang_set]['file_set_1'], command=self.setting_win)
        file_setting.add_command(label=self.lang_json[self.lang_set]['file_set_2'], command=self.set_style_win)

        main_menu.add_cascade(label=self.lang_json[self.lang_set]['add_cascade_1'], menu=file_menu)
        main_menu.add_cascade(label=self.lang_json[self.lang_set]['add_cascade_2'], command=self.protokol)
        main_menu.add_cascade(label=self.lang_json[self.lang_set]['add_cascade_3'], menu=file_setting)
        main_menu.add_cascade(label=self.lang_json[self.lang_set]['add_cascade_4'], command=self.about_win)

        self.tabFrame = tk.Frame(self.parent)
        self.rightFrame = tk.Frame(self.parent)
        self.statusFrame = tk.Frame(self.parent)

        self.tabFrame.grid(row=0, column=0, ipadx=210, ipady=210,sticky="nsew")
        self.rightFrame.grid(row=0, column=1, sticky="ns")
        self.statusFrame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.sb = tk.Scrollbar(self.rightFrame, orient='vertical')
        self.lb = tk.Listbox(self.rightFrame, selectmode='extended', width=39, height=20, relief='ridge')
        self.sb['command'] = self.lb.yview
        self.lb['yscroll'] = self.sb.set
        self.sb.pack(side=tk.RIGHT, fill='y')
        self.lb.pack(side=tk.RIGHT, fill='y')

        self.tab_control = ttk.Notebook(self.tabFrame)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text=self.lang_json[self.lang_set]['tab_control_1'])
        self.tab_control.add(self.tab2, text=self.lang_json[self.lang_set]['tab_control_2'])
        self.tab_control.pack(expand=1, fill='both')

        self.statusbar = tk.Label(self.statusFrame, text=self.lang_json[self.lang_set]['statusbar_1'], background="gray80", anchor='w')
        self.statusbar.pack(side='left', fill='x', expand=True)
        self.statusbar_1 = tk.Label(self.statusFrame, text="I T L ©", background="gray80", anchor='e')
        self.statusbar_1.pack(side='right', fill='x')

        self.tree = ttk.Treeview(self.tab1, columns=['1', '2', '3', '4'], height=5)
        self.tree.heading('#0', text="", anchor='center')
        self.tree.heading('1', text=self.lang_json[self.lang_set]['tree_heading_1'], anchor='center')
        self.tree.heading('2', text=self.lang_json[self.lang_set]['tree_heading_2'], anchor='center')
        self.tree.heading('3', text=self.lang_json[self.lang_set]['tree_heading_3'], anchor='center')
        self.tree.heading('4', text="IDN?", anchor='center')
        self.tree.column('#0', stretch=False, anchor='center', minwidth=30, width=30)
        self.tree.column('1', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('2', stretch=False, anchor='center', minwidth=100, width=100)
        self.tree.column('3', stretch=False, anchor='center', minwidth=120, width=120)
        self.tree.column('4', stretch=False, anchor='center', minwidth=360, width=360)
        self.tree.place(x=5, y=220)

        self.lbf1 = tk.LabelFrame(self.tab1, text=self.lang_json[self.lang_set]['LabelFrame_1'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=("Arial", 10, 'bold'))
        self.lbf1.place(x=5, y=5)
        self.lbf2 = tk.LabelFrame(self.tab1, text=self.lang_json[self.lang_set]['LabelFrame_2'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=("Arial", 10, 'bold'))
        self.lbf2.place(x=205, y=5)
        #self.lbf3 = tk.LabelFrame(self.tab1, text=self.lang_json[self.lang_set]['LabelFrame_3'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=("Arial", 10, 'bold'))
        #self.lbf3.place(x=405, y=5)
        self.lbf4 = tk.LabelFrame(self.tab2, text=self.lang_json[self.lang_set]['LabelFrame_4'], width=200, height=390, fg=self.fg_colour, bg=self.bg_colour, font=("Arial", 10, 'bold'))
        self.lbf4.place(x=5, y=5)

        self.dmm_on = tk.Button(self.lbf1, text=self.lang_json[self.lang_set]['Button_1'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.connect_dmm)
        self.dmm_on.place(x=35, y=130)
        self.fluk_on = tk.Button(self.lbf2, text=self.lang_json[self.lang_set]['Button_2'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.connect_fluke_5500)
        self.fluk_on.place(x=35, y=130)
        self.next = tk.Button(self.tab1, text=self.lang_json[self.lang_set]['Button_4'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.next)
        self.next.place(x=300, y=375)
        self.fresh = tk.Button(self.tab1, text=self.lang_json[self.lang_set]['Button_3'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.pribor)
        self.fresh.place(x=610, y=375)
        self.start_on = tk.Button(self.tab2, text=self.lang_json[self.lang_set]['Button_5'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.start)
        self.start_on.place(x=210, y=20)
        #self.paus_on = tk.Button(self.tab2, text=self.lang_json[self.lang_set]['Button_6'], width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'))
        #self.paus_on.place(x=350, y=20)

        self.combo_dmm = ttk.Combobox(self.lbf1, state='readonly', height=5, width=25)
        self.combo_dmm.place(x=15, y=10)
        self.combo_flu = ttk.Combobox(self.lbf2, state='readonly', height=5, width=25)
        self.combo_flu.place(x=15, y=10)

        self.lab3 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_3'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab3.place(x=10,y=30)
        self.lab4 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_4'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab4.place(x=10,y=60)
        self.lab5 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_5'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab5.place(x=10,y=110)
        self.lab6 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_6'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab6.place(x=10,y=140)
        self.lab7 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_7'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab7.place(x=10,y=170)
        self.lab8 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_8'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab8.place(x=10,y=200)
        self.lab9 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_9'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab9.place(x=10,y=230)
        self.lab10 = tk.Label(self.tab2, text=self.lang_json[self.lang_set]['Label_10'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
        self.lab10.place(x=230,y=180)

        self.entry1 = ttk.Entry(self.tab2, textvariable=self.name_protokol, width=55, font='arial 8')
        self.entry1.place(x=390, y=180)
        self.entry2 = ttk.Entry(self.tab2, textvariable=self.temp, width=10, font='arial 8')
        self.entry2.place(x=130, y=110)
        self.entry3 = ttk.Entry(self.tab2, textvariable=self.humi, width=10, font='arial 8')
        self.entry3.place(x=130, y=140)
        self.entry4 = ttk.Entry(self.tab2, textvariable=self.press, width=10, font='arial 8')
        self.entry4.place(x=130, y=170)
        self.entry5 = ttk.Entry(self.tab2, textvariable=self.custom, width=10, font='arial 8')
        self.entry5.place(x=130, y=200)
        self.entry6 = ttk.Entry(self.tab2, textvariable=self.pover, width=10, font='arial 8')
        self.entry6.place(x=130, y=230)

        self.lb2 = tk.Listbox(self.tab2, selectmode='extended', width=47, height=3, relief='ridge', fg='blue', font=("Arial", 15, 'bold'))
        self.lb2.place(x=210, y=70)

        self.progress1 = ttk.Progressbar(self.tab2, orient='horizontal', mode='determinate', length=730, value=0)
        self.progress1.place(x=5, y=395)

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
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        w = w // 3
        h = h // 2
        w = w - 200
        h = h - 200
        self.top.geometry(size_win.format(w, h))

    def about_win(self):
        self.win_one('О программе', '500x300+{}+{}')
        text1 = ('MEASControl\rVersion: 1.07\rDate: 2021-12-24\rAutor: I T L ©')
        text2_0 = ('\tМультиметры:')
        text2_1 = ('\t\tОсциллографы:')
        text3 = ('Agilent/Keysight:\r34401A\r34410A\r34411A\r34420A\r34460A\r34461A\r34465A\r34470A')
        text4 = ('  АКИП:\r  B7-78/1\r\r\r\r\r\r\r\r')
        text5 = ('       Lecroy:\r       WaveJet 312A\r       WaveJet 324A\r\r\r\r\r\r\r')
        text6 = ('Tektronix:\rTDS1002\rTDS1012\rTDS2002\rTDS2012\rTDS2014\rTDS2022\rTDS2024\r\r')
        text7 = ('Keysight:\rMSO-X 3034A\r\r\r\r\r\r\r\r')

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
        autor = tk.Label(top_1, justify='left', text=text1, font=("Arial", 10, "bold"), foreground='deepskyblue4')
        autor.place(x=260,y=5)
        support_1_0 = tk.Label(top_2, justify='center', text=text2_0, font=('arial', 10, 'bold'), foreground='deepskyblue4')
        support_1_0.grid(row=0, column=0)
        support_1_1 = tk.Label(top_2, justify='center', text=text2_1, font=('arial', 10, 'bold'), foreground='deepskyblue4')
        support_1_1.grid(row=0, column=1)
        support_2 = tk.Label(top_3, text=text3, font=('arial', 10), foreground='deepskyblue4')
        support_2.grid(row=0, column=0)
        support_3 = tk.Label(top_3, text=text4, font=('arial', 10), foreground='deepskyblue4')
        support_3.grid(row=0, column=1)
        support_4 = tk.Label(top_3, text=text5, font=('arial', 10), foreground='deepskyblue4')
        support_4.grid(row=0, column=2)
        support_5 = tk.Label(top_3, text=text6, font=('arial', 10), foreground='deepskyblue4')
        support_5.grid(row=0, column=3)
        support_6 = tk.Label(top_3, text=text7, font=('arial', 10), foreground='deepskyblue4')
        support_6.grid(row=0, column=4)

        _button = tk.Button(bottom_1, text='OK', width=10, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.top.destroy)
        _button.place(x=200,y=2)

    def setting_win(self):
        self.win_one('Настройки', '220x250+{}+{}')
        try:
            if self.a1[1] == '34420A':
                c1 = tk.Checkbutton(self.top, text="Заглушка", variable=self.acv_var, onvalue=1, offvalue=0)
                c1.pack(anchor='w')
                c2 = tk.Checkbutton(self.top, text="Постоянное напряжение", variable=self.dcv_var, onvalue=1, offvalue=0)
                c2.pack(anchor='w')
                c3 = tk.Checkbutton(self.top, text="Сопротивление 4-провода", variable=self.r4_var, onvalue=1, offvalue=0)
                c3.pack(anchor='w')
            elif self.a1[1] in ('34401A', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78/1'):
                c1 = tk.Checkbutton(self.top, text="Постоянное напряжение", variable=self.dcv_var, onvalue=1, offvalue=0)
                c1.pack(anchor='w')
                c2 = tk.Checkbutton(self.top, text="Переменное напряжение", variable=self.acv_var, onvalue=1, offvalue=0)
                c2.pack(anchor='w')
                c3 = tk.Checkbutton(self.top, text="Частота", variable=self.f_var, onvalue=1, offvalue=0)
                c3.pack(anchor='w')
                c4 = tk.Checkbutton(self.top, text="Постоянный ток", variable=self.dci_var, onvalue=1, offvalue=0)
                c4.pack(anchor='w')
                c5 = tk.Checkbutton(self.top, text="Переменный ток", variable=self.aci_var, onvalue=1, offvalue=0)
                c5.pack(anchor='w')
                c6 = tk.Checkbutton(self.top, text="Ёмкость", variable=self.c_var, onvalue=1, offvalue=0)
                c6.pack(anchor='w')
                c7 = tk.Checkbutton(self.top, text="Сопротивление 2-провода", variable=self.r2_var, onvalue=1, offvalue=0)
                c7.pack(anchor='w')
                c8 = tk.Checkbutton(self.top, text="Сопротивление 4-провода", variable=self.r4_var, onvalue=1, offvalue=0)
                c8.pack(anchor='w')
            elif self.a1[1] == 'WJ312A':
                c1 = tk.Checkbutton(self.top, text="Постоянное напряжение", variable=self.dcv_var, onvalue=1, offvalue=0)
                c1.pack(anchor='w')
                c2 = tk.Checkbutton(self.top, text="Время нарастания", variable=self.tr_var, onvalue=1, offvalue=0)
                c2.pack(anchor='w')
                c3 = tk.Checkbutton(self.top, text="Период", variable=self.per_var, onvalue=1, offvalue=0)
                c3.pack(anchor='w')
            elif self.a1[1] in ('TDS 1002B','TDS 1012B','TDS 2002B','TDS 2012B','TDS 2014B', 'TDS 2022B', 'TDS 2024B'):
                c1 = tk.Checkbutton(self.top, text="Постоянное напряжение", variable=self.dcv_var, onvalue=1, offvalue=0)
                c1.pack(anchor='w')
                c2 = tk.Checkbutton(self.top, text="Временной интервал", variable=self.per_var, onvalue=1, offvalue=0)
                c2.pack(anchor='w')
                c3 = tk.Checkbutton(self.top, text="Время нарастания", variable=self.tr_var, onvalue=1, offvalue=0)
                c3.pack(anchor='w')
        except AttributeError:
            clab = tk.Label(self.top, text='Прибор не определён', font='arial 13', foreground='deepskyblue4')
            clab.pack(anchor='w')

        _button = tk.Button(self.top, text="OK", width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=self.top.destroy)
        _button.place(x=40,y=210)

    def set_style_win(self):
        self.win_one('Стили', '350x300+{}+{}')
        self.lab_style = tk.Label(self.top, text='Цветовая тема:', font=('arial', 10, 'bold'))
        self.lab_style.place(x=20,y=15)
        self.combo_style = ttk.Combobox(self.top, state='readonly', values=['Dark', 'Light'], height=5, width=25)
        self.combo_style.place(x=150, y=15)
        self.lab_lang = tk.Label(self.top, text='Язык:', font=('arial', 10, 'bold'))
        self.lab_lang.place(x=20,y=45)
        self.combo_lang = ttk.Combobox(self.top, state='readonly', values=['Russia', 'English'], height=5, width=25)
        self.combo_lang.place(x=150, y=45)

        def set_ok():
            if self.combo_style.get() == 'Dark':
                self.theme_json['bg_colour'] = "#848a98"
                self.theme_json['fg_colour'] = "gold"
                self.theme_json['bg_button'] = "#6699CC"
            elif self.combo_style.get() == 'Light':
                self.theme_json['bg_colour'] = "snow3"
                self.theme_json['fg_colour'] = "cyan4"
                self.theme_json['bg_button'] = "cyan4"
            if self.combo_lang.get() == 'Russia':
                self.sett_json['language'] = '0'
            elif self.combo_lang.get() == 'English':
                self.sett_json['language'] = '1'

            self.theme_json['pastel_setting']["."]["configure"]["background"] = self.theme_json['bg_colour']
            self.theme_json['pastel_setting']["TNotebook"]["configure"]["background"] = self.theme_json['bg_colour']
            self.theme_json['pastel_setting']["TNotebook.Tab"]["configure"]["background"] = self.theme_json['bg_colour']
            self.theme_json['pastel_setting']["TNotebook.Tab"]["map"]["background"] = [["selected",self.theme_json['fg_colour']]]

            with open(f'{self.folder_1}\\theme.json', 'w', encoding='utf-8') as file_json:
                json.dump(self.theme_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)
            with open(f'{self.folder_1}\\setting.json', 'w', encoding='utf-8') as file_json:
                json.dump(self.sett_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)
            self.parent.destroy()
            try:
                self.inst_dmm.close()
                self.inst_fluke.close()
            except AttributeError:
                print ('Стиль изменён')
            os.system(f'{self.folder_1}\\MEASControl.py')

        _button = tk.Button(self.top, text="Применить", width=12, fg='#fff', bg=self.bg_button, font=("Arial", 12, 'bold'), command=set_ok)
        _button.place(x=120,y=250)

    def cnt(self):
        dmm_v778_1 = sum(1 for line in open(f'{self.folder_1}\\file_py\\v7-78.py', encoding='utf-8') if line.lstrip().startswith('_thdmm = Call(')) - 8

        cnt_dict = {'V7-78/1':dmm_v778_1}
        cnt_list = ['34401A', '34401A_gost', '34420A', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'WJ312A', 'WJ324A',
                    'TDS 1002B', 'TDS 1012B', 'TDS 2002B', 'TDS 2012B', 'TDS 2014B', 'TDS 2022B', 'TDS 2024B', 'MSO-X 3034A', 'MSO-X 3104T']

        for item_0 in ['_thdmm = Call(', '_thosc = Call_oscill(']:
            for item_i in cnt_list:
                osc_item = sum(1 for line in open(f'{self.folder_1}\\file_py\\{item_i}.py', encoding='utf-8') if line.lstrip().startswith(item_0))
                if osc_item > 0:
                    cnt_dict[item_i] = osc_item

        return cnt_dict

    def next(self):
        self.tab_control.select(self.tab2)

    def visa_search(self):
        #self.rm = pyvisa.ResourceManager(visa_library='C:/Program Files/IVI Foundation/VISA/Win64/agvisa/agbin/visa32.dll')
        self.rm = pyvisa.ResourceManager()
        self.rm_tuple = self.rm.list_resources()
        self.rm_list = list(self.rm_tuple)
        return self.rm_list

    def decay_cycle(self, rm):
        for j, item in enumerate(self.rg6):
            if re.search(list(self.rg6.keys())[j], rm):
                rm = list(self.rg6.values())[j]
        return rm

    def adres_cycle(self, combo_dmm, rm):
        for j, item in enumerate(self.rg6):
            if combo_dmm == list(self.rg6.values())[j]:
                adres = list(filter(lambda rmt: list(self.rg6.keys())[j] in rmt, rm))
                if len(adres) > 0:
                    return adres

        if combo_dmm[:4] in ('ASRL', 'USB0', 'TCPI'):
            return [combo_dmm]

    def pribor(self):
        self.lb.delete(0, 'end')
        self.lb.insert('end', 'Обнаруженные приборы и порты:')
        self.lb.itemconfig('end', bg='light cyan')
        self.visa_search()
        decay_list = list(map(self.decay_cycle, self.rm_list))
        self.lb.insert('end', *decay_list)
        self.combo_dmm.configure(values=decay_list)
        #self.combo_dmm.current(0)
        self.combo_flu.configure(values=decay_list)
        #self.combo_flu.current(0)
        self.var_spb1.set('10')
        self.var_spb2.set('4')
        self.tree.delete(*self.tree.get_children())

    def connect_dmm(self):
        today = datetime.today()
        self.data_today = today.strftime('%d-%m-%Y,%H-%M-%S')

        self.inst_dmm = self.rm.open_resource(self.adres_cycle(self.combo_dmm.get(), self.rm_list)[0])
        if self.combo_dmm.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
            self.inst_dmm.write('SYST:REM')
            time.sleep(1)

        self.data_1 = self.inst_dmm.query("*IDN?")
        self.a1 = self.data_1.split(',')
        if self.a1[1] == '34401A':
            chkbtn_1 = tk.Checkbutton(self.lbf1, bg="#848a98", activebackground="#848a98", text="МИ 1202-86, ГОСТ 8.366-79", variable=self.gost, onvalue=1, offvalue=0, font=('arial', 9, 'bold'))
            chkbtn_1.place(x=10,y=40)
        if self.a1[1] in ('34401A', '34410A', '34411A', '34420A', '34460A', '34461A', '34465A', '34470A', 'V7-78/1'):
            self.a10 = f'Мультиметр {self.a1[1]} подключен'
        elif self.a1[1] == ' CNT-90XL':
            self.a10 = f'Частотомер {self.a1[1]} подключен'
        elif self.a1[1] in ('WJ312A', 'WJ324A', 'TDS 2014B', 'MSO-X 3034A', 'MSO-X 3104T'):
            self.a10 = f'Осциллограф {self.a1[1]} подключен'
            self.fluk_on.configure(command=self.connect_fluke_9500)
            self.lab1 = tk.Label(self.lbf2, text=self.lang_json[self.lang_set]['Label_1'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
            self.lab1.place(x=40,y=55)
            self.lab2 = tk.Label(self.lbf2, text=self.lang_json[self.lang_set]['Label_2'], bg=self.bg_colour, fg=self.fg_colour, font=('arial', 10, 'bold'))
            self.lab2.place(x=15,y=85)
            self.spinbox1 = tk.Spinbox(self.lbf2, textvariable=self.var_spb1, from_=0, to=30, width=6)
            self.spinbox1.place(x=133, y=55)
            self.spinbox2 = tk.Spinbox(self.lbf2, textvariable=self.var_spb2, from_=0, to=30, width=6)
            self.spinbox2.place(x=133, y=85)
        if self.a1[1] == 'V7-78/1':
            self.name_a1 = self.a1[1][0:5]
        else:
            self.name_a1 = self.a1[1]
        self.name_protokol.set(f'{self.data_today},{self.name_a1},{self.a1[2]}.xlsx')
        self.lab3['text'] = f'Тип: {self.a1[1]}'
        self.lab4['text'] = f'Зав.№: {self.a1[2]}'
        self.lb.insert('end', self.a10)
        self.lb.see('end')
        self.lb.itemconfig('end', bg='cyan')
        self.tree.insert('', 'end', text='', image=self.img2, values=(self.a10.split(' ')[0], self.a1[1], self.a1[2], self.data_1))

    def connect_fluke_set(self):
        self.b1 = self.data_2.split(',')
        self.b10 = f'Калибратор {self.b1[0]} {self.b1[1]} подключен'
        self.lb.insert('end', self.b10)
        self.lb.see('end')
        self.lb.itemconfig('end', bg='aquamarine')
        self.tree.insert('', 'end', text='', image=self.img2, values=(self.b10.split(' ')[0], self.b1[1], self.b1[2], self.data_2))

    def connect_fluke_5500(self):
        try:
            self.inst_fluke = self.rm.open_resource(self.combo_flu.get(), baud_rate=9600, data_bits=8, write_termination='\r', read_termination='\r')
            time.sleep(1)
            self.inst_fluke.write('*IDN?')
            self.data_2 = my_gui.inst_fluke.read()
            self.connect_fluke_set()
        except:
            self.lb.insert('end', 'Ошибка: Калибратор не определён')
            self.lb.itemconfig('end', bg='red')

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
                self.data_2_1 = self.query(f"ROUT:FITT? CH{self.spinbox2.get()}")
                self.lb.insert('end', self.data_2_1)
                self.lb.see('end')
        except:
            self.lb.insert('end', 'Формирователь не обнаружен')

    def start(self):
        if self.gost.get() == 1:
            self.name_a1 = '34401A_gost'
            self.a1[1] = '34401A_gost'
        self.progress1.configure(maximum=self.cnt()[self.a1[1]])
        self.lb.insert('end', f'Время начала: {self.data_today[11:]}')
        self.wb = load_workbook(f'{self.folder_1}\\shablon\\{self.name_a1}.xlsx')
        self.ws = self.wb.active
        exec(open(f'{self.folder_1}\\file_py\\{self.name_a1}.py', encoding='utf-8').read())

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
        self.start()

    def v7_78_agilent(self):
        my_gui.inst_dmm.write(self.confdmm)
        my_gui.inst_dmm.write(self.vary1)
        time.sleep(1)
        my_gui.inst_fluke.write(self.vfluke)
        my_gui.inst_fluke.write('OPER')
        time.sleep(self.vary2)
        my_gui.inst_dmm.write('READ?')
        if self.vary1 == 'DET:BAND 3':
            time.sleep(7)
        else:
            time.sleep(2)
        data_0 = float(my_gui.inst_dmm.read())
        self.data_true = data_0
        if self.vfluke.split(' ')[2] in ('mV', 'mV,', 'mA', 'mA,'):
            self.data_true = data_0 * 1E+3
        elif self.vfluke.split(' ')[2] in ('uA', 'uA,'):
            self.data_true = data_0 * 1E+6
        elif self.vfluke.split(' ')[2] in ('kOHM', 'kOHM;'):
            self.data_true = data_0 / 1E+3
        elif self.vfluke.split(' ')[2] in ('MOHM', 'MOHM;'):
            self.data_true = data_0 / 1E+6
        elif self.vfluke.split(' ')[2] in ('GOHM', 'GOHM;'):
            self.data_true = data_0 / 1E+9
        elif self.vfluke.split(' ')[2] == 'NF':
            self.data_true = (data_0 - varcap) * 1E+9
        elif self.vfluke.split(' ')[2] == 'UF':
            self.data_true = (data_0 - varcap) * 1E+6
        elif self.name == 'fr':
            if self.vfluke.split(' ')[4] == 'kHz':
                self.data_true = data_0 / 1E+3

    def agilent_34420A(self):
        my_gui.inst_dmm.write(self.confdmm)
        my_gui.inst_dmm.write(self.vary1)
        my_gui.inst_dmm.write(self.vary2)
        time.sleep(1)
        if len(self.vfluke) > 0:
            my_gui.inst_fluke.write(self.vfluke)
            my_gui.inst_fluke.write('OPER')
        time.sleep(5)
        my_gui.inst_dmm.write('READ?')
        time.sleep(2)
        data_0 = float(my_gui.inst_dmm.read())
        self.data_true = data_0
        if self.name == 'dcv':
            if self.vfluke.split(' ')[2] == 'mV':
                self.data_true = data_0 * 1E+3
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[1])) * 1E+3
            else:
                if self.accur.split(' ')[1] == 'u':
                    self.data_error = (self.data_true - float(self.vfluke.split(' ')[1])) * 1E+6
                elif self.accur.split(' ')[1] == 'm':
                    self.data_error = (self.data_true - float(self.vfluke.split(' ')[1])) * 1E+3
        elif self.name == 'r':
            if self.vfluke.split(' ')[2] == 'kOHM;':
                self.data_true = data_0 / 1E+3
            elif self.vfluke.split(' ')[2] == 'MOHM;':
                self.data_true = data_0 / 1E+6
            if self.accur in ('72 u', '620 u', '62 m', '620 m', '74 Ohm'):
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[1])) * 1E+6
            elif self.accur in ('6.2 m', '6.4 Ohm'):
                self.data_error = (self.data_true - float(self.vfluke.split(' ')[1])) * 1E+3
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
        global count
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f'Режим {self.name}: {self.vfluke[4:]}')
        my_gui.lb2.see('end')

        if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78/1'):
            self.v7_78_agilent()
        elif my_gui.a1[1] == '34420A':
            self.agilent_34420A()

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cell1:
                    cell.value = self.data_true
                    if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78/1'):
                        if self.data_true > self.accur or self.data_true < self.cell2:
                            cell.fill = colour_cell

                if my_gui.a1[1] == '34420A':
                    if cell.value == self.cell2:
                        cell.value = self.data_error
                        if self.data_error > float(self.accur.split(' ')[0]) or self.data_error < -float(self.accur.split(' ')[0]):
                            cell.fill = colour_cell

        my_gui.wb.save(f'{my_gui.folder_1}\\Protocol\\Multimeter\\{my_gui.name_protokol.get()}')
        my_gui.inst_fluke.write('STBY')
        time.sleep(1)
        my_gui.progress1.step(1)
        count += 1
        sem.release()

# ====================================== Oscilloscop ======================================
# ====================================== WJ312 =======================================
class Param_wj312(Thread):
    """Class setting parametrs oscilloscope WJ312"""
    def __init__(self, name, imp, rezfluke, point ,tdiv):
        Thread.__init__(self)
        self.name = name
        self.imp = imp
        self.rezfluke = rezfluke
        self.point = point
        self.tdiv = tdiv
        self.start()

    def run(self):
        sem.acquire()
        if self.name == '1':
            my_gui.inst_dmm.write('C1:TRA ON')
            my_gui.inst_dmm.write('C2:TRA OFF')
        elif self.name == '2':
            my_gui.inst_dmm.write('C1:TRA OFF')
            my_gui.inst_dmm.write('C2:TRA ON')
        elif self.name == '3':
            my_gui.inst_dmm.write('C3:TRA ON')
        elif self.name == '4':
            my_gui.inst_dmm.write('C4:TRA ON')
        my_gui.inst_dmm.write(f'C{self.name}:CPL DC1M')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        if self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.inst_dmm.write(f'C{self.name}:VDIV 200mv')
            my_gui.inst_dmm.write(f'C{self.name}:OFST 200mv')
            my_gui.inst_dmm.write('TLVL -200mv')
        elif self.rezfluke == 'SCOP:SHAP SIN':
            my_gui.query('FREQ:FIX 10E+06')
            my_gui.inst_dmm.write(f'C{self.name}:OFST 0mv')
            my_gui.inst_dmm.write('TLVL 0mv')
        my_gui.inst_dmm.write(self.point)
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write('TRMD AUTO')
        my_gui.inst_dmm.write('MDSP ON')
        my_gui.inst_dmm.write('DIRM A')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},TOP')
        my_gui.inst_dmm.write('DIRM B')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},BASE')
        my_gui.inst_dmm.write('DIRM C')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},TR10-90')
        my_gui.inst_dmm.write('DIRM D')
        my_gui.inst_dmm.write(f'MSEL CH{self.name},FREQ')
        sem.release()

# ====================================== TDS_1000_2000_B ======================================
class Param_tds2(Thread):
    """Class setting parametrs oscilloscope Tektronix"""
    def __init__(self, name, imp, rezfluke, tdiv, ffluke):
        Thread.__init__(self)
        self.name = name
        self.imp = imp
        self.rezfluke = rezfluke
        self.tdiv = tdiv
        self.ffluke = ffluke
        self.start()

    def run(self):
        sem.acquire()
        global tdiv_2
        if self.name == '1':
            my_gui.inst_dmm.write('SEL:CH1 ON')
            my_gui.inst_dmm.write('SEL:CH2 OFF')
            my_gui.inst_dmm.write('SEL:CH3 OFF')
            my_gui.inst_dmm.write('SEL:CH4 OFF')
        elif self.name == '2':
            my_gui.inst_dmm.write('SEL:CH1 OFF')
            my_gui.inst_dmm.write('SEL:CH2 ON')
            my_gui.inst_dmm.write('SEL:CH3 OFF')
            my_gui.inst_dmm.write('SEL:CH4 OFF')
        elif self.name == '3':
            my_gui.inst_dmm.write('SEL:CH1 OFF')
            my_gui.inst_dmm.write('SEL:CH2 OFF')
            my_gui.inst_dmm.write('SEL:CH3 ON')
            my_gui.inst_dmm.write('SEL:CH4 OFF')
        elif self.name == '4':
            my_gui.inst_dmm.write('SEL:CH1 OFF')
            my_gui.inst_dmm.write('SEL:CH2 OFF')
            my_gui.inst_dmm.write('SEL:CH3 OFF')
            my_gui.inst_dmm.write('SEL:CH4 ON')
        my_gui.inst_dmm.write(f'CH{self.name}:COUP DC')
        my_gui.inst_dmm.write(f'CH{self.name}:PRObe 1')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
        my_gui.inst_dmm.write(f'CH{self.name}:POS 0')  # смещение сигнала
        my_gui.inst_dmm.write('TRIG:MAI:LEV 0')        # уровень запуска
        if self.rezfluke == 'SCOP:SHAP MARK':
            my_gui.query(self.ffluke)
            tdiv_2 = self.ffluke.split(' ')[1]
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            my_gui.inst_dmm.write(f'CH{self.name}:VOL 0.1')
            my_gui.inst_dmm.write(f'CH{self.name}:POS 2')
            my_gui.inst_dmm.write('TRIG:MAI:LEV -0.2')
            tdiv_2 = self.tdiv.split(' ')[1]
        my_gui.inst_dmm.write(self.tdiv)
        my_gui.inst_dmm.write('TRIG:MAI:MOD AUTO')
        my_gui.inst_dmm.write(f'TRIG:MAI:EDGE:SOU CH{self.name}')
        my_gui.inst_dmm.write(f'MEASU:MEAS1:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS1:TYP MEAN')
        my_gui.inst_dmm.write(f'MEASU:MEAS3:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS3:TYP PERIod')
        my_gui.inst_dmm.write(f'MEASU:MEAS4:SOU CH{self.name}')
        my_gui.inst_dmm.write('MEASU:MEAS4:TYP RIS')
        sem.release()

# ====================================== MSO-X 3000 ======================================
class Param_msox3(Thread):
    """Class setting parametrs oscilloscope Keysight"""
    def __init__(self, name, imp, rezfluke, tdiv, ffluke):
        Thread.__init__(self)
        self.name = name
        self.imp = imp
        self.rezfluke = rezfluke
        self.tdiv = tdiv
        self.ffluke = ffluke
        self.start()

    def run(self):
        sem.acquire()
        if self.name == '1':
            my_gui.inst_dmm.write('CHAN1:DISP 1')
            my_gui.inst_dmm.write('CHAN2:DISP 0')
            my_gui.inst_dmm.write('CHAN3:DISP 0')
            my_gui.inst_dmm.write('CHAN4:DISP 0')
        elif self.name == '2':
            my_gui.inst_dmm.write('CHAN1:DISP 0')
            my_gui.inst_dmm.write('CHAN2:DISP 1')
            my_gui.inst_dmm.write('CHAN3:DISP 0')
            my_gui.inst_dmm.write('CHAN4:DISP 0')
        elif self.name == '3':
            my_gui.inst_dmm.write('CHAN1:DISP 0')
            my_gui.inst_dmm.write('CHAN2:DISP 0')
            my_gui.inst_dmm.write('CHAN3:DISP 1')
            my_gui.inst_dmm.write('CHAN4:DISP 0')
        elif self.name == '4':
            my_gui.inst_dmm.write('CHAN1:DISP 0')
            my_gui.inst_dmm.write('CHAN2:DISP 0')
            my_gui.inst_dmm.write('CHAN3:DISP 0')
            my_gui.inst_dmm.write('CHAN4:DISP 1')
        my_gui.inst_dmm.write(f':TRIG:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f':MEAS:SOUR CHAN{self.name}')
        my_gui.inst_dmm.write(f'CHAN{self.name}:COUP DC')
        my_gui.inst_dmm.write(f'CHAN{self.name}:PROB 1')
        my_gui.query(self.imp)
        my_gui.query(self.rezfluke)
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
            #my_gui.inst_dmm.write('CHAN1:IMP FIFT')
        my_gui.inst_dmm.write(self.tdiv)
        sem.release()

class Call_oscill(Thread):
    """Class callibration oscilloscope"""
    def __init__(self, vfluk, vosc1, vosc2, cel1, cel2, accur):
        Thread.__init__(self)
        self.vfluk = vfluk
        self.vosc1 = vosc1
        self.vosc2 = vosc2
        self.cel1 = cel1
        self.cel2 = cel2
        self.accur = accur
        self.start()

    def call_wj312(self):
        time.sleep(5)
        data_true = float(my_gui.inst_dmm.query(self.vosc2))
        data_error = (data_true - float(self.vfluk.split(' ')[1]))*1000

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = data_true
                if cell.value == self.cel2:
                    cell.value = data_error
                    if data_error > self.accur or data_error < -self.accur:
                        cell.fill = colour_cell

    def call_tds2(self):
        time.sleep(2)
        my_gui.inst_dmm.write('ACQ:MOD AVE; NUMAV 16')
        time.sleep(3)
        data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.vosc2 in ('MEASU:MEAS1:VAL?'):
            data_error = ((data_true - float(self.vfluk.split(' ')[1])) / float(self.vfluk.split(' ')[1])) * 100
        elif self.vosc2 == 'MEASU:MEAS3:VAL?':
            data_error = data_true - float(tdiv_2)
            data_true = data_true * float(f'1E+{tdiv_2[-1:]}')
        elif self.vosc2 == 'MEASU:MEAS4:VAL?':
            data_true = data_true * float(f'1E+{tdiv_2[-1:]}')
            data_error = None

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = data_true
                if cell.value == self.cel2:
                    cell.value = data_error
                    if self.vosc2 == 'MEASU:MEAS4:VAL?':
                        if data_true > self.accur:
                            cell.fill = colour_cell
                    else:
                        if data_error > self.accur or data_error < -self.accur:
                            cell.fill = colour_cell

        my_gui.inst_dmm.write('ACQ:MOD SAM')

    def call_msox_3(self):
        time.sleep(2)
        my_gui.inst_dmm.write(':ACQ:TYPE AVER; :ACQ:COUN 64')
        time.sleep(3)
        data_true = float(my_gui.inst_dmm.query(self.vosc2))
        if self.vosc2 in (':MEAS:VMAX?'):
            accur_1 = float(self.vfluk.split(' ')[1]) + self.accur
            accur_2 = float(self.vfluk.split(' ')[1]) - self.accur
            if float(self.vfluk.split(' ')[1]) < 1:
                data_true = data_true * 1000
                accur_1 = accur_1 * 1000
                accur_2 = accur_2 * 1000
        elif self.vosc2 in (':MEAS:RIS?'):
            data_true_1 = data_true / 1E-9
            data_true = (0.35 / data_true) * 1E-6
        elif self.vosc2 in (':MEAS:VPP'):
            data_true = data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = data_true
                    if self.vosc2 in (':MEAS:RIS?', ':MEAS:VPP?'):
                        if data_true < self.accur:
                            cell.fill = colour_cell
                    else:
                        if data_true > accur_1 or data_true < accur_2:
                            cell.fill = colour_cell

                if self.vosc2 in (':MEAS:RIS?'):
                    if cell.value == self.cel2:
                        cell.value = data_true_1

        my_gui.inst_dmm.write(':ACQ:TYPE NORM')

    def run(self):
        sem.acquire()
        global count
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', '{} канал, напряжение {} Вольт'.format(self.vosc1.split(':')[0][-1],self.vfluk.split(' ')[1]))
        my_gui.lb2.see('end')
        my_gui.query(self.vfluk)
        my_gui.inst_dmm.write(self.vosc1)
        my_gui.query("OUTP:STAT ON")

        if my_gui.a1[1] in ('WJ312A', 'WJ324A'):
            self.call_wj312()
        elif my_gui.a1[1] == 'TDS 2014B':
            self.call_tds2()
        elif my_gui.a1[1] in ('MSO-X 3034A', 'MSO-X 3104T'):
            self.call_msox_3()

        my_gui.wb.save(f'{my_gui.folder_1}\\Protocol\\Oscilloscope\\{my_gui.name_protokol.get()}')
        my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        count += 1
        sem.release()
# ============================================================================
class Message(Thread):
    """Class message"""
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text
        self.start()

    def run(self):
        sem.acquire()
        messagebox.showinfo('ВНИМАНИЕ!', self.text)
        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == '_type':
                    cell.value = my_gui.a1[1].split('_')[0]
                if cell.value == '_numb':
                    cell.value = my_gui.a1[2]
                if cell.value == '_customer':
                    cell.value = my_gui.custom.get()
                if cell.value == '_temp':
                    cell.value = my_gui.temp.get()
                if cell.value == '_hum':
                    cell.value = my_gui.humi.get()
                if cell.value == '_pres':
                    cell.value = my_gui.press.get()
                if cell.value == '_pov':
                    cell.value = my_gui.pover.get()
                if cell.value == '_date':
                    cell.value = my_gui.data_today[:10]
        sem.release()

class Reset(Thread):
    """Class reset pribor"""
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        sem.acquire()
        time.sleep(2)
        if my_gui.b1[1] == '9500B':
            my_gui.query('*CLS')
            my_gui.query('*RST')
            if my_gui.a1[1] == 'MSO-X 3034A':
                my_gui.inst_dmm.write('*RST')
        else:
            my_gui.inst_fluke.write('*CLS')
            my_gui.inst_fluke.write('*RST')
            my_gui.inst_dmm.write('*RST')
        time.sleep(2)
        sem.release()

class cap(Thread):
    """Class for capacitor"""
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        sem.acquire()
        global varcap
        my_gui.inst_dmm.write('CONF:CAP')
        time.sleep(5)
        my_gui.inst_dmm.write('READ?')
        time.sleep(5)
        varcap = float(my_gui.inst_dmm.read())
        time.sleep(1)
        my_gui.progress1.step(1)
        sem.release()

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
        self.clear_rows()
        time.sleep(1)
        self.merged_cells()
        time.sleep(1)
        my_gui.wb.save(f'{my_gui.folder_1}\\Protocol\\Multimeter\\{my_gui.name_protokol.get()}')
        sem.release()

root = tk.Tk()
my_gui = MeasControlGUI(root)
if __name__ == '__main__':
    my_gui.cnt()
    my_gui.pribor()
    root.mainloop()
