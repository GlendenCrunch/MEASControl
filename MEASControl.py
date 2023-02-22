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
VARCAP = 0
COUNT = 1


class MeasControlGUI():
    """class GUI"""
    def __init__(self, parent):
        self.parent = parent
        self.folder_1 = os.getcwd()
        self.ser = 0

        self.varlist_str = ['name_protokol','temp','humi','press','custom','pover','var_spb1','var_spb2']
        self.vardict_str = {self.var: tk.StringVar() for self.var in self.varlist_str}

        self.varlist_boo = ['dcv_var','acv_var','f_var','dci_var','aci_var','r2_var','r4_var','tr_var','per_var','c_var','gost']
        self.vardict_boo = {self.var: tk.BooleanVar() for self.var in self.varlist_boo}
        for self.var in self.varlist_boo[:9]:
            self.vardict_boo[self.var].set(1)

        self.ar10b = ('arial', 10, 'bold')
        self.ar12b = ('arial', 12, 'bold')
        self.colour_cell = PatternFill(start_color='FFFFDAB9', end_color='FFFFDAB9', fill_type='solid')

        self.img1 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\pan1.gif')
        self.img2 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\check.gif')
        self.img3 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\error.png')
        self.img4 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\refresh.png')

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
        fmenu.add_command(label=self.lang['fmenu_close'], command=self.parent.destroy)

        fsetting = tk.Menu(main_menu, tearoff=False)
        fsetting.add_command(label=self.lang['fset_1'], command=self.setting_win)
        fsetting.add_command(label=self.lang['fset_2'], command=self.set_style_win)

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
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text=self.lang['tab_control_1'])
        tab_control.add(tab2, text=self.lang['tab_control_2'])
        tab_control.pack(expand=1, fill='both')

        self.statusbar = tk.Label(statusframe, text=self.lang['statusbar_1'], background="gray80", anchor='w')
        self.statusbar.pack(side='left', fill='x', expand=True)
        self.statusbar_1 = tk.Label(statusframe, text="I T L ©", background="gray80", anchor='e')
        self.statusbar_1.pack(side='right', fill='x')

        self.tree = ttk.Treeview(tab1, columns=['1', '2', '3', '4'], height=5)
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

        self.tree2 = ttk.Treeview(tab2, columns=['1', '2', '3', '4'], height=11)
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

        self.lbf1 = tk.LabelFrame(tab1, text=self.lang['LabelFrame_1'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf1.place(x=5, y=5)
        self.lbf2 = tk.LabelFrame(tab1, text=self.lang['LabelFrame_2'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        self.lbf2.place(x=205, y=5)
        #lbf3 = tk.LabelFrame(tab1, text=self.lang['LabelFrame_3'], width=200, height=200, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        #lbf3.place(x=405, y=5)
        lbf4 = tk.LabelFrame(tab2, text=self.lang['LabelFrame_4'], width=200, height=390, fg=self.fg_colour, bg=self.bg_colour, font=self.ar10b)
        lbf4.place(x=5, y=5)

        self.dmm_on = tk.Button(self.lbf1, text=self.lang['Button_1'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_dmm)
        self.dmm_on.place(x=35, y=130)
        self.fluk_on = tk.Button(self.lbf2, text=self.lang['Button_2'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.connect_fluke_5500)
        self.fluk_on.place(x=35, y=130)
        self.fresh = tk.Button(tab1, image=self.img4, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.pribor)
        self.fresh.place(x=690, y=240)
        self.start_on = tk.Button(tab2, text=self.lang['Button_5'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.start)
        self.start_on.place(x=210, y=20)
        #self.paus_on = tk.Button(self.tab2, text=self.lang['Button_6'], width=12, fg='#fff', bg=self.bg_button, font=self.ar12b)
        #self.paus_on.place(x=350, y=20)

        self.combo_dmm = ttk.Combobox(self.lbf1, state='readonly', height=5, width=25)
        self.combo_dmm.place(x=15, y=10)
        self.combo_flu = ttk.Combobox(self.lbf2, state='readonly', height=5, width=25)
        self.combo_flu.place(x=15, y=10)

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
        self.lab10 = tk.Label(tab1, text=self.lang['Label_10'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
        self.lab10.place(x=20,y=230)

        self.entry1 = ttk.Entry(tab1, textvariable=self.vardict_str['name_protokol'], width=50, font=self.ar10b)
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

        self.lb2 = tk.Listbox(tab2, selectmode='extended', width=47, height=2, relief='ridge', fg='blue', font=("Arial", 15, 'bold'))
        self.lb2.place(x=210, y=70)

        self.progress1 = ttk.Progressbar(tab2, orient='horizontal', mode='determinate', length=730, value=0)
        self.progress1.place(x=5, y=395)

    def date_time(self):
        today = datetime.today()
        self.data_today = today.strftime('%d-%m-%Y,%H-%M-%S')

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
        self.win_one('О программе', '500x300+{}+{}')
        text1 = ('MEASControl\rVersion: 1.08\rDate: 2022-09-26\rAutor: g1enden (I T L)')
        text2_0 = ('\tМультиметры:')
        text2_1 = ('\t\tОсциллографы:')
        text3 = ('Agilent/Keysight:\r34401A\r34410A\r34411A\r34420A\r34460A\r34461A\r34465A\r34470A')
        text4 = ('  АКИП:\r  B7-78/1\r\r\r\r\r\r\r\r')
        text5 = ('       Lecroy:\r       WaveJet 312A\r\r\r\r\r\r\r\r')
        text6 = ('Tektronix:\rTDS2014B\r\r\r\r\r\r\r\r')
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
        autor = tk.Label(top_1, justify='left', text=text1, font=self.ar10b, foreground='deepskyblue4')
        autor.place(x=260,y=0)
        support_1_0 = tk.Label(top_2, justify='center', text=text2_0, font=self.ar10b, foreground='deepskyblue4')
        support_1_0.grid(row=0, column=0)
        support_1_1 = tk.Label(top_2, justify='center', text=text2_1, font=self.ar10b, foreground='deepskyblue4')
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

        _button = tk.Button(bottom_1, text='OK', width=10, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=200,y=2)

    def checkbut_widget(self, rng_i, ch_text, ch_var):
        for i in range(rng_i):
            tk.Checkbutton(self.top, text=ch_text[i], variable=ch_var[i], onvalue=1, offvalue=0).pack(anchor='w')

    def setting_win(self):
        self.win_one('Настройки', '220x250+{}+{}')
        try:
            if self.a1[1] == '34420A':
                self.checkbut_widget(3, ["Заглушка","Постоянное напряжение","Сопротивление 4-провода"], [self.vardict_boo['acv_var'],self.vardict_boo['dcv_var'],self.vardict_boo['r4_var']])
            elif self.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78'):
                self.checkbut_widget(8, ["Постоянное напряжение","Переменное напряжение","Частота","Постоянный ток",
                "Переменный ток","Ёмкость","Сопротивление 2-провода","Сопротивление 4-провода"], [self.vardict_boo['dcv_var'],self.vardict_boo['acv_var'],
                self.vardict_boo['f_var'],self.vardict_boo['dci_var'],self.vardict_boo['aci_var'],self.vardict_boo['c_var'],self.vardict_boo['r2_var'],self.vardict_boo['r4_var']])
            elif self.a1[1] == 'WJ312A':
                self.checkbut_widget(3, ["Постоянное напряжение","Время нарастания","Период"], [self.vardict_boo['dcv_var'],self.vardict_boo['tr_var'],self.vardict_boo['per_var']])
            elif self.a1[1] in ('TDS 2014B', 'TDS 2014C'):
                self.checkbut_widget(3, ["Постоянное напряжение","Временной интервал","Время нарастания"], [self.vardict_boo['dcv_var'],self.vardict_boo['per_var'],self.vardict_boo['tr_var']])
        except AttributeError:
            clab = tk.Label(self.top, text='Прибор не определён', font='arial 13', foreground='deepskyblue4')
            clab.pack(anchor='w')

        _button = tk.Button(self.top, text="OK", width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=self.top.destroy)
        _button.place(x=40,y=210)

    def set_style_win(self):
        self.win_one('Стили', '350x300+{}+{}')
        lab_style = tk.Label(self.top, text='Цветовая тема:', font=self.ar10b)
        lab_style.place(x=20,y=15)
        combo_style = ttk.Combobox(self.top, state='readonly', values=['Dark', 'Light'], height=5, width=25)
        combo_style.current(0)
        combo_style.place(x=150, y=15)
        lab_lang = tk.Label(self.top, text='Язык:', font=self.ar10b)
        lab_lang.place(x=20,y=45)
        combo_lang = ttk.Combobox(self.top, state='readonly', values=['Russia', 'English'], height=5, width=25)
        combo_lang.current(0)
        combo_lang.place(x=150, y=45)

        def set_ok():
            self.sett_json['language'] = combo_lang.get()
            self.sett_json['theme'] = combo_style.get()

            with open(f'{self.folder_1}\\setting.json', 'w', encoding='utf-8') as file_json:
                json.dump(self.sett_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)

            self.parent.destroy()
            try:
                self.inst_dmm.close()
                self.inst_fluke.close()
            except AttributeError:
                print ('Стиль изменён')
            os.system(f'{self.folder_1}\\MEASControl.py')

        _button = tk.Button(self.top, text="Применить", width=12, fg='#fff', bg=self.bg_button, font=self.ar12b, command=set_ok)
        _button.place(x=120,y=250)

    def cnt(self):
        cnt_dict = {}
        cnt_list = ['34401A', '34401A_gost', '34420A', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78', 'WJ312A', 'WJ324A',
                    'TDS 1002B', 'TDS 1012B', 'TDS 2002B', 'TDS 2012B', 'TDS 2014B', 'TDS 2022B', 'TDS 2024B', 'MSO-X 3034A', 'MSO-X 3104T']

        for item_0 in ['Call(', 'Call_oscill(']:
            for item_i in cnt_list:
                osc_item = sum(1 for line in open(f'{self.folder_1}\\file_py\\{item_i}.py', encoding='utf-8') if line.lstrip().startswith(item_0))
                if osc_item > 0:
                    cnt_dict[item_i] = osc_item

        return cnt_dict

    def visa_search(self):
        #self.rm = pyvisa.ResourceManager(visa_library='C:/Program Files/IVI Foundation/VISA/Win64/agvisa/agbin/visa32.dll')
        self.rm = pyvisa.ResourceManager()
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
        self.vardict_str['var_spb1'].set('10')
        self.vardict_str['var_spb2'].set('4')
        self.tree.delete(*self.tree.get_children())
        self.tree2.delete(*self.tree2.get_children())

    def connect_dmm(self):
        try:
            self.date_time()
            self.inst_dmm = self.rm.open_resource(self.adres_cycle(self.combo_dmm.get(), self.rm_list)[0])
            if self.combo_dmm.get()[:4] in ('ASRL', 'USB0', 'TCPI'):
                self.inst_dmm.write('SYST:REM')
                time.sleep(1)

            self.data_1 = self.inst_dmm.query("*IDN?")
            self.a1 = self.data_1.split(',')
            if self.a1[1] == '34401A':
                chkbtn_1 = tk.Checkbutton(self.lbf1, bg="#848a98", activebackground="#848a98", text="МИ 1202-86, ГОСТ 8.366-79", variable=self.vardict_boo['gost'], onvalue=1, offvalue=0, font=self.ar10b)
                chkbtn_1.place(x=0,y=40)
            if self.a1[1] in ('34401A', '34410A', '34411A', '34420A', '34460A', '34461A', '34465A', '34470A', 'V7-78/1'):
                self.a10 = f'Мультиметр {self.a1[1]} подключен'
            elif self.a1[1] in ('WJ312A', 'WJ324A', 'TDS 2014B', 'TDS 2014C', 'MSO-X 3034A', 'MSO-X 3104T'):
                self.a10 = f'Осциллограф {self.a1[1]} подключен'
                self.fluk_on.configure(command=self.connect_fluke_9500)
                self.lab1 = tk.Label(self.lbf2, text=self.lang['Label_1'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
                self.lab1.place(x=40,y=55)
                self.lab2 = tk.Label(self.lbf2, text=self.lang['Label_2'], bg=self.bg_colour, fg=self.fg_colour, font=self.ar10b)
                self.lab2.place(x=15,y=85)
                self.spinbox1 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb1'], from_=0, to=30, width=6)
                self.spinbox1.place(x=133, y=55)
                self.spinbox2 = tk.Spinbox(self.lbf2, textvariable=self.vardict_str['var_spb2'], from_=0, to=30, width=6)
                self.spinbox2.place(x=133, y=85)
            if self.a1[1] == 'V7-78/1':
                self.a1[1] = self.a1[1][0:5]
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
        except:
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
                self.data_2_1 = self.query(f"ROUT:FITT? CH{self.spinbox2.get()}")
                self.lb.insert('end', self.data_2_1)
                self.lb.see('end')
        except:
            self.lb.insert('end', 'Формирователь не обнаружен')

    def entry_in_cell(self):
        for row in self.ws.rows:
            for cell in row:
                if cell.value == '_type':
                    cell.value = self.a1[1].split('_')[0]
                if cell.value == '_numb':
                    cell.value = self.a1[2]
                if cell.value == '_customer':
                    cell.value = self.vardict_str['custom'].get()
                if cell.value == '_temp':
                    cell.value = self.vardict_str['temp'].get()
                if cell.value == '_hum':
                    cell.value = self.vardict_str['humi'].get()
                if cell.value == '_pres':
                    cell.value = self.vardict_str['press'].get()
                if cell.value == '_pov':
                    cell.value = self.vardict_str['pover'].get()
                if cell.value == '_date':
                    cell.value = self.data_today[:10]

    def start(self):
        try:
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
        self.start()

    def v7_78_agilent(self):
        my_gui.inst_dmm.write(self.confdmm)
        my_gui.inst_dmm.write(self.vary1)
        time.sleep(1)
        if self.confdmm.split(' ', 1)[0] == 'CONF:FRES':
            my_gui.inst_fluke.write(my_gui.calbr[self.name]+self.vfluke+my_gui.calbr['res4'])
        else:
            my_gui.inst_fluke.write(my_gui.calbr[self.name]+self.vfluke)
        my_gui.inst_fluke.write(my_gui.calbr['ON'])
        time.sleep(self.vary2)
        my_gui.inst_dmm.write('READ?')
        if self.vary1 == 'DET:BAND 3':
            time.sleep(7)
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
            self.data_true = (data_0 - VARCAP) * 1E+9
        elif self.vfluke.split(' ')[1] == 'UF':
            self.data_true = (data_0 - VARCAP) * 1E+6

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
        global COUNT
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {COUNT} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f'Режим измерения: {self.name.upper()}')
        my_gui.lb2.insert('end', 'Установлено: ' + self.vfluke)
        my_gui.lb2.see('end')

        if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78'):
            self.v7_78_agilent()
        elif my_gui.a1[1] == '34420A':
            self.agilent_34420A()

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cell1:
                    cell.value = self.data_true
                    tree2_img = my_gui.img2
                    if my_gui.a1[1] in ('34401A', '34401A_gost', '34410A', '34411A', '34460A', '34461A', '34465A', '34470A', 'V7-78'):
                        if self.data_true > self.set_fluk+self.accur or self.data_true < self.set_fluk-self.accur:
                            cell.fill = my_gui.colour_cell
                            tree2_img = my_gui.img3

                if my_gui.a1[1] == '34420A':
                    if cell.value == self.cell2:
                        cell.value = self.data_error
                        if self.data_error > float(self.accur.split(' ')[0]) or self.data_error < -float(self.accur.split(' ')[0]):
                            cell.fill = my_gui.colour_cell
                            tree2_img = my_gui.img3

        my_gui.entry_in_cell()
        my_gui.tree2.insert('', 0, text='', image=tree2_img, values=(self.vfluke,round(self.data_true,4),self.data_err,f'±{self.accur}'))
        my_gui.wb.save('{}\\Protocol\\Multimeter\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.inst_fluke.write(my_gui.calbr['OFF'])
        time.sleep(1)
        my_gui.progress1.step(1)
        COUNT += 1
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
                        cell.fill = my_gui.colour_cell

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
                            cell.fill = my_gui.colour_cell
                    else:
                        if data_error > self.accur or data_error < -self.accur:
                            cell.fill = my_gui.colour_cell

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
                            cell.fill = my_gui.colour_cell
                    else:
                        if data_true > accur_1 or data_true < accur_2:
                            cell.fill = my_gui.colour_cell

                if self.vosc2 in (':MEAS:RIS?'):
                    if cell.value == self.cel2:
                        cell.value = data_true_1

        my_gui.inst_dmm.write(':ACQ:TYPE NORM')

    def run(self):
        sem.acquire()
        global COUNT
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {COUNT} из {my_gui.cnt()[my_gui.a1[1]]}'
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

        my_gui.entry_in_cell()
        my_gui.wb.save('{}\\Protocol\\Oscilloscope\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        COUNT += 1
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
            my_gui.inst_dmm.write('*CLS')
        if my_gui.b1[1] == 'N4-56':
            my_gui.inst_fluke.write('RES:MODE:HD ON')
        time.sleep(2)
        sem.release()

class cap(Thread):
    """Class for capacitor"""
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        sem.acquire()
        global VARCAP
        my_gui.inst_dmm.write('CONF:CAP')
        time.sleep(5)
        my_gui.inst_dmm.write('READ?')
        time.sleep(5)
        VARCAP = float(my_gui.inst_dmm.read())
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
        my_gui.date_time()
        self.clear_rows()
        time.sleep(1)
        self.merged_cells()
        time.sleep(1)
        my_gui.wb.save('{}\\Protocol\\Multimeter\\{}'.format(my_gui.folder_1,my_gui.vardict_str['name_protokol'].get()))
        my_gui.lb.insert('end', f'Время окончания: {my_gui.data_today[11:]}')
        sem.release()

root = tk.Tk()
my_gui = MeasControlGUI(root)
my_gui.cnt()
my_gui.pribor()
root.mainloop()
