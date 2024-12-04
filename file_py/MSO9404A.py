# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь и мультиметр через тройник на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
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
    Call_DSO9000('VOLT 6', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+9', f'odcv{j}+9', '', '', 2)
    Call_DSO9000('VOLT -6', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-9', f'odcv{j}-9', '', '', 2)
    Call_DSO9000('VOLT 15', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', 'CONF:VOLT:DC 100', f'dcv{j}+10', f'odcv{j}+10', '', '', 2)
    Call_DSO9000('VOLT -15', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', 'CONF:VOLT:DC 100', f'dcv{j}-10', f'odcv{j}-10', '', '', 2)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC50')
    Call_DSO9000('VOLT 0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+11', f'odcv{j}+11', '', '', 2)
    Call_DSO9000('VOLT -0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-11', f'odcv{j}-11', '', '', 2)
    Call_DSO9000('VOLT 0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+12', f'odcv{j}+12', '', '', 2)
    Call_DSO9000('VOLT -0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-12', f'odcv{j}-12', '', '', 2)
    Call_DSO9000('VOLT 0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+13', f'odcv{j}+13', '', '', 2)
    Call_DSO9000('VOLT -0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-13', f'odcv{j}-13', '', '', 2)
    Call_DSO9000('VOLT 0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+14', f'odcv{j}+14', '', '', 2)
    Call_DSO9000('VOLT -0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-14', f'odcv{j}-14', '', '', 2)
    Call_DSO9000('VOLT 0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+15', f'odcv{j}+15', '', '', 2)
    Call_DSO9000('VOLT -0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-15', f'odcv{j}-15', '', '', 2)
    Call_DSO9000('VOLT 1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+16', f'odcv{j}+16', '', '', 2)
    Call_DSO9000('VOLT -1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-16', f'odcv{j}-16', '', '', 2)
    Call_DSO9000('VOLT 3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+17', f'odcv{j}+17', '', '', 2)
    Call_DSO9000('VOLT -3', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-17', f'odcv{j}-17', '', '', 2)
    # offset
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    Call_DSO9000('VOLT 0.06', f'CHAN{j}:SCAL 0.005', '0.06', 'CONF:VOLT:DC 0.1', f'vofs{j}+1', f'ovofs{j}+1', f'vofs0{j}_1', f'ovofs0{j}_1', 1.25)
    Call_DSO9000('VOLT -0.06', f'CHAN{j}:SCAL 0.005', '-0.06', 'CONF:VOLT:DC 0.1', f'vofs{j}-1', f'ovofs{j}-1', f'vofs0{j}_1', f'ovofs0{j}_1', 1.25)
    Call_DSO9000('VOLT 0.12', f'CHAN{j}:SCAL 0.01', '0.12', 'CONF:VOLT:DC 1', f'vofs{j}+2', f'ovofs{j}+2', f'vofs0{j}_2', f'ovofs0{j}_2', 1.25)
    Call_DSO9000('VOLT -0.12', f'CHAN{j}:SCAL 0.01', '-0.12', 'CONF:VOLT:DC 1', f'vofs{j}-2', f'ovofs{j}-2', f'vofs0{j}_2', f'ovofs0{j}_2', 1.25)
    Call_DSO9000('VOLT 0.24', f'CHAN{j}:SCAL 0.02', '0.24', 'CONF:VOLT:DC 1', f'vofs{j}+3', f'ovofs{j}+3', f'vofs0{j}_3', f'ovofs0{j}_3', 1.25)
    Call_DSO9000('VOLT -0.24', f'CHAN{j}:SCAL 0.02', '-0.24', 'CONF:VOLT:DC 1', f'vofs{j}-3', f'ovofs{j}-3', f'vofs0{j}_3', f'ovofs0{j}_3', 1.25)
    Call_DSO9000('VOLT 0.6', f'CHAN{j}:SCAL 0.05', '0.6', 'CONF:VOLT:DC 1', f'vofs{j}+4', f'ovofs{j}+4', f'vofs0{j}_4', f'ovofs0{j}_4', 1.25)
    Call_DSO9000('VOLT -0.6', f'CHAN{j}:SCAL 0.05', '-0.6', 'CONF:VOLT:DC 1', f'vofs{j}-4', f'ovofs{j}-4', f'vofs0{j}_4', f'ovofs0{j}_4', 1.25)
    Call_DSO9000('VOLT 1.2', f'CHAN{j}:SCAL 0.1', '1.2', 'CONF:VOLT:DC 10', f'vofs{j}+5', f'ovofs{j}+5', f'vofs0{j}_5', f'ovofs0{j}_5', 1.25)
    Call_DSO9000('VOLT -1.2', f'CHAN{j}:SCAL 0.1', '-1.2', 'CONF:VOLT:DC 10', f'vofs{j}-5', f'ovofs{j}-5', f'vofs0{j}_5', f'ovofs0{j}_5', 1.25)
    Call_DSO9000('VOLT 2.4', f'CHAN{j}:SCAL 0.2', '2.4', 'CONF:VOLT:DC 10', f'vofs{j}+6', f'ovofs{j}+6', f'vofs0{j}_6', f'ovofs0{j}_6', 1.25)
    Call_DSO9000('VOLT -2.4', f'CHAN{j}:SCAL 0.2', '-2.4', 'CONF:VOLT:DC 10', f'vofs{j}-6', f'ovofs{j}-6', f'vofs0{j}_6', f'ovofs0{j}_6', 1.25)
    Call_DSO9000('VOLT 4', f'CHAN{j}:SCAL 0.5', '4', 'CONF:VOLT:DC 10', f'vofs{j}+7', f'ovofs{j}+7', f'vofs0{j}_7', f'ovofs0{j}_7', 1.25)
    Call_DSO9000('VOLT -4', f'CHAN{j}:SCAL 0.5', '-4', 'CONF:VOLT:DC 10', f'vofs{j}-7', f'ovofs{j}-7', f'vofs0{j}_7', f'ovofs0{j}_7', 1.25)
    Call_DSO9000('VOLT 4', f'CHAN{j}:SCAL 1', '4', 'CONF:VOLT:DC 10', f'vofs{j}+8', f'ovofs{j}+8', f'vofs0{j}_8', f'ovofs0{j}_8', 1.25)
    Call_DSO9000('VOLT -4', f'CHAN{j}:SCAL 1', '-4', 'CONF:VOLT:DC 10', f'vofs{j}-8', f'ovofs{j}-8', f'vofs0{j}_8', f'ovofs0{j}_8', 1.25)
    # null
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', 'DC')
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.005', '', '', '', f'nul{j}_1', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.01', '', '', '', f'nul{j}_2', '', '', 1.8)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.02', '', '', '', f'nul{j}_3', '', '', 2.6)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.05', '', '', '', f'nul{j}_4', '', '', 5)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.1', '', '', '', f'nul{j}_5', '', '', 9)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.2', '', '', '', f'nul{j}_6', '', '', 17)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 0.5', '', '', '', f'nul{j}_7', '', '', 41)
    Call_DSO9000('VOLT 0.01', f'CHAN{j}:SCAL 1', '', '', '', f'nul{j}_8', '', '', 81)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
