#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import time
from datetime import datetime
import math
from tkinter import messagebox
import threading
from threading import Thread
#from main import MeasControlGUI
from calibration_dmm import my_gui
#from main import my_gui

sem = threading.Semaphore()

class Param_osc(Thread):
    """Class setting parammetrs oscilloscopes"""
    def __init__(self, name, imp, rezfluke, tdiv, ffluke):
        #Thread.__init__(self)
        super(Param_osc, self).__init__()
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
        elif my_gui.a1[1] == 'MSO5204':
            my_gui.inst_dmm.write(f':TRIG:EDGE:SOUR CHAN{self.name}')
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
        if my_gui.a1[1] == 'DSOZ594A':
            my_gui.inst_dmm.write(self.rezfluke)

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

    def chanel_select_owon(self, ch, numb_ch, on, off):
            a = on.split('_')
            b = off.split('_')
            for i in range(1, numb_ch+1, 1):
                time.sleep(1)
                if i == int(ch):
                    my_gui.dev.write(3, f'{a[0]}{i}{a[1]}', 1000)
                else:
                    my_gui.dev.write(3, f'{b[0]}{i}{b[1]}', 1000)

    def param_ads(self):
        self.chanel_select_owon(self.name, 2, ':CHAN_:DISP ON', ':CHAN_:DISP OFF')
        time.sleep(1)
        my_gui.dev.write(3, f':CHAN{self.name}:COUP DC', 2000)
        my_gui.dev.write(3, f':CHAN{self.name}:PROB x1', 1000)
        my_gui.dev.write(3, self.tdiv, 1000)
        my_gui.query(self.imp)
        time.sleep(1)
        my_gui.query(self.rezfluke)
        my_gui.dev.write(3, f':CHAN{self.name}:OFFS 0', 1000)  # смещение сигнала
        my_gui.dev.write(3, ':TRIG:SING:EDGE:LEV 0', 1000)   # уровень запуска
        if self.rezfluke == 'SCOP:SHAP MARK':
            my_gui.query(self.ffluke)
            my_gui.tdiv_2 = self.ffluke.split(' ')[1]
        elif self.rezfluke == 'SCOP:SHAP EDGE':
            my_gui.query("PAR:EDGE:TRAN RIS")
            my_gui.query("PAR:EDGE:SPE 500E-12")
            if self.ffluke.split(' ')[1] == 'RISE':
                my_gui.dev.write(3, f':CHAN{self.name}:OFFS 78', 1000)
                my_gui.query('SCOP:TRAN RIS')
            elif self.ffluke.split(' ')[1] == 'FALL':
                my_gui.dev.write(3, f':CHAN{self.name}:OFFS -78', 1000)
                my_gui.query('SCOP:TRAN FALL')
            #my_gui.dev.write(3, self.ffluke, 1000)
            my_gui.tdiv_2 = self.tdiv.split(' ')[1]
        time.sleep(1)
        my_gui.dev.write(3, ':TRIG:MODE AUTO', 1000)
        my_gui.dev.write(3, f':TRIG:SING:EDGE:SOUR CH{self.name}', 1000)
        my_gui.dev.write(3, f':MEAS:SOUR CH{self.name}', 1000)
        my_gui.dev.write(3, f':MEAS:ADD ALL', 1000)

    def param_rigol_mso(self):
        self.chanel_select(self.name, 4, 'CHAN_:DISP 1', 'CHAN_:DISP 0')
        self.default_agilent()
        my_gui.inst_dmm.write(f':MEAS:COUN:SOUR CHAN{self.name}')


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
        elif my_gui.a1[1] in ('MSO-X6004A', 'DSO9104A', 'MSO9404A'):
            self.param_dso9()
        elif my_gui.a1[1] in ('DSOX92004A', 'DSOZ594A'):
            self.param_dsox90000()
        elif my_gui.a1[1] in ('TDS2002', 'TDS2012B', 'TDS2014', 'TDS2014C', 'TDS2014B', 'TDS2024', 'TDS2024B', 'TDS2024C', 'TPS2024'):
            self.param_tds2()
        elif my_gui.a1[1] in ('AKIP-4119-1', 'AKIP-4131-1A', 'AKIP-4131-2A'):
            self.param_akip4131()
        elif my_gui.a1[1] in ('RTO1024', 'RTO1044'):
            self.param_rto()
        elif my_gui.a1[1] == 'ADS-222':
            self.param_ads()
        elif my_gui.a1[1] == 'MSO5204':
            self.param_rigol_mso()
        sem.release()
# ========================================================================================
class Call_oscill(Thread):
    """Class callibration oscilloscopes"""
    #data_true: float
    #data_error: float
    def __init__(self, vfluk, vosc1, vosc2, cel1, cel2, accur):
        #Thread.__init__(self)
        super(Call_oscill, self).__init__()
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
            my_gui.inst_dmm.write(f"CHAN{self.vosc1[4]}:OFFS {float(self.vfluk.split(' ')[1]) / 2}")  # смещение сигнала для периодической поверки
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
            my_gui.inst_dmm.write(f"{self.vosc1.split(':')[0]}:OFST {self.cel2}V")
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
            my_gui.inst_dmm.write(f"{self.vosc1.split(':')[0]}:OFST {self.cel2}v")
            time.sleep(2)

        if self.vosc2.split(' ')[-1] == 'MEAN':
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2).split(',')[1].split('V')[0])
            self.data_error = (self.data_true - float(self.vfluk.split(' ')[1]))

        if self.vosc2.split(' ')[-1] == 'RISE':
            my_gui.inst_dmm.write('PARM CUST,STAT') # усреднение
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
            my_gui.inst_dmm.write(f"{self.vosc1.split(':')[0]}:OFFS {self.vfluk.split(' ')[1]}")
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

    def call_ads(self):
        time.sleep(1)
        my_gui.dev.write(3, ':ACQ:AVER 4', 1000)
        time.sleep(5)
        if self.vosc2 == ':MEAS:RTIM?':
            my_gui.dev.write(3, self.cel2, 1000)
        if self.vosc2[6:] == 'MAX?':
            if self.vosc1.split(' ')[1] in ('2mv','5mv','10mv','20mv','50mv','100mv','200mv'):
                self.data_true = float(my_gui.send_owon(self.vosc2).tobytes().decode('utf-8')[:-2]) / 1000
            else:
                self.data_true = float(my_gui.send_owon(self.vosc2).tobytes().decode('utf-8')[:-2])
            self.data_error = ((self.data_true - float(self.vfluk.split(' ')[1])) / float(self.vfluk.split(' ')[1])) * 100
        elif self.vosc2 == 'MEASU:MEAS3:VAL?':
            self.data_true = self.data_true * float(f'1E+{my_gui.tdiv_2[-1:]}')
            self.data_error = self.data_true - float(my_gui.tdiv_2.split('E')[0])
        elif self.vosc2 == ':MEAS:RTIM?':
            time.sleep(1)
            self.data_true = float(my_gui.send_owon(self.vosc2).tobytes().decode('utf-8')[:-2])
            self.data_error = self.data_true
        elif self.vosc2 == 'MEASU:MEAS2:VAL?':
            self.data_true = self.data_true * 1E+3
            self.data_error = (float(self.vfluk.split(' ')[1]) / (2 * math.sqrt(2))) * 1E+3

        for row in my_gui.ws.rows:
            for cell in row:
                if cell.value == self.cel1:
                    cell.value = self.data_true
                    if self.vosc2  == ':MEAS:RTIM?':
                        if self.data_true > self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                if cell.value == self.cel2:
                    cell.value = self.data_error
                    if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

    def call_rigol_mso(self):
        time.sleep(1)
        my_gui.inst_dmm.write(':ACQ:TYPE AVER; :ACQ:AVER 8')
        time.sleep(3)
        if self.vosc2 == ':MEAS:ITEM? VMAX':
            if int(self.cel1.split('_')[1]) < 9:
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2)) * 1000
            else:
                self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
            self.data_error = self.data_true

        if self.cel1.split('_')[0][:4] == 'vofs':
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS {self.vosc2}')
            time.sleep(2)
            self.data_true = float(my_gui.inst_dmm.query(':MEAS:ITEM? VMAX'))
            self.data_error = self.data_true

        if self.cel1[:2] == 'bw':
            self.data_true = float(my_gui.inst_dmm.query(self.vosc2))
            self.data_error = self.data_true

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
                    if self.vosc2 == 'READ?':
                        if self.data_error > self.accur or self.data_error < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3
                    #elif self.vosc2 == ':MEAS:ITEM? VMAX':
                    else:
                        if self.data_true > self.accur or self.data_true < -self.accur:
                            cell.fill = my_gui.colour_cell
                            self.tree2_img = my_gui.img3

        my_gui.inst_dmm.write(':ACQ:TYPE NORM')

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        if my_gui.a1[1] == 'ADS-222':
            my_gui.lb2.insert('end', f"Канал №{self.vosc1.split(':')[1][-1]}")
        else:
            my_gui.lb2.insert('end', f"Канал №{self.vosc1.split(':')[0][-1]}")
        my_gui.lb2.insert('end', f'Установлено: {self.vfluk}')
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2
        my_gui.query(self.vfluk)
        if my_gui.a1[1] == 'ADS-222':
            my_gui.dev.write(3, self.vosc1, 1000)
        else:
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
        elif my_gui.a1[1] == 'ADS-222':
            self.call_ads()
        elif my_gui.a1[1] == 'MSO5204':
            self.call_rigol_mso()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.vfluk.split(' ')[1],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
        my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()

class Call_DSO9000(Thread):
    """Class callibration oscilloscope DSO9104, MSO9404A, DSOX92004A, 'DSOZ594A'"""
    def __init__(self, vfluk, vosc1, vosc2, vdmm, cel1, cel2, cel3, cel4, accur):
        #Thread.__init__(self)
        super(Call_DSO9000, self).__init__()
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

    def aver_on(self):
        if my_gui.a1[1] == 'MSO-X6004A':
            my_gui.inst_dmm.write(':ACQ:TYPE AVER; :ACQ:COUN 16')
        else:
            my_gui.inst_dmm.write(':ACQ:AVER ON; :ACQ:COUN 16')

    def aver_off(self):
        if my_gui.a1[1] == 'MSO-X6004A':
            my_gui.inst_dmm.write(':ACQ:TYPE NORM')
        else:
            my_gui.inst_dmm.write(':ACQ:AVER OFF')

    def call_dso_9(self):
        time.sleep(1)
        self.aver_on()
        time.sleep(3)
        if self.vosc2 == ':MEAS:VAV?':
            self.meas_aver()

        if self.cel1[0:4] == 'vofs':
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS {self.vosc2}')
            self.meas_aver()
            time.sleep(1)
            self.aver_off() # измерения с 0 смещением и выкл выходом
            time.sleep(1)
            my_gui.inst_dmm.write(f'CHAN{self.vosc1[4]}:OFFS 0')
            if my_gui.a1[1] in ('DSOX92004A', 'DSOZ594A'):
                my_gui.inst_dmm.write(':CAL:OUTP DC,0')
            else:
                my_gui.query('OUTP:STAT OFF')
            time.sleep(1)
            self.aver_on()
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

        self.aver_off()

    def run(self):
        sem.acquire()
        my_gui.statusbar["text"] = f'Статус: работа   Прогресс: {my_gui.count} из {my_gui.cnt()[my_gui.a1[1]]}'
        my_gui.lb2.delete(0, 'end')
        my_gui.lb2.insert('end', f"Канал №{self.vosc1.split(':')[0][-1]}")
        my_gui.lb2.insert('end', f'Установлено: {self.vfluk}')
        my_gui.lb2.see('end')
        self.tree2_img = my_gui.img2
        if my_gui.a1[1] in ('DSOX92004A', 'DSOZ594A'):
            my_gui.inst_dmm.write(self.vfluk) # выход Cal out
        else:
            my_gui.query(self.vfluk)
            if self.vosc2 == ':MEAS:VAV?' or self.cel1[0:4] == 'vofs' or self.vosc2[:11] == (':MEAS:VRMS?'):
                my_gui.query("OUTP:STAT ON")
        my_gui.inst_dmm.write(self.vosc1)

        if my_gui.a1[1] in ('MSO-X6004A', 'DSO9104A', 'MSO9404A', 'DSOX92004A', 'DSOZ594A'):
            self.call_dso_9()

        my_gui.tree2.insert('', 0, text='', image=self.tree2_img, values=(self.vfluk.split(' ')[1],round(self.data_true,4),round(self.data_error,4),f'±{self.accur}'))
        my_gui.wb.save(f"{my_gui.folder_1}\\Protocol\\{my_gui.vardict_str['name_proc'].get()}")
        if my_gui.a1[1] in ('DSOX92004A', 'DSOZ594A'):
            my_gui.inst_dmm.write(':CAL:OUTP DC,0')
        else:
            my_gui.query("OUTP:STAT OFF")
        time.sleep(1)
        my_gui.progress1.step(1)
        my_gui.count += 1
        sem.release()

# ===============================================================================
class Supportfunc(Thread):
    def __init__(self, name):
        #Thread.__init__(self)
        super(Supportfunc, self).__init__()
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
        #Thread.__init__(self)
        super(Clear_merge, self).__init__()
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

#my_gui = MeasControlGUI()
