# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:22:25 2020

@author: Patel
"""

import serial
import time

class Arduino_Serial:
    
    def __init__(self, com, baudrate=9600):
        self.com = com
        self.connected = False
        self.baudrate = baudrate
        self.conn = None
    
    def connect(self):
        try:
            ser = serial.Serial(self.com, baudrate=self.baudrate, timeout=1)
            time.sleep(1)
            print("Succesfully Connected with Port :" + self.com)
            self.connected = True
            self.conn = ser
            return ser
        except:
            raise Exception("Can't establish connection to the given com port.")
    
    def deconnect(self):
        if self.connected:
            try:
                if self.connected:
                    self.conn.close()
                    self.conn = None
                    self.connected = False
                    print("Succesfully Deconnected with Port :" + self.com)
            except:
                raise Exception("Can't close connection to the given com port.")
        else:
            raise Exception("No connection was found to deconnect.")
    
    def connection(self):
        if self.conn != None:
            return self.conn
        else:
            raise Exception("No connection was Found.")
    
    def is_connected(self):
        return self.connected()