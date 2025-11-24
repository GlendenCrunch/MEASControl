# -*- coding: utf-8 -*-
from calibration_oscil import Param_osc, Call_DSO9000, Supportfunc, Clear_merge

num_step = 256
for j in range(2,5,1):
    Supportfunc(f'message-Подключите формирователь и мультиметр через тройник на КАНАЛ №{j} осциллографа')
    # null
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    vert_dev = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    nul_acc = [1.4, 1.8, 2.6, 5, 9, 17, 41, 81]
    for k in range(8):
        Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL {vert_dev[k]}', '', '', '', f'nul{j}_{k}', '', '', nul_acc[k])

    # offset
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    volt_cal = [0.4, 0.4, 0.4, 0.4, 0.4, 0.9, 1.6, 2.2, 2.4, 2.4, 2.4, 2.4]
    vert_dev = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    dmm_ran = [1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10]
    for i in range(12):
        Call_DSO9000(f'VOLT {volt_cal[i]}', f'CHAN{j}:SCAL {vert_dev[i]}', f'{volt_cal[i]}', f'CONF:VOLT:DC {dmm_ran[i]}', f'vofs{j}+{i}', f'ovofs{j}+{i}', f'vofs0{j}_{i}', f'ovofs0{j}_{i}', 2)
        Call_DSO9000(f'VOLT -{volt_cal[i]}', f'CHAN{j}:SCAL {vert_dev[i]}', f'-{volt_cal[i]}', f'CONF:VOLT:DC {dmm_ran[i]}', f'vofs{j}-{i}', f'ovofs{j}-{i}', f'vofs0{j}_{i}', f'ovofs0{j}_{i}', 2)

    # dcv
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    volt_cal = [0.015, 0.03, 0.06, 0.15, 0.3, 0.6, 1.5, 2.4]
    vert_dev = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    dmm_ran = [0.1, 0.1, 0.1, 1, 1, 1, 10, 10]
    for g in range(8):
        Call_DSO9000(f'VOLT {volt_cal[g]}', f'CHAN{j}:SCAL {vert_dev[g]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[g]}', f'dcv{j}+{g}', f'odcv{j}+{g}', '', '', 2)
        Call_DSO9000(f'VOLT -{volt_cal[g]}', f'CHAN{j}:SCAL {vert_dev[g]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[g]}', f'dcv{j}-{g}', f'odcv{j}-{g}', '', '', 2)

    # band
    Supportfunc('resetoscil')
    volt_cal = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 2.2, 2.2]
    vert_dev = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    for l in range(8):
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 50E+06', 'TIM:SCAL 20E-9', '')
        Call_DSO9000(f'VOLT {volt_cal[l]}', f'CHAN{j}:SCAL {vert_dev[l]}', f':MEAS:VRMS? CYCL,AC,CHAN{j}', '', f'pin{j}_50_{l}', f'pdb{j}_50_{l}', '', '', 3)
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 1E+09', 'TIM:SCAL 1E-9', '')
        Call_DSO9000(f'VOLT {volt_cal[l]}', f'CHAN{j}:SCAL {vert_dev[l]}', f':MEAS:VRMS? CYCL,AC,CHAN{j}', '', f'pin{j}_1_{l}', f'pdb{j}_1_{l}', '', '', 3)

    g,h,i,k,l = [0,0,0,0,0]

Supportfunc('message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
