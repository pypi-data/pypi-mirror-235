# -*- coding: utf-8 -*-
# Copyright (c) 2023 PHOXENE
# MIT License: 
# https://opensource.org/license/mit/
#
""" Test for modbus module

"""
__authors__ = ("Aurélien PLANTIN")
__contact__ = ("a.plantin@phoxene.com")
__copyright__ = "MIT"
__date__ = "2023-10-10"

import unittest                     # The test framework
import modbus                       # The module to be tested
from modbus import ModbusError
from serial import PortNotOpenError

def terminal_output(**kwargs):
    '''This function output everything passed as
        key arguments to the terminal.
    '''
    for k, v in kwargs.items():
        print(f"{k}: {v}")

class Test_crc(unittest.TestCase):
    def test_crc(self) -> None:
        # Simple crc computation result test
        self.assertEqual(modbus._crc16([1, 6, 0, 49, 0, 2]), 50265)

class Test_with_port_not_open(unittest.TestCase):
    def setUp(self):
        self.link = modbus.Modbus()

    def test_port_not_open_error(self) -> None:
        with self.assertRaises(PortNotOpenError):
            self.link.read_registers(device_addr = 1, reg_addr = 0, nb_reg = 1)

class Test_with_port_open(unittest.TestCase):
    def setUp(self):
        self.link = modbus.Modbus()
        self.link.open(port = 'COM3')

    def tearDown(self):
        self.link.close()

    def test_single_read(self) -> None:
        # Read BT software revision
        self.assertEqual(self.link.read_register(device_addr = 1, reg_addr = 268), 1033)

    def test_single_write(self) -> None:
        # Read and write sync shift register
        sync_shift = self.link.read_register(device_addr = 1, reg_addr = 268)
        self.link.write_register(device_addr = 1, reg_addr = 52, value = sync_shift + 879)
        self.assertEqual(self.link.read_register(device_addr = 1, reg_addr = 52), sync_shift + 879)

    def test_not_allowed_broadcast(self) -> None:
        with self.assertRaises(ValueError): #Ajouter la vérification du text

            self.link.read_register(device_addr = 0, reg_addr = 0)

class Test_fast_mode(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()