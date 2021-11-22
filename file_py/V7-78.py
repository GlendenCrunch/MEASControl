# -*- coding: utf-8 -*-
if dcv_var.get() == 1:
    _th = Message('Соедините провода для измерения постоянного напряжения')
    _th_Reset.start()         
    # 0.1V
    _thdmm = Call('dc', 0.01, 'OUT 0.01 V', 'CONF:VOLT:DC 0.1', 'dcv1', 9.996, 'DET:BAND 20', 3.0, 10.004)
    _thdmm = Call('dc', 0.05, 'OUT 0.05 V', 'CONF:VOLT:DC 0.1', 'dcv2', 49.994, 'DET:BAND 20', 3.0, 50.006)
    _thdmm = Call('dc', 0.1, 'OUT 0.1 V', 'CONF:VOLT:DC 0.1', 'dcv3', 99.915, 'DET:BAND 20', 3.0, 100.0085)
    _thdmm = Call('dc', -0.1, 'OUT -0.1 V', 'CONF:VOLT:DC 0.1', 'dcv4', -100.0085, 'DET:BAND 20', 3.0, -99.915)
    # 1V
    _thdmm = Call('dc', 0.1, 'OUT 100 mV', 'CONF:VOLT:DC 1.0', 'dcv5', 0.09999, 'DET:BAND 20', 3.0, 0.10001)
    _thdmm = Call('dc', 0.5, 'OUT 500 mV', 'CONF:VOLT:DC 1.0', 'dcv6', 0.49997, 'DET:BAND 20', 3.0, 0.50003)
    _thdmm = Call('dc', 1.0, 'OUT 1.0 V', 'CONF:VOLT:DC 1.0', 'dcv7', 0.999953, 'DET:BAND 20', 3.0, 1.000047)
    _thdmm = Call('dc', -1.0, 'OUT -1.0 V', 'CONF:VOLT:DC 1.0', 'dcv8', -1.000047, 'DET:BAND 20', 3.0, -0.999953)     
    # 10V
    _thdmm = Call('dc', 1.0, 'OUT 1 V', 'CONF:VOLT:DC 10', 'dcv9', 0.999915, 'DET:BAND 20', 3.0, 1.000085)
    _thdmm = Call('dc', 5.0, 'OUT 5 V', 'CONF:VOLT:DC 10', 'dcv10', 4.99981, 'DET:BAND 20', 3.0, 5.00019)
    _thdmm = Call('dc', 10.0, 'OUT 10 V', 'CONF:VOLT:DC 10', 'dcv11', 9.9996, 'DET:BAND 20', 3.0, 10.0004)
    _thdmm = Call('dc', -10.0, 'OUT -10 V', 'CONF:VOLT:DC 10', 'dcv12', -10.0004, 'DET:BAND 20', 3.0, -9.9996)
    # 100V
    _thdmm = Call('dc', 10.0, 'OUT 10 V', 'CONF:VOLT:DC 100', 'dcv13', 9.99895, 'DET:BAND 20', 3.0, 10.00105)
    _thdmm = Call('dc', 50.0, 'OUT 50 V', 'CONF:VOLT:DC 100', 'dcv14', 49.99715, 'DET:BAND 20', 3.0, 50.00285)
    _thdmm = Call('dc', 100.0, 'OUT 100 V', 'CONF:VOLT:DC 100', 'dcv15', 99.9949, 'DET:BAND 20', 4.0, 100.0051)
    _thdmm = Call('dc', -100.0, 'OUT -100 V', 'CONF:VOLT:DC 100', 'dcv16', -100.0051, 'DET:BAND 20', 4.0, -99.9949)
    # 1000V
    _thdmm = Call('dc', 100.0, 'OUT 100 V', 'CONF:VOLT:DC 1000', 'dcv17', 99.9855, 'DET:BAND 20', 4.0, 100.0145)
    _thdmm = Call('dc', 500.0, 'OUT 500 V', 'CONF:VOLT:DC 1000', 'dcv18', 499.9675, 'DET:BAND 20', 4.0, 500.0325)
    _thdmm = Call('dc', 1000.0, 'OUT 1000 V', 'CONF:VOLT:DC 1000', 'dcv19', 999.945, 'DET:BAND 20', 4.0, 1000.055)
    _thdmm = Call('dc', -1000.0, 'OUT -1000 V', 'CONF:VOLT:DC 1000', 'dcv20', -1000.055, 'DET:BAND 20', 8.0, -999.945)  
if acv_var.get() == 1:
    _th_Reset.start()
    # ~0.1V
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv1', 9.925, 'DET:BAND 3', 3.0, 10.075)
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv2', 9.925, 'DET:BAND 20', 3.0, 10.046)
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv3', 9.938, 'DET:BAND 20', 3.0, 10.062)
    _thdmm = Call('ac', 0.01, 'OUT 0.01 V, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv4', 9.86, 'DET:BAND 20', 3.0, 10.14)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv5', 49.785, 'DET:BAND 3', 3.0, 50.215)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv6', 49.93, 'DET:BAND 20', 3.0, 50.07)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv7', 49.89, 'DET:BAND 20', 3.0, 50.11)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv8', 49.62, 'DET:BAND 20', 3.0, 50.38)
    _thdmm = Call('ac', 0.05, 'OUT 0.05 V, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv9', 47.95, 'DET:BAND 20', 3.0, 52.05)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 10 Hz', 'CONF:VOLT:AC 0.1', 'acv10', 99.61, 'DET:BAND 3', 3.0, 100.39)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 1 kHz', 'CONF:VOLT:AC 0.1', 'acv11', 99.9, 'DET:BAND 20', 3.0, 100.1)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 50 kHz', 'CONF:VOLT:AC 0.1', 'acv12', 99.83, 'DET:BAND 20', 3.0, 100.17)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 100 kHz', 'CONF:VOLT:AC 0.1', 'acv13', 99.32, 'DET:BAND 20', 3.0, 100.68)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 300 kHz', 'CONF:VOLT:AC 0.1', 'acv14', 95.95, 'DET:BAND 20', 3.0, 104.05)
    # ~1V                
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv15', 99.62, 'DET:BAND 3', 3.0, 100.38)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv16', 99.91, 'DET:BAND 20', 3.0, 100.09)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv17', 99.83, 'DET:BAND 20', 3.0, 100.17)
    _thdmm = Call('ac', 0.1, 'OUT 0.1 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv18', 99.32, 'DET:BAND 20', 3.0, 100.68)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv19', 498.22, 'DET:BAND 3', 3.0, 501.78)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv20', 499.67, 'DET:BAND 20', 3.0, 500.33)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv21', 499.35, 'DET:BAND 20', 3.0, 500.65)
    _thdmm = Call('ac', 0.5, 'OUT 0.5 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv22', 496.92, 'DET:BAND 20', 3.0, 503.08)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 10 Hz', 'CONF:VOLT:AC 1.0', 'acv23', 0.99647, 'DET:BAND 3', 3.0, 1.00353)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 1 kHz', 'CONF:VOLT:AC 1.0', 'acv24', 0.99937, 'DET:BAND 20', 3.0, 1.00063)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 50 kHz', 'CONF:VOLT:AC 1.0', 'acv25', 0.99875, 'DET:BAND 20', 3.0, 1.00125)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 1.0', 'acv26', 0.99392, 'DET:BAND 20', 3.0, 1.00608)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 300 kHz', 'CONF:VOLT:AC 1.0', 'acv27', 0.95995, 'DET:BAND 20', 3.0, 1.04005)
    # ~10V                
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv28', 0.9935, 'DET:BAND 3', 3.0, 1.0065)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv29', 0.9964, 'DET:BAND 20', 3.0, 1.0036)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv30', 0.9938, 'DET:BAND 20', 3.0, 1.0062)
    _thdmm = Call('ac', 1.0, 'OUT 1 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv31', 0.986, 'DET:BAND 20', 3.0, 1.014)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv32', 4.9795, 'DET:BAND 3', 3.0, 5.0205)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv33', 4.994, 'DET:BAND 20', 3.0, 5.006)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv34', 4.989, 'DET:BAND 20', 3.0, 5.011)
    _thdmm = Call('ac', 5.0, 'OUT 5 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv35', 4.962, 'DET:BAND 20', 3.0, 5.038)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 10 Hz', 'CONF:VOLT:AC 10.0', 'acv36', 9.962, 'DET:BAND 3', 3.0, 10.038)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 1 kHz', 'CONF:VOLT:AC 10.0', 'acv37', 9.991, 'DET:BAND 20', 3.0, 10.009)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 50 kHz', 'CONF:VOLT:AC 10.0', 'acv38', 9.983, 'DET:BAND 20', 3.0, 10.017)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 10.0', 'acv39', 9.932, 'DET:BAND 20', 3.0, 10.068)
    # ~100V                
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 10 Hz', 'CONF:VOLT:AC 100.0', 'acv40', 9.935, 'DET:BAND 3', 3.0, 10.065)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv41', 9.964, 'DET:BAND 20', 3.0, 10.036)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv42', 9.938, 'DET:BAND 20', 3.0, 10.062)
    _thdmm = Call('ac', 10.0, 'OUT 10 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv43', 9.86, 'DET:BAND 20', 3.0, 10.14)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 45 Hz', 'CONF:VOLT:AC 100.0', 'acv44', 49.795, 'DET:BAND 3', 3.0, 50.205)
    _thdmm = Call('ac', 50.0, 'OUT 50 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv45', 49.94, 'DET:BAND 20', 3.0, 50.06)
    if b1[1] == '5522A': 
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv46', 49.89, 'DET:BAND 20', 3.0, 50.11)
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv47', 49.62, 'DET:BAND 20', 3.0, 50.38)
    else:
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv46', 49.89, 'DET:BAND 20', 3.0, 50.11)
        _thdmm = Call('ac', 50.0, 'OUT 50 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv47', 49.62, 'DET:BAND 20', 3.0, 50.38)            
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 45 Hz', 'CONF:VOLT:AC 100.0', 'acv48', 99.62, 'DET:BAND 3', 3.0, 100.38)
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 100.0', 'acv49', 99.91, 'DET:BAND 20', 3.0, 100.09)
    if b1[1] == '5522A':
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 100.0', 'acv50', 99.83, 'DET:BAND 20', 3.0, 100.17)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 100.0', 'acv51', 99.32, 'DET:BAND 20', 3.0, 100.68)
    else:
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv50', 99.83, 'DET:BAND 20', 3.0, 100.17)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 100.0', 'acv51', 99.32, 'DET:BAND 20', 3.0, 100.68)            
    # ~1000V                
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv52', 99.35, 'DET:BAND 3', 3.0, 100.65)
    _thdmm = Call('ac', 100.0, 'OUT 100 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv53', 99.64, 'DET:BAND 20', 3.0, 100.36)
    if b1[1] == '5522A': 
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 50 kHz', 'CONF:VOLT:AC 1000.0', 'acv54', 99.38, 'DET:BAND 20', 3.0, 100.62)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 100 kHz', 'CONF:VOLT:AC 1000.0', 'acv55', 98.6, 'DET:BAND 20', 3.0, 101.4)
    else:
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 1000.0', 'acv54', 99.38, 'DET:BAND 20', 3.0, 100.62)
        _thdmm = Call('ac', 100.0, 'OUT 100 V, 20 kHz', 'CONF:VOLT:AC 1000.0', 'acv55', 98.6, 'DET:BAND 20', 3.0, 101.4)            
    _thdmm = Call('ac', 500.0, 'OUT 500 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv56', 497.95, 'DET:BAND 3', 3.0, 502.05)
    _thdmm = Call('ac', 500.0, 'OUT 500 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv57', 499.4, 'DET:BAND 20', 3.0, 500.6)
    # _thdmm = Call('ac', 500.0, 'OUT 500 V, 50 kHz', 'CONF:VOLT:AC 1000', 'acv58', 498.9, 'DET:BAND 20', 3.0, 501.1)
    # _thdmm = Call('ac', 500.0, 'OUT 500 V, 100 kHz', 'CONF:VOLT:AC 1000', 'acv59', 496.2, 'DET:BAND 20', 3.0, 503.8)
    _thdmm = Call('ac', 750.0, 'OUT 750 V, 45 Hz', 'CONF:VOLT:AC 1000.0', 'acv60', 747.075, 'DET:BAND 3', 3.0, 752.925)
    _thdmm = Call('ac', 750.0, 'OUT 750 V, 1 kHz', 'CONF:VOLT:AC 1000.0', 'acv61', 749.25, 'DET:BAND 20', 3.0, 750.75)
    # _thdmm = Call('ac', 750.0, 'OUT 750 V, 50 kHz', 'CONF:VOLT:AC 1000', 'acv62', 748.8, 'DET:BAND 20', 3.0, 751.4)
    # _thdmm = Call('ac', 750.0, 'OUT 750 V, 100 kHz', 'CONF:VOLT:AC 1000', 'acv63', 744.7, 'DET:BAND 20', 3.0, 755.3)
if f_var.get() == 1:
    _th_Reset.start()
    _thdmm = Call('fr', 40.0, 'OUT 1 V, 40.0 Hz', 'CONF:FREQ 40.0 Hz', 'f_1', 39.99599, 'DET:BAND 20', 3.0, 40.00401)
    _thdmm = Call('fr', 1000.0, 'OUT 1 V, 1.0 kHz', 'CONF:FREQ 1.0 kHz', 'f_2', 0.999899, 'DET:BAND 20', 3.0, 1.000101)
    _thdmm = Call('fr', 10000.0, 'OUT 1 V, 10.0 kHz', 'CONF:FREQ 10.0 kHz', 'f_3', 9.99899, 'DET:BAND 20', 3.0, 10.00101)        
    _thdmm = Call('fr', 100000.0, 'OUT 1 V, 100.0 kHz', 'CONF:FREQ 100.0 kHz', 'f_4', 99.9899, 'DET:BAND 20', 3.0, 100.0101)
    _thdmm = Call('fr', 300000.0, 'OUT 1 V, 300.0 kHz', 'CONF:FREQ 300.0 kHz', 'f_5', 299.9699, 'DET:BAND 20', 3.0, 300.0301)
if r2_var.get() == 1:
    _th = Message('Переключите провода по двухпроводной схеме\n для измерения сопротивления')
    _th_Reset.start()
    # 1kOhm-2-wire
    _thdmm = Call('res2', 100.0, 'OUT 100 OHM', 'CONF:RES 1 KOHM', 'r2_1', 0.09989, 'DET:BAND 20', 3.0, 0.10011)
    _thdmm = Call('res2', 500.0, 'OUT 500 OHM', 'CONF:RES 1 KOHM', 'r2_2', 0.49985, 'DET:BAND 20', 3.0, 0.50015)
    _thdmm = Call('res2', 1.0E+3, 'OUT 1 kOHM', 'CONF:RES 1 KOHM', 'r2_3', 0.9998, 'DET:BAND 20', 3.0, 1.0002)
    # 10kOhm-2-wire
    _thdmm = Call('res2', 1.0E+3, 'OUT 1 kOHM', 'CONF:RES 10 KOHM', 'r2_4', 0.9989, 'DET:BAND 20', 3.0, 1.0011)
    _thdmm = Call('res2', 5.0E+3, 'OUT 5 kOHM', 'CONF:RES 10 KOHM', 'r2_5', 4.9985, 'DET:BAND 20', 3.0, 5.0015)
    _thdmm = Call('res2', 1.0E+4, 'OUT 10 kOHM', 'CONF:RES 10 KOHM', 'r2_6', 9.998, 'DET:BAND 20', 3.0, 10.002)
    # 100kOhm-2-wire
    _thdmm = Call('res2', 1.0E+4, 'OUT 10 kOHM', 'CONF:RES 100 KOHM', 'r2_7', 9.989, 'DET:BAND 20', 3.0, 10.011)
    _thdmm = Call('res2', 5.0E+4, 'OUT 50 kOHM', 'CONF:RES 100 KOHM', 'r2_8', 49.985, 'DET:BAND 20', 3.0, 50.015)
    _thdmm = Call('res2', 1.0E+5, 'OUT 100 kOHM', 'CONF:RES 100 KOHM', 'r2_9', 99.98, 'DET:BAND 20', 3.0, 100.02)
    # 1MOhm-2-wire
    _thdmm = Call('res2', 1.0E+5, 'OUT 100 kOHM', 'CONF:RES 1 MOHM', 'r2_10', 0.09998, 'DET:BAND 20', 3.0, 0.10002)
    _thdmm = Call('res2', 5.0E+5, 'OUT 500 kOHM', 'CONF:RES 1 MOHM', 'r2_11', 0.49994, 'DET:BAND 20', 3.0, 0.50006)
    _thdmm = Call('res2', 1.0E+6, 'OUT 1 MOHM', 'CONF:RES 1 MOHM', 'r2_12', 0.99989, 'DET:BAND 20', 3.0, 1.00011)
    # 10MOhm-2-wire
    _thdmm = Call('res2', 1.0E+6, 'OUT 1 MOHM', 'CONF:RES 10 MOHM', 'r2_13', 0.9995, 'DET:BAND 20', 3.0, 1.0005)
    _thdmm = Call('res2', 5.0E+6, 'OUT 5 MOHM', 'CONF:RES 10 MOHM', 'r2_14', 4.9979, 'DET:BAND 20', 3.0, 5.0021)
    _thdmm = Call('res2', 1.0E+7, 'OUT 10 MOHM', 'CONF:RES 10 MOHM', 'r2_15', 9.9959, 'DET:BAND 20', 3.0, 10.0041)
    # 100MOhm-2-wire
    _thdmm = Call('res2', 1.0E+7, 'OUT 10 MOHM', 'CONF:RES 100 MOHM', 'r2_16', 9.91, 'DET:BAND 20', 3.0, 10.09)
    _thdmm = Call('res2', 5.0E+7, 'OUT 50 MOHM', 'CONF:RES 100 MOHM', 'r2_17', 49.59, 'DET:BAND 20', 3.0, 50.41)
    _thdmm = Call('res2', 1.0E+8, 'OUT 100 MOHM', 'CONF:RES 100 MOHM', 'r2_18', 99.19, 'DET:BAND 20', 3.0, 100.81)
if r4_var.get() == 1:
    _th = Message('Переключите провода по четырехпроводной схеме\n для измерения сопротивления')
    _th_Reset.start()
    # 100Ohm-4-wire
    _thdmm = Call('res4', 1.0, 'OUT 1 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_1', 0.9959, 'DET:BAND 20', 3.0, 1.0041)
    _thdmm = Call('res4', 10.0, 'OUT 10 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_2', 9.995, 'DET:BAND 20', 3.0, 10.005)
    _thdmm = Call('res4', 50.0, 'OUT 50 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_3', 49.991, 'DET:BAND 20', 3.0, 50.009)
    _thdmm = Call('res4', 100.0, 'OUT 100 OHM; ZCOMP WIRE4', 'CONF:FRES 100', 'r4_4', 99.986, 'DET:BAND 20', 3.0, 100.014)
if dci_var.get() == 1:
    _th = Message('Переключите провода\n для измерения тока')
    _th_Reset.start()     
    # 0.01A
    _thdmm = Call('dci', 0.001, 'OUT 0.001 A', 'CONF:CURR:DC 0.01', 'dci1', 0.9993, 'DET:BAND 20', 3.0, 1.0007)
    _thdmm = Call('dci', 0.005, 'OUT 0.005 A', 'CONF:CURR:DC 0.01', 'dci2', 4.9973, 'DET:BAND 20', 3.0, 5.0027)
    _thdmm = Call('dci', 0.01, 'OUT 0.01 A', 'CONF:CURR:DC 0.01', 'dci3', 9.9948, 'DET:BAND 20', 3.0, 10.0052)
    # 0.1A
    _thdmm = Call('dci', 0.01, 'OUT 0.01 A', 'CONF:CURR:DC 0.1', 'dci4', 9.9945, 'DET:BAND 20', 3.0, 10.0055)
    _thdmm = Call('dci', 0.05, 'OUT 0.05 A', 'CONF:CURR:DC 0.1', 'dci5', 49.9745, 'DET:BAND 20', 3.0, 50.0255)
    _thdmm = Call('dci', 0.1, 'OUT 0.1 A', 'CONF:CURR:DC 0.1', 'dci6', 99.9495, 'DET:BAND 20', 3.0, 100.0505)
    # 1A
    _thdmm = Call('dci', 0.1, 'OUT 100 mA', 'CONF:CURR:DC 1.0', 'dci7', 0.09989, 'DET:BAND 20', 3.0, 0.10011)
    _thdmm = Call('dci', 0.5, 'OUT 0.5 A', 'CONF:CURR:DC 1.0', 'dci8', 0.49949, 'DET:BAND 20', 3.0, 0.50051)
    _thdmm = Call('dci', 1.0, 'OUT 1 A', 'CONF:CURR:DC 1.0', 'dci9', 0.99899, 'DET:BAND 20', 3.0, 1.00101)
    # 3A
    _thdmm = Call('dci', 0.3, 'OUT 0.3 A', 'CONF:CURR:DC 3.0', 'dci10', 0.29944, 'DET:BAND 20', 3.0, 0.30056)
    _thdmm = Call('dci', 1.0, 'OUT 1 A', 'CONF:CURR:DC 3.0', 'dci11', 0.9986, 'DET:BAND 20', 3.0, 1.0014)
    _thdmm = Call('dci', 2.0, 'OUT 2 A', 'CONF:CURR:DC 3.0', 'dci12', 1.9974, 'DET:BAND 20', 3.0, 2.0026)
if aci_var.get() == 1:
    _thdmm = Reset()    
    # ~1A
    _thdmm = Call('aci', 0.1, 'OUT 100 mA, 10 Hz', 'CONF:CURR:AC 1', 'aci1', 0.0957, 'DET:BAND 3', 3.0, 0.1043)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 10 Hz', 'CONF:CURR:AC 1', 'aci2', 0.4945, 'DET:BAND 3', 3.0, 0.5055)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 1', 'aci3', 0.993, 'DET:BAND 3', 3.0, 1.007)
    _thdmm = Call('aci', 0.1, 'OUT 100 mA, 1 kHz', 'CONF:CURR:AC 1', 'aci4', 0.0959, 'DET:BAND 20', 3.0, 0.1041)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 1 kHz', 'CONF:CURR:AC 1', 'aci5', 0.4955, 'DET:BAND 20', 3.0, 0.5045)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 1', 'aci6', 0.995, 'DET:BAND 3', 20.0, 1.005)            
    _thdmm = Call('aci', 0.1, 'OUT 100 mA, 5 kHz', 'CONF:CURR:AC 1', 'aci7', 0.0959, 'DET:BAND 20', 3.0, 0.1041)
    _thdmm = Call('aci', 0.5, 'OUT 0.5 A, 5 kHz', 'CONF:CURR:AC 1', 'aci8', 0.4955, 'DET:BAND 20', 3.0, 0.5045)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 1', 'aci9', 0.995, 'DET:BAND 20', 3.0, 1.005)
    # ~3A
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 10 Hz', 'CONF:CURR:AC 3', 'aci10', 0.23895, 'DET:BAND 3', 3.0, 0.36105)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 10 Hz', 'CONF:CURR:AC 3', 'aci11', 0.9365, 'DET:BAND 3', 3.0, 1.0635)
    if b1[1] == '5522A':
        _thdmm = Call('aci', 2.5, 'OUT 2.5 A, 10 Hz', 'CONF:CURR:AC 3', 'aci12', 2.43125, 'DET:BAND 3', 5.0, 2.56875)
    else:
        _thdmm = Call('aci', 2.5, 'OUT 2.5 A, 45 Hz', 'CONF:CURR:AC 3', 'aci12', 2.43125, 'DET:BAND 3', 5.0, 2.56875)
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 1 kHz', 'CONF:CURR:AC 3', 'aci13', 0.23955, 'DET:BAND 20', 3.0, 0.36045)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 1 kHz', 'CONF:CURR:AC 3', 'aci14', 0.9385, 'DET:BAND 20', 3.0, 1.0615)
    _thdmm = Call('aci', 2.5, 'OUT 2.5 A, 1 kHz', 'CONF:CURR:AC 3', 'aci15', 2.43625, 'DET:BAND 20', 5.0, 2.56375)            
    _thdmm = Call('aci', 0.3, 'OUT 0.3 A, 5 kHz', 'CONF:CURR:AC 3', 'aci16', 0.23955, 'DET:BAND 20', 3.0, 0.36045)
    _thdmm = Call('aci', 1.0, 'OUT 1 A, 5 kHz', 'CONF:CURR:AC 3', 'aci17', 0.9385, 'DET:BAND 20', 3.0, 1.0615)
    if b1[1] == '5522A':
        _thdmm = Call('aci', 2.5, 'OUT 2.5 A, 5 kHz', 'CONF:CURR:AC 3', 'aci18', 2.43625, 'DET:BAND 20', 5.0, 2.56375)
    else:
        _thdmm = Call('aci', 2.5, 'OUT 2.5 A, 1 kHz', 'CONF:CURR:AC 3', 'aci18', 2.43625, 'DET:BAND 20', 5.0, 2.56375)

_th = Message('Калибровка завершена')
_th_Reset.start()