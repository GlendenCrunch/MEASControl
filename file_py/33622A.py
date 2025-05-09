# -*- coding: utf-8 -*-
for j in range(1,3,1):
    # freq
    Supportfunc(f'message-Подключите КАНАЛ А частотмера на КАНАЛ №{j} генератора')
    Supportfunc('reset_gener')
    Call_generator(f'SOUR{j}:APPL:SIN 10,1 VPP,0', 'INF', f'f{j}_1', 0.00001)
    Call_generator(f'SOUR{j}:APPL:SIN 10e6,1 VPP,0', 'INF', f'f{j}_2', 10)
    Call_generator(f'SOUR{j}:APPL:SIN 30e6,1 VPP,0', 'INF', f'f{j}_3', 30)
    Call_generator(f'SOUR{j}:APPL:SIN 60e6,1 VPP,0', 'INF', f'f{j}_4', 60)
    Call_generator(f'SOUR{j}:APPL:SIN 80e6,1 VPP,0', 'INF', f'f{j}_5', 80)
    Call_generator(f'SOUR{j}:APPL:SIN 120e6,1 VPP,0', 'INF', f'f{j}_6', 120)
    # ac
    Supportfunc(f'message-Подключите мультиметр на КАНАЛ №{j} генератора')
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,0.4 VRMS,0', 'INF', f'vac{j}_1', 0.004707)
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,1.0 VRMS,0', 'INF', f'vac{j}_2', 0.010707)
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,2.5 VRMS,0', 'INF', f'vac{j}_3', 0.025707)
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,7.0 VRMS,0', 'INF', f'vac{j}_4', 0.070707)
    # dc
    Call_generator(f'SOUR{j}:APPL:DC DEF,DEF,0 V', 'INF', f'vdc{j}_1',  0.002)
    Call_generator(f'SOUR{j}:APPL:DC DEF,DEF,0.5 V', 'INF', f'vdc{j}_2',  0.007)
    Call_generator(f'SOUR{j}:APPL:DC DEF,DEF,10 V', 'INF', f'vdc{j}_3',  0.102)
    # ac power
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,0.354 VRMS,0', 'INF', f'vac_dbm{j}_1', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 1e3,1.414 VRMS,0', 'INF', f'vac_dbm{j}_16', 100)
    #power
    Supportfunc(f'message-Подключите измеритель мощности на КАНАЛ №{j} генератора')
    Call_generator(f'SOUR{j}:APPL:SIN 1e6,0.354 VRMS,0', '50', f'dbm{j}_2', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 5e6,0.354 VRMS,0', '50', f'dbm{j}_3', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 10e6,0.354 VRMS,0', '50', f'dbm{j}_4', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 20e6,0.354 VRMS,0', '50', f'dbm{j}_5', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 30e6,0.354 VRMS,0', '50', f'dbm{j}_6', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 40e6,0.354 VRMS,0', '50', f'dbm{j}_7', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 50e6,0.354 VRMS,0', '50', f'dbm{j}_8', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 60e6,0.354 VRMS,0', '50', f'dbm{j}_9', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 70e6,0.354 VRMS,0', '50', f'dbm{j}_10', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 80e6,0.354 VRMS,0', '50', f'dbm{j}_11', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 90e6,0.354 VRMS,0', '50', f'dbm{j}_12', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 100e6,0.354 VRMS,0', '50', f'dbm{j}_13', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 110e6,0.354 VRMS,0', '50', f'dbm{j}_14', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 120e6,0.354 VRMS,0', '50', f'dbm{j}_15', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 1e6,1.414 VRMS,0', '50', f'dbm{j}_17', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 5e6,1.414 VRMS,0', '50', f'dbm{j}_18', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 10e6,1.4144 VRMS,0', '50', f'dbm{j}_19', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 20e6,1.414 VRMS,0', '50', f'dbm{j}_20', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 30e6,1.414 VRMS,0', '50', f'dbm{j}_21', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 40e6,1.414 VRMS,0', '50', f'dbm{j}_22', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 50e6,1.414 VRMS,0', '50', f'dbm{j}_23', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 60e6,1.414 VRMS,0', '50', f'dbm{j}_24', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 70e6,1.414 VRMS,0', '50', f'dbm{j}_25', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 80e6,1.414 VRMS,0', '50', f'dbm{j}_26', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 90e6,1.414 VRMS,0', '50', f'dbm{j}_27', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 100e6,1.414 VRMS,0', '50', f'dbm{j}_28', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 110e6,1.414 VRMS,0', '50', f'dbm{j}_29', 100)
    Call_generator(f'SOUR{j}:APPL:SIN 120e6,1.414 VRMS,0', '50', f'dbm{j}_30', 100)

    my_gui.inst_dmm.write(f'OUTP{j} OFF')

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('reset_gener')
