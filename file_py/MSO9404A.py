# -*- coding: utf-8 -*-
num_step = 76
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь и мультиметр через тройник на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    volt_cal1 = [0.015, 0.03, 0.06, 0.15, 0.3, 0.6, 1.5, 3, 6, 15]
    vert_dev = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    dmm_ran = [0.1, 0.1, 0.1, 1, 1, 1, 10, 10, 10, 100]
    for g in range(10):
        Call_DSO9000(f'VOLT {volt_cal1[g]}', f'CHAN{j}:SCAL {vert_dev[g]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[g]}', f'dcv{j}+{g}', f'odcv{j}+{g}', '', '', 2)
        Call_DSO9000(f'VOLT -{volt_cal1[g]}', f'CHAN{j}:SCAL {vert_dev[g]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[g]}', f'dcv{j}-{g}', f'odcv{j}-{g}', '', '', 2)
    
    dmm_ran = [0.1, 0.1, 1, 1, 1, 10, 10]
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC50')
    for h in range(7):
        Call_DSO9000(f'VOLT {volt_cal1[h+1]}', f'CHAN{j}:SCAL {vert_dev[h+1]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[h]}', f'dcv{j}_50+{h}', f'odcv{j}_50+{h}', '', '', 2)
        Call_DSO9000(f'VOLT -{volt_cal1[h+1]}', f'CHAN{j}:SCAL {vert_dev[h+1]}', ':MEAS:VAV?', f'CONF:VOLT:DC {dmm_ran[h]}', f'dcv{j}_50-{h}', f'odcv{j}_50-{h}', '', '', 2)
    
    # offset
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    volt_cal2 = [0.06, 0.12, 0.24, 0.6, 1.2, 2.4, 4, 4]
    dmm_ran = [0.1, 1, 1, 1, 10, 10, 10, 10]
    for i in range(8):
        Call_DSO9000(f'VOLT {volt_cal2[i]}', f'CHAN{j}:SCAL {vert_dev[i]}', f'{volt_cal2[i]}', f'CONF:VOLT:DC {dmm_ran[i]}', f'vofs{j}+{i}', f'ovofs{j}+{i}', f'vofs0{j}_{i}', f'ovofs0{j}_{i}', 1.25)
        Call_DSO9000(f'VOLT -{volt_cal2[i]}', f'CHAN{j}:SCAL {vert_dev[i]}', f'-{volt_cal2[i]}', f'CONF:VOLT:DC {dmm_ran[i]}', f'vofs{j}-{i}', f'ovofs{j}-{i}', f'vofs0{j}_{i}', f'ovofs0{j}_{i}', 1.25)
    
    # null
    Supportfunc('resetoscil')
    nul_acc = [1.8, 1.8, 2.6, 5, 9, 17, 41, 81]
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    for k in range(8):
        Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL {vert_dev[k]}', '', '', '', f'nul{j}_{k}', '', '', nul_acc[k])

    # band
    Supportfunc('resetoscil')
    volt_cal3 = [0.03, 0.06, 0.12, 0.3, 0.6, 1.2, 2.2, 2.2]
    for l in range(8):
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 50E+06', 'TIM:SCAL 20E-9', '')
        Call_DSO9000(f'VOLT {volt_cal3[l]}', f'CHAN{j}:SCAL {vert_dev[l]}', f':MEAS:VRMS? CYCL,AC,CHAN{j}', '', f'pin{j}_50_{l}', f'pdb{j}_50_{l}', '', '', 3)
        Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 3.2E+09', 'TIM:SCAL 1E-9', '')
        Call_DSO9000(f'VOLT {volt_cal3[l]}', f'CHAN{j}:SCAL {vert_dev[l]}', f':MEAS:VRMS? CYCL,AC,CHAN{j}', '', f'pin{j}_1_{l}', f'pdb{j}_1_{l}', '', '', 3)
    
    g,h,i,k,l = [0,0,0,0,0]

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
