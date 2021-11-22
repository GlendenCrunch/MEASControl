# -*- coding: utf-8 -*-
if self.dcv_var.get() == 1:
    _th = Message('Соедините провода для измерения постоянного напряжения')
    _th = Reset()        
    # 0.1V
    _thdmm = Call('dc', 0.01, 'OUT 0.01 V', 'CONF:VOLT:DC 0.1', 'dcv_1', 'gdcv_1', 'DET:BAND 20', 3.0, 0.04)
    _thdmm = Call('dc', 0.03, 'OUT 0.03 V', 'CONF:VOLT:DC 0.1', 'dcv_2', 'gdcv_2', 'DET:BAND 20', 3.0, 0.017)
    _thdmm = Call('dc', 0.05, 'OUT 0.05 V', 'CONF:VOLT:DC 0.1', 'dcv_3', 'gdcv_3', 'DET:BAND 20', 3.0, 0.012)
    _thdmm = Call('dc', 0.07, 'OUT 0.07 V', 'CONF:VOLT:DC 0.1', 'dcv_4', 'gdcv_4', 'DET:BAND 20', 3.0, 0.01)
    _thdmm = Call('dc', 0.1, 'OUT 0.1 V', 'CONF:VOLT:DC 0.1', 'dcv_5', 'gdcv_5', 'DET:BAND 20', 3.0, 0.009)
    # 1V
    _thdmm = Call('dc', 0.1, 'OUT 0.1 V', 'CONF:VOLT:DC 1.0', 'dcv_6', 'gdcv_6', 'DET:BAND 20', 3.0, 0.008)
    _thdmm = Call('dc', 0.3, 'OUT 0.3 V', 'CONF:VOLT:DC 1.0', 'dcv_7', 'gdcv_7', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 0.5, 'OUT 0.5 V', 'CONF:VOLT:DC 1.0', 'dcv_8', 'gdcv_8', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 0.7, 'OUT 0.7 V', 'CONF:VOLT:DC 1.0', 'dcv_9', 'gdcv_9', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 1.0, 'OUT 1.0 V', 'CONF:VOLT:DC 1.0', 'dcv_10', 'gdcv_10', 'DET:BAND 20', 3.0, 0.004)
    # 10V
    _thdmm = Call('dc', 1.0, 'OUT 1.0 V', 'CONF:VOLT:DC 10', 'dcv_11', 'gdcv_11', 'DET:BAND 20', 3.0, 0.007)
    _thdmm = Call('dc', 3.0, 'OUT 3.0 V', 'CONF:VOLT:DC 10', 'dcv_12', 'gdcv_12', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 5.0, 'OUT 5.0 V', 'CONF:VOLT:DC 10', 'dcv_13', 'gdcv_13', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 7.0, 'OUT 7.0 V', 'CONF:VOLT:DC 10', 'dcv_14', 'gdcv_14', 'DET:BAND 20', 3.0, 0.004)
    _thdmm = Call('dc', 10.0, 'OUT 10.0 V', 'CONF:VOLT:DC 10', 'dcv_15', 'gdcv_15', 'DET:BAND 20', 3.0, 0.003)
    # 100V
    _thdmm = Call('dc', 10.0, 'OUT 10 V', 'CONF:VOLT:DC 100', 'dcv_16', 'gdcv_16', 'DET:BAND 20', 3.0, 0.01)
    _thdmm = Call('dc', 30.0, 'OUT 30 V', 'CONF:VOLT:DC 100', 'dcv_17', 'gdcv_17', 'DET:BAND 20', 3.0, 0.006)
    _thdmm = Call('dc', 50.0, 'OUT 50 V', 'CONF:VOLT:DC 100', 'dcv_18', 'gdcv_18', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 70.0, 'OUT 70 V', 'CONF:VOLT:DC 100', 'dcv_19', 'gdcv_19', 'DET:BAND 20', 3.0, 0.005)
    _thdmm = Call('dc', 100.0, 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv_20', 'gdcv_20', 'DET:BAND 20', 3.0, 0.005)
    # 1000V
    _thdmm = Call('dc', 100.0, 'OUT 100 V', 'CONF:VOLT:DC 1000', 'dcv_21', 'gdcv_21', 'DET:BAND 20', 3.0, 0.01)
    _thdmm = Call('dc', 300.0, 'OUT 300 V', 'CONF:VOLT:DC 1000', 'dcv_22', 'gdcv_22', 'DET:BAND 20', 3.0, 0.006)
    _thdmm = Call('dc', 500.0, 'OUT 500 V', 'CONF:VOLT:DC 1000', 'dcv_23', 'gdcv_23', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('dc', 700.0, 'OUT 700 V', 'CONF:VOLT:DC 1000', 'dcv_24', 'gdcv_24', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('dc', 1000.0, 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv_25', 'gdcv_25', 'DET:BAND 20', 5.0, 0.006)
if self.acv_var.get() == 1:
    _th = Reset()
    # ~0.1V,20Hz
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 20 Hz', 'CONF:VOLT:AC 0.1', 'acv_1', 'gacv_1', 'DET:BAND 3', 8.0, 0.25)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 20 Hz', 'CONF:VOLT:AC 0.1', 'acv_2', 'gacv_2', 'DET:BAND 3', 8.0, 0.117)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 20 Hz', 'CONF:VOLT:AC 0.1', 'acv_3', 'gacv_3', 'DET:BAND 3', 8.0, 0.09)
    _thdmm = Call('ac', 0.07, 'OUT 0.07 V, 20 Hz', 'CONF:VOLT:AC 0.1', 'acv_4', 'gacv_4', 'DET:BAND 3', 8.0, 0.079)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 20 Hz', 'CONF:VOLT:AC 0.1', 'acv_5', 'gacv_5', 'DET:BAND 3', 8.0, 0.07)
    # ~1V,20Hz
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 20 Hz', 'CONF:VOLT:AC 1.0', 'acv_6', 'gacv_6', 'DET:BAND 3', 8.0, 0.25)
    _thdmm = Call('ac', 0.3, 'OUT 0.3 V, 20 Hz', 'CONF:VOLT:AC 1.0', 'acv_7', 'gacv_7', 'DET:BAND 3', 8.0, 0.117)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 20 Hz', 'CONF:VOLT:AC 1.0', 'acv_8', 'gacv_8', 'DET:BAND 3', 8.0, 0.09)
    _thdmm = Call('ac', 0.7, 'OUT 0.7 V, 20 Hz', 'CONF:VOLT:AC 1.0', 'acv_9', 'gacv_9', 'DET:BAND 3', 8.0, 0.079)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 20 Hz', 'CONF:VOLT:AC 1.0', 'acv_10', 'gacv_10', 'DET:BAND 3', 8.0, 0.07)
    # ~10V,20Hz
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 20 Hz', 'CONF:VOLT:AC 10.0', 'acv_11', 'gacv_11', 'DET:BAND 3', 8.0, 0.25)
    _thdmm = Call('ac', 3.0, 'OUT 3 V, 20 Hz', 'CONF:VOLT:AC 10.0', 'acv_12', 'gacv_12', 'DET:BAND 3', 8.0, 0.117)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 20 Hz', 'CONF:VOLT:AC 10.0', 'acv_13', 'gacv_13', 'DET:BAND 3', 8.0, 0.09)
    _thdmm = Call('ac', 7.0, 'OUT 7 V, 20 Hz', 'CONF:VOLT:AC 10.0', 'acv_14', 'gacv_14', 'DET:BAND 3', 8.0, 0.079)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 20 Hz', 'CONF:VOLT:AC 10.0', 'acv_15', 'gacv_15', 'DET:BAND 3', 8.0, 0.07)
    # ~100V,20Hz
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 20 Hz', 'CONF:VOLT:AC 100', 'acv_16', 'gacv_16', 'DET:BAND 3', 8.0, 0.25)
    _thdmm = Call('ac', 30.0, 'OUT 30 V, 20 Hz', 'CONF:VOLT:AC 100', 'acv_17', 'gacv_17', 'DET:BAND 3', 8.0, 0.117)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_18', 'gacv_18', 'DET:BAND 3', 8.0, 0.09)
    _thdmm = Call('ac', 70.0, 'OUT 70 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_19', 'gacv_19', 'DET:BAND 3', 8.0, 0.079)
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 50 Hz', 'CONF:VOLT:AC 100', 'acv_20', 'gacv_20', 'DET:BAND 3', 8.0, 0.07)
    # ~0.1V,15kHz
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 15 kHz', 'CONF:VOLT:AC 0.1', 'acv_21', 'gacv_21', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 15 kHz', 'CONF:VOLT:AC 0.1', 'acv_22', 'gacv_22', 'DET:BAND 20', 5.0, 0.117)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 15 kHz', 'CONF:VOLT:AC 0.1', 'acv_23', 'gacv_23', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('ac', 0.07, 'OUT 0.07 V, 15 kHz', 'CONF:VOLT:AC 0.1', 'acv_24', 'gacv_24', 'DET:BAND 20', 5.0, 0.079)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 15 kHz', 'CONF:VOLT:AC 0.1', 'acv_25', 'gacv_25', 'DET:BAND 20', 5.0, 0.07)
    # ~1V,15kHz
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 15 kHz', 'CONF:VOLT:AC 1.0', 'acv_26', 'gacv_26', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 0.3, 'OUT 0.3 V, 15 kHz', 'CONF:VOLT:AC 1.0', 'acv_27', 'gacv_27', 'DET:BAND 20', 5.0, 0.117)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 15 kHz', 'CONF:VOLT:AC 1.0', 'acv_28', 'gacv_28', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('ac', 0.7, 'OUT 0.7 V, 15 kHz', 'CONF:VOLT:AC 1.0', 'acv_29', 'gacv_29', 'DET:BAND 20', 5.0, 0.079)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 15 kHz', 'CONF:VOLT:AC 1.0', 'acv_30', 'gacv_30', 'DET:BAND 20', 5.0, 0.07)
    # ~10V,15kHz
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 15 kHz', 'CONF:VOLT:AC 10.0', 'acv_31', 'gacv_31', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 3.0, 'OUT 3 V, 15 kHz', 'CONF:VOLT:AC 10.0', 'acv_32', 'gacv_32', 'DET:BAND 20', 5.0, 0.117)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 15 kHz', 'CONF:VOLT:AC 10.0', 'acv_33', 'gacv_33', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('ac', 7.0, 'OUT 7 V, 15 kHz', 'CONF:VOLT:AC 10.0', 'acv_34', 'gacv_34', 'DET:BAND 20', 5.0, 0.079)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 15 kHz', 'CONF:VOLT:AC 10.0', 'acv_35', 'gacv_35', 'DET:BAND 20', 5.0, 0.07)
    # ~100V,15kHz
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 15 kHz', 'CONF:VOLT:AC 100', 'acv_36', 'gacv_36', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 30.0, 'OUT 30 V, 15 kHz', 'CONF:VOLT:AC 100', 'acv_37', 'gacv_37', 'DET:BAND 20', 5.0, 0.117)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 15 kHz', 'CONF:VOLT:AC 100', 'acv_38', 'gacv_38', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('ac', 70.0, 'OUT 70 V, 15 kHz', 'CONF:VOLT:AC 100', 'acv_39', 'gacv_39', 'DET:BAND 20', 5.0, 0.079)
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 15 kHz', 'CONF:VOLT:AC 100', 'acv_40', 'gacv_40', 'DET:BAND 20', 5.0, 0.07)
    # ~750V,15kHz
    _thdmm = Call('ac', 75.0, 'OUT 75 V, 15 kHz', 'CONF:VOLT:AC 750', 'acv_41', 'gacv_41', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 225.0, 'OUT 225 V, 15 kHz', 'CONF:VOLT:AC 750', 'acv_42', 'gacv_42', 'DET:BAND 20', 5.0, 0.117)
    '''_thdmm = Call('ac', 375.0, 'OUT 375 V, 15 kHz', 'CONF:VOLT:AC 750', 'acv_43', 'gacv_43', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('ac', 525.0, 'OUT 525 V, 15 kHz', 'CONF:VOLT:AC 750', 'acv_44', 'gacv_44', 'DET:BAND 20', 5.0, 0.121)
    _thdmm = Call('ac', 750.0, 'OUT 750 V, 15 kHz', 'CONF:VOLT:AC 750', 'acv_45', 'gacv_45', 'DET:BAND 20', 5.0, 0.13)'''
    # ~0.1V,30kHz
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 30 kHz', 'CONF:VOLT:AC 0.1', 'acv_46', 'gacv_46', 'DET:BAND 20', 5.0, 0.37)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 30 kHz', 'CONF:VOLT:AC 0.1', 'acv_47', 'gacv_47', 'DET:BAND 20', 5.0, 0.17)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 30 kHz', 'CONF:VOLT:AC 0.1', 'acv_48', 'gacv_48', 'DET:BAND 20', 5.0, 0.13)
    _thdmm = Call('ac', 0.07, 'OUT 0.07 V, 30 kHz', 'CONF:VOLT:AC 0.1', 'acv_49', 'gacv_49', 'DET:BAND 20', 5.0, 0.113)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 30 kHz', 'CONF:VOLT:AC 0.1', 'acv_50', 'gacv_50', 'DET:BAND 20', 5.0, 0.1)
    # ~1V,30kHz
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 30 kHz', 'CONF:VOLT:AC 1.0', 'acv_51', 'gacv_51', 'DET:BAND 20', 5.0, 0.37)
    _thdmm = Call('ac', 0.3, 'OUT 0.3 V, 30 kHz', 'CONF:VOLT:AC 1.0', 'acv_52', 'gacv_52', 'DET:BAND 20', 5.0, 0.17)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 30 kHz', 'CONF:VOLT:AC 1.0', 'acv_53', 'gacv_53', 'DET:BAND 20', 5.0, 0.13)
    _thdmm = Call('ac', 0.7, 'OUT 0.7 V, 30 kHz', 'CONF:VOLT:AC 1.0', 'acv_54', 'gacv_54', 'DET:BAND 20', 5.0, 0.113)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 30 kHz', 'CONF:VOLT:AC 1.0', 'acv_55', 'gacv_55', 'DET:BAND 20', 5.0, 0.1)
    # ~10V,30kHz
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 30 kHz', 'CONF:VOLT:AC 10.0', 'acv_56', 'gacv_56', 'DET:BAND 20', 5.0, 0.37)
    _thdmm = Call('ac', 3.0, 'OUT 3 V, 30 kHz', 'CONF:VOLT:AC 10.0', 'acv_57', 'gacv_57, 'DET:BAND 20', 5.0, 0.17)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 30 kHz', 'CONF:VOLT:AC 10.0', 'acv_58', 'gacv_58', 'DET:BAND 20', 5.0, 0.13)
    _thdmm = Call('ac', 7.0, 'OUT 7 V, 30 kHz', 'CONF:VOLT:AC 10.0', 'acv_59', 'gacv_59', 'DET:BAND 20', 5.0, 0.113)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 30 kHz', 'CONF:VOLT:AC 10.0', 'acv_60', 'gacv_60', 'DET:BAND 20', 5.0, 0.1)
    # ~100V,30kHz
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 30 kHz', 'CONF:VOLT:AC 100', 'acv_61', 'gacv_61', 'DET:BAND 20', 5.0, 0.37)
    _thdmm = Call('ac', 30.0, 'OUT 30 V, 30 kHz', 'CONF:VOLT:AC 100', 'acv_62', 'gacv_62', 'DET:BAND 20', 5.0, 0.17)    
    if self.b1[1] == '5500E':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_63', 'gacv_63', 'DET:BAND 20', 5.0, 0.13)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_64', 'gacv_64', 'DET:BAND 20', 5.0, 0.113)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_65', 'gacv_65', 'DET:BAND 20', 5.0, 0.1)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 30 kHz', 'CONF:VOLT:AC 100', 'acv_63', 'gacv_63', 'DET:BAND 20', 5.0, 0.13)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 30 kHz', 'CONF:VOLT:AC 100', 'acv_64', 'gacv_64', 'DET:BAND 20', 5.0, 0.113)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 30 kHz', 'CONF:VOLT:AC 100', 'acv_65', 'gacv_65', 'DET:BAND 20', 5.0, 0.1)
    # ~750V,30kHz
    if self.b1[1] == '5500E':
        _thdmm = Call('ac', 75.0, 'OUT 75 V, 20 kHz', 'CONF:VOLT:AC 750', 'acv_66', 'gacv_66', 'DET:BAND 20', 5.0, 0.37)
        _thdmm = Call('ac', 225.0, 'OUT 225 V, 20 kHz', 'CONF:VOLT:AC 750', 'acv_67', 'gacv_67', 'DET:BAND 20', 5.0, 0.17)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 75.0, 'OUT 75 V, 30 kHz', 'CONF:VOLT:AC 750', 'acv_66', 'gacv_66', 'DET:BAND 20', 5.0, 0.37)
        _thdmm = Call('ac', 225.0, 'OUT 225 V, 30 kHz', 'CONF:VOLT:AC 750', 'acv_67', 'gacv_67', 'DET:BAND 20', 5.0, 0.17)
        '''_thdmm = Call('ac', 375.0, 'OUT 375 V, 10 kHz', 'CONF:VOLT:AC 750', 'acv_68', 'gacv_68', 'DET:BAND 20', 5.0, 0.13)
        _thdmm = Call('ac', 525.0, 'OUT 525 V, 10 kHz', 'CONF:VOLT:AC 750', 'acv_69', 'gacv_69', 'DET:BAND 20', 5.0, 0.156)
        _thdmm = Call('ac', 750.0, 'OUT 750 V, 10 kHz', 'CONF:VOLT:AC 750', 'acv_70', 'gacv_70', 'DET:BAND 20', 5.0, 0.16)'''
    # ~0.1V,70kHz
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 70 kHz', 'CONF:VOLT:AC 0.1', 'acv_71', 'gacv_71', 'DET:BAND 20', 5.0, 0.65)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 70 kHz', 'CONF:VOLT:AC 0.1', 'acv_72', 'gacv_72', 'DET:BAND 20', 5.0, 0.317)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 70 kHz', 'CONF:VOLT:AC 0.1', 'acv_73', 'gacv_73', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 0.07, 'OUT 0.07 V, 70 kHz', 'CONF:VOLT:AC 0.1', 'acv_74', 'gacv_74', 'DET:BAND 20', 5.0, 0.221)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 70 kHz', 'CONF:VOLT:AC 0.1', 'acv_75', 'gacv_75', 'DET:BAND 20', 5.0, 0.2)
    # ~1V,70kHz
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 70 kHz', 'CONF:VOLT:AC 1.0', 'acv_76', 'gacv_76', 'DET:BAND 20', 5.0, 0.65)
    _thdmm = Call('ac', 0.3, 'OUT 0.3 V, 70 kHz', 'CONF:VOLT:AC 1.0', 'acv_77', 'gacv_77', 'DET:BAND 20', 5.0, 0.317)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 70 kHz', 'CONF:VOLT:AC 1.0', 'acv_78', 'gacv_78', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 0.7, 'OUT 0.7 V, 70 kHz', 'CONF:VOLT:AC 1.0', 'acv_79', 'gacv_79', 'DET:BAND 20', 5.0, 0.221)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 70 kHz', 'CONF:VOLT:AC 1.0', 'acv_80', 'gacv_80', 'DET:BAND 20', 5.0, 0.2)
    # ~10V,70kHz
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 70 kHz', 'CONF:VOLT:AC 10.0', 'acv_81', 'gacv_81', 'DET:BAND 20', 5.0, 0.65)
    _thdmm = Call('ac', 3.0, 'OUT 3 V, 70 kHz', 'CONF:VOLT:AC 10.0', 'acv_82', 'gacv_82', 'DET:BAND 20', 5.0, 0.317)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 70 kHz', 'CONF:VOLT:AC 10.0', 'acv_83', 'gacv_83', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('ac', 7.0, 'OUT 7 V, 70 kHz', 'CONF:VOLT:AC 10.0', 'acv_84', 'gacv_84', 'DET:BAND 20', 5.0, 0.221)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 70 kHz', 'CONF:VOLT:AC 10.0', 'acv_85', 'gacv_85', 'DET:BAND 20', 5.0, 0.2)
    # ~100V,70kHz
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 70 kHz', 'CONF:VOLT:AC 100', 'acv_86', 'gacv_86', 'DET:BAND 20', 5.0, 0.65)
    _thdmm = Call('ac', 30.0, 'OUT 30 V, 70 kHz', 'CONF:VOLT:AC 100', 'acv_87', 'gacv_87', 'DET:BAND 20', 5.0, 0.317)    
    if self.b1[1] == '5500E':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_88', 'gacv_88', 'DET:BAND 20', 5.0, 0.25)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_89', 'gacv_89', 'DET:BAND 20', 5.0, 0.221)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_90', 'gacv_90', 'DET:BAND 20', 5.0, 0.2)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 70 kHz', 'CONF:VOLT:AC 100', 'acv_88', 'gacv_88', 'DET:BAND 20', 5.0, 0.25)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 70 kHz', 'CONF:VOLT:AC 100', 'acv_89', 'gacv_89', 'DET:BAND 20', 5.0, 0.221)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 70 kHz', 'CONF:VOLT:AC 100', 'acv_90', 'gacv_90', 'DET:BAND 20', 5.0, 0.2)
    # ~750V,70kHz
    if self.b1[1] == '5500E':
        _thdmm = Call('ac', 75.0, 'OUT 75 V, 20 kHz', 'CONF:VOLT:AC 750', 'acv_91', 'gacv_91', 'DET:BAND 20', 5.0, 0.65)
        _thdmm = Call('ac', 225.0, 'OUT 225 V, 20 kHz', 'CONF:VOLT:AC 750', 'acv_92', 'gacv_92', 'DET:BAND 20', 5.0, 0.317)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 75.0, 'OUT 75 V, 70 kHz', 'CONF:VOLT:AC 750', 'acv_91', 'gacv_91', 'DET:BAND 20', 5.0, 0.65)
        _thdmm = Call('ac', 225.0, 'OUT 225 V, 70 kHz', 'CONF:VOLT:AC 750', 'acv_92', 'gacv_92', 'DET:BAND 20', 5.0, 0.317)
        '''_thdmm = Call('ac', 375.0, 'OUT 375 V, 70 kHz', 'CONF:VOLT:AC 750', 'acv_93', 'gacv_93', 'DET:BAND 20', 5.0, 0.25)
        _thdmm = Call('ac', 525.0, 'OUT 525 V, 70 kHz', 'CONF:VOLT:AC 750', 'acv_94', 'gacv_94', 'DET:BAND 20', 5.0, 0.264)
        _thdmm = Call('ac', 750.0, 'OUT 750 V, 70 kHz', 'CONF:VOLT:AC 750', 'acv_95', 'gacv_95', 'DET:BAND 20', 5.0, 0.26)'''
    # ~0.1V,200kHz
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 200 kHz', 'CONF:VOLT:AC 0.1', 'acv_96', 'gacv_96', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 0.03, 'OUT 0.03 V, 200 kHz', 'CONF:VOLT:AC 0.1', 'acv_97', 'gacv_97', 'DET:BAND 20', 5.0, 1.333)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 200 kHz', 'CONF:VOLT:AC 0.1', 'acv_98', 'gacv_98', 'DET:BAND 20', 5.0, 1.2)
    _thdmm = Call('ac', 0.07, 'OUT 0.07 V, 200 kHz', 'CONF:VOLT:AC 0.1', 'acv_99', 'gacv_99', 'DET:BAND 20', 5.0, 1.143)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 200 kHz', 'CONF:VOLT:AC 0.1', 'acv_100', 'gacv_100', 'DET:BAND 20', 5.0, 1.1)
    # ~1V,200kHz
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 200 kHz', 'CONF:VOLT:AC 1.0', 'acv_101', 'gacv_101', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 0.3, 'OUT 0.3 V, 200 kHz', 'CONF:VOLT:AC 1.0', 'acv_102', 'gacv_102', 'DET:BAND 20', 5.0, 1.333)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 200 kHz', 'CONF:VOLT:AC 1.0', 'acv_103', 'gacv_103', 'DET:BAND 20', 5.0, 1.2)
    _thdmm = Call('ac', 0.7, 'OUT 0.7 V, 200 kHz', 'CONF:VOLT:AC 1.0', 'acv_104', 'gacv_104', 'DET:BAND 20', 5.0, 1.143)
    _thdmm = Call('ac', 1.0, 'OUT 1.0 V, 200 kHz', 'CONF:VOLT:AC 1.0', 'acv_105', 'gacv_105', 'DET:BAND 20', 5.0, 1.1)
    # ~10V,100kHz
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_106', 'gacv_106', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 3.0, 'OUT 3 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_107', 'gacv_107', 'DET:BAND 20', 5.0, 1.333)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_108', 'gacv_108', 'DET:BAND 20', 5.0, 1.2)
    _thdmm = Call('ac', 7.0, 'OUT 7 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_109', 'gacv_109', 'DET:BAND 20', 5.0, 1.143)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv_110', 'gacv_110', 'DET:BAND 20', 5.0, 1.1)
    # ~100V,200kHz
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_111', 'gacv_111', 'DET:BAND 20', 5.0, 2.0)
    _thdmm = Call('ac', 30.0, 'OUT 30 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_112', 'gacv_112', 'DET:BAND 20', 5.0, 1.333)
    if self.b1[1] == '5500E':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_113', 'gacv_113', 'DET:BAND 20', 5.0, 1.2)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_114', 'gacv_114', 'DET:BAND 20', 5.0, 1.143)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 100', 'acv_115', 'gacv_115', 'DET:BAND 20', 5.0, 1.1)
    if self.b1[1] == '5522A':
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_113', 'gacv_113', 'DET:BAND 20', 5.0, 1.2)
        _thdmm = Call('ac', 70.0, 'OUT 70 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_114', 'gacv_114', 'DET:BAND 20', 5.0, 1.143)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 100', 'acv_115', 'gacv_115', 'DET:BAND 20', 5.0, 1.1)
if self.f_var.get() == 1:
    _th = Reset()
    _thdmm = Call('fr', 5.0, 'OUT 0.1 V, 5 Hz', 'CONF:FREQ 5.0 Hz', 'f_1', 'gf_1', 'DET:BAND 20', 5.0, 0.07)
    _thdmm = Call('fr', 5.0, 'OUT 1.0 V, 5 Hz', 'CONF:FREQ 5.0 Hz', 'f_2', 'gf_2', 'DET:BAND 20', 5.0, 0.07)
    _thdmm = Call('fr', 50.0, 'OUT 0.1 V, 50 Hz', 'CONF:FREQ 50.0 Hz', 'f_3', 'gf_3', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('fr', 50.0, 'OUT 1.0 V, 50 Hz', 'CONF:FREQ 50.0 Hz', 'f_4', 'gf_4', 'DET:BAND 20', 5.0, 0.03)
    _thdmm = Call('fr', 500.0, 'OUT 0.1 V, 500 Hz', 'CONF:FREQ 500.0 Hz', 'f_5', 'gf_5', 'DET:BAND 20', 5.0, 0.007)
    _thdmm = Call('fr', 500.0, 'OUT 1.0 V, 500 Hz', 'CONF:FREQ 500.0 Hz', 'f_6', 'gf_6', 'DET:BAND 20', 5.0, 0.007)
    _thdmm = Call('fr', 100000.0, 'OUT 0.1 V, 100 kHz', 'CONF:FREQ 100.0 kHz', 'f_7', 'gf_7', 'DET:BAND 20', 5.0, 0.007)
    _thdmm = Call('fr', 100000.0, 'OUT 1.0 V, 100 kHz', 'CONF:FREQ 100.0 kHz', 'f_8', 'gf_8', 'DET:BAND 20', 5.0, 0.007)
if self.c_var.get() == 1:
    # C
    _th = Message('Измерение ёмкости.\nВытащите красный провод из каллибратора\nдля компенсации проводов')
    _th = cap()
    _th = Message('Верните провод на место')
    _thdmm = Call('cap', 1.0E-9, 'OUT 1 NF', 'CONF:CAP 1 NF', 'c_1', 'gc_1', 'DET:BAND 20', 5.0, 1.0)
    _thdmm = Call('cap', 10.0E-9, 'OUT 10 NF', 'CONF:CAP 10 NF', 'c_2', 'gc_2', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('cap', 100.0E-9, 'OUT 100 NF', 'CONF:CAP 100 NF', 'c_3', 'gc_3', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('cap', 1.0E-6, 'OUT 1 UF', 'CONF:CAP 1 UF', 'c_4', 'gc_4', 'DET:BAND 20', 5.0, 0.5)
if self.dci_var.get() == 1:
    _th = Message('Переключите провода\n для измерения тока до 3А')
    _th = Reset()
    # 0.001A
    _thdmm = Call('dci', 0.0001, 'OUT 0.0001 A', 'CONF:CURR:DC 0.001', 'dci_1', 'gdci_1', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('dci', 0.0003, 'OUT 0.0003 A', 'CONF:CURR:DC 0.001', 'dci_2', 'gdci_2', 'DET:BAND 20', 5.0, 0.067)
    _thdmm = Call('dci', 0.0005, 'OUT 0.0005 A', 'CONF:CURR:DC 0.001', 'dci_3', 'gdci_3', 'DET:BAND 20', 5.0, 0.06)
    _thdmm = Call('dci', 0.0007, 'OUT 0.0007 A', 'CONF:CURR:DC 0.001', 'dci_4', 'gdci_4', 'DET:BAND 20', 5.0, 0.057)
    _thdmm = Call('dci', 0.001, 'OUT 0.001 A', 'CONF:CURR:DC 0.001', 'dci_5', 'gdci_5', 'DET:BAND 20', 5.0, 0.055)
    # 0.01A
    _thdmm = Call('dci', 0.001, 'OUT 0.001 A', 'CONF:CURR:DC 0.01', 'dci_6', 'gdci_6', 'DET:BAND 20', 5.0, 0.25)
    _thdmm = Call('dci', 0.003, 'OUT 0.003 A', 'CONF:CURR:DC 0.01', 'dci_7', 'gdci_7', 'DET:BAND 20', 5.0, 0.117)
    _thdmm = Call('dci', 0.005, 'OUT 0.005 A', 'CONF:CURR:DC 0.01', 'dci_8', 'gdci_8', 'DET:BAND 20', 5.0, 0.09)
    _thdmm = Call('dci', 0.007, 'OUT 0.007 A', 'CONF:CURR:DC 0.01', 'dci_9', 'gdci_9', 'DET:BAND 20', 5.0, 0.079)
    _thdmm = Call('dci', 0.01, 'OUT 0.01 A', 'CONF:CURR:DC 0.01', 'dci_10', 'gdci_10', 'DET:BAND 20', 5.0, 0.07)
    # 0.1A
    _thdmm = Call('dci', 0.01, 'OUT 0.01 A', 'CONF:CURR:DC 0.1', 'dci_11', 'gdci_11', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('dci', 0.03, 'OUT 0.03 A', 'CONF:CURR:DC 0.1', 'dci_12', 'gdci_12', 'DET:BAND 20', 5.0, 0.067)
    _thdmm = Call('dci', 0.05, 'OUT 0.05 A', 'CONF:CURR:DC 0.1', 'dci_13', 'gdci_13', 'DET:BAND 20', 5.0, 0.06)
    _thdmm = Call('dci', 0.07, 'OUT 0.07 A', 'CONF:CURR:DC 0.1', 'dci_14', 'gdci_14', 'DET:BAND 20', 5.0, 0.057)
    _thdmm = Call('dci', 0.1, 'OUT 0.1 A', 'CONF:CURR:DC 0.1', 'dci_15', 'gdci_15', 'DET:BAND 20', 5.0, 0.055)
    # 1A
    _thdmm = Call('dci', 0.1, 'OUT 0.1 A', 'CONF:CURR:DC 1.0', 'dci_16', 'gdci_16', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('dci', 0.3, 'OUT 0.3 A', 'CONF:CURR:DC 1.0', 'dci_17', 'gdci_17', 'DET:BAND 20', 5.0, 0.113)
    _thdmm = Call('dci', 0.5, 'OUT 0.5 A', 'CONF:CURR:DC 1.0', 'dci_18', 'gdci_18', 'DET:BAND 20', 5.0, 0.1)
    _thdmm = Call('dci', 0.7, 'OUT 0.7 A', 'CONF:CURR:DC 1.0', 'dci_19', 'gdci_19', 'DET:BAND 20', 5.0, 0.094)
    _thdmm = Call('dci', 1.0, 'OUT 1.0 A', 'CONF:CURR:DC 1.0', 'dci_20', 'gdci_20', 'DET:BAND 20', 5.0, 0.09)
    # 3A
    _thdmm = Call('dci', 0.3, 'OUT 0.3 A', 'CONF:CURR:DC 3.0', 'dci_21', 'gdci_21', 'DET:BAND 20', 5.0, 0.4)
    _thdmm = Call('dci', 0.9, 'OUT 0.9 A', 'CONF:CURR:DC 3.0', 'dci_22', 'gdci_22', 'DET:BAND 20', 5.0, 0.267)
    _thdmm = Call('dci', 1.5, 'OUT 1.5 A', 'CONF:CURR:DC 3.0', 'dci_23', 'gdci_23', 'DET:BAND 20', 5.0, 0.24)
    _thdmm = Call('dci', 2.1, 'OUT 2.1 A', 'CONF:CURR:DC 3.0', 'dci_24', 'gdci_24', 'DET:BAND 20', 5.0, 0.229)
    if self.b1[1] == '5500E':
        _thdmm = Call('dci', 2.85, 'OUT 2.85 A', 'CONF:CURR:DC 3.0', 'dci_25', 'gdci_25', 'DET:BAND 20', 5.0, 0.232)
        _th = Message('Переключите красный провод на контакт 10А МУЛЬТИМЕТРА')
        _th = Reset()
        _thdmm = Call('dci', 1.0, 'OUT 1.0 A', 'CONF:CURR:DC 10.0', 'dci_26', 'gdci_26', 'DET:BAND 20', 5.0, 0.22)
        _thdmm = Call('dci', 3.0, 'OUT 3.0 A', 'CONF:CURR:DC 10.0', 'dci_27', 'gdci_27', 'DET:BAND 20', 5.0, 0.153)
        _thdmm = Call('dci', 5.0, 'OUT 5.0 A', 'CONF:CURR:DC 10.0', 'dci_28', 'gdci_28', 'DET:BAND 20', 5.0, 0.14)
        _thdmm = Call('dci', 7.0, 'OUT 7.0 A', 'CONF:CURR:DC 10.0', 'dci_29', 'gdci_29', 'DET:BAND 20', 5.0, 0.191)
        _thdmm = Call('dci', 10.0, 'OUT 10.0 A', 'CONF:CURR:DC 10.0', 'dci_30', 'gdci_30', 'DET:BAND 20', 5.0, 0.23)
    elif self.b1[1] == '5522A':
        _th = Message('Переключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        _th = Reset()
        _thdmm = Call('dci', 2.85, 'OUT 2.85 A', 'CONF:CURR:DC 3.0', 'dci_25', 'gdci_25', 'DET:BAND 20', 5.0, 0.232)
        _th = Message('Переключите красный провод на контакт 10А МУЛЬТИМЕТРА')
        _th = Reset()
        _thdmm = Call('dci', 1.0, 'OUT 1.0 A', 'CONF:CURR:DC 10.0', 'dci_26', 'gdci_26', 'DET:BAND 20', 5.0, 0.22)
        _thdmm = Call('dci', 3.0, 'OUT 3.0 A', 'CONF:CURR:DC 10.0', 'dci_27', 'gdci_27', 'DET:BAND 20', 5.0, 0.153)
        _thdmm = Call('dci', 5.0, 'OUT 5.0 A', 'CONF:CURR:DC 10.0', 'dci_28', 'gdci_28', 'DET:BAND 20', 5.0, 0.14)
        _thdmm = Call('dci', 7.0, 'OUT 7.0 A', 'CONF:CURR:DC 10.0', 'dci_29', 'gdci_29', 'DET:BAND 20', 5.0, 0.191)
        _thdmm = Call('dci', 10.0, 'OUT 10.0 A', 'CONF:CURR:DC 10.0', 'dci_30', 'gdci_30', 'DET:BAND 20', 5.0, 0.23)
    _th = Message('Верните красный провод на контакт 3А МУЛЬТИМЕТРА')

if self.aci_var.get() == 1:
    _th = Reset()
    # ~0.0001A, 20Hz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 20 Hz', 'CONF:CURR:AC 0.0001', 'aci_1', 'gaci_1', 'DET:BAND 3', 8.0, 0.14)
    # ~0.001A, 20Hz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 20 Hz', 'CONF:CURR:AC 0.001', 'aci_2', 'gaci_2', 'DET:BAND 3', 8.0, 0.5)
    _thdmm = Call('aci', 0.0003, 'OUT 0.0003 A, 20 Hz', 'CONF:CURR:AC 0.001', 'aci_3', 'gaci_3', 'DET:BAND 3', 8.0, 0.233)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 20 Hz', 'CONF:CURR:AC 0.001', 'aci_4', 'gaci_4', 'DET:BAND 3', 8.0, 0.18)
    _thdmm = Call('aci', 0.0007, 'OUT 0.0007 A, 20 Hz', 'CONF:CURR:AC 0.001', 'aci_5', 'gaci_5', 'DET:BAND 3', 8.0, 0.157)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 20 Hz', 'CONF:CURR:AC 0.001', 'aci_6', 'gaci_6', 'DET:BAND 3', 8.0, 0.14)
    # ~0.01A, 20Hz
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 20 Hz', 'CONF:CURR:AC 0.01', 'aci_7', 'gaci_7', 'DET:BAND 3', 8.0, 0.5)
    _thdmm = Call('aci', 0.003, 'OUT 0.003 A, 20 Hz', 'CONF:CURR:AC 0.01', 'aci_8', 'gaci_8', 'DET:BAND 3', 8.0, 0.233)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 20 Hz', 'CONF:CURR:AC 0.01', 'aci_9', 'gaci_9', 'DET:BAND 3', 8.0, 0.18)
    _thdmm = Call('aci', 0.007, 'OUT 0.007 A, 20 Hz', 'CONF:CURR:AC 0.01', 'aci_10', 'gaci_10', 'DET:BAND 3', 8.0, 0.157)
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 20 Hz', 'CONF:CURR:AC 0.01', 'aci_11', 'gaci_11', 'DET:BAND 3', 8.0, 0.14)
    # ~0.1A, 20Hz
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 20 Hz', 'CONF:CURR:AC 0.1', 'aci_12', 'gaci_12', 'DET:BAND 3', 8.0, 0.5)
    _thdmm = Call('aci', 0.03, 'OUT 0.03 A, 20 Hz', 'CONF:CURR:AC 0.1', 'aci_13', 'gaci_13', 'DET:BAND 3', 8.0, 0.233)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 20 Hz', 'CONF:CURR:AC 0.1', 'aci_14', 'gaci_14', 'DET:BAND 3', 8.0, 0.18)
    _thdmm = Call('aci', 0.07, 'OUT 0.07 A, 20 Hz', 'CONF:CURR:AC 0.1', 'aci_15', 'gaci_15', 'DET:BAND 3', 8.0, 0.157)
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 20 Hz', 'CONF:CURR:AC 0.1', 'aci_16', 'gaci_16', 'DET:BAND 3', 8.0, 0.14)
    # ~1A, 20Hz
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 20 Hz', 'CONF:CURR:AC 1.0', 'aci_17', 'gaci_17', 'DET:BAND 3', 8.0, 0.5)
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 20 Hz', 'CONF:CURR:AC 1.0', 'aci_18', 'gaci_18', 'DET:BAND 3', 8.0, 0.233)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 20 Hz', 'CONF:CURR:AC 1.0', 'aci_19', 'gaci_19', 'DET:BAND 3', 8.0, 0.18)
    _thdmm = Call('aci', 0.7, 'OUT 0.7 A, 20 Hz', 'CONF:CURR:AC 1.0', 'aci_20', 'gaci_20', 'DET:BAND 3', 8.0, 0.157)
    _thdmm = Call('aci', 1.0, 'OUT 1.0 A, 20 Hz', 'CONF:CURR:AC 1.0', 'aci_21', 'gaci_21', 'DET:BAND 3', 8.0, 0.14)
    # ~0.0001A, 1kHz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 1 kHz', 'CONF:CURR:AC 0.0001', 'aci_22', 'gaci_22', 'DET:BAND 20', 5.0, 0.14)
    # ~0.001A, 1kHz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_23', 'gaci_23', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.0003, 'OUT 0.0003 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_24', 'gaci_24', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_25', 'gaci_25', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.0007, 'OUT 0.0007 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_26', 'gaci_26', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 1 kHz', 'CONF:CURR:AC 0.001', 'aci_27', 'gaci_27', 'DET:BAND 20', 5.0, 0.14)
    # ~0.01A, 1kHz
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_28', 'gaci_28', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.003, 'OUT 0.003 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_29', 'gaci_29', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_30', 'gaci_30', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.007, 'OUT 0.007 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_31', 'gaci_31', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 1 kHz', 'CONF:CURR:AC 0.01', 'aci_32', 'gaci_32', 'DET:BAND 20', 5.0, 0.14)
    # ~0.1A, 1kHz
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_33', 'gaci_33', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.03, 'OUT 0.03 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_34', 'gaci_34', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_35', 'gaci_35', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.07, 'OUT 0.07 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_36', 'gaci_36', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 1 kHz', 'CONF:CURR:AC 0.1', 'aci_37', 'gaci_37', 'DET:BAND 20', 5.0, 0.14)
    # ~1A, 1kHz
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_38', 'gaci_38', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_39', 'gaci_39', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_40', 'gaci_40', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.7, 'OUT 0.7 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_41', 'gaci_41', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 1.0, 'OUT 1.0 A, 1 kHz', 'CONF:CURR:AC 1.0', 'aci_42', 'gaci_42', 'DET:BAND 20', 5.0, 0.14)
    # ~3A, 1kHz
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_43', 'gaci_43', 'DET:BAND 20', 5.0, 0.63)
    _thdmm = Call('aci', 0.9, 'OUT 0.9 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_44', 'gaci_44', 'DET:BAND 20', 5.0, 0.363)
    _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_45', 'gaci_45', 'DET:BAND 20', 5.0, 0.31)
    _thdmm = Call('aci', 2.1, 'OUT 2.1 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_46', 'gaci_46', 'DET:BAND 20', 5.0, 0.287)
    if self.b1[1] == '5500E':
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_47', 'gaci_47', 'DET:BAND 20', 5.0, 0.284)
    # ~0.0001A, 5kHz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 5 kHz', 'CONF:CURR:AC 0.0001', 'aci_53', 'gaci_53', 'DET:BAND 20', 5.0, 0.14)
    # ~0.001A, 5kHz
    _thdmm = Call('aci', 0.0001, 'OUT 0.0001 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_54', 'gaci_54', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.0003, 'OUT 0.0003 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_55', 'gaci_55', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.0005, 'OUT 0.0005 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_56', 'gaci_56', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.0007, 'OUT 0.0007 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_57', 'gaci_57', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 5 kHz', 'CONF:CURR:AC 0.001', 'aci_58', 'gaci_58', 'DET:BAND 20', 5.0, 0.14)
    # ~0.01A, 5kHz
    _thdmm = Call('aci', 0.001, 'OUT 0.001 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_59', 'gaci_59', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.003, 'OUT 0.003 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_60', 'gaci_60', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.005, 'OUT 0.005 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_61', 'gaci_61', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.007, 'OUT 0.007 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_62', 'gaci_62', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 5 kHz', 'CONF:CURR:AC 0.01', 'aci_63', 'gaci_63', 'DET:BAND 20', 5.0, 0.14)
    # ~0.1A, 5kHz
    _thdmm = Call('aci', 0.01, 'OUT 0.01 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_64', 'gaci_64', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.03, 'OUT 0.03 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_65', 'gaci_65', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.05, 'OUT 0.05 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_66', 'gaci_66', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.07, 'OUT 0.07 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_67', 'gaci_67', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 5 kHz', 'CONF:CURR:AC 0.1', 'aci_68', 'gaci_68', 'DET:BAND 20', 5.0, 0.14)
    # ~1A, 5kHz
    _thdmm = Call('aci', 0.1, 'OUT 0.1 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_69', 'gaci_69', 'DET:BAND 20', 5.0, 0.5)
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_70', 'gaci_70', 'DET:BAND 20', 5.0, 0.233)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_71', 'gaci_71', 'DET:BAND 20', 5.0, 0.18)
    _thdmm = Call('aci', 0.7, 'OUT 0.7 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_72', 'gaci_72', 'DET:BAND 20', 5.0, 0.157)
    _thdmm = Call('aci', 1.0, 'OUT 1.0 A, 5 kHz', 'CONF:CURR:AC 1.0', 'aci_73', 'gaci_73', 'DET:BAND 20', 5.0, 0.14)
    # ~3A, 5kHz
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_74', 'gaci_74', 'DET:BAND 20', 5.0, 0.63)
    _thdmm = Call('aci', 0.9, 'OUT 0.9 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_75', 'gaci_75', 'DET:BAND 20', 5.0, 0.363)
    _thdmm = Call('aci', 1.5, 'OUT 1.5 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_76', 'gaci_76', 'DET:BAND 20', 5.0, 0.31)
    _thdmm = Call('aci', 2.1, 'OUT 2.1 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_77', 'gaci_77', 'DET:BAND 20', 5.0, 0.287)           
    _th = Message('Переключите красный провод на контакт 10А МУЛЬТИМЕТРА')
    _th = Reset()
    if self.b1[1] == '5500E':           
        # ~10A, 1kHz
        _thdmm = Call('aci', 1.0, 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_48', 'gaci_48', 'DET:BAND 20', 5.0, 0.5)
        _thdmm = Call('aci', 3.0, 'OUT 3 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_49', 'gaci_49', 'DET:BAND 20', 5.0, 0.233)
        _thdmm = Call('aci', 5.0, 'OUT 5 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_50', 'gaci_50', 'DET:BAND 20', 5.0, 0.18)
        _thdmm = Call('aci', 7.0, 'OUT 7 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_51', 'gaci_51', 'DET:BAND 20', 5.0, 0.214)
        _thdmm = Call('aci', 10.0, 'OUT 10 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_52', 'gaci_52', 'DET:BAND 20', 5.0, 0.24)
    elif self.b1[1] == '5522A':
        _thdmm = Call('aci', 1.0, 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_48', 'gaci_48', 'DET:BAND 20', 5.0, 0.5)
        _thdmm = Call('aci', 1.0, 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_79', 'gaci_79', 'DET:BAND 20', 5.0, 0.5)
        _th = Message('Переключите красный провод на КАЛИБРАТОРЕ в разъем больше 2,5 А')
        _thdmm = Call('aci', 3.0, 'OUT 3 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_49', 'gaci_49', 'DET:BAND 20', 5.0, 0.233)
        _thdmm = Call('aci', 5.0, 'OUT 5 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_50', 'gaci_50', 'DET:BAND 20', 5.0, 0.18)
        _thdmm = Call('aci', 7.0, 'OUT 7 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_51', 'gaci_51', 'DET:BAND 20', 5.0, 0.214)
        _thdmm = Call('aci', 10.0, 'OUT 10 A, 1 kHz', 'CONF:CURR:AC 10.0', 'aci_52', 'gaci_52', 'DET:BAND 20', 5.0, 0.24)
        _thdmm = Call('aci', 3.0, 'OUT 3 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_80', 'gaci_80', 'DET:BAND 20', 5.0, 0.233)
        _thdmm = Call('aci', 5.0, 'OUT 5 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_81', 'gaci_81', 'DET:BAND 20', 5.0, 0.18)
        _thdmm = Call('aci', 7.0, 'OUT 7 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_82', 'gaci_82', 'DET:BAND 20', 5.0, 0.214)
        _thdmm = Call('aci', 10.0, 'OUT 10 A, 5 kHz', 'CONF:CURR:AC 10.0', 'aci_83', 'gaci_83', 'DET:BAND 20', 5.0, 0.24)
        _th = Message('Верните красный провод на контакт до 3А МУЛЬТИМЕТРА')
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 1 kHz', 'CONF:CURR:AC 3.0', 'aci_47', 'gaci_47', 'DET:BAND 20', 5.0, 0.284)
        _thdmm = Call('aci', 2.85, 'OUT 2.85 A, 5 kHz', 'CONF:CURR:AC 3.0', 'aci_78', 'gaci_78', 'DET:BAND 20', 5.0, 0.284)                
if self.r4_var.get() == 1:
    _th = Message('Переключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    _thdmm = Call('res4', 100.0, 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 'gr4_1', 'DET:BAND 20', 5.0, 0.01)
    _thdmm = Call('res4', 1.0E+3, 'OUT 1 KOHM; ZCOMP WIRE4', 'CONF:FRES 1 KOHM', 'r4_2', 'gr4_2', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('res4', 10.0E+3, 'OUT 10 KOHM; ZCOMP WIRE4', 'CONF:FRES 10 KOHM', 'r4_3', 'gr4_3', 'DET:BAND 20', 5.0, 0.005)
    _thdmm = Call('res4', 100.0E+3, 'OUT 100 KOHM; ZCOMP WIRE4', 'CONF:FRES 100 KOHM', 'r4_4', 'gr4_4', 'DET:BAND 20', 5.0, 0.005)
if self.r2_var.get() == 1:
    _th = Message('Переключите провода по двухпроводной схеме\n для измерения сопротивления')
    _th = Reset()
    _thdmm = Call('res2', 1.0E+6, 'OUT 1 MOHM; ZCOMP WIRE2', 'CONF:RES 1 MOHM', 'r2_1', 'gr2_1', 'DET:BAND 20', 5.0, 0.075)
    _thdmm = Call('res2', 10.0E+6, 'OUT 10 MOHM; ZCOMP WIRE2', 'CONF:RES 10 MOHM', 'r2_2', 'gr2_2', 'DET:BAND 20', 5.0, 0.026)
    _thdmm = Call('res2', 100.0E+6, 'OUT 100 MOHM; ZCOMP WIRE2', 'CONF:RES 100 MOHM', 'r2_3', 'gr2_3', 'DET:BAND 20', 5.0, 0.301)
    if self.b1[1] == '5522A':
        _thdmm = Call('res2', 1.0E+9, 'OUT 1 GOHM; ZCOMP WIRE2', 'CONF:RES 1 GOHM', 'r2_4', 'gr2_4', 'DET:BAND 20', 5.0, 3.001)

_th = Message('Калибровка завершена')
_th = Reset()