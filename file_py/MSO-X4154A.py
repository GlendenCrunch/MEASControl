# -*- coding: utf-8 -*-
from calibration_oscil import Param_osc, Call_oscill, Supportfunc, Clear_merge

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
    # dcv_cursor
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 100E-6', '')
    Call_oscill('VOLT 35', f'CHAN{j}:SCAL 5', ':MARK:Y1P?', f'c_dcv{j}_1', '', 0.8)
    Call_oscill('VOLT 14', f'CHAN{j}:SCAL 2', ':MARK:Y1P?', f'c_dcv{j}_2', '', 0.32)
    Call_oscill('VOLT 7', f'CHAN{j}:SCAL 1', ':MARK:Y1P?', f'c_dcv{j}_3', '', 0.16)
    Call_oscill('VOLT 3.5', f'CHAN{j}:SCAL 0.5', ':MARK:Y1P?', f'c_dcv{j}_4', '', 0.08)
    Call_oscill('VOLT 1.4', f'CHAN{j}:SCAL 0.2', ':MARK:Y1P?', f'c_dcv{j}_5', '', 0.032)
    Call_oscill('VOLT 0.7', f'CHAN{j}:SCAL 0.1', ':MARK:Y1P?', f'c_dcv{j}_6', '', 0.016)
    Call_oscill('VOLT 0.35', f'CHAN{j}:SCAL 0.05', ':MARK:Y1P?', f'c_dcv{j}_7', '', 0.008)
    Call_oscill('VOLT 0.14', f'CHAN{j}:SCAL 0.02', ':MARK:Y1P?', f'c_dcv{j}_8', '', 0.0032)
    Call_oscill('VOLT 0.07', f'CHAN{j}:SCAL 0.01', ':MARK:Y1P?', f'c_dcv{j}_9', '', 0.0016)
    Call_oscill('VOLT 0.035', f'CHAN{j}:SCAL 0.005', ':MARK:Y1P?', f'c_dcv{j}_10', '', 0.0008)
    Call_oscill('VOLT 0.014', f'CHAN{j}:SCAL 0.002', ':MARK:Y1P?', f'c_dcv{j}_11', '', 0.00064)
    # trise
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 1E+06', 'TIM:SCAL 1E-6', 'band')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN;, FREQ:FIX 1.5E+09', 'TIM:SCAL 1E-9', '')
    Call_oscill('VOLT 0.12', f'CHAN{j}:SCAL 0.02', ':MEAS:VRMS?', f'db_{j}', '', 3)

Supportfunc('message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
