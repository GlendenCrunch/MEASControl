# -*- coding: utf-8 -*-
for j in range(1,3,1):
    Supportfunc(f'message-Подключите формирователь на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    # dcv # изменена для периодической поверки
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', '')
    Call_oscill('VOLT 0.014', f'CHAN{j}:SCAL 0.002', ':MEAS:VAV?', f'dcv{j}+_1', f'gdcv{j}+_1', 0.787)
    Call_oscill('VOLT -0.014', f'CHAN{j}:SCAL 0.002', ':MEAS:VAV?', f'dcv{j}-_1', f'gdcv{j}-_1', 0.787)
    Call_oscill('VOLT 0.035', f'CHAN{j}:SCAL 0.005', ':MEAS:VAV?', f'dcv{j}+_2', f'gdcv{j}+_2', 0.96)
    Call_oscill('VOLT -0.035', f'CHAN{j}:SCAL 0.005', ':MEAS:VAV?', f'dcv{j}-_2', f'gdcv{j}-_2', 0.96)
    Call_oscill('VOLT 0.07', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', f'dcv{j}+_3', f'gdcv{j}+_3', 1.92)
    Call_oscill('VOLT -0.07', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', f'dcv{j}-_3', f'gdcv{j}-_3', 1.92)
    Call_oscill('VOLT 0.14', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', f'dcv{j}+_4', f'gdcv{j}+_4', 3.84)
    Call_oscill('VOLT -0.14', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', f'dcv{j}-_4', f'gdcv{j}-_4', 3.84)
    Call_oscill('VOLT 0.35', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', f'dcv{j}+_5', f'gdcv{j}+_5', 9.6)
    Call_oscill('VOLT -0.35', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', f'dcv{j}-_5', f'gdcv{j}-_5', 9.6)
    Call_oscill('VOLT 0.7', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', f'dcv{j}+_6', f'gdcv{j}+_6', 19.2)
    Call_oscill('VOLT -0.7', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', f'dcv{j}-_6', f'gdcv{j}-_6', 19.2)
    Call_oscill('VOLT 1.4', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', f'dcv{j}+_7', f'gdcv{j}+_7', 38.4)
    Call_oscill('VOLT -1.4', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', f'dcv{j}-_7', f'gdcv{j}-_7', 38.4)
    Call_oscill('VOLT 3.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', f'dcv{j}+_8', f'gdcv{j}+_8', 96)
    Call_oscill('VOLT -3.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', f'dcv{j}-_8', f'gdcv{j}-_8', 96)
    Call_oscill('VOLT 7', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', f'dcv{j}+_9', f'gdcv{j}+_9', 192)
    Call_oscill('VOLT -7', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', f'dcv{j}-_9', f'gdcv{j}-_9', 192)
    Call_oscill('VOLT 14', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', f'dcv{j}+_10', f'gdcv{j}+_10', 384)
    Call_oscill('VOLT -14', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', f'dcv{j}-_10', f'gdcv{j}-_10', 384)
    Call_oscill('VOLT 35', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', f'dcv{j}+_11', f'gdcv{j}+_11', 960)
    Call_oscill('VOLT -35', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', f'dcv{j}-_11', f'gdcv{j}-_11', 960)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
