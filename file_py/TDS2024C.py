# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SQU;, PAR:SQU:POL SYMM', 'HOR:SEC 500E-6', '')
    Call_oscill('VOLT 0.012', f'CH{j}:VOL 0.002', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_1', 4)
    Call_oscill('VOLT 0.03', f'CH{j}:VOL 0.005', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_2', 4)
    Call_oscill('VOLT 0.06', f'CH{j}:VOL 0.01', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_3', 3)
    Call_oscill('VOLT 0.12', f'CH{j}:VOL 0.02', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_4', 3)
    Call_oscill('VOLT 0.3', f'CH{j}:VOL 0.05', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_5', 3)
    Call_oscill('VOLT 0.6', f'CH{j}:VOL 0.1', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_6', 3)
    Call_oscill('VOLT 1.2', f'CH{j}:VOL 0.2', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_7', 3)
    Call_oscill('VOLT 3', f'CH{j}:VOL 0.5', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_8', 3)
    Call_oscill('VOLT 6', f'CH{j}:VOL 1', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_9', 3)
    Call_oscill('VOLT 12', f'CH{j}:VOL 2', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_10', 3)
    Call_oscill('VOLT 30', f'CH{j}:VOL 5', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_11', 3)
    # period
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-9', 'PER:FIX 5E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_31', '', 0.625)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-9', 'PER:FIX 10E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_30', '', 0.645)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-9', 'PER:FIX 20E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_29', '', 0.685)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 50E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_28', '', 0.805)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 100E-9', 'PER:FIX 100E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_27', '', 1.005)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 200E-9', 'PER:FIX 200E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_26', '', 1.405)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-9', 'PER:FIX 500E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_25', '', 2.605)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 1E-6', 'PER:FIX 1E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_24', '', 0.0096)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2E-6', 'PER:FIX 2E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_23', '', 0.0136)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-6', 'PER:FIX 5E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_22', '', 0.0256)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-6', 'PER:FIX 10E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_21', '', 0.0456)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-6', 'PER:FIX 20E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_20', '', 0.0856)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-6', 'PER:FIX 50E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_19', '', 0.2056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 100E-6', 'PER:FIX 100E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_18', '', 0.4056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 200E-6', 'PER:FIX 200E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_17', '', 0.8056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 500E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_16', '', 2.0056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 1E-3', 'PER:FIX 1E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_15', '', 0.009)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2E-3', 'PER:FIX 2E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_14', '', 0.013)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-3', 'PER:FIX 5E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_13', '', 0.025)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-3', 'PER:FIX 10E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_12', '', 0.045)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-3', 'PER:FIX 20E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_11', '', 0.085)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-3', 'PER:FIX 50E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_10', '', 0.205)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 100E-3', 'PER:FIX 100E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_9', '', 0.405)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 200E-3', 'PER:FIX 200E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_8', '', 0.805)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-3', 'PER:FIX 500E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_7', '', 2.005)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 1', 'PER:FIX 1')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_6', '', 0.009)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2', 'PER:FIX 2')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_5', '', 0.013)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5', 'PER:FIX 5')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_4', '', 0.025)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10', 'PER:FIX 10')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_3', '', 0.045)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20', 'PER:FIX 20')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_2', '', 0.085)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50', 'PER:FIX 50')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_1', '', 0.205)
    # trise
    Supportfunc(f'message-Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 2.5E-9', '')
    Call_oscill('VOLT 0.03', f'CH{j}:VOL 0.005\nTRIG:MAI:LEV -0.02', 'MEASU:MEAS4:VAL?', f'tr{j}_2', '', 2.1)
    Call_oscill('VOLT 0.06', f'CH{j}:VOL 0.01\nTRIG:MAI:LEV -0.02', 'MEASU:MEAS4:VAL?', f'tr{j}_3', '', 2.1)
    Call_oscill('VOLT 0.12', f'CH{j}:VOL 0.02\nTRIG:MAI:LEV -0.02', 'MEASU:MEAS4:VAL?', f'tr{j}_4', '', 2.1)
    Call_oscill('VOLT 0.3', f'CH{j}:VOL 0.05\nTRIG:MAI:LEV -0.02', 'MEASU:MEAS4:VAL?', f'tr{j}_5', '', 2.1)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 2.5E-9', '')
    Call_oscill('VOLT 0.6', f'CH{j}:VOL 0.1\nTRIG:MAI:LEV -0.1', 'MEASU:MEAS4:VAL?', f'tr{j}_6', '', 2.1)
    Call_oscill('VOLT 1.2', f'CH{j}:VOL 0.2\nTRIG:MAI:LEV -0.1', 'MEASU:MEAS4:VAL?', f'tr{j}_7', '', 2.1)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 2.5E-9', '')
    Call_oscill('VOLT 2.9', f'CH{j}:VOL 0.5\nTRIG:MAI:LEV -1.6', 'MEASU:MEAS4:VAL?', f'tr{j}_8', '', 2.1)
    Call_oscill('VOLT 3', f'CH{j}:VOL 1\nTRIG:MAI:LEV -1.6', 'MEASU:MEAS4:VAL?', f'tr{j}_9', '', 2.1)
    Call_oscill('VOLT 3', f'CH{j}:VOL 2\nTRIG:MAI:LEV -1.6', 'MEASU:MEAS4:VAL?', f'tr{j}_10', '', 2.1)
    Call_oscill('VOLT 3', f'CH{j}:VOL 5\nTRIG:MAI:LEV -1.6', 'MEASU:MEAS4:VAL?', f'tr{j}_11', '', 2.1)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
