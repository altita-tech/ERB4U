"""
How to run this demo
1) Connect 9 ERB4U boards by custom cable
2) Set each ERB4U address to 0, 1, 2 ... 8 respectively 
3) Connect one of the ERB4U boards to the PC via USB type-C cable, and run this demo code 

Demo code explanation:
1) For boards 0, 1, 2 ... 8, turn ON all relays, wait for 1 sec, then OFF all relays 
2) Repeat step 1 by 3 times 
"""

# Add the parent directory to the Python path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from API.erb4u_api import ERB4U
import time 

NUM_BOARDS = 9
COM_PORT = "COM9"
relay_boards = ERB4U(port=COM_PORT)
relay_boards.connect()

for _ in range(3):
    time.sleep(1)
    for board_id in range(NUM_BOARDS):
        relay_boards.turn_on_all_relays(board_num=board_id)

    time.sleep(1)
    for board_id in range(NUM_BOARDS):
        relay_boards.turn_off_all_relays(board_num=board_id)


