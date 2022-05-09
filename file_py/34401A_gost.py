#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
_th = Reset()
if self.dcv_var.get() == 1 or self.acv_var.get() == 1 or self.f_var.get() == 1 or self.r2_var.get():
    _th = Message('Подключите провода к клеммам измерения напряжения, частоты или сопротивления')
elif self.aci_var.get() == 1:
    _th = Message('Подключите провода для измерения тока')
if self.dcv_var.get() == 1:
    _thdmm = Call('dc', 'OUT 10 mV', 'CONF:VOLT:DC 0.1', 'dcv_1', 9.996, 'DET:BAND 20', 3.0, 10.004)
    _thdmm = Call('dc', 'OUT 50 mV', 'CONF:VOLT:DC 0.1', 'dcv_2', 49.994, 'DET:BAND 20', 3.0, 50.006) 
    _thdmm = Call('dc', 'OUT 100 mV', 'CONF:VOLT:DC 0.1', 'dcv_3', 99.9915, 'DET:BAND 20', 3.0, 100.0085)
    _thdmm = Call('dc', 'OUT -100 mV', 'CONF:VOLT:DC 0.1', 'dcv_4', -100.0085, 'DET:BAND 20', 3.0, -99.9915)
    _thdmm = Call('dc', 'OUT 0.1 V', 'CONF:VOLT:DC 1.0', 'dcv_5', 0.099989, 'DET:BAND 20', 3.0, 0.1000011)
    _thdmm = Call('dc', 'OUT 0.5 V', 'CONF:VOLT:DC 1.0', 'dcv_6', 0.499973, 'DET:BAND 20', 3.0, 0.500027)
    _thdmm = Call('dc', 'OUT 1 V', 'CONF:VOLT:DC 1.0', 'dcv_7', 0.999953, 'DET:BAND 20', 3.0, 1.000047)
    _thdmm = Call('dc', 'OUT -1 V', 'CONF:VOLT:DC 1.0', 'dcv_8', -1.000047, 'DET:BAND 20', 3.0, -0.999953)
    _thdmm = Call('dc', 'OUT 1 V', 'CONF:VOLT:DC 10', 'dcv_9', 0.999915, 'DET:BAND 20', 3.0, 1.000085)
    _thdmm = Call('dc', 'OUT 5 V', 'CONF:VOLT:DC 10', 'dcv_10', 4.999775, 'DET:BAND 20', 3.0, 5.000225)
    _thdmm = Call('dc', 'OUT 10 V', 'CONF:VOLT:DC 10', 'dcv_11', 9.9996, 'DET:BAND 20', 3.0, 10.0004)
    _thdmm = Call('dc', 'OUT -10 V', 'CONF:VOLT:DC 10', 'dcv_12', -10.0004, 'DET:BAND 20', 3.0, -9.9996)
    _thdmm = Call('dc', 'OUT 10 V', 'CONF:VOLT:DC 100', 'dcv_13', 9.99955, 'DET:BAND 20', 3.0, 10.00045)
    _thdmm = Call('dc', 'OUT 50 V', 'CONF:VOLT:DC 100', 'dcv_14', 49.99715, 'DET:BAND 20', 4.0, 50.00285)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_15', 99.9949, 'DET:BAND 20', 4.0, 100.0051)
    _thdmm = Call('dc', 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv_16', -100.0051, 'DET:BAND 20', 4.0, -99.9949)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 1000', 'dcv_17', 99.9855, 'DET:BAND 20', 4.0, 100.0145)
    _thdmm = Call('dc', 'OUT 500 V', 'CONF:VOLT:DC 1000', 'dcv_18', 499.9675, 'DET:BAND 20', 4.0, 500.0325)
    _thdmm = Call('dc', 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_19', 999.945, 'DET:BAND 20', 4.0, 1000.055)
    _thdmm = Call('dc', 'OUT -1000 V', 'CONF:VOLT:DC 1000', 'dcv_20', -1000.055, 'DET:BAND 20', 8.0, -999.945)
if self.acv_var.get() == 1:
    _thdmm = Call('ac', 'OUT 10 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_1', 9.925, 'DET:BAND 3', 4.0, 10.075)
    _thdmm = Call('ac', 'OUT 10 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_2', 9.954, 'DET:BAND 20', 4.0, 10.046)
    _thdmm = Call('ac', 'OUT 10 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', 9.938, 'DET:BAND 20', 4.0, 10.062)
    _thdmm = Call('ac', 'OUT 10 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_4', 9.86, 'DET:BAND 20', 4.0, 10.14)
    _thdmm = Call('ac', 'OUT 50 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_5', 49.785, 'DET:BAND 3', 4.0, 50.215)
    _thdmm = Call('ac', 'OUT 50 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_6', 49.93, 'DET:BAND 20', 4.0, 50.07)
    _thdmm = Call('ac', 'OUT 50 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_7', 49.89, 'DET:BAND 20', 4.0, 50.11)
    _thdmm = Call('ac', 'OUT 50 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_8', 49.62, 'DET:BAND 20', 4.0, 50.38)
    _thdmm = Call('ac', 'OUT 50 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_9', 47.5, 'DET:BAND 20', 4.0, 52.5)   
    _thdmm = Call('ac', 'OUT 100 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_10', 99.61, 'DET:BAND 3', 4.0, 100.39)
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_11', 99.9, 'DET:BAND 20', 4.0, 100.1)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_12', 99.83, 'DET:BAND 20', 4.0, 100.17)
    _thdmm = Call('ac', 'OUT 100 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_13', 99.32, 'DET:BAND 20', 4.0, 100.68)
    _thdmm = Call('ac', 'OUT 100 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_14', 95.5, 'DET:BAND 20', 4.0, 104.5)
    _thdmm = Call('ac', 'OUT 100 mV, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_15', 99.35, 'DET:BAND 3', 4.0, 100.65)
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_16', 99.64, 'DET:BAND 20', 4.0, 100.36)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_17', 99.38, 'DET:BAND 20', 4.0, 100.62)
    _thdmm = Call('ac', 'OUT 100 mV, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_18', 98.6, 'DET:BAND 20', 4.0, 101.4)
    _thdmm = Call('ac', 'OUT 100 mV, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_19', 91, 'DET:BAND 20', 4.0, 109)
    _thdmm = Call('ac', 'OUT 500 mV, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_20', 497.95, 'DET:BAND 3', 4.0, 502.05)
    _thdmm = Call('ac', 'OUT 500 mV, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_21', 499.4, 'DET:BAND 20', 4.0, 500.6)
    _thdmm = Call('ac', 'OUT 500 mV, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_22', 498.9, 'DET:BAND 20', 4.0, 501.1)
    _thdmm = Call('ac', 'OUT 500 mV, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_23', 496.2, 'DET:BAND 20', 4.0, 503.8)
    _thdmm = Call('ac', 'OUT 500 mV, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_24', 475, 'DET:BAND 20', 4.0, 525)   
    _thdmm = Call('ac', 'OUT 1.0 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_25', 0.9962, 'DET:BAND 3', 4.0, 1.0038)
    _thdmm = Call('ac', 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_26', 0.9991, 'DET:BAND 20', 4.0, 1.0009)
    _thdmm = Call('ac', 'OUT 1.0 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_27', 0.9983, 'DET:BAND 20', 4.0, 1.0017)
    _thdmm = Call('ac', 'OUT 1.0 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_28', 0.9932, 'DET:BAND 20', 4.0, 1.0068)
    _thdmm = Call('ac', 'OUT 1.0 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_29', 0.955, 'DET:BAND 20', 4.0, 1.045)
    _thdmm = Call('ac', 'OUT 1 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_30', 0.9935, 'DET:BAND 3', 4.0, 1.0065)
    _thdmm = Call('ac', 'OUT 1 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_31', 0.9964, 'DET:BAND 20', 4.0, 1.0036)
    _thdmm = Call('ac', 'OUT 1 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_32', 0.9938, 'DET:BAND 20', 4.0, 1.0062)
    _thdmm = Call('ac', 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_33', 0.986, 'DET:BAND 20', 4.0, 1.014)
    _thdmm = Call('ac', 'OUT 5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_34', 4.9795, 'DET:BAND 3', 4.0, 5.0205)
    _thdmm = Call('ac', 'OUT 5 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_35', 4.994, 'DET:BAND 20', 4.0, 5.006)
    _thdmm = Call('ac', 'OUT 5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_36', 4.989, 'DET:BAND 20', 4.0, 5.011)
    _thdmm = Call('ac', 'OUT 5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_37', 4.962, 'DET:BAND 20', 4.0, 5.038)
    _thdmm = Call('ac', 'OUT 10.0 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_38', 9.962, 'DET:BAND 3', 4.0, 10.038)
    _thdmm = Call('ac', 'OUT 10.0 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_39', 9.991, 'DET:BAND 20', 4.0, 10.009)
    _thdmm = Call('ac', 'OUT 10.0 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_40', 9.983, 'DET:BAND 20', 4.0, 10.017)
    _thdmm = Call('ac', 'OUT 10.0 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_41', 9.932, 'DET:BAND 203', 4.0, 10.068)
    _thdmm = Call('ac', 'OUT 10 V, 10 Hz', 'CONF:VOLT:AC 100', 'acv_42', 9.935, 'DET:BAND 3', 4.0, 10.065)
    _thdmm = Call('ac', 'OUT 10 V, 1 kHz', 'CONF:VOLT:AC 100', 'acv_43', 9.964, 'DET:BAND 20', 4.0, 10.036)
    _thdmm = Call('ac', 'OUT 10 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_44', 9.938, 'DET:BAND 20', 4.0, 10.062)
    _thdmm = Call('ac', 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_45', 9.86, 'DET:BAND 20', 4.0, 10.14)    
    _thdmm = Call('ac', 'OUT 30 V, 10 Hz', 'CONF:VOLT:AC 100', 'acv_46', 29.795, 'DET:BAND 3', 4.0, 30.205)    
    _thdmm = Call('ac', 'OUT 30 V, 1 kHz', 'CONF:VOLT:AC 100', 'acv_47', 29.94, 'DET:BAND 20', 4.0, 30.06)
    _thdmm = Call('ac', 'OUT 30 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_48', 29.89, 'DET:BAND 20', 4.0, 30.11)
    _thdmm = Call('ac', 'OUT 30 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_49', 29.62, 'DET:BAND 20', 4.0, 30.38)    
    _thdmm = Call('ac', 'OUT 100 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_50', 99.62, 'DET:BAND 3', 4.0, 100.38)
    _thdmm = Call('ac', 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 100', 'acv_51', 99.91, 'DET:BAND 20', 4.0, 100.09)            
    _thdmm = Call('ac', 'OUT 100 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_54', 99.425, 'DET:BAND 3', 4.0, 100.575)
    _thdmm = Call('ac', 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 750', 'acv_55', 99.715, 'DET:BAND 20', 4.0, 100.285)            
    _thdmm = Call('ac', 'OUT 500 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_58', 498.025, 'DET:BAND 3', 4.0, 501.975)
    _thdmm = Call('ac', 'OUT 500 V, 1 kHz', 'CONF:VOLT:AC 750', 'acv_59', 499.475, 'DET:BAND 20', 4.0, 500.525)           
    _thdmm = Call('ac', 'OUT 750 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_62', 747.15, 'DET:BAND 3', 4.0, 752.85)
    _thdmm = Call('ac', 'OUT 750 V, 1 kHz', 'CONF:VOLT:AC 750', 'acv_63', 749.325, 'DET:BAND 20', 4.0, 750.675)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_52', 99.83, 'DET:BAND 20', 4.0, 100.17)
        _thdmm = Call('ac', 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_53', 99.32, 'DET:BAND 20', 4.0, 100.68)
        _thdmm = Call('ac', 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 750', 'acv_56', 99.505, 'DET:BAND 20', 4.0, 100.495)
        _thdmm = Call('ac', 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 750', 'acv_57', 98.8, 'DET:BAND 20', 4.0, 101.2)
        '''_thdmm = Call('ac', 'OUT 500 V, 50 kHz', 'CONF:VOLT:AC 750', 'acv_60', 499.025, 'DET:BAND 20', 4.0, 500.975)
        _thdmm = Call('ac', 'OUT 500 V, 100 kHz', 'CONF:VOLT:AC 750', 'acv_61', 496.4, 'DET:BAND 20', 4.0, 503.6)
        _thdmm = Call('ac', 'OUT 750 V, 50 kHz', 'CONF:VOLT:AC 750', 'acv_64', 748.725, 'DET:BAND 20', 4.0, 751.275)
        _thdmm = Call('ac', 'OUT 750 V, 100 kHz', 'CONF:VOLT:AC 750', 'acv_65', 744.9, 'DET:BAND 20', 4.0, 755.1)'''
if self.f_var.get() == 1:
    _thdmm = Call('fr', 'OUT 0.01 V, 10 Hz', 'CONF:FREQ 100.0 Hz', 'f_1', 9.995, 'DET:BAND 3', 4.0, 10.005)
    _thdmm = Call('fr', 'OUT 1.0 V, 50 kHz', 'CONF:FREQ 100.0 kHz', 'f_2', 49.985, 'DET:BAND 20', 4.0, 50.015)
    _thdmm = Call('fr', 'OUT 1.0 V, 300 kHz', 'CONF:FREQ 300.0 kHz', 'f_3', 299.970, 'DET:BAND 20', 4.0, 300.03)
if self.r2_var.get() == 1:    
    _thdmm = Call('res2', 'OUT 1 kOHM', 'CONF:RES 10 KOHM', 'r2_1', 0.9998, 'DET:BAND 20', 4.0, 1.0002)
    _thdmm = Call('res2', 'OUT 5 kOHM', 'CONF:RES 10 KOHM', 'r2_2', 4.9994, 'DET:BAND 20', 4.0, 5.0006)
    _thdmm = Call('res2', 'OUT 10 kOHM', 'CONF:RES 10 KOHM', 'r2_3', 9.9989, 'DET:BAND 20', 4.0, 10.0011)
    _thdmm = Call('res2', 'OUT 10 kOHM', 'CONF:RES 100 KOHM', 'r2_4', 9.998, 'DET:BAND 20', 4.0, 10.002)
    _thdmm = Call('res2', 'OUT 50 kOHM', 'CONF:RES 100 KOHM', 'r2_5', 49.994, 'DET:BAND 20', 4.0, 50.006)
    _thdmm = Call('res2', 'OUT 100 kOHM', 'CONF:RES 100 KOHM', 'r2_6', 99.989, 'DET:BAND 20', 4.0, 100.011)
    _thdmm = Call('res2', 'OUT 0.1 MOHM', 'CONF:RES 1 MOHM', 'r2_7', 0.09998, 'DET:BAND 20', 4.0, 0.10002)
    _thdmm = Call('res2', 'OUT 0.5 MOHM', 'CONF:RES 1 MOHM', 'r2_8', 0.49994, 'DET:BAND 20', 4.0, 0.50006)
    _thdmm = Call('res2', 'OUT 1 MOHM', 'CONF:RES 1 MOHM', 'r2_9', 0.99989, 'DET:BAND 20', 4.0, 1.00011)
    _thdmm = Call('res2', 'OUT 1 MOHM', 'CONF:RES 10 MOHM', 'r2_10', 0.9995, 'DET:BAND 20', 4.0, 1.0005)
    _thdmm = Call('res2', 'OUT 5 MOHM', 'CONF:RES 10 MOHM', 'r2_11', 4.9979, 'DET:BAND 20', 4.0, 5.0021)
    _thdmm = Call('res2', 'OUT 10 MOHM', 'CONF:RES 10 MOHM', 'r2_12', 9.9959, 'DET:BAND 20', 4.0, 10.0041)
    _thdmm = Call('res2', 'OUT 10 MOHM', 'CONF:RES 100 MOHM', 'r2_13', 9.91, 'DET:BAND 20', 4.0, 10.09)
    _thdmm = Call('res2', 'OUT 50 MOHM', 'CONF:RES 100 MOHM', 'r2_14', 49.59, 'DET:BAND 20', 4.0, 50.41)
    _thdmm = Call('res2', 'OUT 100 MOHM', 'CONF:RES 100 MOHM', 'r2_15', 99.19, 'DET:BAND 20', 4.0, 100.81)
if self.r4_var.get() == 1:
    _th = Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _thdmm = Call('res4', 'OUT 10 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 9.995, 'DET:BAND 20', 4.0, 10.005)
    _thdmm = Call('res4', 'OUT 50 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_2', 49.991, 'DET:BAND 20', 4.0, 50.009)
    _thdmm = Call('res4', 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_3', 99.986, 'DET:BAND 20', 4.0, 100.014)
    _thdmm = Call('res4', 'OUT 0.1 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_4', 0.09998, 'DET:BAND 20', 4.0, 0.10002)
    _thdmm = Call('res4', 'OUT 0.5 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_5', 0.49994, 'DET:BAND 20', 4.0, 0.50006)
    _thdmm = Call('res4', 'OUT 1 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_6', 0.99989, 'DET:BAND 20', 4.0, 1.00011)
if self.dci_var.get() == 1:
    _th = Message('Подключите провода для измерения тока')
    _thdmm = Call('dci', 'OUT 1 mA', 'CONF:CURR:DC 0.01', 'dci_1', 0.9975, 'DET:BAND 20', 4.0, 1.0025)
    _thdmm = Call('dci', 'OUT 5 mA', 'CONF:CURR:DC 0.01', 'dci_2', 4.9955, 'DET:BAND 20', 4.0, 5.0045)
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.01', 'dci_3', 9.993, 'DET:BAND 20', 4.0, 10.007)
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.1', 'dci_4', 9.99, 'DET:BAND 20', 4.0, 10.01)
    _thdmm = Call('dci', 'OUT 50 mA', 'CONF:CURR:DC 0.1', 'dci_5', 49.97, 'DET:BAND 20', 4.0, 50.03)
    _thdmm = Call('dci', 'OUT 100 mA', 'CONF:CURR:DC 0.1', 'dci_6', 99.945, 'DET:BAND 20', 4.0, 100.055)
    _thdmm = Call('dci', 'OUT 0.1 A', 'CONF:CURR:DC 1.0', 'dci_7', 0.0998, 'DET:BAND 20', 4.0, 0.1002)
    _thdmm = Call('dci', 'OUT 0.5 A', 'CONF:CURR:DC 1.0', 'dci_8', 0.4994, 'DET:BAND 20', 4.0, 0.5006)
    _thdmm = Call('dci', 'OUT 1 A', 'CONF:CURR:DC 1.0', 'dci_9', 0.9989, 'DET:BAND 20', 4.0, 1.0011)
    _thdmm = Call('dci', 'OUT 0.3 A', 'CONF:CURR:DC 3.0', 'dci_10', 0.29904, 'DET:BAND 20', 4.0, 0.30096)
    _thdmm = Call('dci', 'OUT 1 A', 'CONF:CURR:DC 3.0', 'dci_11', 0.9982, 'DET:BAND 20', 4.0, 1.0018)
    _thdmm = Call('dci', 'OUT 2.5 A', 'CONF:CURR:DC 3.0', 'dci_12', 2.4964, 'DET:BAND 20', 4.0, 2.5036)
if self.aci_var.get() == 1:
    _thdmm = Call('aci', 'OUT 0.1 A, 10 Hz', 'CONF:CURR:AC 1.0', 'aci_1', 0.0993, 'DET:BAND 3', 4.0, 0.1007)
    _thdmm = Call('aci', 'OUT 0.1 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_2', 0.0995, 'DET:BAND 20', 4.0, 0.1005)
    _thdmm = Call('aci', 'OUT 0.1 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_3', 0.0995, 'DET:BAND 20', 4.0, 0.1005)
    _thdmm = Call('aci', 'OUT 0.5 A, 10 Hz', 'CONF:CURR:AC 1.0', 'aci_4', 0.4981, 'DET:BAND 3', 4.0, 0.5015)
    _thdmm = Call('aci', 'OUT 0.5 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_5', 0.4991, 'DET:BAND 20', 4.0, 0.5009)
    _thdmm = Call('aci', 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_6', 0.4991, 'DET:BAND 20', 4.0, 0.5009)
    _thdmm = Call('aci', 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 1.0', 'aci_7', 0.9966, 'DET:BAND 3', 4.0, 1.0034)
    _thdmm = Call('aci', 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_8', 0.9986, 'DET:BAND 20', 4.0, 1.0014)
    _thdmm = Call('aci', 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_9', 0.9986, 'DET:BAND 20', 4.0, 1.0014)
    _thdmm = Call('aci', 'OUT 0.3 A, 10 Hz', 'CONF:CURR:AC 3.0', 'aci_10', 0.29715, 'DET:BAND 3', 4.0, 0.30285)
    _thdmm = Call('aci', 'OUT 0.3 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_11', 0.29775, 'DET:BAND 20', 4.0, 0.30225)
    _thdmm = Call('aci', 'OUT 0.3 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_12', 0.29775, 'DET:BAND 20', 4.0, 0.30225)
    _thdmm = Call('aci', 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 3.0', 'aci_13', 0.9947, 'DET:BAND 3', 4.0, 1.0053)
    _thdmm = Call('aci', 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_14', 0.9979, 'DET:BAND 20', 4.0, 1.0021)
    _thdmm = Call('aci', 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_15', 0.9979, 'DET:BAND 20', 4.0, 1.0021)
    _thdmm = Call('aci', 'OUT 2.5 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_17', 2.49445, 'DET:BAND 20', 5.0, 2.50555)
    if self.b1[1] == '5522A':
        _thdmm = Call('aci', 'OUT 2.5 A, 10 Hz', 'CONF:CURR:AC 3.0', 'aci_16', 2.48945, 'DET:BAND 3', 5.0, 2.51055)
        _thdmm = Call('aci', 'OUT 2.5 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_18', 2.49445, 'DET:BAND 20', 5.0, 2.50555)

_th = Message('Калибровка завершена')
_th = Clear_merge()
_th = Reset()