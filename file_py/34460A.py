#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
_th = Reset()
if self.dcv_var.get() == 1 or self.acv_var.get() == 1 or self.f_var.get() == 1 or self.r2_var.get():
    _th = Message('Подключите провода к клеммам измерения напряжения, частоты или сопротивления')
elif self.aci_var.get() == 1:
    _th = Message('Подключите провода для измерения тока')
if self.dcv_var.get() == 1:       
    _thdmm = Call('dc', 'OUT 100 mV', 'CONF:VOLT:DC 0.1', 'dcv_1', 99.9845, 'DET:BAND 20', 3.0, 100.0155)
    _thdmm = Call('dc', 'OUT -100 mV', 'CONF:VOLT:DC 0.1', 'dcv_2', -100.0155, 'DET:BAND 20', 3.0, -99.9845)
    _thdmm = Call('dc', 'OUT 1 V', 'CONF:VOLT:DC 1.0', 'dcv_3', 0.99991, 'DET:BAND 20', 3.0, 1.00009)
    _thdmm = Call('dc', 'OUT -1 V', 'CONF:VOLT:DC 1.0', 'dcv_4', -1.00009, 'DET:BAND 20', 3.0, -0.99991)
    _thdmm = Call('dc', 'OUT 4 V', 'CONF:VOLT:DC 10', 'dcv_5', 3.99965, 'DET:BAND 20', 3.0, 4.00035)
    _thdmm = Call('dc', 'OUT 10 V', 'CONF:VOLT:DC 10', 'dcv_6', 9.9992, 'DET:BAND 20', 3.0, 10.0008)
    _thdmm = Call('dc', 'OUT -10 V', 'CONF:VOLT:DC 10', 'dcv_7', -10.0008, 'DET:BAND 20', 3.0, -9.9992)
    _thdmm = Call('dc', 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_8', 99.9909, 'DET:BAND 20', 4.0, 100.0091)
    _thdmm = Call('dc', 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv_9', -100.0091, 'DET:BAND 20', 4.0, -99.9909)
    _thdmm = Call('dc', 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_10', 999.905, 'DET:BAND 20', 8.0, 1000.095)
    _thdmm = Call('dc', 'OUT -500 V', 'CONF:VOLT:DC 1000', 'dcv_11', -500.0525, 'DET:BAND 20', 8.0, -499.9475)
if self.acv_var.get() == 1:
    _thdmm = Call('ac', 'OUT 100 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_1', 99.88, 'DET:BAND 20', 5.0, 100.12)
    _thdmm = Call('ac', 'OUT 100 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_2', 99.8, 'DET:BAND 20', 5.0, 100.2)
    _thdmm = Call('ac', 'OUT 100 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', 95.5, 'DET:BAND 20', 5.0, 104.5)
    _thdmm = Call('ac', 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_4', 0.9988, 'DET:BAND 20', 5.0, 1.0012)
    _thdmm = Call('ac', 'OUT 1.0 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_5', 0.998, 'DET:BAND 20', 5.0, 1.002)
    _thdmm = Call('ac', 'OUT 1.0 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_6', 0.955, 'DET:BAND 20', 5.0, 1.045)    
    _thdmm = Call('ac', 'OUT 30 mV, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_7', 29.997, 'DET:BAND 200', 8.0, 30.003)
    _thdmm = Call('ac', 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_8', 0.9961, 'DET:BAND 20', 5.0, 1.0039)
    _thdmm = Call('ac', 'OUT 10.0 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_9', 9.988, 'DET:BAND 3', 5.0, 10.012)
    _thdmm = Call('ac', 'OUT 10.0 V, 100 Hz', 'CONF:VOLT:AC 10.0', 'acv_10', 9.988, 'DET:BAND 20', 5.0, 10.012)
    _thdmm = Call('ac', 'OUT 10.0 V, 20 kHz', 'CONF:VOLT:AC 10.0', 'acv_11', 9.988, 'DET:BAND 20', 5.0, 10.012)
    _thdmm = Call('ac', 'OUT 10.0 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_12', 9.98, 'DET:BAND 20', 5.0, 10.02)
    _thdmm = Call('ac', 'OUT 10.0 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_13', 9.929, 'DET:BAND 20', 5.0, 10.071)
    _thdmm = Call('ac', 'OUT 100.0 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_15', 99.88, 'DET:BAND 20', 5.0, 100.12)   
    _thdmm = Call('ac', 'OUT 750.0 V, 1 kHz', 'CONF:VOLT:AC 750.0', 'acv_18', 749.1, 'DET:BAND 20', 5.0, 750.9)        
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 'OUT 10.0 V, 300 kHz', 'CONF:VOLT:AC 10.0', 'acv_14', 9.55, 'DET:BAND 20', 5.0, 10.45)
        _thdmm = Call('ac', 'OUT 100.0 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_16', 99.8, 'DET:BAND 20', 5.0, 100.2)
        _thdmm = Call('ac', 'OUT 70.0 V, 300 kHz', 'CONF:VOLT:AC 100.0', 'acv_17', 66.7, 'DET:BAND 20', 5.0, 73.3)      
        _thdmm = Call('ac', 'OUT 210.0 V, 50 kHz', 'CONF:VOLT:AC 750.0', 'acv_19', 209.31, 'DET:BAND 20', 5.0, 210.69)           
        _thdmm = Call('ac', 'OUT 70.0 V, 300 kHz', 'CONF:VOLT:AC 750.0', 'acv_20', 63.4, 'DET:BAND 20', 5.0, 76.6)
if self.f_var.get() == 1:
    _thdmm = Call('fr', 'OUT 0.1 V, 10 Hz', 'CONF:FREQ 10 Hz', 'f_1', 9.997, 'DET:BAND 20', 5.0, 10.003)
    _thdmm = Call('fr', 'OUT 0.01 V, 300 kHz', 'CONF:FREQ 300 kHz', 'f_2', 299.64, 'DET:BAND 20', 5.0, 300.36)
if self.r2_var.get() == 1:
    _thdmm = Call('res2', 'OUT 1 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_1', 0.99985, 'DET:BAND 20', 5.0, 1.00015)
    _thdmm = Call('res2', 'OUT 10 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_2', 9.9959, 'DET:BAND 20', 5.0, 10.0041)
    _thdmm = Call('res2', 'OUT 100 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_3', 99.919, 'DET:BAND 20', 8.0, 100.081)
if self.r4_var.get() == 1:
    _th = Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _thdmm = Call('res4', 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 99.979, 'DET:BAND 20', 5.0, 100.021)
    _thdmm = Call('res4', 'OUT 1 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_2', 0.99985, 'DET:BAND 20', 5.0, 1.00015)
    _thdmm = Call('res4', 'OUT 10 kOHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_3', 9.9985, 'DET:BAND 20', 5.0, 10.0015)
    _thdmm = Call('res4', 'OUT 100 kOHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_4', 99.985, 'DET:BAND 20', 5.0, 100.015)
if self.dci_var.get() == 1:
    _th = Message('Подключите провода\n для измерения тока до 3 Ампер')
    _thdmm = Call('dci', 'OUT 100 uA', 'CONF:CURR:DC 0.0001', 'dci_1', 99.925, 'DET:BAND 20', 5.0, 100.075)
    _thdmm = Call('dci', 'OUT 1 mA', 'CONF:CURR:DC 0.001', 'dci_2', 0.99944, 'DET:BAND 20', 5.0, 1.00056)
    _thdmm = Call('dci', 'OUT 10 mA', 'CONF:CURR:DC 0.01', 'dci_3', 9.993, 'DET:BAND 20', 5.0, 10.007)
    _thdmm = Call('dci', 'OUT 100 mA', 'CONF:CURR:DC 0.1', 'dci_4', 99.945, 'DET:BAND 20', 5.0, 100.055)
    _thdmm = Call('dci', 'OUT 1 A', 'CONF:CURR:DC 1', 'dci_5', 0.9989, 'DET:BAND 20', 5.0, 1.0011)
    _thdmm = Call('dci', 'OUT 2 A', 'CONF:CURR:DC 3', 'dci_6', 1.9954, 'DET:BAND 20', 5.0, 2.0046)
if self.aci_var.get() == 1:
    _thdmm = Call('aci', 'OUT 100 uA, 1 kHz', 'CONF:CURR:AC 0.0001', 'aci_1', 99.86, 'DET:BAND 20', 5.0, 100.14)
    _thdmm = Call('aci', 'OUT 100 uA, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_2', 99.86, 'DET:BAND 20', 5.0, 100.14)
    _thdmm = Call('aci', 'OUT 1 mA, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_3', 0.9986, 'DET:BAND 20', 5.0, 1.0014)
    _thdmm = Call('aci', 'OUT 1 mA, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_4', 0.9986, 'DET:BAND 20', 5.0, 1.0014)
    _thdmm = Call('aci', 'OUT 100 uA, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_5', 95.9, 'DET:BAND 20', 5.0, 104.1)
    _thdmm = Call('aci', 'OUT 1 mA, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_6', 0.995, 'DET:BAND 20', 5.0, 1.005)
    _thdmm = Call('aci', 'OUT 10 mA, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_7', 9.986, 'DET:BAND 20', 5.0, 10.014)
    _thdmm = Call('aci', 'OUT 10 mA, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_8', 9.986, 'DET:BAND 20', 5.0, 10.014)
    _thdmm = Call('aci', 'OUT 10 mA, 10 Hz', 'CONF:CURR:AC 0.1', 'aci_9', 99.86, 'DET:BAND 3', 8.0, 100.14)   
    _thdmm = Call('aci', 'OUT 100 mA, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_10', 99.86, 'DET:BAND 20', 5.0, 100.14)
    _thdmm = Call('aci', 'OUT 100 mA, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_11', 99.86, 'DET:BAND 20', 5.0, 100.14)
    _thdmm = Call('aci', 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 1', 'aci_12', 0.9986, 'DET:BAND 20', 5.0, 1.0014)
    _thdmm = Call('aci', 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 1', 'aci_13', 0.9986, 'DET:BAND 20', 5.0, 1.0014)
    _thdmm = Call('aci', 'OUT 2 A, 1 kHz', 'CONF:CURR:AC 3', 'aci_14', 1.9942, 'DET:BAND 20', 5.0, 2.0058)
    _thdmm = Call('aci', 'OUT 2 A, 5 kHz', 'CONF:CURR:AC 3', 'aci_15', 1.9942, 'DET:BAND 20', 5.0, 2.0058)

_th = Message('Калибровка завершена')
_th = Clear_merge()
_th = Reset()