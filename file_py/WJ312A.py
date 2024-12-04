# -*- coding: utf-8 -*-
for j in range(1,3,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TDIV 1ms', 'MLEN 500')
    Call_oscill('VOLT 0.015', f'C{j}: VDIV 5mv', 'MSRA?', f'dcv{j}+_1', f'gdcv{j}+_1', 2.425)
    Call_oscill('VOLT -0.015', f'C{j}: VDIV 5mv', 'MSRB?', f'dcv{j}-_1', f'gdcv{j}-_1', 2.425)
    Call_oscill('VOLT 0.03', f'C{j}: VDIV 10mv', 'MSRA?', f'dcv{j}+_2', f'gdcv{j}+_2', 2.85)
    Call_oscill('VOLT -0.03', f'C{j}: VDIV 10mv', 'MSRB?', f'dcv{j}-_2', f'gdcv{j}-_2', 2.85)
    Call_oscill('VOLT 0.3', f'C{j}: VDIV 100mv', 'MSRA?', f'dcv{j}+_3', f'gdcv{j}+_3', 10.5)
    Call_oscill('VOLT -0.3', f'C{j}: VDIV 100mv', 'MSRB?', f'dcv{j}-_3', f'gdcv{j}-_3', 10.5)
    Call_oscill('VOLT 1.5', f'C{j}: VDIV 500mv', 'MSRA?', f'dcv{j}+_4', f'gdcv{j}+_4', 44.5)
    Call_oscill('VOLT -1.5', f'C{j}: VDIV 500mv', 'MSRB?', f'dcv{j}-_4', f'gdcv{j}-_4', 44.5)
    Call_oscill('VOLT 3', f'C{j}: VDIV 1', 'MSRA?', f'dcv{j}+_5', f'gdcv{j}+_5', 87)
    Call_oscill('VOLT -3', f'C{j}: VDIV 1', 'MSRB?', f'dcv{j}-_5', f'gdcv{j}-_5', 87)
    Call_oscill('VOLT 30', f'C{j}: VDIV 10', 'MSRA?', f'dcv{j}+_6', f'gdcv{j}+_6', 852)
    Call_oscill('VOLT -30', f'C{j}: VDIV 10', 'MSRB?', f'dcv{j}-_6', f'gdcv{j}-_6', 852)
    # trise
    Supportfunc(f'message-Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TDIV 5ns', 'MLEN 50')
    Call_oscill('VOLT 0.5', f'C{j}:VDIV 200mv', 'MSRC?', f'tr_{j}', '', 3.5)
    # period
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP SIN', 'TDIV 20ms', 'MLEN 500')
    Call_oscill('VOLT 0.6', f'C{j}: VDIV 100mv', 'MSRD?', f'frq_{j}', '', 100)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
