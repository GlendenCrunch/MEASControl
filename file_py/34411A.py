# -*- coding: utf-8 -*-
if self.dcv_var.get() == 1:
    _th = Message('Соедините провода для измерения постоянного напряжения')
    _th = Reset()         
    # 0.1V
    _thdmm = Call('dc', 0.005, 'OUT 0.005 V', 'CONF:VOLT:DC 0.1', 'dcv_1', 'gdcv_1', 'DET:BAND 20', 3.0, 0.075)
    _thdmm = Call('dc', 0.05, 'OUT 0.05 V', 'CONF:VOLT:DC 0.1', 'dcv_2', 'gdcv_2', 'DET:BAND 20', 3.0, 0.012)
    _thdmm = Call('dc', 0.095, 'OUT 0.095 V', 'CONF:VOLT:DC 0.1', 'dcv_3', 'gdcv_3', 'DET:BAND 20', 3.0, 0.009)
    # 1V
    _thdmm = Call('dc', 0.05, 'OUT 0.05 V', 'CONF:VOLT:DC 1.0', 'dcv_4', 'gdcv_4', 'DET:BAND 20', 3.0, 0.018)
    _thdmm = Call('dc', 0.5, 'OUT 0.5 V', 'CONF:VOLT:DC 1.0', 'dcv_5', 'gdcv_5', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 0.95, 'OUT 0.95 V', 'CONF:VOLT:DC 1.0', 'dcv_6', 'gdcv_6', 'DET:BAND 20', 3.0, 0.004)
    # 10V
    _thdmm = Call('dc', 0.5, 'OUT 0.5 V', 'CONF:VOLT:DC 10', 'dcv_7', 'gdcv_7', 'DET:BAND 20', 3.0, 0.013)
    _thdmm = Call('dc', 5.0, 'OUT 5 V', 'CONF:VOLT:DC 10', 'dcv_8', 'gdcv_8', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 9.5, 'OUT 9.5 V', 'CONF:VOLT:DC 10', 'dcv_9', 'gdcv_9', 'DET:BAND 20', 3.0, 0.004)
    # 100V
    _thdmm = Call('dc', 5.0, 'OUT 5 V', 'CONF:VOLT:DC 100', 'dcv_10', 'gdcv_10', 'DET:BAND 20', 3.0, 0.016)
    _thdmm = Call('dc', 50.0, 'OUT 50 V', 'CONF:VOLT:DC 100', 'dcv_11', 'gdcv_11', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 95.0, 'OUT 95 V', 'CONF:VOLT:DC 100', 'dcv_12', 'gdcv_12', 'DET:BAND 20', 3.0, 0.005)
    # 1000V
    _thdmm = Call('dc', 50.0, 'OUT 50 V', 'CONF:VOLT:DC 1000', 'dcv_13', 'gdcv_13', 'DET:BAND 20', 3.0, 0.016)
    _thdmm = Call('dc', 500.0, 'OUT 500 V', 'CONF:VOLT:DC 1000', 'dcv_14', 'gdcv_14', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 950.0, 'OUT 950 V', 'CONF:VOLT:DC 1000', 'dcv_15', 'gdcv_15', 'DET:BAND 20', 3.0, 0.005)	
if self.acv_var.get() == 1:
    _thdmm = Reset()
     # ~0.1V,10Hz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_1', 'gacv_1', 'DET:BAND 3', 8.0, 0.7)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_2', 'gacv_2', 'DET:BAND 3', 8.0, 0.16)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv_3', 'gacv_3', 'DET:BAND 3', 8.0, 0.132)
    # ~1V,10Hz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_4', 'gacv_4', 'DET:BAND 3', 8.0, 0.7)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_5', 'gacv_5', 'DET:BAND 3', 8.0, 0.16)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv_6', 'gacv_6', 'DET:BAND 3', 8.0, 0.132)
    # ~10V,10Hz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_7', 'gacv_7', 'DET:BAND 3', 8.0, 0.7)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_8', 'gacv_8', 'DET:BAND 3', 8.0, 0.16)
    _thdmm = Call('ac', 9.5, 'OUT 9.5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv_9', 'gacv_9', 'DET:BAND 3', 8.0, 0.132)
    # ~100V,10Hz
    _thdmm = Call('ac', 5, 'OUT 5 V, 10 Hz', 'CONF:VOLT:AC 100', 'acv_10', 'gacv_10', 'DET:BAND 3', 8.0, 0.7)
    # ~0.1V,50Hz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_11', 'gacv_11', 'DET:BAND 20', 5.0, 0.66)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_12', 'gacv_12', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 50 Hz', 'CONF:VOLT:AC 0.1', 'acv_13', 'gacv_13', 'DET:BAND 20', 5.0, 0.092)
    # ~1V,50Hz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_14', 'gacv_14', 'DET:BAND 20', 5.0, 0.66)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_15', 'gacv_15', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 50 Hz', 'CONF:VOLT:AC 1.0', 'acv_16', 'gacv_16', 'DET:BAND 20', 5.0, 0.092)
    # ~10V,50Hz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_17', 'gacv_17', 'DET:BAND 20', 5.0, 0.66)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_18', 'gacv_18', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 9.5, 'OUT 9.5 V, 50 Hz', 'CONF:VOLT:AC 10.0', 'acv_19', 'gacv_19', 'DET:BAND 20', 5.0, 0.092)
    # ~100V,50Hz
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_20', 'gacv_20', 'DET:BAND 20', 5.0, 0.66)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_21', 'gacv_21', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 95.0, 'OUT 95 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_22', 'gacv_22', 'DET:BAND 20', 5.0, 0.092)	
    # ~750V,50Hz
    _thdmm = Call('ac', 37.5, 'OUT 37.5 V, 50 Hz', 'CONF:VOLT:AC 750.0', 'acv_23', 'gacv_23', 'DET:BAND 20', 5.0, 0.66)
    _thdmm = Call('ac', 375.0, 'OUT 375 V, 50 Hz', 'CONF:VOLT:AC 750.0', 'acv_24', 'gacv_24', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('ac', 712.5, 'OUT 712.5 V, 50 Hz', 'CONF:VOLT:AC 750.0', 'acv_25', 'gacv_25', 'DET:BAND 20', 5.0, 0.092)	
    # ~0.1V,20кHz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 20000 Hz', 'CONF:VOLT:AC 0.1', 'acv_26', 'gacv_26', 'DET:BAND 20', 5.0, 1.1)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 20000 Hz', 'CONF:VOLT:AC 0.1', 'acv_27', 'gacv_27', 'DET:BAND 20', 5.0, 0.2)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 20000 Hz', 'CONF:VOLT:AC 0.1', 'acv_28', 'gacv_28', 'DET:BAND 20', 5.0, 0.153)
    # ~1V,20kHz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 20000 Hz', 'CONF:VOLT:AC 1.0', 'acv_29', 'gacv_29', 'DET:BAND 20', 5.0, 1.1)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 20000 Hz', 'CONF:VOLT:AC 1.0', 'acv_30', 'gacv_30', 'DET:BAND 20', 5.0, 0.2)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 20000 Hz', 'CONF:VOLT:AC 1.0', 'acv_31', 'gacv_31', 'DET:BAND 20', 5.0, 0.153)
    # ~10V,20kHz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 20000 Hz', 'CONF:VOLT:AC 10.0', 'acv_32', 'gacv_32', 'DET:BAND 20', 5.0, 1.1)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 20000 Hz', 'CONF:VOLT:AC 10.0', 'acv_33', 'gacv_33', 'DET:BAND 20', 5.0, 0.2)
    _thdmm = Call('ac', 9.5, 'OUT 9.5 V, 20000 Hz', 'CONF:VOLT:AC 10.0', 'acv_34', 'gacv_34', 'DET:BAND 20', 5.0, 0.153)
    # ~100V,20kHz
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 20000 Hz', 'CONF:VOLT:AC 100', 'acv_35', 'gacv_35', 'DET:BAND 20', 5.0, 1.1)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 20000 Hz', 'CONF:VOLT:AC 100', 'acv_36', 'gacv_36', 'DET:BAND 200', 5.0, 0.2)
    _thdmm = Call('ac', 95.0, 'OUT 95 V, 20000 Hz', 'CONF:VOLT:AC 100', 'acv_37', 'gacv_37', 'DET:BAND 20', 5.0, 0.153)
    # ~750V,20kHz
    _thdmm = Call('ac', 37.5, 'OUT 37.5 V, 20000 Hz', 'CONF:VOLT:AC 750', 'acv_38', 'gacv_38', 'DET:BAND 20', 5.0, 1.1)
    # ~0.1V,50кHz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 50000 Hz', 'CONF:VOLT:AC 0.1', 'acv_39', 'gacv_39', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 50000 Hz', 'CONF:VOLT:AC 0.1', 'acv_40', 'gacv_40', 'DET:BAND 20', 5.0, 0.56)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 50000 Hz', 'CONF:VOLT:AC 0.1', 'acv_41', 'gacv_41', 'DET:BAND 20', 5.0, 0.484)
    # ~1V,50kHz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 50000 Hz', 'CONF:VOLT:AC 1.0', 'acv_42', 'gacv_42', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 50000 Hz', 'CONF:VOLT:AC 1.0', 'acv_43', 'gacv_43', 'DET:BAND 20', 5.0, 0.56)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 50000 Hz', 'CONF:VOLT:AC 1.0', 'acv_44', 'gacv_44', 'DET:BAND 20', 5.0, 0.484)
    # ~10V,50kHz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 50000 Hz', 'CONF:VOLT:AC 10.0', 'acv_45', 'gacv_45', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 50000 Hz', 'CONF:VOLT:AC 10.0', 'acv_46', 'gacv_46', 'DET:BAND 20', 5.0, 0.56)
    _thdmm = Call('ac', 9.5, 'OUT 9.5 V, 50000 Hz', 'CONF:VOLT:AC 10.0', 'acv_47', 'gacv_47', 'DET:BAND 20', 5.0, 0.484)
    # ~100V,50kHz
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 50000 Hz', 'CONF:VOLT:AC 100', 'acv_48', 'gacv_48', 'DET:BAND 20', 5.0, 2.0)
    # ~0.1V,100кHz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 100000 Hz', 'CONF:VOLT:AC 0.1', 'acv_49', 'gacv_49', 'DET:BAND 20', 5.0, 11.2)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 100000 Hz', 'CONF:VOLT:AC 0.1', 'acv_50', 'gacv_50', 'DET:BAND 20', 5.0, 2.2)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 100000 Hz', 'CONF:VOLT:AC 0.1', 'acv_51', 'gacv_51', 'DET:BAND 20', 5.0, 1.726)
    # ~1V,100kHz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 100000 Hz', 'CONF:VOLT:AC 1.0', 'acv_52', 'gacv_52', 'DET:BAND 20', 5.0, 11.2)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 100000 Hz', 'CONF:VOLT:AC 1.0', 'acv_53', 'gacv_53', 'DET:BAND 20', 5.0, 2.2)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 100000 Hz', 'CONF:VOLT:AC 1.0', 'acv_54', 'gacv_54', 'DET:BAND 20', 5.0, 1.726)
    # ~10V,100kHz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 100000 Hz', 'CONF:VOLT:AC 10.0', 'acv_55', 'gacv_55', 'DET:BAND 20', 5.0, 11.2)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 100000 Hz', 'CONF:VOLT:AC 10.0', 'acv_56', 'gacv_56', 'DET:BAND 20', 5.0, 2.2)
    _thdmm = Call('ac', 9.5, 'OUT 9.5 V, 100000 Hz', 'CONF:VOLT:AC 10.0', 'acv_57', 'gacv_57', 'DET:BAND 20', 5.0, 1.726)
    # ~100V,100kHz
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 100000 Hz', 'CONF:VOLT:AC 100', 'acv_58', 'gacv_58', 'DET:BAND 20', 5.0, 11.2)
    # ~0.1V,300kHz
    _thdmm = Call('ac', 0.005, 'OUT 0.005 V, 300000 Hz', 'CONF:VOLT:AC 0.1', 'acv_59', 'gacv_59', 'DET:BAND 3', 5.0, 11.2)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 300000 Hz', 'CONF:VOLT:AC 0.1', 'acv_60', 'gacv_60', 'DET:BAND 3', 5.0, 2.2)
    _thdmm = Call('ac', 0.095, 'OUT 0.095 V, 300000 Hz', 'CONF:VOLT:AC 0.1', 'acv_61', 'gacv_61', 'DET:BAND 3', 5.0, 1.726)
    # ~1V,300kHz
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 300000 Hz', 'CONF:VOLT:AC 1.0', 'acv_62', 'gacv_62', 'DET:BAND 20', 5.0, 11.2)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 300000 Hz', 'CONF:VOLT:AC 1.0', 'acv_63', 'gacv_63', 'DET:BAND 20', 5.0, 2.2)
    _thdmm = Call('ac', 0.95, 'OUT 0.95 V, 300000 Hz', 'CONF:VOLT:AC 1.0', 'acv_64', 'gacv_64', 'DET:BAND 20', 5.0, 1.726)
    # ~10V,300kHz
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 300000 Hz', 'CONF:VOLT:AC 10', 'acv_65', 'gacv_65', 'DET:BAND 20', 5.0, 11.2)
if self.f_var.get() == 1:
    _thdmm = Reset()
    # 5Hz
    _thdmm = Call('fr', 5.0, 'OUT 0.1 V, 5.0 Hz', 'CONF:FREQ 5.0 Hz', 'f_1', 'gf_1', 'DET:BAND 20', 5.0, 0.07)
    _thdmm = Call('fr', 5.0, 'OUT 10.0 V, 5.0 Hz', 'CONF:FREQ 5.0 Hz', 'f_2', 'gf_2', 'DET:BAND 20', 5.0, 0.07)
    # 10Hz
    _thdmm = Call('fr', 10.0, 'OUT 0.1 V, 10.0 Hz', 'CONF:FREQ 10.0 Hz', 'f_3', 'gf_3', 'DET:BAND 20', 5.0, 0.04)
    _thdmm = Call('fr', 10.0, 'OUT 10.0 V, 10.0 Hz', 'CONF:FREQ 10.0 Hz', 'f_4', 'gf_4', 'DET:BAND 20', 5.0, 0.04)
    # 40Hz
    _thdmm = Call('fr', 40.0, 'OUT 0.1 V, 40.0 Hz', 'CONF:FREQ 40.0 Hz', 'f_5', 'gf_5', 'DET:BAND 20', 5.0, 0.02)
    _thdmm = Call('fr', 40.0, 'OUT 10.0 V, 40.0 Hz', 'CONF:FREQ 40.0 Hz', 'f_6', 'gf_6', 'DET:BAND 20', 5.0, 0.02)	
    # 1kHz
    _thdmm = Call('fr', 1.0E+3, 'OUT 0.1 V, 1.0 kHz', 'CONF:FREQ 1.0 kHz', 'f_7', 'gf_7', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('fr', 1.0E+3, 'OUT 10.0 V, 1.0 kHz', 'CONF:FREQ 1.0 kHz', 'f_8', 'gf_8', 'DET:BAND 20', 5.0, 0.005)
    # 100kHz
    _thdmm = Call('fr', 100.0E+3, 'OUT 0.1 V, 100.0 kHz', 'CONF:FREQ 100.0 kHz', 'f_9', 'gf_9', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('fr', 100.0E+3, 'OUT 10.0 V, 100.0 kHz', 'CONF:FREQ 100.0 kHz', 'f_10', 'gf_10', 'DET:BAND 20', 5.0, 0.005)
    # 300kHz
    _thdmm = Call('fr', 300.0E+3, 'OUT 0.1 V, 300.0 kHz', 'CONF:FREQ 300.0 kHz', 'f_11', 'gf_11', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('fr', 300.0E+3, 'OUT 10.0 V, 300.0 kHz', 'CONF:FREQ 300.0 kHz', 'f_12', 'gf_12', 'DET:BAND 20', 5.0, 0.005)
if self.c_var.get() == 1:
    # 1NF
    _th = Message('Измерение ёмкости.\nВытащите красный провод из каллибратора\nдля компенсации проводов')
    _th = cap()
    _th = Message('Верните провод на место')
    _thdmm = Call('cap', 0.35E-9, 'OUT 0.35 NF', 'CONF:CAP 1 NF', 'c_1', 'gc_1', 'DET:BAND 20', 5.0, 1.929)
    _thdmm = Call('cap', 0.5E-9, 'OUT 0.5 NF', 'CONF:CAP 1 NF', 'c_2', 'gc_2', 'DET:BAND 20', 5.0, 1.5)
    _thdmm = Call('cap', 0.95E-9, 'OUT 0.95 NF', 'CONF:CAP 1 NF', 'c_3', 'gc_3', 'DET:BAND 20', 5.0, 1.026)
    # 10NF
    _thdmm = Call('cap', 0.5E-9, 'OUT 0.5 NF', 'CONF:CAP 10 NF', 'c_4', 'gc_4', 'DET:BAND 20', 5.0, 2.4)
    _thdmm = Call('cap', 5.0E-9, 'OUT 5.0 NF', 'CONF:CAP 10 NF', 'c_5', 'gc_5', 'DET:BAND 20', 5.0, 0.6)
    _thdmm = Call('cap', 9.5E-9, 'OUT 9.5 NF', 'CONF:CAP 10 NF', 'c_6', 'gc_6', 'DET:BAND 20', 5.0, 0.505)
    # 100NF
    _thdmm = Call('cap', 5.0E-9, 'OUT 5.0 NF', 'CONF:CAP 100 NF', 'c_7', 'gc_7', 'DET:BAND 20', 5.0, 2.4)
    _thdmm = Call('cap', 50.0E-9, 'OUT 50.0 NF', 'CONF:CAP 100 NF', 'c_8', 'gc_8', 'DET:BAND 20', 5.0, 0.6)
    _thdmm = Call('cap', 95.0E-9, 'OUT 95.0 NF', 'CONF:CAP 100 NF', 'c_9', 'gc_9', 'DET:BAND 20', 5.0, 0.505)
    # 1000NF
    _thdmm = Call('cap', 50.0E-9, 'OUT 50.0 NF', 'CONF:CAP 1 UF', 'c_10', 'gc_10', 'DET:BAND 20', 5.0, 2.4)
    _thdmm = Call('cap', 500.0E-9, 'OUT 500.0 NF', 'CONF:CAP 1 UF', 'c_11', 'gc_11', 'DET:BAND 20', 5.0, 0.6)
    _thdmm = Call('cap', 950.0E-9, 'OUT 950.0 NF', 'CONF:CAP 1 UF', 'c_12', 'gc_12', 'DET:BAND 20', 5.0, 0.505)
    # 10000NF
    _thdmm = Call('cap', 500.0E-9, 'OUT 500.0 NF', 'CONF:CAP 10 UF', 'c_13', 'gc_13', 'DET:BAND 20', 5.0, 2.4)
    _thdmm = Call('cap', 5000.0E-9, 'OUT 5000.0 NF', 'CONF:CAP 10 UF', 'c_14', 'gc_14', 'DET:BAND 20', 5.0, 0.6)
    _thdmm = Call('cap', 9500.0E-9, 'OUT 9500.0 NF', 'CONF:CAP 10 UF', 'c_15', 'gc_15', 'DET:BAND 20', 5.0, 0.505)	
if self.dci_var.get() == 1:
    _th = Message('Переключите провода\n для измерения тока')
    _th = Reset()
    # 0.0001A
    _thdmm = Call('dci', 0.000005, 'OUT 0.000005 A', 'CONF:CURR:DC 0.0001', 'dci_1', 'gdci_1', 'DET:BAND 20', 5.0, 0.55)
    _thdmm = Call('dci', 0.00005, 'OUT 0.00005 A', 'CONF:CURR:DC 0.0001', 'dci_2', 'gdci_2', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('dci', 0.000095, 'OUT 0.000095 A', 'CONF:CURR:DC 0.0001', 'dci_3', 'gdci_3', 'DET:BAND 20', 5.0, 0.076)
    # 0.001A
    _thdmm = Call('dci', 0.00005, 'OUT 0.00005 A', 'CONF:CURR:DC 0.001', 'dci_4', 'gdci_4', 'DET:BAND 20', 5.0, 0.17)
    _thdmm = Call('dci', 0.0005, 'OUT 0.0005 A', 'CONF:CURR:DC 0.001', 'dci_5', 'gdci_5', 'DET:BAND 20', 5.0, 0.062)
    _thdmm = Call('dci', 0.00095, 'OUT 0.00095 A', 'CONF:CURR:DC 0.001', 'dci_6', 'gdci_6', 'DET:BAND 20', 5.0, 0.056)
    # 0.01A
    _thdmm = Call('dci', 0.0005, 'OUT 0.0005 A', 'CONF:CURR:DC 0.01', 'dci_7', 'gdci_7', 'DET:BAND 20', 5.0, 0.45)
    _thdmm = Call('dci', 0.005, 'OUT 0.005 A', 'CONF:CURR:DC 0.01', 'dci_8', 'gdci_8', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('dci', 0.0095, 'OUT 0.0095 A', 'CONF:CURR:DC 0.01', 'dci_9', 'gdci_9', 'DET:BAND 20', 5.0, 0.071)
    # 0.1A
    _thdmm = Call('dci', 0.005, 'OUT 0.005 A', 'CONF:CURR:DC 0.1', 'dci_10', 'gdci_10', 'DET:BAND 20', 5.0, 0.15)
    _thdmm = Call('dci', 0.05, 'OUT 0.05 A', 'CONF:CURR:DC 0.1', 'dci_11', 'gdci_11', 'DET:BAND 20', 5.0, 0.06)
    _thdmm = Call('dci', 0.095, 'OUT 0.095 A', 'CONF:CURR:DC 0.1', 'dci_12', 'gdci_12', 'DET:BAND 20', 5.0, 0.055)
    # 1A
    _thdmm = Call('dci', 0.05, 'OUT 0.05 A', 'CONF:CURR:DC 1.0', 'dci_13', 'gdci_13', 'DET:BAND 20', 5.0, 0.3)
    _thdmm = Call('dci', 0.5, 'OUT 0.5 A', 'CONF:CURR:DC 1.0', 'dci_14', 'gdci_14', 'DET:BAND 20', 5.0, 0.12)
    _thdmm = Call('dci', 0.95, 'OUT 0.95 A', 'CONF:CURR:DC 1.0', 'dci_15', 'gdci_15', 'DET:BAND 20', 5.0, 0.111)
    # 3A
    _thdmm = Call('dci', 0.15, 'OUT 0.15 A', 'CONF:CURR:DC 3.0', 'dci_16', 'gdci_16', 'DET:BAND 20', 5.0, 0.55)
    _thdmm = Call('dci', 1.5, 'OUT 1.5 A', 'CONF:CURR:DC 3.0', 'dci_17', 'gdci_17', 'DET:BAND 20', 5.0, 0.19)
    if self.b1[1] == '5500E':
        _thdmm = Call('dci', 2.85, 'OUT 2.85 A', 'CONF:CURR:DC 3.0', 'dci_18', 'gdci_18', 'DET:BAND 20', 5.0, 0.171)
    elif self.b1[1] == '5522A':
        _th = Message('Переключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        _thdmm = Call('dci', 2.85, 'OUT 2.85 A', 'CONF:CURR:DC 3.0', 'dci_18', 'gdci_18', 'DET:BAND 20', 5.0, 0.171)
        _th = Message('Верните провод на КАЛИБРАТОРЕ обратно в разъем меньше 2,5 А')
if self.aci_var.get() == 1:
    _thdmm = Reset()
    # ~0.0001A, 50Hz
    _thdmm = Call('aci', 0.00003, 'OUT 0.00003 A, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_1', 'gaci_1', 'DET:BAND 20', 5.0, 0.143)
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_2', 'gaci_2', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('aci', 0.000095, 'OUT 0.000095 A, 50 Hz', 'CONF:CURR:AC 0.0001', 'aci_3', 'gaci_3', 'DET:BAND 20', 5.0, 0.052)
    # ~0.001A, 50Hz
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_4', 'gaci_4', 'DET:BAND 20', 5.0, 0.81)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_5', 'gaci_5', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('aci', 0.00095, 'OUT 0.00095 A, 50 Hz', 'CONF:CURR:AC 0.001', 'aci_6', 'gaci_6', 'DET:BAND 20', 5.0, 0.052)
    # ~0.01A, 50Hz
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_7', 'gaci_7', 'DET:BAND 20', 5.0, 0.81)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_8', 'gaci_8', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('aci', 0.0095, 'OUT 0.0095 A, 50 Hz', 'CONF:CURR:AC 0.01', 'aci_9', 'gaci_9', 'DET:BAND 20', 5.0, 0.052)
    # ~0.1A, 50Hz
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_10', 'gaci_10', 'DET:BAND 20', 5.0, 0.81)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_11', 'gaci_11', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('aci', 0.095, 'OUT 0.095 A, 50 Hz', 'CONF:CURR:AC 0.1', 'aci_12', 'gaci_12', 'DET:BAND 20', 5.0, 0.052)
    # ~1A, 50Hz
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_13', 'gaci_13', 'DET:BAND 20', 5.0, 0.81)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_14', 'gaci_14', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('aci', 0.95, 'OUT 0.95 A, 50 Hz', 'CONF:CURR:AC 1.0', 'aci_15', 'gaci_15', 'DET:BAND 20', 5.0, 0.052)
    # ~3A, 50Hz
    _thdmm = Call('aci', 0.15, 'OUT 0.15 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_16', 'gaci_16', 'DET:BAND 20', 5.0, 0.81)
    _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_17', 'gaci_17', 'DET:BAND 20', 5.0, 0.09)
    if self.b1[1] == '5500E':
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_18', 'gaci_18', 'DET:BAND 20', 8.0, 0.052)
    # ~0.0001A, 5kHz
    _thdmm = Call('aci', 0.00003, 'OUT 0.00003 A, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_19', 'gaci_19', 'DET:BAND 20', 5.0, 0.153)
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_20', 'gaci_20', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.000095, 'OUT 0.000095 A, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_21', 'gaci_21', 'DET:BAND 20', 5.0, 0.062)
    # ~0.001A, 5kHz
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_22', 'gaci_22', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_23', 'gaci_23', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.00095, 'OUT 0.00095 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_24', 'gaci_24', 'DET:BAND 20', 5.0, 0.062)
    # ~0.01A, 5kHz
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_25', 'gaci_25', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_26', 'gaci_26', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.0095, 'OUT 0.0095 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_27', 'gaci_27', 'DET:BAND 20', 5.0, 0.062)
    # ~0.1A, 5kHz
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_28', 'gaci_28', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_29', 'gaci_29', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.095, 'OUT 0.095 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_30', 'gaci_30', 'DET:BAND 20', 5.0, 0.062)
    # ~1A, 5kHz
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_31', 'gaci_31', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_32', 'gaci_32', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.95, 'OUT 0.95 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_33', 'gaci_33', 'DET:BAND 20', 5.0, 0.062)
    # ~3A, 5kHz
    _thdmm = Call('aci', 0.15, 'OUT 0.15 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_34', 'gaci_34', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_35', 'gaci_35', 'DET:BAND 20', 5.0, 0.1)
    if self.b1[1] == '5500E':
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_36', 'gaci_36', 'DET:BAND 20', 5.0, 0.062)
    # ~0.0001A, 10kHz
    _thdmm = Call('aci', 0.00003, 'OUT 0.00003 A, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_37', 'gaci_37', 'DET:BAND 20', 5.0, 0.153)
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_38', 'gaci_38', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.000095, 'OUT 0.000095 A, 10 kHz', 'CONF:CURR:AC 0.0001', 'aci_39', 'gaci_39', 'DET:BAND 20', 5.0, 0.062)
    # ~0.001A, 10kHz
    _thdmm = Call('aci', 0.00005, 'OUT 0.00005 A, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_40', 'gaci_40', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_41', 'gaci_41', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.00095, 'OUT 0.00095 A, 10 kHz', 'CONF:CURR:AC 0.001', 'aci_42', 'gaci_42', 'DET:BAND 20', 5.0, 0.062)
    # ~0.01A, 10kHz
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_43', 'gaci_43', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_44', 'gaci_44', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.0095, 'OUT 0.0095 A, 10 kHz', 'CONF:CURR:AC 0.01', 'aci_45', 'gaci_45', 'DET:BAND 20', 5.0, 0.062)
    # ~0.1A, 10kHz
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_46', 'gaci_46', 'DET:BAND 20', 5.0, 0.82)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_47', 'gaci_47', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('aci', 0.095, 'OUT 0.095 A, 10 kHz', 'CONF:CURR:AC 0.1', 'aci_48', 'gaci_48', 'DET:BAND 20', 5.0, 0.062)
    # ~1A, 10kHz
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_49', 'gaci_49', 'DET:BAND 20', 5.0, 0.82)
    if self.b1[1] == '5500E':
        _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_50', 'gaci_50', 'DET:BAND 20', 5.0, 0.1)
        _thdmm = Call('aci', 0.95, 'OUT 0.95 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_51', 'gaci_51', 'DET:BAND 20', 5.0, 0.062)
    elif self.b1[1] == '5522A':
        _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_50', 'gaci_50', 'DET:BAND 20', 5.0, 0.1)
        _thdmm = Call('aci', 0.95, 'OUT 0.95 A, 10 kHz', 'CONF:CURR:AC 1.0', 'aci_51', 'gaci_51', 'DET:BAND 20', 5.0, 0.062)
    # ~3A, 10kHz
    _thdmm = Call('aci', 0.15, 'OUT 0.15 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_52', 'gaci_52', 'DET:BAND 20', 5.0, 0.82)
    if self.b1[1] == '5500E':
        _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_53', 'gaci_53', 'DET:BAND 20', 5.0, 0.1)
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_54', 'gaci_54', 'DET:BAND 20', 5.0, 0.062)
    elif self.b1[1] == '5522A':
        _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_53', 'gaci_53', 'DET:BAND 20', 5.0, 0.1)
    if self.b1[1] == '5522A':
        _th = Message('Переключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 50 Hz', 'CONF:CURR:AC 3.0', 'aci_18', 'gaci_18', 'DET:BAND 20', 8.0, 0.052)
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_36', 'gaci_36', 'DET:BAND 20', 5.0, 0.062)
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 10 kHz', 'CONF:CURR:AC 3.0', 'aci_54', 'gaci_54', 'DET:BAND 20', 5.0, 0.062)
if self.r4_var.get() == 1:
    _th = Message('Переключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    # 100Ohm-4-wire
    _thdmm = Call('res4', 5.0, 'OUT 5 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 'gr4_1', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('res4', 50.0, 'OUT 50 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_2', 'gr4_2', 'DET:BAND 20', 5.0, 0.018)
    _thdmm = Call('res4', 95.0, 'OUT 95 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_3', 'gr4_3', 'DET:BAND 20', 5.0, 0.014)
    # 1kOhm-4-wire
    _thdmm = Call('res4', 50.0, 'OUT 50 OHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_4', 'gr4_4', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res4', 500.0, 'OUT 500 OHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_5', 'gr4_5', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res4', 950.0, 'OUT 950 OHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_6', 'gr4_6', 'DET:BAND 20', 5.0, 0.011)
    # 10kOhm-4-wire
    _thdmm = Call('res4', 500.0, 'OUT 500 OHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_7', 'gr4_7', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res4', 5000.0, 'OUT 5000 OHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_8', 'gr4_8', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res4', 9500.0, 'OUT 9500 OHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_9', 'gr4_9', 'DET:BAND 20', 5.0, 0.011)
    # 100kOhm-4-wire
    _thdmm = Call('res4', 5000.0, 'OUT 5000 OHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_10', 'gr4_10', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res4', 50000.0, 'OUT 50000 OHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_11', 'gr4_11', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res4', 95000.0, 'OUT 95000 OHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_12', 'gr4_12', 'DET:BAND 20', 5.0, 0.011)
if self.r2_var.get() == 1:
    _th = Message('Переключите провода по двухпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    # 1MOhm-2-wire
    _thdmm = Call('res2', 0.05E+6, 'OUT 0.05 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_1', 'gr2_1', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res2', 0.5E+6, 'OUT 0.5 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_2', 'gr2_2', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res2', 0.95E+6, 'OUT 0.95 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_3', 'gr2_3', 'DET:BAND 20', 5.0, 0.011)
    # 10MOhm-2-wire
    _thdmm = Call('res2', 0.5E+6, 'OUT 0.5 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_4', 'gr2_4', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res2', 5.0E+6, 'OUT 5.0 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_5', 'gr2_5', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res2', 9.5E+6, 'OUT 9.5 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_6', 'gr2_6', 'DET:BAND 20', 5.0, 0.011)
    # 100MOhm-2-wire
    _thdmm = Call('res2', 5.0E+6, 'OUT 5.0 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_7', 'gr2_7', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('res2', 50.0E+6, 'OUT 50.0 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_8', 'gr2_8', 'DET:BAND 20', 5.0, 0.012)
    _thdmm = Call('res2', 95.0E+6, 'OUT 95.0 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_9', 'gr2_9', 'DET:BAND 20', 5.0, 0.011)
    # 1GOhm-2-wire
    _thdmm = Call('res2', 50.0E+6, 'OUT 50.0 MOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_10', 'gr2_10', 'DET:BAND 20', 5.0, 0.03)
    if self.b1[1] == '5522A':
        _thdmm = Call('res2', 500.0E+6, 'OUT 500.0 MOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_11', 'gr2_11', 'DET:BAND 20', 5.0, 0.012)
        _thdmm = Call('res2', 950.0E+6, 'OUT 950.0 MOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_12', 'gr2_12', 'DET:BAND 20', 5.0, 0.011)

_th = Message('Калибровка завершена')
_th = Reset()