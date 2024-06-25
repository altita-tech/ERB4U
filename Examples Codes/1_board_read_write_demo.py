"""
How to run this demo
1) Connect 1 ERB4U board to the PC via USB type-C cable
2) Set ERB4U board address to 0

Demo code explanation:
1) Read board's PN, SN, hardware rev, firmware rev, number of relays, MCU temperature, LDO voltage 
2) Turn ON/OFF relays, and read relay states 
"""

# Add the parent directory to the Python path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from API.erb4u_api import ERB4U
import time 

COM_PORT = 'COM9'
relay_board = ERB4U(port=COM_PORT)
relay_board.disconnect()
relay_board.connect()

board_id = 0

pn               = relay_board.read_pn(board_id)
sn               = relay_board.read_sn(board_id)
hardware_rev     = relay_board.read_hardware_rev(board_id)
firmware_rev     = relay_board.read_firmware_rev(board_id)
num_of_relay     = relay_board.read_num_of_relay(board_id)
mcu_temp_degree  = relay_board.read_temperature_degree(board_id)
ldo_voltage      = relay_board.read_ldo_vdda(board_id)
print(f"PN                  = {pn}")
print(f"SN                  = {sn}")
print(f"hardware_rev        = {hardware_rev}")
print(f"firmware_rev        = {firmware_rev}")
print(f"num_of_relay        = {num_of_relay}")
print(f"mcu_temp_degree     = {mcu_temp_degree}")
print(f"ldo_voltage         = {ldo_voltage}")

print("-------------------- Turn ON all relays at once --------------------")
relay_board.turn_on_all_relays(board_id)
all_relays_states = relay_board.read_all_relays_states(board_id)
print(f"Board = {board_id}, all relays state = {all_relays_states}")

for i in range(8):
    relay_state = relay_board.read_relay_state(board_id, relay_num=i+1)
    print(f"Board = {board_id}, state = {relay_state}")
    time.sleep(0.1)


print("-------------------- Turn OFF all relays at once --------------------")
relay_board.turn_off_all_relays(board_id)
all_relays_states = relay_board.read_all_relays_states(board_id)
print(f"Board = {board_id}, all relays state = {all_relays_states}")

for i in range(8):
    relay_state = relay_board.read_relay_state(board_id, relay_num=i+1)
    print(f"Board = {board_id}, state = {relay_state}")
    time.sleep(0.1)

print("-------------------- Turn ON each relays 1 by 1 --------------------")
for i in range(8):
    relay_board.turn_on_relay(board_id, relay_num=i+1)
    time.sleep(0.1)

print("-------------------- Turn OFF each relays 1 by 1 -------------------")
for i in range(8):
    relay_board.turn_off_relay(board_id, relay_num=i+1)
    time.sleep(0.1)
    
