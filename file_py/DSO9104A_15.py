# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # null
    Supportfunc(f'message-Подключите формирователь и мультиметр через тройник на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC50')
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.005', '', '', '', f'nul{j}_50_1', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.01', '', '', '', f'nul{j}_50_2', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.02', '', '', '', f'nul{j}_50_3', '', '', 2.6)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.05', '', '', '', f'nul{j}_50_4', '', '', 5)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.1', '', '', '', f'nul{j}_50_5', '', '', 9)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.2', '', '', '', f'nul{j}_50_6', '', '', 17)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.5', '', '', '', f'nul{j}_50_7', '', '', 41)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 1', '', '', '', f'nul{j}_50_8', '', '', 81)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.005', '', '', '', f'nul{j}_1_1', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.01', '', '', '', f'nul{j}_1_2', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.02', '', '', '', f'nul{j}_1_3', '', '', 2.6)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.05', '', '', '', f'nul{j}_1_4', '', '', 5)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.1', '', '', '', f'nul{j}_1_5', '', '', 9)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.2', '', '', '', f'nul{j}_1_6', '', '', 17)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.5', '', '', '', f'nul{j}_1_7', '', '', 41)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 1', '', '', '', f'nul{j}_1_8', '', '', 81)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 2', '', '', '', f'nul{j}_1_9', '', '', 161)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 5', '', '', '', f'nul{j}_1_10', '', '', 401)
    # offset
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC50')
    Call_DSO9000('VOLT 0.06', f'CHAN{j}:SCAL 0.005', '0.06', 'CONF:VOLT:DC 0.1', f'vofs{j}_50+1', f'ovofs{j}_50+1', f'vofs0{j}_50_1', f'ovofs0{j}_50_1', 2.55)
    Call_DSO9000('VOLT -0.06', f'CHAN{j}:SCAL 0.005', '-0.06', 'CONF:VOLT:DC 0.1', f'vofs{j}_50-1', f'ovofs{j}_50-1', f'vofs0{j}_50_1', f'ovofs0{j}_50_1', 2.33)
    Call_DSO9000('VOLT 0.12', f'CHAN{j}:SCAL 0.01', '0.12', 'CONF:VOLT:DC 1', f'vofs{j}_50+2', f'ovofs{j}_50+2', f'vofs0{j}_50_2', f'ovofs0{j}_50_2', 3.3)
    Call_DSO9000('VOLT -0.12', f'CHAN{j}:SCAL 0.01', '-0.12', 'CONF:VOLT:DC 1', f'vofs{j}_50-2', f'ovofs{j}_50-2', f'vofs0{j}_50_2', f'ovofs0{j}_50_2', 3.3)
    Call_DSO9000('VOLT 0.24', f'CHAN{j}:SCAL 0.02', '0.24', 'CONF:VOLT:DC 1', f'vofs{j}_50+3', f'ovofs{j}_50+3', f'vofs0{j}_50_3', f'ovofs0{j}_50_3', 5.6)
    Call_DSO9000('VOLT -0.24', f'CHAN{j}:SCAL 0.02', '-0.24', 'CONF:VOLT:DC 1', f'vofs{j}_50-3', f'ovofs{j}_50-3', f'vofs0{j}_50_3', f'ovofs0{j}_50_3', 5.6)
    Call_DSO9000('VOLT 0.6', f'CHAN{j}:SCAL 0.05', '0.6', 'CONF:VOLT:DC 1', f'vofs{j}_50+4', f'ovofs{j}_50+4', f'vofs0{j}_50_4', f'ovofs0{j}_50_4', 12.5)
    Call_DSO9000('VOLT -0.6', f'CHAN{j}:SCAL 0.05', '-0.6', 'CONF:VOLT:DC 1', f'vofs{j}_50-4', f'ovofs{j}_50-4', f'vofs0{j}_50_4', f'ovofs0{j}_50_4', 12.5)
    Call_DSO9000('VOLT 1.2', f'CHAN{j}:SCAL 0.1', '1.2', 'CONF:VOLT:DC 10', f'vofs{j}_50+5', f'ovofs{j}_50+5', f'vofs0{j}_50_5', f'ovofs0{j}_50_5', 24)
    Call_DSO9000('VOLT -1.2', f'CHAN{j}:SCAL 0.1', '-1.2', 'CONF:VOLT:DC 10', f'vofs{j}_50-5', f'ovofs{j}_50-5', f'vofs0{j}_50_5', f'ovofs0{j}_50_5', 24)
    Call_DSO9000('VOLT 2.4', f'CHAN{j}:SCAL 0.2', '2.4', 'CONF:VOLT:DC 10', f'vofs{j}_50+6', f'ovofs{j}_50+6', f'vofs0{j}_50_6', f'ovofs0{j}_50_6', 47)
    Call_DSO9000('VOLT -2.4', f'CHAN{j}:SCAL 0.2', '-2.4', 'CONF:VOLT:DC 10', f'vofs{j}_50-6', f'ovofs{j}_50-6', f'vofs0{j}_50_6', f'ovofs0{j}_50_6', 47)
    Call_DSO9000('VOLT 4', f'CHAN{j}:SCAL 0.5', '4', 'CONF:VOLT:DC 10', f'vofs{j}_50+7', f'ovofs{j}_50+7', f'vofs0{j}_50_7', f'ovofs0{j}_50_7', 91)
    Call_DSO9000('VOLT -4', f'CHAN{j}:SCAL 0.5', '-4', 'CONF:VOLT:DC 10', f'vofs{j}_50-7', f'ovofs{j}_50-7', f'vofs0{j}_50_7', f'ovofs0{j}_50_7', 91)
    Call_DSO9000('VOLT 4', f'CHAN{j}:SCAL 1', '4', 'CONF:VOLT:DC 10', f'vofs{j}_50+8', f'ovofs{j}_50+8', f'vofs0{j}_50_8', f'ovofs0{j}_50_8', 131)
    Call_DSO9000('VOLT -4', f'CHAN{j}:SCAL 1', '-4', 'CONF:VOLT:DC 10', f'vofs{j}_50-8', f'ovofs{j}_50-8', f'vofs0{j}_50_8', f'ovofs0{j}_50_8', 131)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    Call_DSO9000('VOLT 2', f'CHAN{j}:SCAL 0.005', '2', 'CONF:VOLT:DC 0.1', f'vofs{j}_1+1', f'ovofs{j}_1+1', f'vofs0{j}_1_1', f'ovofs0{j}_1_1', 26.4)
    Call_DSO9000('VOLT -2', f'CHAN{j}:SCAL 0.005', '-2', 'CONF:VOLT:DC 0.1', f'vofs{j}_1-1', f'ovofs{j}_1-1', f'vofs0{j}_1_1', f'ovofs0{j}_1_1', 26.4)
    Call_DSO9000('VOLT 5', f'CHAN{j}:SCAL 0.01', '5', 'CONF:VOLT:DC 1', f'vofs{j}_1+2', f'ovofs{j}_1+2', f'vofs0{j}_1_2', f'ovofs0{j}_1_2', 64.3)
    Call_DSO9000('VOLT -5', f'CHAN{j}:SCAL 0.01', '-5', 'CONF:VOLT:DC 1', f'vofs{j}_1-2', f'ovofs{j}_1-2', f'vofs0{j}_1_2', f'ovofs0{j}_1_2', 64.3)
    Call_DSO9000('VOLT 10', f'CHAN{j}:SCAL 0.02', '10', 'CONF:VOLT:DC 1', f'vofs{j}_1+3', f'ovofs{j}_1+3', f'vofs0{j}_1_3', f'ovofs0{j}_1_3', 127.6)
    Call_DSO9000('VOLT -10', f'CHAN{j}:SCAL 0.02', '-10', 'CONF:VOLT:DC 1', f'vofs{j}_1-3', f'ovofs{j}_1-3', f'vofs0{j}_1_3', f'ovofs0{j}_1_3', 127.6)
    Call_DSO9000('VOLT 10', f'CHAN{j}:SCAL 0.05', '10', 'CONF:VOLT:DC 1', f'vofs{j}_1+4', f'ovofs{j}_1+4', f'vofs0{j}_1_4', f'ovofs0{j}_1_4', 130)
    Call_DSO9000('VOLT -10', f'CHAN{j}:SCAL 0.05', '-10', 'CONF:VOLT:DC 1', f'vofs{j}_1-4', f'ovofs{j}_1-4', f'vofs0{j}_1_4', f'ovofs0{j}_1_4', 130)
    Call_DSO9000('VOLT 20', f'CHAN{j}:SCAL 0.1', '20', 'CONF:VOLT:DC 10', f'vofs{j}_1+5', f'ovofs{j}_1+5', f'vofs0{j}_1_5', f'ovofs0{j}_1_5', 259)
    Call_DSO9000('VOLT -20', f'CHAN{j}:SCAL 0.1', '-20', 'CONF:VOLT:DC 10', f'vofs{j}_1-5', f'ovofs{j}_1-5', f'vofs0{j}_1_5', f'ovofs0{j}_1_5', 259)
    Call_DSO9000('VOLT 20', f'CHAN{j}:SCAL 0.2', '20', 'CONF:VOLT:DC 10', f'vofs{j}_1+6', f'ovofs{j}_1+6', f'vofs0{j}_1_6', f'ovofs0{j}_1_6', 267)
    Call_DSO9000('VOLT -20', f'CHAN{j}:SCAL 0.2', '-20', 'CONF:VOLT:DC 10', f'vofs{j}_1-6', f'ovofs{j}_1-6', f'vofs0{j}_1_6', f'ovofs0{j}_1_6', 267)
    Call_DSO9000('VOLT 20', f'CHAN{j}:SCAL 0.5', '20', 'CONF:VOLT:DC 10', f'vofs{j}_1+7', f'ovofs{j}_1+7', f'vofs0{j}_1_7', f'ovofs0{j}_1_7', 291)
    Call_DSO9000('VOLT -20', f'CHAN{j}:SCAL 0.5', '-20', 'CONF:VOLT:DC 10', f'vofs{j}_1-7', f'ovofs{j}_1-7', f'vofs0{j}_1_7', f'ovofs0{j}_1_7', 291)
    Call_DSO9000('VOLT 100', f'CHAN{j}:SCAL 1', '100', 'CONF:VOLT:DC 10', f'vofs{j}_1+8', f'ovofs{j}_1+8', f'vofs0{j}_1_8', f'ovofs0{j}_1_8', 1310)
    Call_DSO9000('VOLT -100', f'CHAN{j}:SCAL 1', '-100', 'CONF:VOLT:DC 10', f'vofs{j}_1-8', f'ovofs{j}_1-8', f'vofs0{j}_1_8', f'ovofs0{j}_1_8', 1310)
    Call_DSO9000('VOLT 100', f'CHAN{j}:SCAL 2', '100', 'CONF:VOLT:DC 10', f'vofs{j}_1+9', f'ovofs{j}_1+9', f'vofs0{j}_1_9', f'ovofs0{j}_1_9', 1410)
    Call_DSO9000('VOLT -100', f'CHAN{j}:SCAL 2', '-100', 'CONF:VOLT:DC 10', f'vofs{j}_1-9', f'ovofs{j}_1-9', f'vofs0{j}_1_9', f'ovofs0{j}_1_9', 1410)
    Call_DSO9000('VOLT 100', f'CHAN{j}:SCAL 5', '100', 'CONF:VOLT:DC 10', f'vofs{j}_1+10', f'ovofs{j}_1+10', f'vofs0{j}_1_10', f'ovofs0{j}_1_10', 1650)
    Call_DSO9000('VOLT -100', f'CHAN{j}:SCAL 5', '-100', 'CONF:VOLT:DC 10', f'vofs{j}_1-10', f'ovofs{j}_1-10', f'vofs0{j}_1_10', f'ovofs0{j}_1_10', 1650)
    # dcv
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC50')
    Call_DSO9000('VOLT 0.015', f'CHAN{j}:SCAL 0.005', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+1', f'odcv{j}+1', '', '', 2)
    Call_DSO9000('VOLT -0.015', f'CHAN{j}:SCAL 0.005', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-1', f'odcv{j}-1', '', '', 2)
    Call_DSO9000('VOLT 0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+2', f'odcv{j}+2', '', '', 2)
    Call_DSO9000('VOLT -0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-2', f'odcv{j}-2', '', '', 2)
    Call_DSO9000('VOLT 0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+3', f'odcv{j}+3', '', '', 2)
    Call_DSO9000('VOLT -0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-3', f'odcv{j}-3', '', '', 2)
    Call_DSO9000('VOLT 0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+4', f'odcv{j}+4', '', '', 2)
    Call_DSO9000('VOLT -0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-4', f'odcv{j}-4', '', '', 2)
    Call_DSO9000('VOLT 0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+5', f'odcv{j}+5', '', '', 2)
    Call_DSO9000('VOLT -0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-5', f'odcv{j}-5', '', '', 2)
    Call_DSO9000('VOLT 0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+6', f'odcv{j}+6', '', '', 2)
    Call_DSO9000('VOLT -0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-6', f'odcv{j}-6', '', '', 2)
    Call_DSO9000('VOLT 1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+7', f'odcv{j}+7', '', '', 2)
    Call_DSO9000('VOLT -1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-7', f'odcv{j}-7', '', '', 2)
    Call_DSO9000('VOLT 3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+8', f'odcv{j}+8', '', '', 2)
    Call_DSO9000('VOLT -3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-8', f'odcv{j}-8', '', '', 2)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    Call_DSO9000('VOLT 1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+9', f'odcv{j}+9', '', '', 2)
    Call_DSO9000('VOLT -1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-9', f'odcv{j}-9', '', '', 2)
    Call_DSO9000('VOLT 3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+10', f'odcv{j}+10', '', '', 2)
    Call_DSO9000('VOLT -3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-10', f'odcv{j}-10', '', '', 2)
    Call_DSO9000('VOLT 6', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+11', f'odcv{j}+11', '', '', 2)
    Call_DSO9000('VOLT -6', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-11', f'odcv{j}-11', '', '', 2)
    Call_DSO9000('VOLT 15', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', 'CONF:VOLT:DC 100', f'dcv{j}+12', f'odcv{j}+12', '', '', 2)
    Call_DSO9000('VOLT -15', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', 'CONF:VOLT:DC 100', f'dcv{j}-12', f'odcv{j}-12', '', '', 2)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
