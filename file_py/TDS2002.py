# -*- coding: utf-8 -*-
for j in range(1,3,1):
    # dcv
    Message(f'Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Reset()
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 500E-6', '')
    Call_oscill('VOLT 0.006', f'CH{j}:VOL 0.002', 'MEASU:MEAS1:VAL?', f'dcv{j}+_1', f'gdcv{j}+_1', 4)
    Call_oscill('VOLT -0.006', f'CH{j}:VOL 0.002', 'MEASU:MEAS1:VAL?', f'dcv{j}-_1', f'gdcv{j}-_1', 4)
    Call_oscill('VOLT 0.015', f'CH{j}:VOL 0.005', 'MEASU:MEAS1:VAL?', f'dcv{j}+_2', f'gdcv{j}+_2', 3)
    Call_oscill('VOLT -0.015', f'CH{j}:VOL 0.005', 'MEASU:MEAS1:VAL?', f'dcv{j}-_2', f'gdcv{j}-_2', 3)
    Call_oscill('VOLT 0.03', f'CH{j}:VOL 0.01', 'MEASU:MEAS1:VAL?', f'dcv{j}+_3', f'gdcv{j}+_3', 3)
    Call_oscill('VOLT -0.03', f'CH{j}:VOL 0.01', 'MEASU:MEAS1:VAL?', f'dcv{j}-_3', f'gdcv{j}-_3', 3)
    Call_oscill('VOLT 0.06', f'CH{j}:VOL 0.02', 'MEASU:MEAS1:VAL?', f'dcv{j}+_4', f'gdcv{j}+_4', 3)
    Call_oscill('VOLT -0.06', f'CH{j}:VOL 0.02', 'MEASU:MEAS1:VAL?', f'dcv{j}-_4', f'gdcv{j}-_4', 3)
    Call_oscill('VOLT 0.15', f'CH{j}:VOL 0.05', 'MEASU:MEAS1:VAL?', f'dcv{j}+_5', f'gdcv{j}+_5', 3)
    Call_oscill('VOLT -0.15', f'CH{j}:VOL 0.05', 'MEASU:MEAS1:VAL?', f'dcv{j}-_5', f'gdcv{j}-_5', 3)
    Call_oscill('VOLT 0.3', f'CH{j}:VOL 0.1', 'MEASU:MEAS1:VAL?', f'dcv{j}+_6', f'gdcv{j}+_6', 3)
    Call_oscill('VOLT -0.3', f'CH{j}:VOL 0.1', 'MEASU:MEAS1:VAL?', f'dcv{j}-_6', f'gdcv{j}-_6', 3)
    Call_oscill('VOLT 0.6', f'CH{j}:VOL 0.2', 'MEASU:MEAS1:VAL?', f'dcv{j}+_7', f'gdcv{j}+_7', 3)
    Call_oscill('VOLT -0.6', f'CH{j}:VOL 0.2', 'MEASU:MEAS1:VAL?', f'dcv{j}-_7', f'gdcv{j}-_7', 3)
    Call_oscill('VOLT 1.5', f'CH{j}:VOL 0.5', 'MEASU:MEAS1:VAL?', f'dcv{j}+_8', f'gdcv{j}+_8', 3)
    Call_oscill('VOLT -1.5', f'CH{j}:VOL 0.5', 'MEASU:MEAS1:VAL?', f'dcv{j}-_8', f'gdcv{j}-_8', 3)
    Call_oscill('VOLT 3', f'CH{j}:VOL 1', 'MEASU:MEAS1:VAL?', f'dcv{j}+_9', f'gdcv{j}+_9', 3)
    Call_oscill('VOLT -3', f'CH{j}:VOL 1', 'MEASU:MEAS1:VAL?', f'dcv{j}-_9', f'gdcv{j}-_9', 3)
    Call_oscill('VOLT 6', f'CH{j}:VOL 2', 'MEASU:MEAS1:VAL?', f'dcv{j}+_10', f'gdcv{j}+_10', 3)
    Call_oscill('VOLT -6', f'CH{j}:VOL 2', 'MEASU:MEAS1:VAL?', f'dcv{j}-_10', f'gdcv{j}-_10', 3)
    Call_oscill('VOLT 15', f'CH{j}:VOL 5', 'MEASU:MEAS1:VAL?', f'dcv{j}+_11', f'gdcv{j}+_11', 3)
    Call_oscill('VOLT -15', f'CH{j}:VOL 5', 'MEASU:MEAS1:VAL?', f'dcv{j}-_11', f'gdcv{j}-_11', 3)
    # period
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_1', f'gti{j}_1', 0.61)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 100E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_2', f'gti{j}_2', 0.81)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 250E-9', 'PER:FIX 500E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_3', f'gti{j}_3', 1.63)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 1E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_4', f'gti{j}_4', 2.05)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2.5E-3', 'PER:FIX 5E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_5', f'gti{j}_5', 10.25)
    # trise
    Message(f'Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5E-9', '')
    Call_oscill('VOLT 3.1', f'CH{j}:VOL 5\nTRIG:MAI:LEV -1.8', 'MEASU:MEAS4:VAL?', f'tr{j}_1', '', 5.8)
    Call_oscill('VOLT 3.1', f'CH{j}:VOL 2\nTRIG:MAI:LEV -1.5', 'MEASU:MEAS4:VAL?', f'tr{j}_2', '', 5.8)
    Call_oscill('VOLT 3.1', f'CH{j}:VOL 1\nTRIG:MAI:LEV -1.5', 'MEASU:MEAS4:VAL?', f'tr{j}_3', '', 5.8)
    Call_oscill('VOLT 3', f'CH{j}:VOL 0.5\nTRIG:MAI:LEV -0.5', 'MEASU:MEAS4:VAL?', f'tr{j}_4', '', 5.8)
    Call_oscill('VOLT 1.2', f'CH{j}:VOL 0.2\nTRIG:MAI:LEV -0.1', 'MEASU:MEAS4:VAL?', f'tr{j}_5', '', 5.8)
    Call_oscill('VOLT 0.6', f'CH{j}:VOL 0.1\nTRIG:MAI:LEV -0.1', 'MEASU:MEAS4:VAL?', f'tr{j}_6', '', 5.8)
    Call_oscill('VOLT 0.3', f'CH{j}:VOL 0.05\nTRIG:MAI:LEV -0.05', 'MEASU:MEAS4:VAL?', f'tr{j}_7', '', 5.8)
    Call_oscill('VOLT 0.12', f'CH{j}:VOL 0.02\nTRIG:MAI:LEV -0.05', 'MEASU:MEAS4:VAL?', f'tr{j}_8', '', 5.8)
    Call_oscill('VOLT 0.06', f'CH{j}:VOL 0.01\nTRIG:MAI:LEV -0.03', 'MEASU:MEAS4:VAL?', f'tr{j}_9', '', 5.8)
    Call_oscill('VOLT 0.03', f'CH{j}:VOL 0.005\nTRIG:MAI:LEV -0.015', 'MEASU:MEAS4:VAL?', f'tr{j}_10', '', 5.8)

Message('Калибровка завершена')
Clear_merge()
Reset()
