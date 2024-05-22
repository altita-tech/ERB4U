"""
How to run this demo
1) Connect 3 ERB4U boards by custom cable
2) Set each ERB4U address to 0, 1 and 2 respectively 
3) Connect one of the ERB4U boards to the PC via USB type-C cable, and run this demo code 


Demo code explanation:
1) Read board 0, 1 and 2's information: PN, SN, hardware rev, firmware rev, MCU temperature
2) Print results 
"""

# Add the parent directory to the Python path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from API.erb4u_api import ERB4U

COM_PORT = 'COM9'
relay_boards = ERB4U(port=COM_PORT)
relay_boards.disconnect()
relay_boards.connect()


pn_0 = relay_boards.read_pn(board_num=0)
pn_1 = relay_boards.read_pn(board_num=1)
pn_2 = relay_boards.read_pn(board_num=2)
print(f"Board 0: PN             = {pn_0}")
print(f"Board 1: PN             = {pn_1}")
print(f"Board 2: PN             = {pn_2}")

sn_0 = relay_boards.read_sn(board_num=0)
sn_1 = relay_boards.read_sn(board_num=1)
sn_2 = relay_boards.read_sn(board_num=2)
print(f"Board 0: SN             = {sn_0}")
print(f"Board 1: SN             = {sn_1}")
print(f"Board 2: SN             = {sn_2}")

hardware_rev_0 = relay_boards.read_hardware_rev(board_num=0)
hardware_rev_1 = relay_boards.read_hardware_rev(board_num=1)
hardware_rev_2 = relay_boards.read_hardware_rev(board_num=2)
print(f"Board 0: hardware_rev   = {hardware_rev_0}")
print(f"Board 1: hardware_rev   = {hardware_rev_1}")
print(f"Board 2: hardware_rev   = {hardware_rev_2}")

firmware_rev_0 = relay_boards.read_firmware_rev(board_num=0)
firmware_rev_1 = relay_boards.read_firmware_rev(board_num=1)
firmware_rev_2 = relay_boards.read_firmware_rev(board_num=2)
print(f"Board 0: firmware_rev   = {firmware_rev_0}")
print(f"Board 1: firmware_rev   = {firmware_rev_1}")
print(f"Board 2: firmware_rev   = {firmware_rev_2}")

pcba_temp_degree_0 = relay_boards.read_temperature_degree(board_num=0)
pcba_temp_degree_1 = relay_boards.read_temperature_degree(board_num=1)
pcba_temp_degree_2 = relay_boards.read_temperature_degree(board_num=2)
print(f"Board 0: temperature    = {pcba_temp_degree_0}")
print(f"Board 1: temperature    = {pcba_temp_degree_1}")
print(f"Board 2: temperature    = {pcba_temp_degree_2}")
