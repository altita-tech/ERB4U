"""
How to run this demo
1) Connect 3 ERB4U boards by custom cable, connect the 1st board to PC
2) Set each ERB4U address to 0, 1 and 2 respectively 
3) Connect 1st ERB4U board to the PC via USB type-C cable, and run this demo code 


Demo code explanation:
1) Turn ON/OFF all relays at once
2) Turn ON/OFF each relay 1 by 1
"""

# Add the parent directory to the Python path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from API.erb4u_api import ERB4U
import time 

COM_PORT = 'COM9'
relay_boards = ERB4U(port=COM_PORT)
relay_boards.connect()


print("-------------------- Turn ON all relays at once --------------------")
relay_boards.turn_on_all_relays(board_num=0)
relay_boards.turn_on_all_relays(board_num=1)
relay_boards.turn_on_all_relays(board_num=2)

time.sleep(1)
print("-------------------- Turn OFF all relays at once --------------------")
relay_boards.turn_off_all_relays(board_num=0)
relay_boards.turn_off_all_relays(board_num=1)
relay_boards.turn_off_all_relays(board_num=2)

time.sleep(1)
print("-------------------- Turn ON each relay 1 by 1 --------------------")
for i in range(8):
    relay_boards.turn_on_relay(board_num=0, relay_num=(i+1))

for i in range(8):
    relay_boards.turn_on_relay(board_num=1, relay_num=(i+1))

for i in range(8):
    relay_boards.turn_on_relay(board_num=2, relay_num=(i+1))

time.sleep(1)
print("-------------------- Turn OFF each relay 1 by 1 --------------------")
for i in range(8):
    relay_boards.turn_off_relay(board_num=0, relay_num=(i+1))

for i in range(8):
    relay_boards.turn_off_relay(board_num=1, relay_num=(i+1))

for i in range(8):
    relay_boards.turn_off_relay(board_num=2, relay_num=(i+1))

