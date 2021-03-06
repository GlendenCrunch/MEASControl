# -*- coding: utf-8 -*-
#1 dcv
_th = Message('Подключите формирователь без внешней нагрузки на первый канал осциллографа')
_th = Reset()
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 50.0E-9', '')
_thosc = Call_oscill('VOLT 0.006', 'CH1:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_1', 'gdcv_1', 4)
_thosc = Call_oscill('VOLT -0.006', 'CH1:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_2', 'gdcv_2', 4)
_thosc = Call_oscill('VOLT 0.015', 'CH1:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_3', 'gdcv_3', 4)
_thosc = Call_oscill('VOLT -0.015', 'CH1:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_4', 'gdcv_4', 4)
_thosc = Call_oscill('VOLT 0.03', 'CH1:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_5', 'gdcv_5', 3)
_thosc = Call_oscill('VOLT -0.03', 'CH1:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_6', 'gdcv_6', 3)
_thosc = Call_oscill('VOLT 0.06', 'CH1:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_7', 'gdcv_7', 3)
_thosc = Call_oscill('VOLT -0.06', 'CH1:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_8', 'gdcv_8', 3)
_thosc = Call_oscill('VOLT 0.15', 'CH1:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_9', 'gdcv_9', 3)
_thosc = Call_oscill('VOLT -0.15', 'CH1:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_10', 'gdcv_10', 3)
_thosc = Call_oscill('VOLT 0.3', 'CH1:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_11', 'gdcv_11', 3)
_thosc = Call_oscill('VOLT -0.3', 'CH1:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_12', 'gdcv_12', 3)
_thosc = Call_oscill('VOLT 0.6', 'CH1:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_13', 'gdcv_13', 3)
_thosc = Call_oscill('VOLT -0.6', 'CH1:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_14', 'gdcv_14', 3)
_thosc = Call_oscill('VOLT 1.5', 'CH1:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_15', 'gdcv_15', 3)
_thosc = Call_oscill('VOLT -1.5', 'CH1:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_16', 'gdcv_16', 3)
_thosc = Call_oscill('VOLT 3.0', 'CH1:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_17', 'gdcv_17', 3)
_thosc = Call_oscill('VOLT -3.0', 'CH1:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_18', 'gdcv_18', 3)
_thosc = Call_oscill('VOLT 6.0', 'CH1:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_19', 'gdcv_19', 3)
_thosc = Call_oscill('VOLT -6.0', 'CH1:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_20', 'gdcv_20', 3)
_thosc = Call_oscill('VOLT 15.0', 'CH1:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_21', 'gdcv_21', 3)
_thosc = Call_oscill('VOLT -15.0', 'CH1:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_22', 'gdcv_22', 3)
#1 period
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH1:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_1', 'gti_1', 0.61)
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 100E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH1:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_2', 'gti_2', 0.81)
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 250E-9', 'PER:FIX 500E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH1:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_3', 'gti_3', 1.63)
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 1E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH1:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_4', 'gti_4', 2.05)
_th = Param_tds2('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2.5E-3', 'PER:FIX 5E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH1:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_5', 'gti_5', 10.25)
#1 trise
_th = Message('Подключите внешнию нагрузку 50 Ом на первый канал осциллографа')
_th = Param_tds2('1', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5.0E-9', '')
_thosc = Call_oscill('VOLT 0.5', 'CH1:VOL 0.1', 'MEASU:MEAS4:VAL?', 'tr_1', '', 2.1)
#2 dcv
_th = Message('Подключите формирователь без внешней нагрузки на второй канал осциллографа')
_th = Reset()
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 50.0E-9', '')
_thosc = Call_oscill('VOLT 0.006', 'CH2:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_23', 'gdcv_23', 4)
_thosc = Call_oscill('VOLT -0.006', 'CH2:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_24', 'gdcv_24', 4)
_thosc = Call_oscill('VOLT 0.015', 'CH2:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_25', 'gdcv_25', 4)
_thosc = Call_oscill('VOLT -0.015', 'CH2:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_26', 'gdcv_26', 4)
_thosc = Call_oscill('VOLT 0.03', 'CH2:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_27', 'gdcv_27', 3)
_thosc = Call_oscill('VOLT -0.03', 'CH2:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_28', 'gdcv_28', 3)
_thosc = Call_oscill('VOLT 0.06', 'CH2:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_29', 'gdcv_29', 3)
_thosc = Call_oscill('VOLT -0.06', 'CH2:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_30', 'gdcv_30', 3)
_thosc = Call_oscill('VOLT 0.15', 'CH2:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_31', 'gdcv_31', 3)
_thosc = Call_oscill('VOLT -0.15', 'CH2:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_32', 'gdcv_32', 3)
_thosc = Call_oscill('VOLT 0.3', 'CH2:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_33', 'gdcv_33', 3)
_thosc = Call_oscill('VOLT -0.3', 'CH2:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_34', 'gdcv_34', 3)
_thosc = Call_oscill('VOLT 0.6', 'CH2:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_35', 'gdcv_35', 3)
_thosc = Call_oscill('VOLT -0.6', 'CH2:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_36', 'gdcv_36', 3)
_thosc = Call_oscill('VOLT 1.5', 'CH2:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_37', 'gdcv_37', 3)
_thosc = Call_oscill('VOLT -1.5', 'CH2:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_38', 'gdcv_38', 3)
_thosc = Call_oscill('VOLT 3.0', 'CH2:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_39', 'gdcv_39', 3)
_thosc = Call_oscill('VOLT -3.0', 'CH2:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_40', 'gdcv_40', 3)
_thosc = Call_oscill('VOLT 6.0', 'CH2:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_41', 'gdcv_41', 3)
_thosc = Call_oscill('VOLT -6.0', 'CH2:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_42', 'gdcv_42', 3)
_thosc = Call_oscill('VOLT 15.0', 'CH2:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_43', 'gdcv_43', 3)
_thosc = Call_oscill('VOLT -15.0', 'CH2:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_44', 'gdcv_44', 3)
#2 period
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH2:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_6', 'gti_6', 0.61)
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 100E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH2:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_7', 'gti_7', 0.81)
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 250E-9', 'PER:FIX 500E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH2:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_8', 'gti_8', 1.63)
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 1E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH2:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_9', 'gti_9', 2.05)
_th = Param_tds2('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2.5E-3', 'PER:FIX 5E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH2:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_10', 'gti_10', 10.25)
#2 trise
_th = Message('Подключите внешнию нагрузку 50 Ом на второй канал осциллографа')
_th = Param_tds2('2', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5.0E-9', '')
_thosc = Call_oscill('VOLT 0.5', 'CH2:VOL 0.1', 'MEASU:MEAS4:VAL?', 'tr_2', '', 2.1)
#3 dcv
_th = Message('Подключите формирователь без внешней нагрузки на третий канал осциллографа')
_th = Reset()
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 50.0E-9', '')
_thosc = Call_oscill('VOLT 0.006', 'CH3:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_45', 'gdcv_45', 4)
_thosc = Call_oscill('VOLT -0.006', 'CH3:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_46', 'gdcv_46', 4)
_thosc = Call_oscill('VOLT 0.015', 'CH3:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_47', 'gdcv_47', 4)
_thosc = Call_oscill('VOLT -0.015', 'CH3:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_48', 'gdcv_48', 4)
_thosc = Call_oscill('VOLT 0.03', 'CH3:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_49', 'gdcv_49', 3)
_thosc = Call_oscill('VOLT -0.03', 'CH3:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_50', 'gdcv_50', 3)
_thosc = Call_oscill('VOLT 0.06', 'CH3:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_51', 'gdcv_51', 3)
_thosc = Call_oscill('VOLT -0.06', 'CH3:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_52', 'gdcv_52', 3)
_thosc = Call_oscill('VOLT 0.15', 'CH3:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_53', 'gdcv_53', 3)
_thosc = Call_oscill('VOLT -0.15', 'CH3:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_54', 'gdcv_54', 3)
_thosc = Call_oscill('VOLT 0.3', 'CH3:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_55', 'gdcv_55', 3)
_thosc = Call_oscill('VOLT -0.3', 'CH3:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_56', 'gdcv_56', 3)
_thosc = Call_oscill('VOLT 0.6', 'CH3:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_57', 'gdcv_57', 3)
_thosc = Call_oscill('VOLT -0.6', 'CH3:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_58', 'gdcv_58', 3)
_thosc = Call_oscill('VOLT 1.5', 'CH3:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_59', 'gdcv_59', 3)
_thosc = Call_oscill('VOLT -1.5', 'CH3:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_60', 'gdcv_60', 3)
_thosc = Call_oscill('VOLT 3.0', 'CH3:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_61', 'gdcv_61', 3)
_thosc = Call_oscill('VOLT -3.0', 'CH3:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_62', 'gdcv_62', 3)
_thosc = Call_oscill('VOLT 6.0', 'CH3:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_63', 'gdcv_63', 3)
_thosc = Call_oscill('VOLT -6.0', 'CH3:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_64', 'gdcv_64', 3)
_thosc = Call_oscill('VOLT 15.0', 'CH3:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_65', 'gdcv_65', 3)
_thosc = Call_oscill('VOLT -15.0', 'CH3:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_66', 'gdcv_66', 3)
#3 period
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH3:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_11', 'gti_11', 0.61)
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 100E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH3:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_12', 'gti_12', 0.81)
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 250E-9', 'PER:FIX 500E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH3:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_13', 'gti_13', 1.63)
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 1E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH3:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_14', 'gti_14', 2.05)
_th = Param_tds2('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2.5E-3', 'PER:FIX 5E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH3:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_15', 'gti_15', 10.25)
#3 trise
_th = Message('Подключите внешнию нагрузку 50 Ом на третий канал осциллографа')
_th = Param_tds2('3', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5.0E-9', '')
_thosc = Call_oscill('VOLT 0.5', 'CH3:VOL 0.1', 'MEASU:MEAS4:VAL?', 'tr_3', '', 2.1)
#4 dcv
_th = Message('Подключите формирователь без внешней нагрузки на четвертый канал осциллографа')
_th = Reset()
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 50.0E-9', '')
_thosc = Call_oscill('VOLT 0.006', 'CH4:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_67', 'gdcv_67', 4)
_thosc = Call_oscill('VOLT -0.006', 'CH4:VOL 0.002', 'MEASU:MEAS1:VAL?', 'dcv_68', 'gdcv_68', 4)
_thosc = Call_oscill('VOLT 0.015', 'CH4:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_69', 'gdcv_69', 4)
_thosc = Call_oscill('VOLT -0.015', 'CH4:VOL 0.005', 'MEASU:MEAS1:VAL?', 'dcv_70', 'gdcv_70', 4)
_thosc = Call_oscill('VOLT 0.03', 'CH4:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_71', 'gdcv_71', 3)
_thosc = Call_oscill('VOLT -0.03', 'CH4:VOL 0.01', 'MEASU:MEAS1:VAL?', 'dcv_72', 'gdcv_72', 3)
_thosc = Call_oscill('VOLT 0.06', 'CH4:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_73', 'gdcv_73', 3)
_thosc = Call_oscill('VOLT -0.06', 'CH4:VOL 0.02', 'MEASU:MEAS1:VAL?', 'dcv_74', 'gdcv_74', 3)
_thosc = Call_oscill('VOLT 0.15', 'CH4:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_75', 'gdcv_75', 3)
_thosc = Call_oscill('VOLT -0.15', 'CH4:VOL 0.05', 'MEASU:MEAS1:VAL?', 'dcv_76', 'gdcv_76', 3)
_thosc = Call_oscill('VOLT 0.3', 'CH4:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_77', 'gdcv_77', 3)
_thosc = Call_oscill('VOLT -0.3', 'CH4:VOL 0.1', 'MEASU:MEAS1:VAL?', 'dcv_78', 'gdcv_78', 3)
_thosc = Call_oscill('VOLT 0.6', 'CH4:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_79', 'gdcv_79', 3)
_thosc = Call_oscill('VOLT -0.6', 'CH4:VOL 0.2', 'MEASU:MEAS1:VAL?', 'dcv_80', 'gdcv_80', 3)
_thosc = Call_oscill('VOLT 1.5', 'CH4:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_81', 'gdcv_81', 3)
_thosc = Call_oscill('VOLT -1.5', 'CH4:VOL 0.5', 'MEASU:MEAS1:VAL?', 'dcv_82', 'gdcv_82', 3)
_thosc = Call_oscill('VOLT 3.0', 'CH4:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_83', 'gdcv_83', 3)
_thosc = Call_oscill('VOLT -3.0', 'CH4:VOL 1', 'MEASU:MEAS1:VAL?', 'dcv_84', 'gdcv_84', 3)
_thosc = Call_oscill('VOLT 6.0', 'CH4:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_85', 'gdcv_85', 3)
_thosc = Call_oscill('VOLT -6.0', 'CH4:VOL 2', 'MEASU:MEAS1:VAL?', 'dcv_86', 'gdcv_86', 3)
_thosc = Call_oscill('VOLT 15.0', 'CH4:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_87', 'gdcv_87', 3)
_thosc = Call_oscill('VOLT -15.0', 'CH4:VOL 5', 'MEASU:MEAS1:VAL?', 'dcv_88', 'gdcv_88', 3)
#4 period
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH4:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_16', 'gti_16', 0.61)
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 100E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH4:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_17', 'gti_17', 0.81)
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 250E-9', 'PER:FIX 500E-09')
_thosc = Call_oscill('VOLT 1.0', 'CH4:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_18', 'gti_18', 1.63)
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 1E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH4:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_19', 'gti_19', 2.05)
_th = Param_tds2('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2.5E-3', 'PER:FIX 5E-03')
_thosc = Call_oscill('VOLT 1.0', 'CH4:VOL 0.2', 'MEASU:MEAS3:VAL?', 'ti_20', 'gti_20', 10.25)
#4 trise
_th = Message('Подключите внешнию нагрузку 50 Ом на четвертый канал осциллографа')
_th = Param_tds2('4', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5.0E-9', '')
_thosc = Call_oscill('VOLT 0.5', 'CH4:VOL 0.1', 'MEASU:MEAS4:VAL?', 'tr_4', '', 2.1)
_th = Message('Калибровка завершена')
_th = Reset()
