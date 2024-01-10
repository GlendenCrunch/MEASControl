# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Message(f'Подключите формирователь без вешней нагрузки на КАНАЛ №{j} осциллографа')
    Reset()
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'HOR:SEC 500E-6', '')
    Call_oscill('VOLT 0.02', f'CH{j}:VOL 0.01', 'MEASU:MEAS1:VAL?', f'dcv{j}_1', f'gdcv{j}_1', 2.6)
    Call_oscill('VOLT 0.5', f'CH{j}:VOL 0.1', 'MEASU:MEAS1:VAL?', f'dcv{j}_2', f'gdcv{j}_2', 26)
    Call_oscill('VOLT 3', f'CH{j}:VOL 0.5', 'MEASU:MEAS1:VAL?', f'dcv{j}_3', f'gdcv{j}_3', 141)
    Call_oscill('VOLT 6', f'CH{j}:VOL 1', 'MEASU:MEAS1:VAL?', f'dcv{j}_4', f'gdcv{j}_4', 281)
    Call_oscill('VOLT 12', f'CH{j}:VOL 2', 'MEASU:MEAS1:VAL?', f'dcv{j}_5', f'gdcv{j}_5', 561)
    Call_oscill('VOLT 30', f'CH{j}:VOL 5', 'MEASU:MEAS1:VAL?', f'dcv{j}_6', f'gdcv{j}_6', 1400)
    # trise
    Message(f'Подключите внешнию нагрузку 50 Ом на КАНАЛ №{j} осциллографа')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'HOR:SEC 5E-9', '')
    Call_oscill('VOLT 3.1', f'CH{j}:VOL 1\nTRIG:MAI:LEV -1.5', 'MEASU:MEAS4:VAL?', f'tr{j}_1', '', 2.1)

Message('Калибровка завершена')
Clear_merge()
Reset()
