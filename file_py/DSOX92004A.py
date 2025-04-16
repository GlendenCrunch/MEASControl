# -*- coding: utf-8 -*-
Supportfunc('message-Отключите все кабели от входов осциллографа')
Supportfunc('reset_common')
for j in range(1,5,1):
    # null
    Param_osc(f'{j}', '', '', 'TIM:SCAL 100E-6', '')
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.01', '', '', '', f'nul{j}_1', '', '', 1.8)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.02', '', '', '', f'nul{j}_2', '', '', 2.6)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.05', '', '', '', f'nul{j}_3', '', '', 5)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.1', '', '', '', f'nul{j}_4', '', '', 9)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.2', '', '', '', f'nul{j}_5', '', '', 17)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 0.5', '', '', '', f'nul{j}_6', '', '', 41)
    Call_DSO9000('VOLT 0', f'CHAN{j}:SCAL 1', '', '', '', f'nul{j}_7', '', '', 81)

for j in range(1,5,1):
    Supportfunc(f'message-Подключите выход Cal Out через тройник к мультиметру и осциллографу КАНАЛ №{j}')
    # offset
    Param_osc(f'{j}', '', '', 'TIM:SCAL 100E-6', '')
    Call_DSO9000(':CAL:OUTP DC,2.4', f'CHAN{j}:SCAL 1', '2.4', 'CONF:VOLT:DC 10', f'vofs{j}+1', f'ovofs{j}+1', f'vofs0{j}_1', f'ovofs0{j}_1', 2)
    Call_DSO9000(':CAL:OUTP DC,-2.4', f'CHAN{j}:SCAL 1', '-2.4', 'CONF:VOLT:DC 10', f'vofs{j}-1', f'ovofs{j}-1', f'vofs0{j}_1', f'ovofs0{j}_1', 2)
    Call_DSO9000(':CAL:OUTP DC,2.4', f'CHAN{j}:SCAL 0.5', '2.4', 'CONF:VOLT:DC 10', f'vofs{j}+2', f'ovofs{j}+2', f'vofs0{j}_2', f'ovofs0{j}_2', 2)
    Call_DSO9000(':CAL:OUTP DC,-2.4', f'CHAN{j}:SCAL 0.5', '-2.4', 'CONF:VOLT:DC 10', f'vofs{j}-2', f'ovofs{j}-2', f'vofs0{j}_2', f'ovofs0{j}_2', 2)
    Call_DSO9000(':CAL:OUTP DC,2.2', f'CHAN{j}:SCAL 0.2', '2.2', 'CONF:VOLT:DC 10', f'vofs{j}+3', f'ovofs{j}+3', f'vofs0{j}_3', f'ovofs0{j}_3', 2)
    Call_DSO9000(':CAL:OUTP DC,-2.2', f'CHAN{j}:SCAL 0.2', '-2.2', 'CONF:VOLT:DC 10', f'vofs{j}-3', f'ovofs{j}-3', f'vofs0{j}_3', f'ovofs0{j}_3', 2)
    Call_DSO9000(':CAL:OUTP DC,1.2', f'CHAN{j}:SCAL 0.1', '1.2', 'CONF:VOLT:DC 10', f'vofs{j}+4', f'ovofs{j}+4', f'vofs0{j}_4', f'ovofs0{j}_4', 2)
    Call_DSO9000(':CAL:OUTP DC,-1.2', f'CHAN{j}:SCAL 0.1', '-1.2', 'CONF:VOLT:DC 10', f'vofs{j}-4', f'ovofs{j}-4', f'vofs0{j}_4', f'ovofs0{j}_4', 2)
    Call_DSO9000(':CAL:OUTP DC,0.7', f'CHAN{j}:SCAL 0.05', '0.7', 'CONF:VOLT:DC 1', f'vofs{j}+5', f'ovofs{j}+5', f'vofs0{j}_5', f'ovofs0{j}_5', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.7', f'CHAN{j}:SCAL 0.05', '-0.7', 'CONF:VOLT:DC 1', f'vofs{j}-5', f'ovofs{j}-5', f'vofs0{j}_5', f'ovofs0{j}_5', 2)
    Call_DSO9000(':CAL:OUTP DC,0.4', f'CHAN{j}:SCAL 0.02', '0.4', 'CONF:VOLT:DC 1', f'vofs{j}+6', f'ovofs{j}+6', f'vofs0{j}_6', f'ovofs0{j}_6', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.4', f'CHAN{j}:SCAL 0.02', '-0.4', 'CONF:VOLT:DC 1', f'vofs{j}-6', f'ovofs{j}-6', f'vofs0{j}_6', f'ovofs0{j}_6', 2)
    Call_DSO9000(':CAL:OUTP DC,0.4', f'CHAN{j}:SCAL 0.01', '0.4', 'CONF:VOLT:DC 1', f'vofs{j}+7', f'ovofs{j}+7', f'vofs0{j}_7', f'ovofs0{j}_7', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.4', f'CHAN{j}:SCAL 0.01', '-0.4', 'CONF:VOLT:DC 1', f'vofs{j}-7', f'ovofs{j}-7', f'vofs0{j}_7', f'ovofs0{j}_7', 2)
    # dcv
    Param_osc(f'{j}', '', '', 'TIM:SCAL 100E-6', '')
    Call_DSO9000(':CAL:OUTP DC,0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+1', f'odcv{j}+1', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.03', f'CHAN{j}:SCAL 0.01', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-1', f'odcv{j}-1', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}+2', f'odcv{j}+2', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.06', f'CHAN{j}:SCAL 0.02', ':MEAS:VAV?', 'CONF:VOLT:DC 0.1', f'dcv{j}-2', f'odcv{j}-2', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+3', f'odcv{j}+3', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.15', f'CHAN{j}:SCAL 0.05', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-3', f'odcv{j}-3', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+4', f'odcv{j}+4', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.3', f'CHAN{j}:SCAL 0.1', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-4', f'odcv{j}-4', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}+5', f'odcv{j}+5', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-0.6', f'CHAN{j}:SCAL 0.2', ':MEAS:VAV?', 'CONF:VOLT:DC 1', f'dcv{j}-5', f'odcv{j}-5', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+6', f'odcv{j}+6', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-1.5', f'CHAN{j}:SCAL 0.5', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-6', f'odcv{j}-6', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,2.4', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}+7', f'odcv{j}+7', '', '', 2)
    Call_DSO9000(':CAL:OUTP DC,-2.4', f'CHAN{j}:SCAL 1', ':MEAS:VAV?', 'CONF:VOLT:DC 10', f'dcv{j}-7', f'odcv{j}-7', '', '', 2)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('reset_common')
