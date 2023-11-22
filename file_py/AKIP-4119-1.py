# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Message(f'Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Reset()
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TDIV 1MS', '')
    Call_oscill('VOLT 0.06', f'C{j}:VDIV 0.02', f'C{j}:PAVA? MEAN', f'dcv{j}_1', '', 4.8)
    Call_oscill('VOLT -0.06', f'C{j}:VDIV 0.02', f'C{j}:PAVA? MEAN', f'dcv{j}_2', '', 4.8)
    Call_oscill('VOLT 0.15', f'C{j}:VDIV 0.05', f'C{j}:PAVA? MEAN', f'dcv{j}_3', '', 10.5)
    Call_oscill('VOLT -0.15', f'C{j}:VDIV 0.05', f'C{j}:PAVA? MEAN', f'dcv{j}_4', '', 10.5)
    Call_oscill('VOLT 0.3', f'C{j}:VDIV 0.1', f'C{j}:PAVA? MEAN', f'dcv{j}_5', '', 20)
    Call_oscill('VOLT -0.3', f'C{j}:VDIV 0.1', f'C{j}:PAVA? MEAN', f'dcv{j}_6', '', 20)
    Call_oscill('VOLT 0.6', f'C{j}:VDIV 0.2', f'C{j}:PAVA? MEAN', f'dcv{j}_7', '', 48)
    Call_oscill('VOLT -0.6', f'C{j}:VDIV 0.2', f'C{j}:PAVA? MEAN', f'dcv{j}_8', '', 48)
    Call_oscill('VOLT 1.5', f'C{j}:VDIV 0.5', f'C{j}:PAVA? MEAN', f'dcv{j}_9', '', 105)
    Call_oscill('VOLT -1.5', f'C{j}:VDIV 0.5', f'C{j}:PAVA? MEAN', f'dcv{j}_10', '', 105)
    Call_oscill('VOLT 3', f'C{j}:VDIV 1', f'C{j}:PAVA? MEAN', f'dcv{j}_11', '', 0.2)
    Call_oscill('VOLT -3', f'C{j}:VDIV 1', f'C{j}:PAVA? MEAN', f'dcv{j}_12', '', 0.2)
    Call_oscill('VOLT 6', f'C{j}:VDIV 2', f'C{j}:PAVA? MEAN', f'dcv{j}_13', '', 0.39)
    Call_oscill('VOLT -6', f'C{j}:VDIV 2', f'C{j}:PAVA? MEAN', f'dcv{j}_14', '', 0.39)
    Call_oscill('VOLT 15', f'C{j}:VDIV 5', f'C{j}:PAVA? MEAN', f'dcv{j}_15', '', 0.96)
    Call_oscill('VOLT -15', f'C{j}:VDIV 5', f'C{j}:PAVA? MEAN', f'dcv{j}_16', '', 0.96)
    # band
    Reset()
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP SIN', 'TDIV 10US', '')
    Call_oscill('VOLT 0.12', f'C{j}:VDIV 0.02', f'C{j}:PAVA? RMS', f'bw{j}_1', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 0.3', f'C{j}:VDIV 0.05', f'C{j}:PAVA? RMS', f'bw{j}_2', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 0.6', f'C{j}:VDIV 0.1', f'C{j}:PAVA? RMS', f'bw{j}_3', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 1.2', f'C{j}:VDIV 0.2', f'C{j}:PAVA? RMS', f'bw{j}_4', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 3', f'C{j}:VDIV 0.5', f'C{j}:PAVA? RMS', f'bw{j}_5', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 5.5', f'C{j}:VDIV 1', f'C{j}:PAVA? RMS', f'bw{j}_6', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 5.5', f'C{j}:VDIV 2', f'C{j}:PAVA? RMS', f'bw{j}_7', 'FREQ:FIX 50E+03', 70)
    Call_oscill('VOLT 5.5', f'C{j}:VDIV 5', f'C{j}:PAVA? RMS', f'bw{j}_8', 'FREQ:FIX 50E+03', 70)
    # trise
    Message(f'Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Reset()
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TDIV 5E-9', '')
    Call_oscill('VOLT 0.11', f'C{j}:VDIV 0.02', f'C{j}:PAVA? RISE', f'tr{j}_1', '0.06', 5)
    Call_oscill('VOLT 0.27', f'C{j}:VDIV 0.05', f'C{j}:PAVA? RISE', f'tr{j}_2', '0.15', 5)
    Call_oscill('VOLT 0.55', f'C{j}:VDIV 0.1', f'C{j}:PAVA? RISE', f'tr{j}_3', '0.3', 5)
    Call_oscill('VOLT 1.2', f'C{j}:VDIV 0.2', f'C{j}:PAVA? RISE', f'tr{j}_4', '0.6', 5)
    Call_oscill('VOLT 2.7', f'C{j}:VDIV 0.5', f'C{j}:PAVA? RISE', f'tr{j}_5', '1.5', 5)
    Call_oscill('VOLT 3.1', f'C{j}:VDIV 1', f'C{j}:PAVA? RISE', f'tr{j}_6', '3', 5)

Message('Калибровка завершена')
Clear_merge()
Reset()
