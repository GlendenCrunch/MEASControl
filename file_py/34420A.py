#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
Reset()
if self.vardict_boo['dcv_var'].get() == 1:
    Message('Соедините провода для измерения постоянного напряжения по КАНАЛУ 1 (красный(+)-черный(-))')
    Call('dcv', '100 mV', 'CONF:VOLT', 'dcv1', 'gdcv1', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG .1', '4.4 u')
    Call('dcv', '1 V', 'CONF:VOLT', 'dcv2', 'gdcv2', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 1', '39 u')
    Call('dcv', '10 V', 'CONF:VOLT', 'dcv3', 'gdcv3', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 10', '340 u')
    Call('dcv', '100 V', 'CONF:VOLT', 'dcv4', 'gdcv4', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 100', '4 m')
    Message('Соедините провода для измерения постоянного напряжения по КАНАЛУ 2 (зеленый(+)-белый(-))')
    Call('dcv', '100 mV', 'CONF:VOLT', 'dcv5', 'gdcv5', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG .1', '4.4 u')
    Call('dcv', '1 V', 'CONF:VOLT', 'dcv6', 'gdcv6', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG 1', '39 u')
    Call('dcv', '10 V', 'CONF:VOLT', 'dcv7', 'gdcv7', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG 10', '340 u')
if self.vardict_boo['r4_var'].get() == 1:
    Message('Соедините провода по четырехпроводной схеме для измерения сопротивления (красный(+)-черный(-); зеленый(+)-белый(-))')
    Call('r', '1.0001291 OHM', 'CONF:FRES', 'r1', 'gr1', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1', '72 u')
    Call('r', '9.999627 OHM', 'CONF:FRES', 'r2', 'gr2', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 10', '620 u')
    Call('r', '99.99911 OHM', 'CONF:FRES', 'r3', 'gr3', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 100', '6.2 m')
    Call('r', '1.0000143 kOHM', 'CONF:FRES', 'r4', 'gr4', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1000', '62 m')
    Call('r', '9.999776 kOHM', 'CONF:FRES', 'r5', 'gr5', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 10000', '620 m')
    Call('r', '99.99833 kOHM', 'CONF:FRES', 'r6', 'gr6', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 100000', '6.4 Ohm')
    Call('r', '1.0001291 OHM', 'CONF:FRES', 'r8', 'gr8', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1', '72 u')
    Call('r', '9.999627 OHM', 'CONF:FRES', 'r9', 'gr9', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 10', '620 u')
    Call('r', '99.99911 OHM', 'CONF:FRES', 'r10', 'gr10', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 100', '6.2 m')
    Call('r', '1.0000143 kOHM', 'CONF:FRES', 'r11', 'gr11', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1000', '62 m')
    Call('r', '9.999776 kOHM', 'CONF:FRES', 'r12', 'gr12', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 10000', '620 m')
    Call('r', '99.99833 kOHM', 'CONF:FRES', 'r13', 'gr13', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 100000', '6.4 Ohm')
    Message('Соедините провода по двухпроводной схеме для измерения сопротивления (красный-зеленый(+); черный-белый(-))')
    Call('r', '0.9999655 MOHM; ZCOMP OFF', 'CONF:FRES', 'r7', 'gr7', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1.0E+6', '74 Ohm')
    Call('r', '0.9999655 MOHM; ZCOMP OFF', 'CONF:FRES', 'r14', 'gr14', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1.0E+6', '74 Ohm')
if self.vardict_boo['acv_var'].get() == 1:
    Message('Подключите заглушку')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_1', 'gdcv0_1', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG .001', '120 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_2', 'gdcv0_2', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG .01', '130 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_3', 'gdcv0_3', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG .1', '400 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_4', 'gdcv0_4', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 1', '4 u')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_5', 'gdcv0_5', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 10', '40 u')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_6', 'gdcv0_6', 'ROUT:TERM FRON1', 'SENS1:VOLT:RANG 100', '500 u')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_7', 'gdcv0_7', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG .001', '120 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_8', 'gdcv0_8', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG .01', '130 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_9', 'gdcv0_9', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG .1', '400 n')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_10', 'gdcv0_10', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG 1', '4 u')
    Call('dcv0', '', 'CONF:VOLT', 'dcv0_11', 'gdcv0_11', 'ROUT:TERM FRON2', 'SENS2:VOLT:RANG 10', '40 u')
    Call('r0', '', 'CONF:FRES', 'r0_1', 'gr0_1', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1', '2 u')
    Call('r0', '', 'CONF:FRES', 'r0_2', 'gr0_2', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 10', '20 u')
    Call('r0', '', 'CONF:FRES', 'r0_3', 'gr0_3', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 100', '200 u')
    Call('r0', '', 'CONF:FRES', 'r0_4', 'gr0_4', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1000', '2 m')
    Call('r0', '', 'CONF:FRES', 'r0_5', 'gr0_5', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 10000', '20 m')
    Call('r0', '', 'CONF:FRES', 'r0_6', 'gr0_6', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1.0E+5', '400 m')
    Call('r0', '', 'CONF:FRES', 'r0_7', 'gr0_7', 'SENS:FRES:POW:LIM OFF', 'SENS:FRES:RANG 1.0E+6', '4 Ohm')
    Call('r0', '', 'CONF:FRES', 'r0_8', 'gr0_8', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1', '2 u')
    Call('r0', '', 'CONF:FRES', 'r0_9', 'gr0_9', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 10', '20 u')
    Call('r0', '', 'CONF:FRES', 'r0_10', 'gr0_10', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 100', '200 u')
    Call('r0', '', 'CONF:FRES', 'r0_11', 'gr0_11', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1000', '2 m')
    Call('r0', '', 'CONF:FRES', 'r0_12', 'gr0_12', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 10000', '20 m')
    Call('r0', '', 'CONF:FRES', 'r0_13', 'gr0_13', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1.0E+5', '400 m')
    Call('r0', '', 'CONF:FRES', 'r0_14', 'gr0_14', 'SENS:FRES:POW:LIM ON', 'SENS:FRES:RANG 1.0E+6', '4 Ohm')

Message('Калибровка завершена')
Clear_merge()
Reset()
