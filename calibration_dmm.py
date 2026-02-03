#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import time
from datetime import datetime
import math
from tkinter import messagebox
import threading
from threading import Thread
from main import MeasControlGUI
#from calibration_oscil import *
#from main import my_gui

sem = threading.Semaphore()

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
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
        my_gui.inst_fluke.write(my_gui.calbr['OFF'])
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
        my_gui.inst_dmm.write(f"OUTP{self.form.split(':')[0][-1]}:LOAD {self.load}")
        my_gui.inst_dmm.write(self.form)
        my_gui.inst_dmm.write(f"OUTP{self.form.split(':')[0][-1]} ON")
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
        
        #my_gui.inst_dmm.write(f'OUTP{j} OFF')

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f"Канал №{self.form.split(':')[0][-1]}")
        my_gui.lb2.insert('end', f"Установлено: {self.form.split(',')[-2]}")
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2

        if my_gui.a1[1] == '33622A':
            self.call_33622a()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.form.split(',')[-2],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()

class Param_generator_uhf(Thread):
    """Class callibration generators ultra high frequencies"""
    def __init__(self, freq, power, pribor):
        Thread.__init__(self)
        self.freq = freq
        self.power = power
        self.pribor = pribor
        self.run_once = False
        self.start()

    def param_pribor(self):
        my_gui.inst_dmm2.write('CAL:AUTO OFF')
        my_gui.inst_dmm2.write('FREQ:SPAN 25 kHz')
        my_gui.inst_dmm2.write('UNIT:POW dBm') # mW
        self.run_once = True
        print('Yes!')

    def param_g7m(self):
        if self.run_once is False:
            self.param_pribor()

        my_gui.inst_dmm.write(self.freq)
        my_gui.inst_dmm.write(self.power)
        my_gui.inst_dmm2.write('DISP:WIND:TRAC:Y:SCALe:RLEV 10')
        my_gui.inst_dmm.write('OUTP:STAT ON')
        time.sleep(1)
        my_gui.inst_dmm2.write(self.pribor)
        time.sleep(1)
        my_gui.inst_dmm2.write('CALC:MARK1:MAX')
        my_gui.inst_dmm2.write('CALC:MARK1:MODE DELT')
        time.sleep(1)

    def run(self):
        sem.acquire()
        self.param_g7m()
        sem.release()

class Call_generator_uhf(Thread):
    """Class callibration generators ultra high frequencies"""
    def __init__(self, freq, power, pribor, cel, accur):
        Thread.__init__(self)
        self.freq = freq
        self.power = power
        self.pribor = pribor
        self.cel = cel
        self.accur = accur
        self.start()

    def call_g7m(self):
        my_gui.inst_dmm.write(self.freq)
        my_gui.inst_dmm.write(self.power)
        my_gui.inst_dmm.write('OUTP:STAT ON')
        time.sleep(3)
        if self.cel[0] == 'f':
            my_gui.inst_count.write(f':CONF:FREQ {self.pribor.split(" ")[1]}')
            time.sleep(1)
            my_gui.inst_count.write(self.pribor)
            time.sleep(2)
            self.data_true = float(my_gui.inst_count.read())
            self.data_error = (self.data_true - (float(self.freq.split(' ')[1]) * 1E+6)) / float(self.freq.split(' ')[1])
        elif self.cel[0] == 'p': # use power meter
            my_gui.inst_power.write('UNIT:POW DBM')
            my_gui.inst_power.write(self.pribor)
            time.sleep(1)
            self.data_true = float(my_gui.inst_power.query('FETC1?'))
            self.data_error = self.data_true - float(self.power.split(' ')[1])
        elif self.cel[:2] == 'no' or self.cel[0] in ('h', 'a'): # use signal analyzer
            my_gui.inst_dmm2.write(self.pribor)
            if self.cel[0] == 'a':
                my_gui.inst_dmm2.write('DISP:WIND:TRAC:Y:SCALe:RLEV -30')
            time.sleep(1)
            my_gui.inst_dmm2.write('CALC:MARK1:MAX')
            time.sleep(1)
            self.data_true = float(my_gui.inst_dmm2.query('CALC:MARK1:Y?'))
            if self.cel[0] == 'a':
                self.data_error = self.data_true - float(self.power.split(' ')[1])
            else:
                self.data_error = self.data_true

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel:
                    cell.value = self.data_true
                    if self.cel[0] == 'h' or self.cel[:2] == 'no':
                        if self.data_error > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    else:
                        if self.data_error > self.accur or self.data_error < -self.accur:
                                cell.fill = my_gui.colour_cell
                                self.tree2_img = my_gui.img3
        
        my_gui.inst_dmm.write('OUTP:STAT OFF')

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f"Установлено: {self.freq.split(' ')[1]} MГц, {self.power.split(' ')[1]} dBm")
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2
        
        if my_gui.a1[1] == 'Г7М-20А-6':
            self.call_g7m()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.freq.split(' ')[1],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
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

    def reset_ads(self):
        my_gui.dev.write(3, '*RST', 1000)
        my_gui.dev.write(3, '*CLS', 1000)
        my_gui.query('*RST')
        my_gui.query('*CLS')
        time.sleep(5)

    def reset_gener(self):
        self.reset_common()
        #my_gui.inst_power.write('*RST')
        #my_gui.inst_power.write('*CLS')

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
        elif self.name.split('-')[0] == 'reset_ads':
            self.reset_ads()
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
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
        my_gui.lb.insert('end', f'Время окончания: {my_gui.data_today[11:]}')
        my_gui.lb.insert('end', f'Время поверки: {stop_time - my_gui.start_time}')
        sem.release()

my_gui = MeasControlGUI()
