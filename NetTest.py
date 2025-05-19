#!/usr/bin/env python

#-----------------------------------------------------------------------------
#
#   Internet Remote Switching with ezTCP via Modbus/TCP (Python 3)
#
#   by Oliver Thamm - Elektronikladen Microcomputer
#   https://github.com/elmicro/eztcp_modbus_py
#
#   Test example to access an ezTCP Remote I/O-Controller
#   model CIE-H10 / CIE-H12 / CIE-H14 (Sollae Systems)
#   via Modbus/TCP protocol using Python 3
#
#   Requires EasyModbusTCP/UDP/RTU Python by Stefan Rossmann
#   https://github.com/rossmann-engineering/EasyModbusTCP.PY
#   https://sourceforge.net/projects/easymodbustcp-udp-rtu-python/
#
#   This software is Copyright (C)2017 by ELMICRO - https://elmicro.com
#   and may be freely used, modified and distributed under the terms of
#   the MIT License - see accompanying LICENSE.md for details
#
#-----------------------------------------------------------------------------

import time
from pyModbusTCP.client import ModbusClient
# from ModbusClient import *

ip_addr = '192.168.1.204'
tcp_port = 4370
addr_out = 9

eztcp = ModbusClient(host=ip_addr, port=tcp_port)

if eztcp.open():
    print("Connected to Modbus server.")

    eztcp.write_single_coil(addr_out, True)
    time.sleep(1)
    eztcp.write_single_coil(addr_out, False)

    eztcp.close()
else:
    print("Failed to connect to Modbus server.")
