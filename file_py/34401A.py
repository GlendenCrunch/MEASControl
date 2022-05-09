#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
_th = Reset()
if self.dcv_var.get() == 1 or self.acv_var.get() == 1 or self.f_var.get() == 1 or self.r2_var.get():
    _th = Message('Подключите провода к клеммам измерения напряжения, частоты или сопротивления')
elif self.aci_var.get() == 1:
    _th = Message('Подключите провода для измерения тока')
if self.dcv_var.get() == 1:     
    _thdmm = Call('dc', 'OUT 100 mV', 'CONF:VOLT:DC 0.1', 'dcv_1', 99.9915, 'DET:BAND 20', 3.0, 100.0085)
    _thdmm = Call('dc', 'OUT -100 mV', 'CONF:VOLT:DC 0.1', 'dcv_2', -100.0085, 'DET:BAND 20', 3.0, -99.9915)
    _thdmm = Call('dc', 'OUT 1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_3', 0.999953, 'DET:BAND 20', 3.0, 1.000047)
    _thdmm = Call('dc', 'OUT -1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_4', -1.000047, 'DET:BAND 20', 3.0, -0.999953)
    _thdmm = Call('dc', 'OUT 10.0 V', 'CONF:VOLT:DC 10', 'dcv_5', 9.9996, 'DET:BAND 20', 3.0, 10.004)
    _thdmm = Call('dc', 'OUT -10.0 V', 'CONF:VOLT:DC 10', 'dcv_6', -10.004, 'DET:BAND 20', 3.0, -9.9996)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_7', 99.9949, 'DET:BAND 20', 5.0, 100.0051)
    _thdmm = Call('dc', 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv_8', -100.0051, 'DET:BAND 20', 5.0, -99.9949)
    _thdmm = Call('dc', 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_9', 999.945, 'DET:BAND 20', 5.0, 1000.055)
    _thdmm = Call('dc', 'OUT -1000 V', 'CONF:VOLT:DC 1000', 'dcv_10', -1000.055, 'DET:BAND 20', 8.0, -999.945)
if self.acv_var.get() == 1:
    _thdmm = Call('ac', 'OUT 10 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_1', 9.954, 'DET:BAND 20', 6.0, 10.046)
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_2', 99.9, 'DET:BAND 20', 5.0, 100.1)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', 99.83, 'DET:BAND 20', 5.0, 100.17)
    _thdmm = Call('ac', 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_4', 0.9999, 'DET:BAND 20', 5.0, 1.0001)
    _thdmm = Call('ac', 'OUT 1.0 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_5', 0.9983, 'DET:BAND 20', 5.0, 1.0017)
    _thdmm = Call('ac', 'OUT 10.0 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_6', 9.991, 'DET:BAND 3', 8.0, 10.009)  
    _thdmm = Call('ac', 'OUT 10.0 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_7', 9.991, 'DET:BAND 20', 5.0, 10.009)
    _thdmm = Call('ac', 'OUT 10.0 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_8', 9.983, 'DET:BAND 20', 5.0, 10.017)
    _thdmm = Call('ac', 'OUT 100.0 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_9', 99.91, 'DET:BAND 20', 5.0, 100.09)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 'OUT 100.0 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_10', 99.83, 'DET:BAND 20', 5.0, 100.17)
    else:
        _thdmm = Call('ac', 'OUT 100.0 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv_10', 99.83, 'DET:BAND 20', 5.0, 100.17)  
    _thdmm = Call('ac', 'OUT 750.0 V, 1 kHz', 'CONF:VOLT:AC 750.0', 'acv_11', 749.375, 'DET:BAND 3', 5.0, 750.625) 
    _thdmm = Call('ac', 'OUT 750.0 V, 10 kHz', 'CONF:VOLT:AC 750.0', 'acv_12', 748.725, 'DET:BAND 20', 5.0, 751.275)
if self.f_var.get() == 1:
    _thdmm = Call('fr', 'OUT 0.01 V, 100.0 Hz', 'CONF:FREQ 100.0 Hz', 'f_1', 99.9, 'DET:BAND 20', 4.0, 100.1)
    _thdmm = Call('fr', 'OUT 1.0 V, 100.0 kHz', 'CONF:FREQ 100.0 kHz', 'f_2', 99.99, 'DET:BAND 20', 4.0, 100.01)
if self.r2_var.get() == 1:
    _thdmm = Call('res2', 'OUT 1 MOHM', 'CONF:RES 1 MOHM', 'r2_1', 0.99989, 'DET:BAND 20', 4.0, 1.00011)
    _thdmm = Call('res2', 'OUT 10 MOHM', 'CONF:RES 10 MOHM', 'r2_2', 9.9959, 'DET:BAND 20', 4.0, 10.0041)
    _thdmm = Call('res2', 'OUT 100 MOHM', 'CONF:RES 100 MOHM', 'r2_3', 99.19, 'DET:BAND 20', 4.0, 100.81)
if self.r4_var.get() == 1:
    _th = Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')       
    _thdmm = Call('res4', 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 99.986, 'DET:BAND 20', 4.0, 100.014)
    _thdmm = Call('res4', 'OUT 1 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_2', 0.9999, 'DET:BAND 20', 4.0, 1.0001)
    _thdmm = Call('res4', 'OUT 10 kOHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_3', 9.9989, 'DET:BAND 20', 4.0, 10.0011)
    _thdmm = Call('res4', 'OUT 100 kOHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_4', 99.989, 'DET:BAND 20', 4.0, 100.011)
if self.dci_var.get() == 1:
    _th = Message('Подключите провода\n для измерения тока')
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.01', 'dci_1', 9.993, 'DET:BAND 20', 4.0, 10.007)
    _thdmm = Call('dci', 'OUT 100 mA', 'CONF:CURR:DC 0.1', 'dci_2', 99.945, 'DET:BAND 20', 4.0, 100.055)
    _thdmm = Call('dci', 'OUT 1.0 A', 'CONF:CURR:DC 1.0', 'dci_3', 0.9989, 'DET:BAND 20', 4.0, 1.0011)
    _thdmm = Call('dci', 'OUT 2.0 A', 'CONF:CURR:DC 3.0', 'dci_4', 1.997, 'DET:BAND 20', 4.0, 2.003)
if self.aci_var.get() == 1:
    _thdmm = Call('aci', 'OUT 1.0 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_1', 0.9986, 'DET:BAND 20', 4.0, 1.0014)
    _thdmm = Call('aci', 'OUT 2.0 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_2', 1.9952, 'DET:BAND 20', 4.0, 2.0048)

_th = Message('Калибровка завершена')
_th = Clear_merge()
_th = Reset()
