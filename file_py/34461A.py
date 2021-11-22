# -*- coding: utf-8 -*-
if self.dcv_var.get() == 1:
    _th = Message('Соедините провода для измерения постоянного напряжения')
    _th = Reset()        
    _thdmm = Call('dc', 0.1, 'OUT 0.1 V', 'CONF:VOLT:DC 0.1', 'dcv_1', 'gdcv_1', 'DET:BAND 20', 3.0, 0.016)
    _thdmm = Call('dc', -0.1, 'OUT -0.1 V', 'CONF:VOLT:DC 0.1', 'dcv_2', 'gdcv_2', 'DET:BAND 20', 3.0, 0.016)
    _thdmm = Call('dc', 1.0, 'OUT 1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_3', 'gdcv_3', 'DET:BAND 20', 3.0, 0.009)
    _thdmm = Call('dc', -1.0, 'OUT -1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_4', 'gdcv_4', 'DET:BAND 20', 3.0, 0.009)
    _thdmm = Call('dc', 4.0, 'OUT 4.0 V', 'CONF:VOLT:DC 10', 'dcv_5', 'gdcv_5', 'DET:BAND 20', 3.0, 0.009)
    _thdmm = Call('dc', 10.0, 'OUT 10.0 V', 'CONF:VOLT:DC 10', 'dcv_6', 'gdcv_6', 'DET:BAND 20', 3.0, 0.008)
    _thdmm = Call('dc', -10.0, 'OUT -10.0 V', 'CONF:VOLT:DC 10', 'dcv_7', 'gdcv_7', 'DET:BAND 20', 3.0, 0.008)
    _thdmm = Call('dc', 100.0, 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_8', 'gdcv_8', 'DET:BAND 20', 4.0, 0.009)
    _thdmm = Call('dc', -100.0, 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv_9', 'gdcv_9', 'DET:BAND 20', 4.0, 0.009)
    _thdmm = Call('dc', 1000.0, 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_10', 'gdcv_10', 'DET:BAND 20', 8.0, 0.01)
    _thdmm = Call('dc', -500.0, 'OUT -500 V', 'CONF:VOLT:DC 1000', 'dcv_11', 'gdcv_11', 'DET:BAND 20', 8.0, 0.011)
if self.аcv_var.get() == 1:
    _th = Reset()
    _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_1', 'gacv_1', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 100 Hz', 'CONF:VOLT:AC 10.0', 'acv_2', 'gacv_2', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', 'gacv_3', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv_4', 'gacv_4', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_5', 'gacv_5', 'DET:BAND 20', 5.0, 10.0)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv_6', 'gacv_6', 'DET:BAND 20', 5.0, 0.39)
    _thdmm = Call('ac', 100.0, 'OUT 100.0 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv_7', 'gacv_7', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 750.0, 'OUT 750.0 V, 1 kHz', 'CONF:VOLT:AC 750.0', 'acv_8', 'gacv_8', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 20 kHz', 'CONF:VOLT:AC 10.0', 'acv_9', 'gacv_9', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_10', 'gacv_10', 'DET:BAND 20', 5.0, 0.2)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_11', 'gacv_11', 'DET:BAND 20', 5.0, 0.2)
    _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_12', 'gacv_12', 'DET:BAND 20', 5.0, 0.2)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 100.0, 'OUT 100.0 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv_13', 'gacv_13', 'DET:BAND 20', 5.0, 0.2)
        _thdmm = Call('ac', 750.0, 'OUT 750.0 V, 50 kHz', 'CONF:VOLT:AC 750.0', 'acv_14', 'gacv_14', 'DET:BAND 20', 5.0, 0.329)
    else:
        _thdmm = Call('ac', 100.0, 'OUT 100.0 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv_13', 'gacv_13', 'DET:BAND 20', 5.0, 0.2)
        _thdmm = Call('ac', 750.0, 'OUT 750.0 V, 10 kHz', 'CONF:VOLT:AC 750.0', 'acv_14', 'gacv_14', 'DET:BAND 20', 5.0, 0.329)
    _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_15', 'gacv_15', 'DET:BAND 20', 5.0, 0.71)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_16', 'gacv_16', 'DET:BAND 20', 5.0, 4.5)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_17', 'gacv_17', 'DET:BAND 20', 5.0, 4.5)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 10.0, 'OUT 10.0 V, 300 kHz', 'CONF:VOLT:AC 10.0', 'acv_18', 'gacv_18', 'DET:BAND 20', 5.0, 4.5)
        _thdmm = Call('ac', 70.0, 'OUT 70.0 V, 300 kHz', 'CONF:VOLT:AC 100.0', 'acv_19', 'gacv_19', 'DET:BAND 20', 5.0, 4.714)
        _thdmm = Call('ac', 70.0, 'OUT 70.0 V, 300 kHz', 'CONF:VOLT:AC 750.0', 'acv_20', 'gacv_20', 'DET:BAND 20', 5.0, 9.429)
if self.f_var.get() == 1:
    _th = Reset()
    _thdmm = Call('fr', 10.0, 'OUT 0.1 V, 10.0 Hz', 'CONF:FREQ 10.0 Hz', 'f_1', 'gf_1', 'DET:BAND 20', 5.0, 0.035)
    _thdmm = Call('fr', 300000.0, 'OUT 0.01 V, 300.0 kHz', 'CONF:FREQ 300.0 kHz', 'f_2', 'gf_2', 'DET:BAND 20', 5.0, 0.17)
if self.dci_var.get() == 1:
    _th = Message('Переключите провода\n для измерения тока до 3 Ампер')
    _th = Reset()
    _thdmm = Call('dci', 0.0001, 'OUT 0.0001 A', 'CONF:CURR:DC 0.0001', 'dci_1', 'gdci_1', 'DET:BAND 20', 5.0, 0.075)
    _thdmm = Call('dci', 0.001, 'OUT 0.001 A', 'CONF:CURR:DC 0.001', 'dci_2', 'gdci_2', 'DET:BAND 20', 5.0, 0.056)
    _thdmm = Call('dci', 0.01, 'OUT 0.01 A', 'CONF:CURR:DC 0.01', 'dci_3', 'gdci_3', 'DET:BAND 20', 5.0, 0.07)
    _thdmm = Call('dci', 0.1, 'OUT 0.1 A', 'CONF:CURR:DC 0.1', 'dci_4', 'gdci_4', 'DET:BAND 20', 5.0, 0.055)
    _thdmm = Call('dci', 1.0, 'OUT 1.0 A', 'CONF:CURR:DC 1.0', 'dci_5', 'gdci_5', 'DET:BAND 20', 5.0, 0.11)
    _thdmm = Call('dci', 2.0, 'OUT 2.0 A', 'CONF:CURR:DC 3.0', 'dci_6', 'gdci_6', 'DET:BAND 20', 5.0, 0.23)
if self.aci_var.get() == 1:
    _th = Reset()
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 10 Hz', 'CONF:CURR:AC 0.1', 'aci_1', 'gaci_1', 'DET:BAND 3', 8.0, 0.14)
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 1 kHz', 'CONF:CURR:AC 0.0001', 'aci_2', 'gaci_2', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_3', 'gaci_3', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_4', 'gaci_4', 'DET:BAND 20', 5.0, 4.1)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_5', 'gaci_5', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_6', 'gaci_6', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_7', 'gaci_7', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 1.0, 'OUT 1.0 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_8', 'gaci_8', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 2.0, 'OUT 2.0 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_9', 'gaci_9', 'DET:BAND 20', 5.0, 0.29)
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_10', 'gaci_10', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_11', 'gaci_11', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_12', 'gaci_12', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_13', 'gaci_13', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 1.0, 'OUT 1.0 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_14', 'gaci_14', 'DET:BAND 20', 5.0, 0.14)
    _thdmm = Call('aci', 2.0, 'OUT 2.0 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_15', 'gaci_15', 'DET:BAND 20', 5.0, 0.29)
if self.dci_var.get() and self.aci_var.get() == 1:
    _th = Message('Переключите провода\n для измерения тока больше 3 Ампер')
    _thdmm = Call('dci', 5.0, 'OUT 5.0 A', 'CONF:CURR:DC 10.0', 'dci_7', 'gdci_7', 'DET:BAND 20', 5.0, 0.24)
    _thdmm = Call('dci', 10.0, 'OUT 10.0 A', 'CONF:CURR:DC 10.0', 'dci_8', 'gdci_8', 'DET:BAND 20', 5.0, 0.22)
    if self.b1[1] == '5522A':
        _thdmm = Call('aci', 10.0, 'OUT 10.0 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_16', 'gaci_16', 'DET:BAND 20', 5.0, 0.19)
    else:
        _thdmm = Call('aci', 10.0, 'OUT 10.0 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_16', 'gaci_16', 'DET:BAND 20', 5.0, 0.19)
if self.r4_var.get() == 1:
    _th = Message('Переключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    _thdmm = Call('res4', 100.0, 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 'gr4_1', 'DET:BAND 20', 5.0, 0.021)
    _thdmm = Call('res4', 1.0E+3, 'OUT 1 kOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_2', 'gr4_2', 'DET:BAND 20', 5.0, 0.015)
    _thdmm = Call('res4', 10.0E+3, 'OUT 10 kOHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_3', 'gr4_3', 'DET:BAND 20', 5.0, 0.015)
    _thdmm = Call('res4', 100.0E+3, 'OUT 100 kOHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_4', 'gr4_4', 'DET:BAND 20', 5.0, 0.015)
if self.r2_var.get() == 1:
    _th = Message('Переключите провода по двухпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    _thdmm = Call('res2', 1.0E+6, 'OUT 1 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_1', 'gr2_1', 'DET:BAND 20', 5.0, 0.015)
    _thdmm = Call('res2', 10.0E+6, 'OUT 10 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_2', 'gr2_2', 'DET:BAND 20', 5.0, 0.041)
    _thdmm = Call('res2', 100.0E+6, 'OUT 100 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_3', 'gr2_3', 'DET:BAND 20', 5.0, 0.81)

_th = Message('Калибровка завершена')
_th = Reset()