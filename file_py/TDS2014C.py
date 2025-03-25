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
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_22', '', 0.625)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-9', 'PER:FIX 10E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_21', '', 0.645)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-9', 'PER:FIX 20E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_20', '', 0.685)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-9', 'PER:FIX 50E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_19', '', 0.805)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 100E-9', 'PER:FIX 100E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_18', '', 1.005)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 200E-9', 'PER:FIX 200E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_17', '', 1.405)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-9', 'PER:FIX 500E-09')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_16', '', 2.605)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 1E-6', 'PER:FIX 1E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_15', '', 0.0096)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2E-6', 'PER:FIX 2E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_14', '', 0.0136)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-6', 'PER:FIX 5E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_13', '', 0.0256)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-6', 'PER:FIX 10E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_12', '', 0.0456)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-6', 'PER:FIX 20E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_11', '', 0.0856)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-6', 'PER:FIX 50E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_10', '', 0.2056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 100E-6', 'PER:FIX 100E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_9', '', 0.4056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 200E-6', 'PER:FIX 200E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_8', '', 0.8056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 500E-6', 'PER:FIX 500E-06')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_7', '', 2.0056)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 1E-3', 'PER:FIX 1E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_6', '', 0.009)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 2E-3', 'PER:FIX 2E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_5', '', 0.013)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 5E-3', 'PER:FIX 5E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_4', '', 0.025)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 10E-3', 'PER:FIX 10E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_3', '', 0.045)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 20E-3', 'PER:FIX 20E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_2', '', 0.085)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', 'HOR:SEC 50E-3', 'PER:FIX 50E-03')
    Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_1', '', 0.205)
    # band
    volt_calibration = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 3, 5.5, 5.5, 5.5]
    vertical_deviation = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    for k in range(10):
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SIN;, FREQ:FIX 5E+06', 'HOR:SEC 1E-6', '')
        Call_oscill(f'VOLT {volt_calibration[k]}', f'CH{j}:VOL {vertical_deviation[k]}', 'MEASU:MEAS2:VAL?', f'uout5_{j}_{k}', f'uin5_{j}_{k}', 1E+4)
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SIN;, FREQ:FIX 100E+06', 'HOR:SEC 10E-9', '')
        Call_oscill(f'VOLT {volt_calibration[k]}', f'CH{j}:VOL {vertical_deviation[k]}', 'MEASU:MEAS2:VAL?', f'uoutgr{j}_{k}', f'uingr{j}_{k}', 1E+4)
    k = 0
    # trise
    Supportfunc(f'message-Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 2.5E-9', '')
    volt_calibration = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 2.9, 3, 3, 3]
    vertical_deviation = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    vertical_offset = [-0.02, -0.02, -0.02, -0.02, -0.1, -0.1, -1.6, -1.6, -1.6, -1.8]
    for l in range(10):
        Call_oscill(f'VOLT {volt_calibration[l]}', f'CH{j}:VOL {vertical_deviation[l]}\nTRIG:MAI:LEV {vertical_offset[l]}',
                    'MEASU:MEAS4:VAL?', f'tr{j}_{l}', '', 3.5)
    l = 0

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
