#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
Reset()
if self.dcv_var.get() == 1 or self.acv_var.get() == 1 or self.f_var.get() == 1 or self.r2_var.get():
    Message('Подключите провода к клеммам измерения напряжения, частоты или сопротивления')
elif self.aci_var.get() == 1:
    Message('Подключите провода для измерения тока')
if self.dcv_var.get() == 1:
    Call('dcv', '100 mV', 'CONF:VOLT:DC 0.1', 'dcv_1', '', 'DET:BAND 20', 3, 0.0085)
    Call('dcv', '-100 mV', 'CONF:VOLT:DC 0.1', 'dcv_2', '', 'DET:BAND 20', 3, 0.0085)
    Call('dcv', '1 V', 'CONF:VOLT:DC 1', 'dcv_3', '', 'DET:BAND 20', 3, 0.000047)
    Call('dcv', '-1 V', 'CONF:VOLT:DC 1', 'dcv_4', '', 'DET:BAND 20', 3, 0.000047)
    Call('dcv', '10 V', 'CONF:VOLT:DC 10', 'dcv_5', '', 'DET:BAND 20', 3, 0.004)
    Call('dcv', '-10 V', 'CONF:VOLT:DC 10', 'dcv_6', '', 'DET:BAND 20', 3, 0.004)
    Call('dcv','100 V', 'CONF:VOLT:DC 100', 'dcv_7', '', 'DET:BAND 20', 5, 0.0051)
    Call('dcv','-100 V', 'CONF:VOLT:DC 100', 'dcv_8', '', 'DET:BAND 20', 5, 0.0051)
    Call('dcv','1000 V', 'CONF:VOLT:DC 1000', 'dcv_9', '', 'DET:BAND 20', 5, 0.055)
    Call('dcv','-1000 V', 'CONF:VOLT:DC 1000', 'dcv_10', '', 'DET:BAND 20', 8, 0.055)
if self.acv_var.get() == 1:
    Call('acv','10 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_1', '', 'DET:BAND 20', 6, 0.046)
    Call('acv','100 mV, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv_2', '', 'DET:BAND 20', 5, 0.1)
    Call('acv','100 mV, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv_3', '', 'DET:BAND 20', 5, 0.17)
    Call('acv','1 V, 1 kHz', 'CONF:VOLT:AC 1', 'acv_4', '', 'DET:BAND 20', 5, 0.0001)
    Call('acv','1 V, 50 kHz', 'CONF:VOLT:AC 1', 'acv_5', '', 'DET:BAND 20', 5, 0.0017)
    Call('acv','10 V, 10 Hz', 'CONF:VOLT:AC 10', 'acv_6', '', 'DET:BAND 3', 8, 0.009)
    Call('acv','10 V, 1 kHz', 'CONF:VOLT:AC 10', 'acv_7', '', 'DET:BAND 20', 5, 0.009)
    Call('acv','10 V, 50 kHz', 'CONF:VOLT:AC 10', 'acv_8', '', 'DET:BAND 20', 5, 0.017)
    Call('acv','100 V, 1 kHz', 'CONF:VOLT:AC 100', 'acv_9', '', 'DET:BAND 20', 5, 0.09)
    if self.b1[1] == '5522A':
        Call('acv','100 V, 50 kHz', 'CONF:VOLT:AC 100', 'acv_10', '', 'DET:BAND 20', 5, 0.17)
    else:
        Call('acv','100 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_10', '', 'DET:BAND 20', 5, 0.17)
    Call('acv','750 V, 1 kHz', 'CONF:VOLT:AC 750', 'acv_11', '', 'DET:BAND 3', 5, 0.625)
    Call('acv','750 V, 10 kHz', 'CONF:VOLT:AC 750', 'acv_12', '', 'DET:BAND 20', 5, 1.275)
if self.f_var.get() == 1:
    Call('fr','0.01 V, 100 Hz', 'CONF:FREQ 100 Hz', 'f_1', '', 'DET:BAND 20', 4, 0.1)
    Call('fr','1 V, 100 kHz', 'CONF:FREQ 100 kHz', 'f_2', '', 'DET:BAND 20', 4, 0.01)
if self.r2_var.get() == 1:
    Call('res','1 MOHM', 'CONF:RES 1 MOHM', 'r2_1', '', 'DET:BAND 20', 4, 0.00011)
    Call('res','10 MOHM', 'CONF:RES 10 MOHM', 'r2_2', '', 'DET:BAND 20', 4, 0.0041)
    Call('res','100 MOHM', 'CONF:RES 100 MOHM', 'r2_3', '', 'DET:BAND 20', 4, 0.81)
if self.r4_var.get() == 1:
    Message('Подключите провода по четырехпроводной схеме\n для измерения сопротивления')
    Call('res','100 OHM', 'CONF:FRES 100', 'r4_1', '', 'DET:BAND 20', 4, 0.014)
    Call('res','1 kOHM4', 'CONF:FRES 1 KOHM', 'r4_2', '', 'DET:BAND 20', 4, 0.0001)
    Call('res','10 kOHM', 'CONF:FRES 10 KOHM', 'r4_3', '', 'DET:BAND 20', 4, 0.0011)
    Call('res','100 kOHM', 'CONF:FRES 100 KOHM', 'r4_4', '', 'DET:BAND 20', 4, 0.011)
if self.dci_var.get() == 1:
    Message('Подключите провода\n для измерения тока')
    Call('dci','10 mA', 'CONF:CURR:DC 0.01', 'dci_1', '', 'DET:BAND 20', 4, 0.007)
    Call('dci','100 mA', 'CONF:CURR:DC 0.1', 'dci_2', '', 'DET:BAND 20', 4, 0.055)
    Call('dci','1 A', 'CONF:CURR:DC 1', 'dci_3', '', 'DET:BAND 20', 4, 0.0011)
    Call('dci','2 A', 'CONF:CURR:DC 3', 'dci_4', '', 'DET:BAND 20', 4, 0.003)
if self.aci_var.get() == 1:
    Call('aci','1 A, 1 kHz', 'CONF:CURR:AC 1', 'aci_1', '', 'DET:BAND 20', 4, 0.0014)
    Call('aci','2 A, 1 kHz', 'CONF:CURR:AC 3', 'aci_2', '', 'DET:BAND 20', 4, 0.0048)

Message('Калибровка завершена')
Clear_merge()
Reset()
