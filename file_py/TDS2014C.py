# -*- coding: utf-8 -*-
num_step = 63
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SQU;, PAR:SQU:POL SYMM', 'HOR:SEC 500E-6', '')
    volt_cal1 = [0.012, 0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 3, 6, 12, 30]
    vert_deviation1 = [0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    dcv_acc = [4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    for g in range(11):
        Call_oscill(f'VOLT {volt_cal1[g]}', f'CH{j}:VOL {vert_deviation1[g]}', 'MEASU:MEAS1:VAL?', '', f'gdcv{j}_{g}', dcv_acc[g])
    
    # period
    hor_deviation = ['50E-03', '20E-03', '10E-03', '5E-03', '2E-03', '1E-03', '500E-06', '200E-06', '100E-06', '50E-06', '20E-06', '10E-06',
                    '5E-06', '2E-06', '1E-06', '500E-09', '200E-09', '100E-09', '50E-09', '20E-09', '10E-09', '5E-09']
    per_acc = [0.205, 0.085, 0.045, 0.025, 0.013, 0.009, 2.0056, 0.8056, 0.4056, 0.2056, 0.0856, 0.0456, 0.0256, 0.0136,
                0.0096, 2.605, 1.405, 1.005, 0.805, 0.685, 0.645, 0.625]
    for h in range(22):
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP MARK', f'HOR:SEC {hor_deviation[h]}', f'PER:FIX {hor_deviation[h]}')
        Call_oscill('VOLT 1', f'CH{j}:VOL 0.2', 'MEASU:MEAS3:VAL?', f'ti{j}_{h}', '', per_acc[h])
    
    # band
    volt_cal = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 3, 5.5, 5.5, 5.5]
    vert_deviation = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    for k in range(10):
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SIN;, FREQ:FIX 5E+06', 'HOR:SEC 1E-6', '')
        Call_oscill(f'VOLT {volt_cal[k]}', f'CH{j}:VOL {vert_deviation[k]}', 'MEASU:MEAS2:VAL?', f'uout5_{j}_{k}', f'uin5_{j}_{k}', 1E+4)
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SIN;, FREQ:FIX 100E+06', 'HOR:SEC 10E-9', '')
        Call_oscill(f'VOLT {volt_cal[k]}', f'CH{j}:VOL {vert_deviation[k]}', 'MEASU:MEAS2:VAL?', f'uoutgr{j}_{k}', f'uingr{j}_{k}', 1E+4)
    # trise
    Supportfunc(f'message-Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 2.5E-9', '')
    volt_cal = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 2.9, 3, 3, 3]
    vert_offset = [-0.02, -0.02, -0.02, -0.02, -0.1, -0.1, -1.6, -1.6, -1.6, -1.8]
    for l in range(10):
        Call_oscill(f'VOLT {volt_cal[l]}', f'CH{j}:VOL {vert_deviation[l]}\nTRIG:MAI:LEV {vert_offset[l]}',
                    'MEASU:MEAS4:VAL?', f'tr{j}_{l}', '', 3.5)

    g,h,k,l = [0,0,0,0]

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
