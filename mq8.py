"""
+-----------------------------------------------------------------+
|                                                                 |
|   Micropython library for dealing with MQ8 Hydrogen gas Sensor  |
|   porting from sandbox electronics arduino MQ-8 sensor code     |
|                                                                 |
|   More info:                                                    |
|       https://sandboxelectronics.com/?p=196                     |
|                                                                 |
+-----------------------------------------------------------------+
"""

import math
import utime as time
from machine import ADC,Pin

class MQ8(object):
    """ Class for dealing with MQ-8 Hydrogen Sensors """
    # The load resistance on the board
    RLOAD = 10.0

    # Calibration resistance at atmospheric H2 level
    RO_CLEAN_AIR_FACTOR = 9.21

    #sensor ADC Bit Width (on A0 Pin) MQ-8 is 10-bit
    ADC_BIT_WIDTH = ADC.WIDTH_10BIT

    #port from arduino
    CALIBRATION_SAMPLE_TIMES = 50
    CALIBRATION_SAMPLE_INTERVAL = 500
    READ_SAMPLE_TIMES = 5
    READ_SAMPLE_INTERVAL = 500

    #Gas id
    GAS_H2 = 0

    #Sensor resistance change curve when detecting H2
    H2_CURVE = [2.3,0.93,-1.44]

    #max resistance of the sensor with the presence of H2 gas
    RO = 10.0

    def __init__(self, pin):
        'Constuctor method of MQ8'
        self.pin = pin

    def get_resistance(self):
        'Return sensor resistance'
        adc = ADC(self.pin)
        adc.width(MQ8.ADC_BIT_WIDTH)
        value = adc.read()
        if value == 0:
            return -1

        return (1023./value - 1.) * MQ8.RLOAD

    def check_condition(self):
        'call during calibration when needed'
        r = self.get_resistance()
        if r == -1:
            print('''
                -------------------
                No data detected !
                -------------------
                1. Please make sure your MQ-8 Sensor is connected to the board.
                2. Check your connection. Make sure your solder or cable in a good condition.
                3. Make sure you already supply board and MQ-8 sensor with enough voltage.

                ''')

    def calibration(self,check=False):
        'Calibrate H2 Sample Before Read'
        if check == True:
            self.check_condition()

        val = 0
        for i in range(0,MQ8.CALIBRATION_SAMPLE_TIMES):
            val += self.get_resistance()
            time.sleep_ms(MQ8.CALIBRATION_SAMPLE_INTERVAL)

        val = val / MQ8.CALIBRATION_SAMPLE_TIMES
        val = val / MQ8.RO_CLEAN_AIR_FACTOR

        return val

    def read(self,check=False):
        'Read MQ-8 Sensor rs overtime'
        if check == True:
            self.check_condition()

        rs = 0
        for i in range(0,MQ8.READ_SAMPLE_TIMES):
            rs += self.get_resistance()
            time.sleep_ms(MQ8.READ_SAMPLE_INTERVAL)

        rs = rs / MQ8.READ_SAMPLE_TIMES

        return rs

    def get_percentage(self,rs_ro_ratio,pcurve):
        'calculate percentage of gas'
        pct = math.pow(10, ((math.log(rs_ro_ratio)-pcurve[1]) / pcurve[2]) + pcurve[0])
        return pct

    def gas_percentage(self,rs_ro_ratio,gas_id):
        'return the calculated percentage of H2'
        if gas_id == MQ8.GAS_H2:
            gas_pct = self.get_percentage(rs_ro_ratio,MQ8.H2_CURVE)
            return gas_pct

    def get_ppm(self):
        'calculate ppm of H2 gas'
        ppm = self.gas_percentage(self.read(self.pin) / MQ8.RO, MQ8.GAS_H2)
        return ppm

def example():
    """MQ8 H2 example"""

    #instantiate mq8 sensor object
    mq8 = MQ8(Pin(36)) # analog PIN 0 A0 is GPIO36

    #calibrate before use
    print('Calibrating...')
    print('This may take a while')

    #calibrate before use
    mq8.calibration(check=True)

    # loop
    while True:
        #read all data
        rs = mq8.read()
        ppm = mq8.get_ppm()
        resistance = mq8.get_resistance()

        print('Rs = {}\nH2 Concentration : {} ppm \nSensor resistance : {} kohm'.format(rs,ppm,resistance))

        time.sleep(0.3)

if __name__ == "__main__":
    mq8_example()
