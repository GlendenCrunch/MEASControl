# -*- coding: utf-8 -*-
for j in range(1,5,1):
    # dcv
    Supportfunc(f'message-Подключите формирователь 9530 на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 0.001', f'CHAN{j}:COUP DCLimit')
    Call_oscill('VOLT 0.0045', f'CHAN{j}:SCAL 0.001', 'MEAS1:ARES?', f'dcv{j}+_1_1', '', 2)
    Call_oscill('VOLT -0.0045', f'CHAN{j}:SCAL 0.001', 'MEAS1:ARES?', f'dcv{j}-_1_1', '', 2)
    Call_oscill('VOLT 0.0135', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'dcv{j}+_1_2', '', 2)
    Call_oscill('VOLT -0.0135', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'dcv{j}-_1_2', '', 2)
    Call_oscill('VOLT 0.0145', f'CHAN{j}:SCAL 0.0032', 'MEAS1:ARES?', f'dcv{j}+_1_3', '', 2)
    Call_oscill('VOLT -0.0145', f'CHAN{j}:SCAL 0.0032', 'MEAS1:ARES?', f'dcv{j}-_1_3', '', 2)
    Call_oscill('VOLT 0.045', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'dcv{j}+_1_4', '', 1.5)
    Call_oscill('VOLT -0.045', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'dcv{j}-_1_4', '', 1.5)
    Call_oscill('VOLT 0.05', f'CHAN{j}:SCAL 0.011', 'MEAS1:ARES?', f'dcv{j}+_1_5', '', 1.5)
    Call_oscill('VOLT -0.05', f'CHAN{j}:SCAL 0.011', 'MEAS1:ARES?', f'dcv{j}-_1_5', '', 1.5)
    Call_oscill('VOLT 0.135', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'dcv{j}+_1_6', '', 1.5)
    Call_oscill('VOLT -0.135', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'dcv{j}-_1_6', '', 1.5)
    Call_oscill('VOLT 0.145', f'CHAN{j}:SCAL 0.032', 'MEAS1:ARES?', f'dcv{j}+_1_7', '', 1.5)
    Call_oscill('VOLT -0.145', f'CHAN{j}:SCAL 0.032', 'MEAS1:ARES?', f'dcv{j}-_1_7', '', 1.5)
    Call_oscill('VOLT 0.32', f'CHAN{j}:SCAL 0.07', 'MEAS1:ARES?', f'dcv{j}+_1_8', '', 1.5)
    Call_oscill('VOLT -0.32', f'CHAN{j}:SCAL 0.07', 'MEAS1:ARES?', f'dcv{j}-_1_8', '', 1.5)
    Call_oscill('VOLT 0.45', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'dcv{j}+_1_9', '', 1.5)
    Call_oscill('VOLT -0.45', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'dcv{j}-_1_9', '', 1.5)
    Call_oscill('VOLT 0.5', f'CHAN{j}:SCAL 0.11', 'MEAS1:ARES?', f'dcv{j}+_1_10', '', 1.5)
    Call_oscill('VOLT -0.5', f'CHAN{j}:SCAL 0.11', 'MEAS1:ARES?', f'dcv{j}-_1_10', '', 1.5)
    Call_oscill('VOLT 1.35', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'dcv{j}+_1_11', '', 1.5)
    Call_oscill('VOLT -1.35', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'dcv{j}-_1_11', '', 1.5)
    Call_oscill('VOLT 1.45', f'CHAN{j}:SCAL 0.32', 'MEAS1:ARES?', f'dcv{j}+_1_12', '', 1.5)
    Call_oscill('VOLT -1.45', f'CHAN{j}:SCAL 0.32', 'MEAS1:ARES?', f'dcv{j}-_1_12', '', 1.5)
    Call_oscill('VOLT 4.5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'dcv{j}+_1_13', '', 1.5)
    Call_oscill('VOLT -4.5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'dcv{j}-_1_13', '', 1.5)
    Call_oscill('VOLT 5', f'CHAN{j}:SCAL 1.1', 'MEAS1:ARES?', f'dcv{j}+_1_14', '', 1.5)
    Call_oscill('VOLT -5', f'CHAN{j}:SCAL 1.1', 'MEAS1:ARES?', f'dcv{j}-_1_14', '', 1.5)
    Call_oscill('VOLT 13.5', f'CHAN{j}:SCAL 3', 'MEAS1:ARES?', f'dcv{j}+_1_15', '', 1.5)
    Call_oscill('VOLT -13.5', f'CHAN{j}:SCAL 3', 'MEAS1:ARES?', f'dcv{j}-_1_15', '', 1.5)
    Call_oscill('VOLT 14.5', f'CHAN{j}:SCAL 3.2', 'MEAS1:ARES?', f'dcv{j}+_1_16', '', 1.5)
    Call_oscill('VOLT -14.5', f'CHAN{j}:SCAL 3.2', 'MEAS1:ARES?', f'dcv{j}-_1_16', '', 1.5)
    Call_oscill('VOLT 40', f'CHAN{j}:SCAL 10', 'MEAS1:ARES?', f'dcv{j}+_1_17', '', 1.5)
    Call_oscill('VOLT -40', f'CHAN{j}:SCAL 10', 'MEAS1:ARES?', f'dcv{j}-_1_17', '', 1.5)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP DC', 'TIM:SCAL 0.001', f'CHAN{j}:COUP DC')
    Call_oscill('VOLT 0.0045', f'CHAN{j}:SCAL 0.001', 'MEAS1:ARES?', f'dcv{j}+_50_1', '', 2)
    Call_oscill('VOLT -0.0045', f'CHAN{j}:SCAL 0.001', 'MEAS1:ARES?', f'dcv{j}-_50_1', '', 2)
    Call_oscill('VOLT 0.0135', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'dcv{j}+_50_2', '', 2)
    Call_oscill('VOLT -0.0135', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'dcv{j}-_50_2', '', 2)
    Call_oscill('VOLT 0.0145', f'CHAN{j}:SCAL 0.0032', 'MEAS1:ARES?', f'dcv{j}+_50_3', '', 2)
    Call_oscill('VOLT -0.0145', f'CHAN{j}:SCAL 0.0032', 'MEAS1:ARES?', f'dcv{j}-_50_3', '', 2)
    Call_oscill('VOLT 0.045', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'dcv{j}+_50_4', '', 1.5)
    Call_oscill('VOLT -0.045', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'dcv{j}-_50_4', '', 1.5)
    Call_oscill('VOLT 0.05', f'CHAN{j}:SCAL 0.011', 'MEAS1:ARES?', f'dcv{j}+_50_5', '', 1.5)
    Call_oscill('VOLT -0.05', f'CHAN{j}:SCAL 0.011', 'MEAS1:ARES?', f'dcv{j}-_50_5', '', 1.5)
    Call_oscill('VOLT 0.135', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'dcv{j}+_50_6', '', 1.5)
    Call_oscill('VOLT -0.135', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'dcv{j}-_50_6', '', 1.5)
    Call_oscill('VOLT 0.145', f'CHAN{j}:SCAL 0.032', 'MEAS1:ARES?', f'dcv{j}+_50_7', '', 1.5)
    Call_oscill('VOLT -0.145', f'CHAN{j}:SCAL 0.032', 'MEAS1:ARES?', f'dcv{j}-_50_7', '', 1.5)
    Call_oscill('VOLT 0.32', f'CHAN{j}:SCAL 0.07', 'MEAS1:ARES?', f'dcv{j}+_50_8', '', 1.5)
    Call_oscill('VOLT -0.32', f'CHAN{j}:SCAL 0.07', 'MEAS1:ARES?', f'dcv{j}-_50_8', '', 1.5)
    Call_oscill('VOLT 0.45', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'dcv{j}+_50_9', '', 1.5)
    Call_oscill('VOLT -0.45', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'dcv{j}-_50_9', '', 1.5)
    Call_oscill('VOLT 0.5', f'CHAN{j}:SCAL 0.11', 'MEAS1:ARES?', f'dcv{j}+_50_10', '', 1.5)
    Call_oscill('VOLT -0.5', f'CHAN{j}:SCAL 0.11', 'MEAS1:ARES?', f'dcv{j}-_50_10', '', 1.5)
    Call_oscill('VOLT 0.79', f'CHAN{j}:SCAL 0.175', 'MEAS1:ARES?', f'dcv{j}+_50_11', '', 1.5)
    Call_oscill('VOLT -0.79', f'CHAN{j}:SCAL 0.175', 'MEAS1:ARES?', f'dcv{j}-_50_11', '', 1.5)
    Call_oscill('VOLT 0.81', f'CHAN{j}:SCAL 0.18', 'MEAS1:ARES?', f'dcv{j}+_50_12', '', 1.5)
    Call_oscill('VOLT -0.81', f'CHAN{j}:SCAL 0.18', 'MEAS1:ARES?', f'dcv{j}-_50_12', '', 1.5)
    Call_oscill('VOLT 1.35', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'dcv{j}+_50_13', '', 1.5)
    Call_oscill('VOLT -1.35', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'dcv{j}-_50_13', '', 1.5)
    Call_oscill('VOLT 1.45', f'CHAN{j}:SCAL 0.32', 'MEAS1:ARES?', f'dcv{j}+_50_14', '', 1.5)
    Call_oscill('VOLT -1.45', f'CHAN{j}:SCAL 0.32', 'MEAS1:ARES?', f'dcv{j}-_50_14', '', 1.5)
    Call_oscill('VOLT 2.5', f'CHAN{j}:SCAL 0.56', 'MEAS1:ARES?', f'dcv{j}+_50_15', '', 1.5)
    Call_oscill('VOLT -2.5', f'CHAN{j}:SCAL 0.56', 'MEAS1:ARES?', f'dcv{j}-_50_15', '', 1.5)
    Call_oscill('VOLT 2.6', f'CHAN{j}:SCAL 0.57', 'MEAS1:ARES?', f'dcv{j}+_50_16', '', 1.5)
    Call_oscill('VOLT -2.6', f'CHAN{j}:SCAL 0.57', 'MEAS1:ARES?', f'dcv{j}-_50_16', '', 1.5)
    Call_oscill('VOLT 4.5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'dcv{j}+_50_17', '', 1.5)
    Call_oscill('VOLT -4.5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'dcv{j}-_50_17', '', 1.5)
    # ofset
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 0.01', f'CHAN{j}:COUP DCLimit')
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_1_1', '', 2.8)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_1_2', '', 6.3)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_1_3', '', 6.3)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_1_4', '', 3.5)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_1_5', '', 7)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_1_6', '', 7)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_1_7', '', 5.5)
    Call_oscill('VOLT 0.5', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_1_8', '', 7.25)
    Call_oscill('VOLT -0.5', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_1_9', '', 7.25)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_1_10', '', 12.5)
    Call_oscill('VOLT 0.5', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_1_11', '', 14.25)
    Call_oscill('VOLT -0.5', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_1_12', '', 14.25)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_1_13', '', 32.5)
    Call_oscill('VOLT 5', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_1_14', '', 50)
    Call_oscill('VOLT -5', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_1_15', '', 50)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_1_16', '', 102.5)
    Call_oscill('VOLT 5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_1_17', '', 120)
    Call_oscill('VOLT -5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_1_18', '', 120)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 3', 'MEAS1:ARES?', f'odcv{j}_1_19', '', 302.5)
    Call_oscill('VOLT 40', f'CHAN{j}:SCAL 3', 'MEAS1:ARES?', f'odcv{j}_1_20', '', 442.5)
    Call_oscill('VOLT -40', f'CHAN{j}:SCAL 3', 'MEAS1:ARES?', f'odcv{j}_1_21', '', 442.5)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 10', 'MEAS1:ARES?', f'odcv{j}_1_22', '', 442.5)
    Call_oscill('VOLT 40', f'CHAN{j}:SCAL 10', 'MEAS1:ARES?', f'odcv{j}_1_23', '', 1002.5)
    Call_oscill('VOLT -40', f'CHAN{j}:SCAL 10', 'MEAS1:ARES?', f'odcv{j}_1_24', '', 1002.5)
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 1E+06', 'SCOP:SHAP DC', 'TIM:SCAL 0.01', f'CHAN{j}:COUP DC')
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_50_1', '', 2.8)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_50_2', '', 6.3)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.003', 'MEAS1:ARES?', f'odcv{j}_50_3', '', 6.3)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_50_4', '', 3.5)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_50_5', '', 7)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.01', 'MEAS1:ARES?', f'odcv{j}_50_6', '', 7)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_50_7', '', 5.5)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_50_8', '', 9)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.03', 'MEAS1:ARES?', f'odcv{j}_50_9', '', 9)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_50_10', '', 12.5)
    Call_oscill('VOLT 1', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_50_11', '', 16)
    Call_oscill('VOLT -1', f'CHAN{j}:SCAL 0.1', 'MEAS1:ARES?', f'odcv{j}_50_12', '', 16)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.15', 'MEAS1:ARES?', f'odcv{j}_50_13', '', 17.5)
    Call_oscill('VOLT 3', f'CHAN{j}:SCAL 0.15', 'MEAS1:ARES?', f'odcv{j}_50_14', '', 28)
    Call_oscill('VOLT -3', f'CHAN{j}:SCAL 0.15', 'MEAS1:ARES?', f'odcv{j}_50_15', '', 28)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_50_16', '', 32.5)
    Call_oscill('VOLT 3', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_50_17', '', 43)
    Call_oscill('VOLT -3', f'CHAN{j}:SCAL 0.3', 'MEAS1:ARES?', f'odcv{j}_50_18', '', 43)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 0.5', 'MEAS1:ARES?', f'odcv{j}_50_19', '', 52.5)
    Call_oscill('VOLT 5', f'CHAN{j}:SCAL 0.5', 'MEAS1:ARES?', f'odcv{j}_50_20', '', 70)
    Call_oscill('VOLT -5', f'CHAN{j}:SCAL 0.5', 'MEAS1:ARES?', f'odcv{j}_50_21', '', 70)
    Call_oscill('VOLT 0.0009', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_50_22', '', 102.5)
    Call_oscill('VOLT 5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_50_23', '', 120)
    Call_oscill('VOLT -5', f'CHAN{j}:SCAL 1', 'MEAS1:ARES?', f'odcv{j}_50_24', '', 120)

for j in range(1,5,1):
    # trise
    Supportfunc(f'message-Подключите формирователь 9550 на КАНАЛ №{j} осциллографа')
    Supportfunc('resetoscil')
    Param_osc(f'{j}', 'ROUT:SIGN:IMP 50', 'SCOP:SHAP EDGE', 'TIM:SCAL 0.00000000005', f'CHAN{j}:COUP DC')
    Call_oscill('VOLT 0.4', f'CHAN{j}:SCAL 0.05', 'MEAS2:ARES?', f'tr{j}_1', '', 103.08)

Supportfunc(f'message-Калибровка завершена')
Clear_merge()
Supportfunc('resetoscil')
