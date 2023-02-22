#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
Reset()
if self.vardict_boo['dcv_var'].get() == 1 or self.vardict_boo['acv_var'].get() == 1 or self.vardict_boo['f_var'].get() == 1 or self.vardict_boo['r2_var'].get() == 1:
    Message('Подключите провода к клеммам измерения напряжения, частоты или сопротивления')
elif self.vardict_boo['aci_var'].get() == 1:
    Message('Подключите провода для измерения тока')
if self.vardict_boo['dcv_var'].get() == 1:
    Call('dcv', '5 mV', 'CONF:VOLT:DC 0.1', 'dcv_1', '', 'DET:BAND 20', 3.0, 0.00375)
    Call('dcv', '50 mV', 'CONF:VOLT:DC 0.1', 'dcv_2', '', 'DET:BAND 20', 3.0, 0.0025)
    Call('dcv', '95 mV', 'CONF:VOLT:DC 0.1', 'dcv_3', '', 'DET:BAND 20', 3.0, 0.00475)
    Call('dcv', '50 mV', 'CONF:VOLT:DC 1', 'dcv_4', '', 'DET:BAND 20', 3.0, 0.00875)
    Call('dcv', '0.5 V', 'CONF:VOLT:DC 1', 'dcv_5', '', 'DET:BAND 20', 3.0, 0.0000175)
    Call('dcv', '0.95 V', 'CONF:VOLT:DC 1', 'dcv_6', '', 'DET:BAND 20', 3.0, 0.00003325)
    Call('dcv', '0.5 V', 'CONF:VOLT:DC 10', 'dcv_7', '', 'DET:BAND 20', 3.0, 0.000065)
    Call('dcv', '5 V', 'CONF:VOLT:DC 10', 'dcv_8', '', 'DET:BAND 20', 3.0, 0.00015)
    Call('dcv', '9.5 V', 'CONF:VOLT:DC 10', 'dcv_9', '', 'DET:BAND 20', 3.0, 0.000285)
    Call('dcv', '5 V', 'CONF:VOLT:DC 100', 'dcv_10', '', 'DET:BAND 20', 3.0, 0.0008)
    Call('dcv', '50 V', 'CONF:VOLT:DC 100', 'dcv_11', '', 'DET:BAND 20', 3.0, 0.002)
    Call('dcv', '95 V', 'CONF:VOLT:DC 100', 'dcv_12', '', 'DET:BAND 20', 3.0, 0.0038)
    Call('dcv', '50 V', 'CONF:VOLT:DC 1000', 'dcv_13', '', 'DET:BAND 20', 3.0, 0.008)
    Call('dcv', '500 V', 'CONF:VOLT:DC 1000', 'dcv_14', '', 'DET:BAND 20', 3.0, 0.02)
    Call('dcv', '950 V', 'CONF:VOLT:DC 1000', 'dcv_15', '', 'DET:BAND 20', 4.0, 0.038)
if self.vardict_boo['acv_var'].get() == 1:
    Call('acv', '5 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_1', '', 'DET:BAND 3', 8.0, 0.035)
    Call('acv', '5 mV, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_2', '', 'DET:BAND 20', 8.0, 0.033)
    Call('acv', '5 mV, 20 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', '', 'DET:BAND 20', 5.0, 0.033)
    Call('acv', '5 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_4', '', 'DET:BAND 20', 5.0, 0.055)
    Call('acv', '5 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_5', '', 'DET:BAND 20', 5.0, 0.1)
    Call('acv', '5 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_6', '', 'DET:BAND 3', 5.0, 0.56)
    Call('acv', '50 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_7', '', 'DET:BAND 3', 8.0, 0.08)
    Call('acv', '50 mV, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_8', '', 'DET:BAND 20', 8.0, 0.06)
    Call('acv', '50 mV, 20 kHz', 'CONF:VOLT:AC 0.1', 'acv_9', '', 'DET:BAND 20', 5.0, 0.06)
    Call('acv', '50 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_10', '', 'DET:BAND 20', 5.0, 0.1)
    Call('acv', '50 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_11', '', 'DET:BAND 20', 5.0, 0.3)
    Call('acv', '50 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_12', '', 'DET:BAND 3', 5.0, 1.1)
    Call('acv', '95 mV, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_13', '', 'DET:BAND 3', 8.0, 0.125)
    Call('acv', '95 mV, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_14', '', 'DET:BAND 20', 8.0, 0.087)
    Call('acv', '95 mV, 20 kHz', 'CONF:VOLT:AC 0.1', 'acv_15', '', 'DET:BAND 20', 5.0, 0.087)
    Call('acv', '95 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_16', '', 'DET:BAND 20', 5.0, 0.145)
    Call('acv', '95 mV, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv_17', '', 'DET:BAND 20', 5.0, 0.5)
    Call('acv', '95 mV, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv_18', '', 'DET:BAND 3', 5.0, 1.64)
    Call('acv', '50 mV, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_19', '', 'DET:BAND 3', 8.0, 0.35)
    Call('acv', '50 mV, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_20', '', 'DET:BAND 20', 8.0, 0.33)
    Call('acv', '50 mV, 20 kHz', 'CONF:VOLT:AC 1.0', 'acv_21', '', 'DET:BAND 20', 5.0, 0.33)
    Call('acv', '50 mV, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_22', '', 'DET:BAND 20', 5.0, 0.55)
    Call('acv', '50 mV, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_23', '', 'DET:BAND 20', 5.0, 1.0)
    Call('acv', '50 mV 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_24', '', 'DET:BAND 20', 5.0, 5.6)
    Call('acv', '0.5 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_25', '', 'DET:BAND 3', 8.0, 0.0008)
    Call('acv', '0.5 V, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_26', '', 'DET:BAND 20', 8.0, 0.0006)
    Call('acv', '0.5 V, 20 kHz', 'CONF:VOLT:AC 1.0', 'acv_27', '', 'DET:BAND 20', 5.0, 0.0006)
    Call('acv', '0.5 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_28', '', 'DET:BAND 20', 5.0, 0.001)
    Call('acv', '0.5 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_29', '', 'DET:BAND 20', 5.0, 0.0028)
    Call('acv', '0.5 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_30', '', 'DET:BAND 20', 5.0, 0.011)
    Call('acv', '0.95 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_31', '', 'DET:BAND 3', 8.0, 0.00125)
    Call('acv', '0.95 V, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_32', '', 'DET:BAND 20', 8.0, 0.00087)
    Call('acv', '0.95 V, 20 kHz', 'CONF:VOLT:AC 1.0', 'acv_33', '', 'DET:BAND 20', 5.0, 0.00087)
    Call('acv', '0.95 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv_34', '', 'DET:BAND 20', 5.0, 0.00145)
    Call('acv', '0.95 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv_35', '', 'DET:BAND 20', 5.0, 0.0046)
    Call('acv', '0.95 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv_36', '', 'DET:BAND 20', 5.0, 0.0164)
    Call('acv', '0.5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_37', '', 'DET:BAND 3', 8.0, 0.0035)
    Call('acv', '0.5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_38', '', 'DET:BAND 20', 8.0, 0.0033)
    Call('acv', '0.5 V, 20 kHz', 'CONF:VOLT:AC 10.0', 'acv_39', '', 'DET:BAND 20', 5.0, 0.0033)
    Call('acv', '0.5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_40', '', 'DET:BAND 20', 5.0, 0.0055)
    Call('acv', '0.5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_41', '', 'DET:BAND 20', 5.0, 0.01)
    Call('acv', '0.5 V, 300 kHz', 'CONF:VOLT:AC 10.0', 'acv_42', '', 'DET:BAND 20', 5.0, 0.056)
    Call('acv', '5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_43', '', 'DET:BAND 3', 8.0, 0.008)
    Call('acv', '5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_44', '', 'DET:BAND 20', 8.0, 0.006)
    Call('acv', '5 V, 20 kHz', 'CONF:VOLT:AC 10.0', 'acv_45', '', 'DET:BAND 20', 5.0, 0.006)
    Call('acv', '5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_46', '', 'DET:BAND 20', 5.0, 0.01)
    Call('acv', '5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_47', '', 'DET:BAND 20', 5.0, 0.028)
    Call('acv', '9.5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_49', '', 'DET:BAND 3', 8.0, 0.0125)
    Call('acv', '9.5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_50', '', 'DET:BAND 20', 8.0, 0.0087)
    Call('acv', '9.5 V, 20 kHz', 'CONF:VOLT:AC 10.0', 'acv_51', '', 'DET:BAND 20', 5.0, 0.0087)
    Call('acv', '9.5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv_52', '', 'DET:BAND 20', 5.0, 0.0145)
    Call('acv', '9.5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_53', '', 'DET:BAND 20', 5.0, 0.046)
    Call('acv', '5 V, 10 Hz', 'CONF:VOLT:AC 100', 'acv_55', '', 'DET:BAND 3', 8.0, 0.035)
    Call('acv', '5 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_56', '', 'DET:BAND 20', 8.0, 0.033)
    Call('acv', '5 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_57', '', 'DET:BAND 20', 5.0, 0.033)
    Call('acv', '5 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_58', '', 'DET:BAND 20', 5.0, 0.055)
    Call('acv', '5 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_59', '', 'DET:BAND 20', 5.0, 0.1)
    Call('acv', '50 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_62', '', 'DET:BAND 20', 5.0, 0.06)
    Call('acv', '50 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_63', '', 'DET:BAND 200', 5.0, 0.06)
    if self.b1[1] == '5522A':
        Call('acv', '50 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_64', '', 'DET:BAND 200', 5.0, 0.1)
        Call('acv', '50 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_65', '', 'DET:BAND 200', 5.0, 0.3)
    Call('acv', '95 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_68', '', 'DET:BAND 20', 5.0, 0.087)
    Call('acv', '95 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_69', '', 'DET:BAND 20', 5.0, 0.087)
    if self.b1[1] == '5522A':
        Call('acv', '95 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_70', '', 'DET:BAND 20', 5.0, 0.5)
        Call('acv', '95 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_71', '', 'DET:BAND 20', 5.0, 1.64)
    Call('acv', '37.5 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_74', '', 'DET:BAND 20', 5.0, 0.248)
    Call('acv', '37.5 V, 20 kHz', 'CONF:VOLT:AC 750', 'acv_75', '', 'DET:BAND 20', 5.0, 0.248)
    if self.b1[1] == '5522A':
        Call('acv', '37.5 V, 50 kHz', 'CONF:VOLT:AC 750', 'acv_76', '', 'DET:BAND 20', 5.0, 0.413)
        Call('acv', '37.5 V, 100 kHz', 'CONF:VOLT:AC 750', 'acv_77', '', 'DET:BAND 20', 5.0, 0.8)
    Call('acv', '375 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_80', '', 'DET:BAND 20', 5.0, 0.45)
    Call('acv', '712.5 V, 50 Hz', 'CONF:VOLT:AC 750', 'acv_86', '', 'DET:BAND 20', 5.0, 0.152)
if self.vardict_boo['f_var'].get() == 1:
    Call('fr', '0.1 V, 5 Hz', 'CONF:FREQ 5 Hz', 'f_1', '', 'DET:BAND 20', 8.0, 0.0035)
    Call('fr', '10 V, 5 Hz', 'CONF:FREQ 5 Hz', 'f_2', '', 'DET:BAND 20', 8.0, 0.0035)
    Call('fr', '0.1 V, 10 Hz', 'CONF:FREQ 10 Hz', 'f_3', '', 'DET:BAND 20', 5.0, 0.004)
    Call('fr', '10 V, 10 Hz', 'CONF:FREQ 10 Hz', 'f_4', '', 'DET:BAND 20', 5.0, 0.004)
    Call('fr', '0.1 V, 40 Hz', 'CONF:FREQ 40 Hz', 'f_5', '', 'DET:BAND 20', 5.0, 0.008)
    Call('fr', '10 V, 40 Hz', 'CONF:FREQ 40 Hz', 'f_6', '', 'DET:BAND 20', 5.0, 0.008)
    Call('fr', '0.1 V, 1 kHz', 'CONF:FREQ 1 kHz', 'f_7', '', 'DET:BAND 20', 5.0, 0.00005)
    Call('fr', '10 V, 1 kHz', 'CONF:FREQ 1 kHz', 'f_8', '', 'DET:BAND 20', 5.0, 0.00005)
    Call('fr', '0.1 V, 100 kHz', 'CONF:FREQ 100 kHz', 'f_9', '', 'DET:BAND 20', 5.0, 0.005)
    Call('fr', '10 V, 100 kHz', 'CONF:FREQ 100 kHz', 'f_10', '', 'DET:BAND 20', 5.0, 0.005)
    Call('fr', '0.1 V, 300 kHz', 'CONF:FREQ 300 kHz', 'f_11', '', 'DET:BAND 20', 5.0, 0.015)
    Call('fr', '10 V, 300 kHz', 'CONF:FREQ 300 kHz', 'f_12', '', 'DET:BAND 20', 5.0, 0.015)
if self.vardict_boo['c_var'].get() == 1:
    Message('Измерение ёмкости.\nВытащите красный провод из каллибратора\nдля компенсации проводов')
    cap()
    Message('Верните провод на место')
    Call('cap', '0.35 NF', 'CONF:CAP 1 NF', 'c_1', '', 'DET:BAND 20', 5.0, 0.00675)
    Call('cap', '0.5 NF', 'CONF:CAP 1 NF', 'c_2', '', 'DET:BAND 20', 5.0, 0.0025)
    Call('cap', '0.95 NF', 'CONF:CAP 1 NF', 'c_3', '', 'DET:BAND 20', 5.0, 0.00475)
    Call('cap', '0.5 NF', 'CONF:CAP 10 NF', 'c_4', '', 'DET:BAND 20', 5.0, 0.012)
    Call('cap', '5 NF', 'CONF:CAP 10 NF', 'c_5', '', 'DET:BAND 20', 5.0, 0.02)
    Call('cap', '9.5 NF', 'CONF:CAP 10 NF', 'c_6', '', 'DET:BAND 20', 5.0, 0.038)
    Call('cap', '5 NF', 'CONF:CAP 100 NF', 'c_7', '', 'DET:BAND 20', 5.0, 0.12)
    Call('cap', '50 NF', 'CONF:CAP 100 NF', 'c_8', '', 'DET:BAND 20', 5.0, 0.2)
    Call('cap', '95 NF', 'CONF:CAP 100 NF', 'c_9', '', 'DET:BAND 20', 5.0, 0.38)
    Call('cap', '50 NF', 'CONF:CAP 1 UF', 'c_10', '', 'DET:BAND 20', 5.0, 0.201)
    Call('cap', '0.5 UF', 'CONF:CAP 1 UF', 'c_11', '', 'DET:BAND 20', 5.0, 0.002)
    Call('cap', '0.95 UF', 'CONF:CAP 1 UF', 'c_12', '', 'DET:BAND 20', 5.0, 0.004)
    Call('cap', '0.5 UF', 'CONF:CAP 10 UF', 'c_13', '', 'DET:BAND 20', 5.0, 0.012)
    Call('cap', '5 UF', 'CONF:CAP 10 UF', 'c_14', '', 'DET:BAND 20', 5.0, 0.02)
    Call('cap', '9.5 UF', 'CONF:CAP 10 UF', 'c_15', '', 'DET:BAND 20', 5.0, 0.038)
if self.vardict_boo['r2_var'].get() == 1:
    Call('res', '50 kOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_1', '', 'DET:BAND 20', 5.0, 0.016)
    Call('res', '0.5 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_2', '', 'DET:BAND 20', 5.0, 0.00006)
    Call('res', '0.95 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_3', '', 'DET:BAND 20', 5.0, 0.000114)
    Call('res', '0.5 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_4', '', 'DET:BAND 20', 5.0, 0.0003)
    Call('res', '5 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_5', '', 'DET:BAND 20', 5.0, 0.002)
    Call('res', '9.5 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_6', '', 'DET:BAND 20', 5.0, 0.0038)
    Call('res', '5 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_7', '', 'DET:BAND 20', 5.0, 0.041)
    Call('res', '50 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_8', '', 'DET:BAND 20', 5.0, 0.4)
    Call('res', '95 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_9', '', 'DET:BAND 20', 5.0, 0.76)
    Call('res', '50 MOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_10', '', 'DET:BAND 20', 5.0, 4.00001)
    if self.b1[1] == '5522A':
        Call('res', '0.5 GOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_11', '', 'DET:BAND 20', 5.0, 0.04)
        Call('res', '0.95 GOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_12', '', 'DET:BAND 20', 5.0, 0.076)
if self.vardict_boo['r4_var'].get() == 1:
    Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')
    Call('res', '5 OHM', 'CONF:FRES 100', 'r4_1', '', 'DET:BAND 20', 5.0, 0.0045)
    Call('res', '50 OHM', 'CONF:FRES 100', 'r4_2', '', 'DET:BAND 20', 5.0, 0.005)
    Call('res', '95 OHM', 'CONF:FRES 100', 'r4_3', '', 'DET:BAND 20', 5.0, 0.0095)
    Call('res', '50 OHM', 'CONF:FRES 1 KOHM', 'r4_4', '', 'DET:BAND 20', 5.0, 0.015)
    Call('res', '500 OHM', 'CONF:FRES 1 KOHM', 'r4_5', '', 'DET:BAND 20', 5.0, 0.05)
    Call('res', '950 OHM', 'CONF:FRES 1 KOHM', 'r4_6', '', 'DET:BAND 20', 5.0, 0.095)
    Call('res', '0.5 kOHM', 'CONF:FRES 10 KOHM', 'r4_7', '', 'DET:BAND 20', 5.0, 0.00015)
    Call('res', '5 kOHM', 'CONF:FRES 10 KOHM', 'r4_8', '', 'DET:BAND 20', 5.0, 0.0005)
    Call('res', '9.5 kOHM', 'CONF:FRES 10 KOHM', 'r4_9', '', 'DET:BAND 20', 5.0, 0.00095)
    Call('res', '5 kOHM', 'CONF:FRES 100 KOHM', 'r4_10', '', 'DET:BAND 20', 5.0, 0.0015)
    Call('res', '50 kOHM', 'CONF:FRES 100 KOHM', 'r4_11', '', 'DET:BAND 20', 5.0, 0.005)
    Call('res', '95 kOHM', 'CONF:FRES 100 KOHM', 'r4_12', '', 'DET:BAND 20', 5.0, 0.0095)
if self.vardict_boo['dci_var'].get() == 1:
    Message('Подключите провода\n для измерения тока')
    Call('dci', '5 uA', 'CONF:CURR:DC 0.0001', 'dci_1', '', 'DET:BAND 20', 5.0, 0.0275)
    Call('dci', '50 uA', 'CONF:CURR:DC 0.0001', 'dci_2', '', 'DET:BAND 20', 5.0, 0.025)
    Call('dci', '95 uA', 'CONF:CURR:DC 0.0001', 'dci_3', '', 'DET:BAND 20', 5.0, 0.0475)
    Call('dci', '0.05 mA', 'CONF:CURR:DC 0.001', 'dci_4', '', 'DET:BAND 20', 5.0, 0.000085)
    Call('dci', '0.5 mA', 'CONF:CURR:DC 0.001', 'dci_5', '', 'DET:BAND 20', 5.0, 0.00025)
    Call('dci', '0.95 mA', 'CONF:CURR:DC 0.001', 'dci_6', '', 'DET:BAND 20', 5.0, 0.000475)
    Call('dci', '0.5 mA', 'CONF:CURR:DC 0.01', 'dci_7', '', 'DET:BAND 20', 5.0, 0.00225)
    Call('dci', '5 mA', 'CONF:CURR:DC 0.01', 'dci_8', '', 'DET:BAND 20', 5.0, 0.0025)
    Call('dci', '9.5 mA', 'CONF:CURR:DC 0.01', 'dci_9', '', 'DET:BAND 20', 5.0, 0.00475)
    Call('dci', '5 mA', 'CONF:CURR:DC 0.1', 'dci_10', '', 'DET:BAND 20', 5.0, 0.0075)
    Call('dci', '50 mA', 'CONF:CURR:DC 0.1', 'dci_11', '', 'DET:BAND 20', 5.0, 0.025)
    Call('dci', '95 mA', 'CONF:CURR:DC 0.1', 'dci_12', '', 'DET:BAND 20', 5.0, 0.0475)
    Call('dci', '0.05 A', 'CONF:CURR:DC 1', 'dci_13', '', 'DET:BAND 20', 5.0, 0.00015)
    Call('dci', '0.5 A', 'CONF:CURR:DC 1', 'dci_14', '', 'DET:BAND 20', 5.0, 0.0005)
    Call('dci', '0.95 A', 'CONF:CURR:DC 1', 'dci_15', '', 'DET:BAND 20', 5.0, 0.001)
    Call('dci', '0.15 A', 'CONF:CURR:DC 3', 'dci_16', '', 'DET:BAND 20', 5.0, 0.000825)
    Call('dci', '1.5 A', 'CONF:CURR:DC 3', 'dci_17', '', 'DET:BAND 20', 5.0, 0.00225)
    if self.b1[1] == '5500E':
        Call('dci', '2.85 A', 'CONF:CURR:DC 3', 'dci_18', '', 'DET:BAND 20', 5.0, 0.004275)
    elif self.b1[1] == '5522A':
        Message('Подключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        Call('dci', '2.85 A', 'CONF:CURR:DC 3', 'dci_18', '', 'DET:BAND 20', 5.0, 0.004275)
        Message('Верните провод на КАЛИБРАТОРЕ обратно в разъем меньше 2,5 А')
if self.vardict_boo['aci_var'].get() == 1:
    Call('aci', '30 uA, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_1', '', 'DET:BAND 20', 10.0, 0.07)
    Call('aci', '30 uA, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_2', '', 'DET:BAND 20', 5.0, 0.07)
    Call('aci', '30 uA, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_3', '', 'DET:BAND 20', 5.0, 0.1)
    Call('aci', '50 uA, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_4', '', 'DET:BAND 20', 10.0, 0.09)
    Call('aci', '50 uA, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_5', '', 'DET:BAND 20', 5.0, 0.09)
    Call('aci', '50 uA, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_6', '', 'DET:BAND 20', 5.0, 0.14)
    Call('aci', '95 uA, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_7', '', 'DET:BAND 20', 5.0, 0.135)
    Call('aci', '95 uA, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_8', '', 'DET:BAND 20', 5.0, 0.135)
    Call('aci', '95 uA, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_9', '', 'DET:BAND 20', 5.0, 0.23)
    Call('aci', '0.05 mA, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_10', '', 'DET:BAND 20', 5.0, 0.00045)
    Call('aci', '0.05 mA, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_11', '', 'DET:BAND 20', 5.0, 0.00045)
    Call('aci', '0.05 mA, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_12', '', 'DET:BAND 20', 5.0, 0.0005)
    Call('aci', '0.5 mA, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_13', '', 'DET:BAND 20', 5.0, 0.0009)
    Call('aci', '0.5 mA, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_14', '', 'DET:BAND 20', 5.0, 0.0009)
    Call('aci', '0.5 mA, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_15', '', 'DET:BAND 20', 5.0,0.0014)
    Call('aci', '0.95 mA, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_16', '', 'DET:BAND 20', 5.0, 0.00135)
    Call('aci', '0.95 mA, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_17', '', 'DET:BAND 20', 5.0, 0.00135)
    Call('aci', '0.95 mA, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_18', '', 'DET:BAND 20', 5.0, 0.0023)
    Call('aci', '0.5 mA, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_19', '', 'DET:BAND 20', 5.0, 0.0045)
    Call('aci', '0.5 mA, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_20', '', 'DET:BAND 20', 5.0, 0.0045)
    Call('aci', '0.5 mA, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_21', '', 'DET:BAND 20', 5.0, 0.005)
    Call('aci', '5 mA, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_22', '', 'DET:BAND 20', 5.0, 0.009)
    Call('aci', '5 mA, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_23', '', 'DET:BAND 20', 5.0, 0.009)
    Call('aci', '5 mA, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_24', '', 'DET:BAND 20', 5.0, 0.014)
    Call('aci', '9.5 mA, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_25', '', 'DET:BAND 20', 5.0, 0.014)
    Call('aci', '9.5 mA, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_26', '', 'DET:BAND 20', 5.0, 0.014)
    Call('aci', '9.5 mA, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_27', '', 'DET:BAND 20', 5.0, 0.023)
    Call('aci', '5 mA, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_28', '', 'DET:BAND 20', 5.0, 0.045)
    Call('aci', '5 mA, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_29', '', 'DET:BAND 20', 5.0, 0.045)
    Call('aci', '5 mA, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_30', '', 'DET:BAND 20', 5.0, 0.05)
    Call('aci', '50 mA, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_31', '', 'DET:BAND 20', 5.0, 0.09)
    Call('aci', '50 mA, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_32', '', 'DET:BAND 20', 5.0, 0.09)
    Call('aci', '50 mA, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_33', '', 'DET:BAND 20', 5.0, 0.14)
    Call('aci', '95 mA, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_34', '', 'DET:BAND 20', 5.0, 0.135)
    Call('aci', '95 mA, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_35', '', 'DET:BAND 20', 5.0, 0.135)
    Call('aci', '95 mA, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_36', '', 'DET:BAND 20', 5.0, 0.23)
    Call('aci', '0.05 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_37', '', 'DET:BAND 20', 5.0, 0.00045)
    Call('aci', '0.05 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_38', '', 'DET:BAND 20', 5.0, 0.00045)
    Call('aci', '0.05 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_39', '', 'DET:BAND 20', 5.0, 0.0005)
    Call('aci', '0.5 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_40', '', 'DET:BAND 20', 5.0, 0.0009)
    Call('aci', '0.5 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_41', '', 'DET:BAND 20', 5.0, 0.0009)
    if self.b1[1] == '5522A':
        Call('aci', '0.5 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_42', '', 'DET:BAND 20', 5.0, 0.0014)
    Call('aci', '0.95 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_43', '', 'DET:BAND 20', 5.0, 0.00135)
    Call('aci', '0.95 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_44', '', 'DET:BAND 20', 5.0, 0.00135)
    if self.b1[1] == '5522A':
        Call('aci', '0.95 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_45', '', 'DET:BAND 20', 5.0, 0.0023)
    Call('aci', '0.15 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_46', '', 'DET:BAND 20', 5.0, 0.00135)
    Call('aci', '0.15 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_47', '', 'DET:BAND 20', 5.0, 0.00135)
    Call('aci', '0.15 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_48', '', 'DET:BAND 20', 5.0, 0.0015)
    Call('aci', '1.5 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_49', '', 'DET:BAND 20', 5.0, 0.0027)
    Call('aci', '1.5 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_50', '', 'DET:BAND 20', 5.0, 0.0027)
    if self.b1[1] == '5500E':
        Call('aci', '2.85 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_52', '', 'DET:BAND 20', 8.0, 0.00405)
    if self.b1[1] == '5522A':
        Call('aci', '1.5 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_51', '', 'DET:BAND 20', 5.0, 0.0042)
        Message('Подключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        Call('aci', '2.85 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_52', '', 'DET:BAND 20', 8.0, 0.00405)
        Call('aci', '2.85 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_53', '', 'DET:BAND 20', 5.0, 0.00405)
        Call('aci', '2.85 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_54', '', 'DET:BAND 20', 5.0, 0.0069)

Message('Калибровка завершена')
Clear_merge()
Reset()
