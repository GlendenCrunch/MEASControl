### MEASControl - программа поверки/калибровки цифровых мультиметров и осциллографов
+ Python 3.8.6 32-bit
+ pip install: pyvisa, pyvisa-sim, openpyexcel, pyserial
+ Драйверы: NI-VISA
+ Калибратор для мультиметров: Fluke 5500A (5522A), N4-56
+ Калибратор для осциллографов: Fluke 9500B (connect: GPIB-Arduino-USB)
+ Поддерживаемые мультиметры:
  + Keysight/Agilent: 34401A, 34410A, 34411A, 34460A, 34461A, 34465A, 34470A, 34420A
  + АКИП: В7-78/1
+ Поддерживаемые осциллографы:
  + Keysight/Agilent: MSO-X 3034A, MSO-X 3054A, MSO-X 3104A, DSO6102A, DSO9104A, DSO7034B
  + Tektronix: TDS2002, TDS2014, TDS2014B, TDS2014C, TDS2024, TDS2024C, TPS2024
  + Siglent: AKIP4119/1, AKIP4131/1A
  + Lecroy: WJ312A, HDO8108A
  + R&S: RTO1024
+ Виртуальные приборы (pyvisa-sim):
  + Agilent 34401A (ASRL9::INSTR)
  + Agilent 34411A (ASRL8::INSTR)
  + Fluke 5522A (ASRL10::INSTR)
+ Interface:
![alt text](https://github.com/GlendenCrunch/MEASControl/blob/main/image/1.png)
![alt text](https://github.com/GlendenCrunch/MEASControl/blob/main/image/2.png)
