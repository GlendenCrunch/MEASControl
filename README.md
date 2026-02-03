### MEASControl - calibration DMM & oscilloscope
+ Python 3.11.9
+ pip install: pyvisa, pyvisa-sim, openpyexcel, pyserial, pyusb
+ Driver: NI-VISA
+ Connect: RS-232, USB, Ethernet
+ Calibrator: Fluke 5500A (5522A), N4-56
+ Calibrator oscilloscope: Fluke 9500B (connect: GPIB-Arduino-USB)
  + Active Head: 9530 (150 ps) & 9550 (25 ps)
+ Suported DMM:
  + Keysight/Agilent: 34401A, 34410A, 34411A, 34460A, 34461A, 34465A, 34470A, 34420A
  + AKIP: V7-78/1
+ Suported osciloscope:
  + Keysight/Agilent: MSO-X 3032T, MSO-X 3034A, MSO-X 3054A, MSO-X 3104(A,T), MSO-X 4104A, MSO-X 4154A, 
                      MSO-X 6004A, DSO-X 4034A, MSO6012A, DSO6102A, DSO7034B, DSO9104A, MSO9404A,
                       DSO-X 92004A, DSOZ594A
  + Tektronix: TDS2002, TDS2012B, TDS2014, TDS2014B, TDS2014C, TDS2024, TDS2024C, TPS2024
  + Siglent (AKIP): AKIP4119/1, AKIP4131/1A
  + Lecroy: WJ312A, WJ324A, HDO8108A
  + R&S: RTO1024, RTO1044
  + OWON (AKTAKOM): ADS-222
  + Rigol: MSO5204
+ Suported generators:
  + Keysight/Agilent: 33622A
  + Micran: G7M-20A
+ Virtual pribors (pyvisa-sim):
  + Agilent 34401A (ASRL9::INSTR)
  + Agilent 34411A (ASRL8::INSTR)
  + Fluke 5522A (ASRL10::INSTR)
+ Interface:
![alt text](https://github.com/GlendenCrunch/MEASControl/blob/main/image/1.png)
![alt text](https://github.com/GlendenCrunch/MEASControl/blob/main/image/2.png)
