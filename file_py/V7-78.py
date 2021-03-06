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
    _thdmm = Call('dc', 'OUT 100 mV', 'CONF:VOLT:DC 0.1', 'dcv_3', 99.915, 'DET:BAND 20', 3.0, 100.0085)
    _thdmm = Call('dc', 'OUT -100 mV', 'CONF:VOLT:DC 0.1', 'dcv_4', -100.0085, 'DET:BAND 20', 3.0, -99.915)
    _thdmm = Call('dc', 'OUT 0.1 V', 'CONF:VOLT:DC 1.0', 'dcv_5', 0.09999, 'DET:BAND 20', 3.0, 0.10001)
    _thdmm = Call('dc', 'OUT 0.5 V', 'CONF:VOLT:DC 1.0', 'dcv_6', 0.49997, 'DET:BAND 20', 3.0, 0.50003)
    _thdmm = Call('dc', 'OUT 1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_7', 0.999953, 'DET:BAND 20', 3.0, 1.000047)
    _thdmm = Call('dc', 'OUT -1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_8', -1.000047, 'DET:BAND 20', 3.0, -0.999953)     
    _thdmm = Call('dc', 'OUT 1 V', 'CONF:VOLT:DC 10', 'dcv_9', 0.999915, 'DET:BAND 20', 3.0, 1.000085)
    _thdmm = Call('dc', 'OUT 5 V', 'CONF:VOLT:DC 10', 'dcv_10', 4.99981, 'DET:BAND 20', 3.0, 5.00019)
    _thdmm = Call('dc', 'OUT 10 V', 'CONF:VOLT:DC 10', 'dcv_11', 9.9996, 'DET:BAND 20', 3.0, 10.0004)
    _thdmm = Call('dc', 'OUT -10 V', 'CONF:VOLT:DC 10', 'dcv_12', -10.0004, 'DET:BAND 20', 3.0, -9.9996)
    _thdmm = Call('dc', 'OUT 10 V', 'CONF:VOLT:DC 100', 'dcv_13', 9.99895, 'DET:BAND 20', 3.0, 10.00105)
    _thdmm = Call('dc', 'OUT 50 V', 'CONF:VOLT:DC 100', 'dcv_14', 49.99715, 'DET:BAND 20', 3.0, 50.00285)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_15', 99.9949, 'DET:BAND 20', 4.0, 100.0051)
    _thdmm = Call('dc', 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv_16', -100.0051, 'DET:BAND 20', 4.0, -99.9949)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 1000', 'dcv_17', 99.9855, 'DET:BAND 20', 4.0, 100.0145)
    _thdmm = Call('dc', 'OUT 500 V', 'CONF:VOLT:DC 1000', 'dcv_18', 499.9675, 'DET:BAND 20', 4.0, 500.0325)
    _thdmm = Call('dc', 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_19', 999.945, 'DET:BAND 20', 4.0, 1000.055)
    _thdmm = Call('dc', 'OUT -1000 V', 'CONF:VOLT:DC 1000', 'dcv_20', -1000.055, 'DET:BAND 20', 8.0, -999.945)  
if self.acv_var.get() == 1:
    # ~0.1V
    _thdmm = Call('ac', 'OUT 10 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_1', 9.925, 'DET:BAND 3', 3.0, 10.075)
    _thdmm = Call('ac', 'OUT 10 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_2', 9.925, 'DET:BAND 20', 3.0, 10.046)
    _thdmm = Call('ac', 'OUT 10 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', 9.938, 'DET:BAND 20', 3.0, 10.062)
    _thdmm = Call('ac', 'OUT 10 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_4', 9.86, 'DET:BAND 20', 3.0, 10.14)
    _thdmm = Call('ac', 'OUT 50 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_5', 49.785, 'DET:BAND 3', 3.0, 50.215)
    _thdmm = Call('ac', 'OUT 50 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_6', 49.93, 'DET:BAND 20', 3.0, 50.07)
    _thdmm = Call('ac', 'OUT 50 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_7', 49.89, 'DET:BAND 20', 3.0, 50.11)
    _thdmm = Call('ac', 'OUT 50 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_8', 49.62, 'DET:BAND 20', 3.0, 50.38)
    _thdmm = Call('ac', 'OUT 50 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_9', 47.95, 'DET:BAND 20', 3.0, 52.05)
    _thdmm = Call('ac', 'OUT 100 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_10', 99.61, 'DET:BAND 3', 3.0, 100.39)
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_11', 99.9, 'DET:BAND 20', 3.0, 100.1)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_12', 99.83, 'DET:BAND 20', 3.0, 100.17)
    _thdmm = Call('ac', 'OUT 100 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_13', 99.32, 'DET:BAND 20', 3.0, 100.68)
    _thdmm = Call('ac', 'OUT 100 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_14', 95.95, 'DET:BAND 20', 3.0, 104.05)              
    _thdmm = Call('ac', 'OUT 100 mV, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_15', 99.62, 'DET:BAND 3', 3.0, 100.38)
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_16', 99.91, 'DET:BAND 20', 3.0, 100.09)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_17', 99.83, 'DET:BAND 20', 3.0, 100.17)
    _thdmm = Call('ac', 'OUT 100 mV, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_18', 99.32, 'DET:BAND 20', 3.0, 100.68)
    _thdmm = Call('ac', 'OUT 500 mV, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_19', 498.22, 'DET:BAND 3', 3.0, 501.78)
    _thdmm = Call('ac', 'OUT 500 mV, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_20', 499.67, 'DET:BAND 20', 3.0, 500.33)
    _thdmm = Call('ac', 'OUT 500 mV, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_21', 499.35, 'DET:BAND 20', 3.0, 500.65)
    _thdmm = Call('ac', 'OUT 500 mV, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_22', 496.92, 'DET:BAND 20', 3.0, 503.08)
    _thdmm = Call('ac', 'OUT 1 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_23', 0.99647, 'DET:BAND 3', 3.0, 1.00353)
    _thdmm = Call('ac', 'OUT 1 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_24', 0.99937, 'DET:BAND 20', 3.0, 1.00063)
    _thdmm = Call('ac', 'OUT 1 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_25', 0.99875, 'DET:BAND 20', 3.0, 1.00125)
    _thdmm = Call('ac', 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_26', 0.99392, 'DET:BAND 20', 3.0, 1.00608)
    _thdmm = Call('ac', 'OUT 1 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_27', 0.95995, 'DET:BAND 20', 3.0, 1.04005)               
    _thdmm = Call('ac', 'OUT 1 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_28', 0.9935, 'DET:BAND 3', 3.0, 1.0065)
    _thdmm = Call('ac', 'OUT 1 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_29', 0.9964, 'DET:BAND 20', 3.0, 1.0036)
    _thdmm = Call('ac', 'OUT 1 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_30', 0.9938, 'DET:BAND 20', 3.0, 1.0062)
    _thdmm = Call('ac', 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_31', 0.986, 'DET:BAND 20', 3.0, 1.014)
    _thdmm = Call('ac', 'OUT 5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_32', 4.9795, 'DET:BAND 3', 3.0, 5.0205)
    _thdmm = Call('ac', 'OUT 5 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_33', 4.994, 'DET:BAND 20', 3.0, 5.006)
    _thdmm = Call('ac', 'OUT 5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_34', 4.989, 'DET:BAND 20', 3.0, 5.011)
    _thdmm = Call('ac', 'OUT 5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_35', 4.962, 'DET:BAND 20', 3.0, 5.038)
    _thdmm = Call('ac', 'OUT 10 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_36', 9.962, 'DET:BAND 3', 3.0, 10.038)
    _thdmm = Call('ac', 'OUT 10 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_37', 9.991, 'DET:BAND 20', 3.0, 10.009)
    _thdmm = Call('ac', 'OUT 10 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_38', 9.983, 'DET:BAND 20', 3.0, 10.017)
    _thdmm = Call('ac', 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_39', 9.932, 'DET:BAND 20', 3.0, 10.068)               
    _thdmm = Call('ac', 'OUT 10 V, 10 Hz', 'CONF:VOLT:AC 100.0', 'acv_40', 9.935, 'DET:BAND 3', 3.0, 10.065)
    _thdmm = Call('ac', 'OUT 10 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_41', 9.964, 'DET:BAND 20', 3.0, 10.036)
    _thdmm = Call('ac', 'OUT 10 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_42', 9.938, 'DET:BAND 20', 3.0, 10.062)
    _thdmm = Call('ac', 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv_43', 9.86, 'DET:BAND 20', 3.0, 10.14)
    _thdmm = Call('ac', 'OUT 50 V, 45 Hz', 'CONF:VOLT:AC 100.0', 'acv_44', 49.795, 'DET:BAND 3', 3.0, 50.205)
    _thdmm = Call('ac', 'OUT 50 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_45', 49.94, 'DET:BAND 20', 3.0, 50.06)
    _thdmm = Call('ac', 'OUT 100 V, 45 Hz', 'CONF:VOLT:AC 100.0', 'acv_48', 99.62, 'DET:BAND 3', 3.0, 100.38)
    _thdmm = Call('ac', 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_49', 99.91, 'DET:BAND 20', 3.0, 100.09)                       
    _thdmm = Call('ac', 'OUT 100 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv_52', 99.35, 'DET:BAND 3', 3.0, 100.65)
    _thdmm = Call('ac', 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv_53', 99.64, 'DET:BAND 20', 3.0, 100.36)       
    _thdmm = Call('ac', 'OUT 500 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv_56', 497.95, 'DET:BAND 3', 3.0, 502.05)
    _thdmm = Call('ac', 'OUT 500 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv_57', 499.4, 'DET:BAND 20', 3.0, 500.6)
    _thdmm = Call('ac', 'OUT 750 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv_60', 747.075, 'DET:BAND 3', 3.0, 752.925)
    _thdmm = Call('ac', 'OUT 750 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv_61', 749.25, 'DET:BAND 20', 3.0, 750.75)
    if self.b1[1] == '5522A': 
        _thdmm = Call('ac', 'OUT 50 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_46', 49.89, 'DET:BAND 20', 3.0, 50.11)
        _thdmm = Call('ac', 'OUT 50 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv_47', 49.62, 'DET:BAND 20', 3.0, 50.38)
        _thdmm = Call('ac', 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_50', 99.83, 'DET:BAND 20', 3.0, 100.17)
        _thdmm = Call('ac', 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv_51', 99.32, 'DET:BAND 20', 3.0, 100.68)
        _thdmm = Call('ac', 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 1000.0', 'acv_54', 99.38, 'DET:BAND 20', 3.0, 100.62)
        _thdmm = Call('ac', 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 1000.0', 'acv_55', 98.6, 'DET:BAND 20', 3.0, 101.4)
    # _thdmm = Call('ac', 'OUT 500 V, 50 kHz', 'CONF:VOLT:AC 1000', 'acv_58', 498.9, 'DET:BAND 20', 3.0, 501.1)
    # _thdmm = Call('ac', 'OUT 500 V, 100 kHz', 'CONF:VOLT:AC 1000', 'acv_59', 496.2, 'DET:BAND 20', 3.0, 503.8)
    # _thdmm = Call('ac', 'OUT 750 V, 50 kHz', 'CONF:VOLT:AC 1000', 'acv_62', 748.8, 'DET:BAND 20', 3.0, 751.4)
    # _thdmm = Call('ac', 'OUT 750 V, 100 kHz', 'CONF:VOLT:AC 1000', 'acv_63', 744.7, 'DET:BAND 20', 3.0, 755.3)
if self.f_var.get() == 1:
    _thdmm = Call('fr', 'OUT 1 V, 40.0 Hz', 'CONF:FREQ 40.0 Hz', 'f_1', 39.99599, 'DET:BAND 20', 3.0, 40.00401)
    _thdmm = Call('fr', 'OUT 1 V, 1.0 kHz', 'CONF:FREQ 1.0 kHz', 'f_2', 0.999899, 'DET:BAND 20', 3.0, 1.000101)
    _thdmm = Call('fr', 'OUT 1 V, 10.0 kHz', 'CONF:FREQ 10.0 kHz', 'f_3', 9.99899, 'DET:BAND 20', 3.0, 10.00101)        
    _thdmm = Call('fr', 'OUT 1 V, 100.0 kHz', 'CONF:FREQ 100.0 kHz', 'f_4', 99.9899, 'DET:BAND 20', 3.0, 100.0101)
    _thdmm = Call('fr', 'OUT 1 V, 300.0 kHz', 'CONF:FREQ 300.0 kHz', 'f_5', 299.9699, 'DET:BAND 20', 3.0, 300.0301)
if self.r2_var.get() == 1:
    _thdmm = Call('res2', 'OUT 0.1 kOHM', 'CONF:RES 1 KOHM', 'r2_1', 0.09989, 'DET:BAND 20', 3.0, 0.10011)
    _thdmm = Call('res2', 'OUT 0.5 kOHM', 'CONF:RES 1 KOHM', 'r2_2', 0.49985, 'DET:BAND 20', 3.0, 0.50015)
    _thdmm = Call('res2', 'OUT 1 kOHM', 'CONF:RES 1 KOHM', 'r2_3', 0.9998, 'DET:BAND 20', 3.0, 1.0002)
    _thdmm = Call('res2', 'OUT 1 kOHM', 'CONF:RES 10 KOHM', 'r2_4', 0.9989, 'DET:BAND 20', 3.0, 1.0011)
    _thdmm = Call('res2', 'OUT 5 kOHM', 'CONF:RES 10 KOHM', 'r2_5', 4.9985, 'DET:BAND 20', 3.0, 5.0015)
    _thdmm = Call('res2', 'OUT 10 kOHM', 'CONF:RES 10 KOHM', 'r2_6', 9.998, 'DET:BAND 20', 3.0, 10.002)
    _thdmm = Call('res2', 'OUT 10 kOHM', 'CONF:RES 100 KOHM', 'r2_7', 9.989, 'DET:BAND 20', 3.0, 10.011)
    _thdmm = Call('res2', 'OUT 50 kOHM', 'CONF:RES 100 KOHM', 'r2_8', 49.985, 'DET:BAND 20', 3.0, 50.015)
    _thdmm = Call('res2', 'OUT 100 kOHM', 'CONF:RES 100 KOHM', 'r2_9', 99.98, 'DET:BAND 20', 3.0, 100.02)
    _thdmm = Call('res2', 'OUT 0.1 MOHM', 'CONF:RES 1 MOHM', 'r2_10', 0.09998, 'DET:BAND 20', 3.0, 0.10002)
    _thdmm = Call('res2', 'OUT 0.5 MOHM', 'CONF:RES 1 MOHM', 'r2_11', 0.49994, 'DET:BAND 20', 3.0, 0.50006)
    _thdmm = Call('res2', 'OUT 1 MOHM', 'CONF:RES 1 MOHM', 'r2_12', 0.99989, 'DET:BAND 20', 3.0, 1.00011)
    _thdmm = Call('res2', 'OUT 1 MOHM', 'CONF:RES 10 MOHM', 'r2_13', 0.9995, 'DET:BAND 20', 3.0, 1.0005)
    _thdmm = Call('res2', 'OUT 5 MOHM', 'CONF:RES 10 MOHM', 'r2_14', 4.9979, 'DET:BAND 20', 3.0, 5.0021)
    _thdmm = Call('res2', 'OUT 10 MOHM', 'CONF:RES 10 MOHM', 'r2_15', 9.9959, 'DET:BAND 20', 3.0, 10.0041)
    _thdmm = Call('res2', 'OUT 10 MOHM', 'CONF:RES 100 MOHM', 'r2_16', 9.91, 'DET:BAND 20', 3.0, 10.09)
    _thdmm = Call('res2', 'OUT 50 MOHM', 'CONF:RES 100 MOHM', 'r2_17', 49.59, 'DET:BAND 20', 3.0, 50.41)
    _thdmm = Call('res2', 'OUT 100 MOHM', 'CONF:RES 100 MOHM', 'r2_18', 99.19, 'DET:BAND 20', 3.0, 100.81)
if self.r4_var.get() == 1:
    _th = Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _thdmm = Call('res4', 'OUT 1 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 0.9959, 'DET:BAND 20', 3.0, 1.0041)
    _thdmm = Call('res4', 'OUT 10 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_2', 9.995, 'DET:BAND 20', 3.0, 10.005)
    _thdmm = Call('res4', 'OUT 50 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_3', 49.991, 'DET:BAND 20', 3.0, 50.009)
    _thdmm = Call('res4', 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_4', 99.986, 'DET:BAND 20', 3.0, 100.014)
if self.dci_var.get() == 1:
    _th = Message('Подключите провода\n для измерения тока')     
    _thdmm = Call('dci', 'OUT 1 mA', 'CONF:CURR:DC 0.01', 'dci_1', 0.9993, 'DET:BAND 20', 3.0, 1.0007)
    _thdmm = Call('dci', 'OUT 5 mA', 'CONF:CURR:DC 0.01', 'dci_2', 4.9973, 'DET:BAND 20', 3.0, 5.0027)
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.01', 'dci_3', 9.9948, 'DET:BAND 20', 3.0, 10.0052)
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.1', 'dci_4', 9.9945, 'DET:BAND 20', 3.0, 10.0055)
    _thdmm = Call('dci', 'OUT 50 mA', 'CONF:CURR:DC 0.1', 'dci_5', 49.9745, 'DET:BAND 20', 3.0, 50.0255)
    _thdmm = Call('dci', 'OUT 100 mA', 'CONF:CURR:DC 0.1', 'dci_6', 99.9495, 'DET:BAND 20', 3.0, 100.0505)
    _thdmm = Call('dci', 'OUT 0.1 A', 'CONF:CURR:DC 1.0', 'dci_7', 0.09989, 'DET:BAND 20', 3.0, 0.10011)
    _thdmm = Call('dci', 'OUT 0.5 A', 'CONF:CURR:DC 1.0', 'dci_8', 0.49949, 'DET:BAND 20', 3.0, 0.50051)
    _thdmm = Call('dci', 'OUT 1 A', 'CONF:CURR:DC 1.0', 'dci_9', 0.99899, 'DET:BAND 20', 3.0, 1.00101)
    _thdmm = Call('dci', 'OUT 0.3 A', 'CONF:CURR:DC 3.0', 'dci_10', 0.29944, 'DET:BAND 20', 3.0, 0.30056)
    _thdmm = Call('dci', 'OUT 1 A', 'CONF:CURR:DC 3.0', 'dci_11', 0.9986, 'DET:BAND 20', 3.0, 1.0014)
    _thdmm = Call('dci', 'OUT 2 A', 'CONF:CURR:DC 3.0', 'dci_12', 1.9974, 'DET:BAND 20', 3.0, 2.0026)
if self.aci_var.get() == 1:   
    _thdmm = Call('aci', 'OUT 0.1 A, 10 Hz', 'CONF:CURR:AC 1', 'aci_1', 0.0957, 'DET:BAND 3', 3.0, 0.1043)
    _thdmm = Call('aci', 'OUT 0.5 A, 10 Hz', 'CONF:CURR:AC 1', 'aci_2', 0.4945, 'DET:BAND 3', 3.0, 0.5055)
    _thdmm = Call('aci', 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 1', 'aci_3', 0.993, 'DET:BAND 3', 3.0, 1.007)
    _thdmm = Call('aci', 'OUT 0.1 A, 1 kHz', 'CONF:CURR:AC 1', 'aci_4', 0.0959, 'DET:BAND 20', 3.0, 0.1041)
    _thdmm = Call('aci', 'OUT 0.5 A, 1 kHz', 'CONF:CURR:AC 1', 'aci_5', 0.4955, 'DET:BAND 20', 3.0, 0.5045)
    _thdmm = Call('aci', 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 1', 'aci_6', 0.995, 'DET:BAND 3', 20.0, 1.005)            
    _thdmm = Call('aci', 'OUT 0.1 A, 5 kHz', 'CONF:CURR:AC 1', 'aci_7', 0.0959, 'DET:BAND 20', 3.0, 0.1041)
    _thdmm = Call('aci', 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1', 'aci_8', 0.4955, 'DET:BAND 20', 3.0, 0.5045)
    _thdmm = Call('aci', 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 1', 'aci_9', 0.995, 'DET:BAND 20', 3.0, 1.005)
    _thdmm = Call('aci', 'OUT 0.3 A, 10 Hz', 'CONF:CURR:AC 3', 'aci_10', 0.23895, 'DET:BAND 3', 3.0, 0.36105)
    _thdmm = Call('aci', 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 3', 'aci_11', 0.9365, 'DET:BAND 3', 3.0, 1.0635)
    _thdmm = Call('aci', 'OUT 0.3 A, 1 kHz', 'CONF:CURR:AC 3', 'aci_13', 0.23955, 'DET:BAND 20', 3.0, 0.36045)
    _thdmm = Call('aci', 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 3', 'aci_14', 0.9385, 'DET:BAND 20', 3.0, 1.0615)
    _thdmm = Call('aci', 'OUT 2.5 A, 1 kHz', 'CONF:CURR:AC 3', 'aci_15', 2.43625, 'DET:BAND 20', 5.0, 2.56375)            
    _thdmm = Call('aci', 'OUT 0.3 A, 5 kHz', 'CONF:CURR:AC 3', 'aci_16', 0.23955, 'DET:BAND 20', 3.0, 0.36045)
    _thdmm = Call('aci', 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 3', 'aci_17', 0.9385, 'DET:BAND 20', 3.0, 1.0615)
    if self.b1[1] == '5522A':
        _thdmm = Call('aci', 'OUT 2.5 A, 10 Hz', 'CONF:CURR:AC 3', 'aci_12', 2.43125, 'DET:BAND 3', 5.0, 2.56875)
        _thdmm = Call('aci', 'OUT 2.5 A, 5 kHz', 'CONF:CURR:AC 3', 'aci_18', 2.43625, 'DET:BAND 20', 5.0, 2.56375)

_th = Message('Калибровка завершена')
_th = Clear_merge()
_th = Reset()
