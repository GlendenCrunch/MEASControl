# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', '')
    Call_oscill('VOLT 35', f'CHAN{j}:SCAL 5', ':MEAS:VAV?', f'dcv{j}_1', '', 0.8)
    Call_oscill('VOLT 14', f'CHAN{j}:SCAL 2', ':MEAS:VAV?', f'dcv{j}_2', '', 0.32)
    Call_oscill('VOLT 7', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', f'dcv{j}_3', '', 0.16)
    Call_oscill('VOLT 3.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', f'dcv{j}_4', '', 0.08)
    Call_oscill('VOLT 1.4', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', f'dcv{j}_5', '', 0.032)
    Call_oscill('VOLT 0.7', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', f'dcv{j}_6', '', 0.016)
    Call_oscill('VOLT 0.35', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', f'dcv{j}_7', '', 0.008)
    Call_oscill('VOLT 0.14', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', f'dcv{j}_8', '', 0.0032)
    Call_oscill('VOLT 0.07', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', f'dcv{j}_9', '', 0.0016)
    Call_oscill('VOLT 0.035', f'CHAN{j}:SCAL 0.005', ':MEAS:VAV?', f'dcv{j}_10', '', 0.0008)
    Call_oscill('VOLT 0.014', f'CHAN{j}:SCAL 0.002', ':MEAS:VAV?', f'dcv{j}_11', '', 0.00064)
    Call_oscill('VOLT 0.007', f'CHAN{j}:SCAL 0.001', ':MEAS:v?', f'dcv{j}_12', '', 0.00064)
    # band
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP MARK', f'TIM:SCAL 100E-6;CHAN{j}:IMP FIFT', 'PER:FIX 1E-06')
    Call_oscill('VOLT 0.12', f'CHAN{j}:SCAL 0.02', ':MEAS:VPP?', 'pp_1', '', 84)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1000', 'SCOP:SHAP MARK', f'TIM:SCAL 100E-6;CHAN{j}:IMP ONEM', 'PER:FIX 1E-09')
    Call_oscill('VOLT 0.12', f'CHAN{j}:SCAL 0.02', ':MEAS:VPP?', 'pp_9', '', 84)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
