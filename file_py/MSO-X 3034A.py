# -*- coding: utf-8 -*-
#1 dcv
Message('Подключите формирователь без внешней нагрузки на первый канал осциллографа')
Reset()
Param_msox3('1', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100.0E-6', '')
Call_oscill('VOLT 35.0', 'CHAN1:SCAL 5', ':MEAS:VMAX?', 'dcv_1', '', 0.8)
Call_oscill('VOLT 14.0', 'CHAN1:SCAL 2', ':MEAS:VMAX?', 'dcv_2', '', 0.32)
Call_oscill('VOLT 7.0', 'CHAN1:SCAL 1', ':MEAS:VMAX?', 'dcv_3', '', 0.16)
Call_oscill('VOLT 3.5', 'CHAN1:SCAL 0.5', ':MEAS:VMAX?', 'dcv_4', '', 0.08)
Call_oscill('VOLT 1.4', 'CHAN1:SCAL 0.2', ':MEAS:VMAX?', 'dcv_5', '', 0.032)
Call_oscill('VOLT 0.7', 'CHAN1:SCAL 0.1', ':MEAS:VMAX?', 'dcv_6', '', 0.016)
Call_oscill('VOLT 0.35', 'CHAN1:SCAL 0.05', ':MEAS:VMAX?', 'dcv_7', '', 0.008)
Call_oscill('VOLT 0.14', 'CHAN1:SCAL 0.02', ':MEAS:VMAX?', 'dcv_8', '', 0.0032)
Call_oscill('VOLT 0.07', 'CHAN1:SCAL 0.01', ':MEAS:VMAX?', 'dcv_9', '', 0.0016)
Call_oscill('VOLT 0.035', 'CHAN1:SCAL 0.005', ':MEAS:VMAX?', 'dcv_10', '', 0.0008)
Call_oscill('VOLT 0.014', 'CHAN1:SCAL 0.002', ':MEAS:VMAX?', 'dcv_11', '', 0.00064)
#1 trise
Reset()
Message('Подключите внешнию нагрузку 50 Ом на первый канал осциллографа')
Param_msox3('1', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TIM:SCAL 5.0E-9', '')
Call_oscill('VOLT 0.25', 'CHAN1:SCAL 0.05', ':MEAS:RIS?', 'fr_1', 'tr_1', 350)
#2 dcv
th = Message('Подключите формирователь без внешней нагрузки на второй канал осциллографа')
Reset()
Param_msox3('2', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100.0E-6', '')
Call_oscill('VOLT 35.0', 'CHAN2:SCAL 5', ':MEAS:VMAX?', 'dcv_12', '', 0.8)
Call_oscill('VOLT 14.0', 'CHAN2:SCAL 2', ':MEAS:VMAX?', 'dcv_13', '', 0.32)
Call_oscill('VOLT 7.0', 'CHAN2:SCAL 1', ':MEAS:VMAX?', 'dcv_14', '', 0.16)
Call_oscill('VOLT 3.5', 'CHAN2:SCAL 0.5', ':MEAS:VMAX?', 'dcv_15', '', 0.08)
Call_oscill('VOLT 1.4', 'CHAN2:SCAL 0.2', ':MEAS:VMAX?', 'dcv_16', '', 0.032)
Call_oscill('VOLT 0.7', 'CHAN2:SCAL 0.1', ':MEAS:VMAX?', 'dcv_17', '', 0.016)
Call_oscill('VOLT 0.35', 'CHAN2:SCAL 0.05', ':MEAS:VMAX?', 'dcv_18', '', 0.008)
Call_oscill('VOLT 0.14', 'CHAN2:SCAL 0.02', ':MEAS:VMAX?', 'dcv_19', '', 0.0032)
Call_oscill('VOLT 0.07', 'CHAN2:SCAL 0.01', ':MEAS:VMAX?', 'dcv_20', '', 0.0016)
Call_oscill('VOLT 0.035', 'CHAN2:SCAL 0.005', ':MEAS:VMAX?', 'dcv_21', '', 0.0008)
Call_oscill('VOLT 0.014', 'CHAN2:SCAL 0.002', ':MEAS:VMAX?', 'dcv_22', '', 0.00064)
#2 trise
Reset()
Message('Подключите внешнию нагрузку 50 Ом на второй канал осциллографа')
Param_msox3('2', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TIM:SCAL 5.0E-9', '')
Call_oscill('VOLT 0.25', 'CHAN2:SCAL 0.05', ':MEAS:RIS?', 'fr_2', 'tr_2', 350)
#3 dcv
th = Message('Подключите формирователь без внешней нагрузки на третий канал осциллографа')
Reset()
Param_msox3('3', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100.0E-6', '')
Call_oscill('VOLT 35.0', 'CHAN3:SCAL 5', ':MEAS:VMAX?', 'dcv_23', '', 0.8)
Call_oscill('VOLT 14.0', 'CHAN3:SCAL 2', ':MEAS:VMAX?', 'dcv_24', '', 0.32)
Call_oscill('VOLT 7.0', 'CHAN3:SCAL 1', ':MEAS:VMAX?', 'dcv_25', '', 0.16)
Call_oscill('VOLT 3.5', 'CHAN3:SCAL 0.5', ':MEAS:VMAX?', 'dcv_26', '', 0.08)
Call_oscill('VOLT 1.4', 'CHAN3:SCAL 0.2', ':MEAS:VMAX?', 'dcv_27', '', 0.032)
Call_oscill('VOLT 0.7', 'CHAN3:SCAL 0.1', ':MEAS:VMAX?', 'dcv_28', '', 0.016)
Call_oscill('VOLT 0.35', 'CHAN3:SCAL 0.05', ':MEAS:VMAX?', 'dcv_29', '', 0.008)
Call_oscill('VOLT 0.14', 'CHAN3:SCAL 0.02', ':MEAS:VMAX?', 'dcv_30', '', 0.0032)
Call_oscill('VOLT 0.07', 'CHAN3:SCAL 0.01', ':MEAS:VMAX?', 'dcv_31', '', 0.0016)
Call_oscill('VOLT 0.035', 'CHAN3:SCAL 0.005', ':MEAS:VMAX?', 'dcv_32', '', 0.0008)
Call_oscill('VOLT 0.014', 'CHAN3:SCAL 0.002', ':MEAS:VMAX?', 'dcv_33', '', 0.00064)
#3 trise
Reset()
Message('Подключите внешнию нагрузку 50 Ом на третий канал осциллографа')
Param_msox3('3', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TIM:SCAL 5.0E-9', '')
Call_oscill('VOLT 0.25', 'CHAN2:SCAL 0.05', ':MEAS:RIS?', 'fr_3', 'tr_3', 350)
#4 dcv
th = Message('Подключите формирователь без внешней нагрузки на четвёртный канал осциллографа')
Reset()
Param_msox3('4', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100.0E-6', '')
Call_oscill('VOLT 35.0', 'CHAN4:SCAL 5', ':MEAS:VMAX?', 'dcv_34', '', 0.8)
Call_oscill('VOLT 14.0', 'CHAN4:SCAL 2', ':MEAS:VMAX?', 'dcv_35', '', 0.32)
Call_oscill('VOLT 7.0', 'CHAN4:SCAL 1', ':MEAS:VMAX?', 'dcv_36', '', 0.16)
Call_oscill('VOLT 3.5', 'CHAN4:SCAL 0.5', ':MEAS:VMAX?', 'dcv_37', '', 0.08)
Call_oscill('VOLT 1.4', 'CHAN4:SCAL 0.2', ':MEAS:VMAX?', 'dcv_38', '', 0.032)
Call_oscill('VOLT 0.7', 'CHAN4:SCAL 0.1', ':MEAS:VMAX?', 'dcv_39', '', 0.016)
Call_oscill('VOLT 0.35', 'CHAN4:SCAL 0.05', ':MEAS:VMAX?', 'dcv_40', '', 0.008)
Call_oscill('VOLT 0.14', 'CHAN4:SCAL 0.02', ':MEAS:VMAX?', 'dcv_41', '', 0.0032)
Call_oscill('VOLT 0.07', 'CHAN4:SCAL 0.01', ':MEAS:VMAX?', 'dcv_42', '', 0.0016)
Call_oscill('VOLT 0.035', 'CHAN4:SCAL 0.005', ':MEAS:VMAX?', 'dcv_43', '', 0.0008)
Call_oscill('VOLT 0.014', 'CHAN4:SCAL 0.002', ':MEAS:VMAX?', 'dcv_44', '', 0.00064)
#4 trise
Reset()
Message('Подключите внешнию нагрузку 50 Ом на четвертый канал осциллографа')
Param_msox3('4', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TIM:SCAL 5.0E-9', '')
Call_oscill('VOLT 0.25', 'CHAN2:SCAL 0.05', ':MEAS:RIS?', 'fr_4', 'tr_4', 350)
Message('Калибровка завершена')
#Reset()
