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
NUM_RELAY = 8
COM_PORT = "COM10"
relay_boards = ERB4U(port=COM_PORT)
relay_boards.connect()


"""
All ON, all OFF
"""
for _ in range(9999):
    for board_id in range(NUM_BOARDS):
        # board_id = NUM_BOARDS - board_id - 1
        relay_boards.turn_on_all_relays(board_num=board_id)
    time.sleep(1)

    for board_id in range(NUM_BOARDS):
        # board_id = NUM_BOARDS - board_id - 1
        relay_boards.turn_off_all_relays(board_num=board_id)
    time.sleep(1)


"""
Turn ON/OFF like a rhombus
"""
for _ in range(2):
    relay_boards.turn_on_all_relays(board_num=8)
    relay_boards.turn_on_all_relays(board_num=6)
    relay_boards.turn_on_all_relays(board_num=2)
    relay_boards.turn_on_all_relays(board_num=0)
    time.sleep(1)

    relay_boards.turn_off_all_relays(board_num=8)
    relay_boards.turn_off_all_relays(board_num=6)
    relay_boards.turn_off_all_relays(board_num=2)
    relay_boards.turn_off_all_relays(board_num=0)
    relay_boards.turn_on_all_relays(board_num=7)
    relay_boards.turn_on_all_relays(board_num=5)
    relay_boards.turn_on_all_relays(board_num=3)
    relay_boards.turn_on_all_relays(board_num=1)
    time.sleep(1)


    relay_boards.turn_off_all_relays(board_num=7)
    relay_boards.turn_off_all_relays(board_num=5)
    relay_boards.turn_off_all_relays(board_num=3)
    relay_boards.turn_off_all_relays(board_num=1)







"""
Turn ON/OFF horizontally
"""
relay_boards.turn_on_all_relays(board_num=0)
relay_boards.turn_on_all_relays(board_num=1)
relay_boards.turn_on_all_relays(board_num=2)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=0)
relay_boards.turn_off_all_relays(board_num=1)
relay_boards.turn_off_all_relays(board_num=2)
relay_boards.turn_on_all_relays(board_num=3)
relay_boards.turn_on_all_relays(board_num=4)
relay_boards.turn_on_all_relays(board_num=5)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=3)
relay_boards.turn_off_all_relays(board_num=4)
relay_boards.turn_off_all_relays(board_num=5)
relay_boards.turn_on_all_relays(board_num=6)
relay_boards.turn_on_all_relays(board_num=7)
relay_boards.turn_on_all_relays(board_num=8)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=6)
relay_boards.turn_off_all_relays(board_num=7)
relay_boards.turn_off_all_relays(board_num=8)
# time.sleep(1)


# ----------------------------

"""
Turn ON/OFF vertically
"""
relay_boards.turn_on_all_relays(board_num=0)
relay_boards.turn_on_all_relays(board_num=5)
relay_boards.turn_on_all_relays(board_num=6)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=0)
relay_boards.turn_off_all_relays(board_num=5)
relay_boards.turn_off_all_relays(board_num=6)
relay_boards.turn_on_all_relays(board_num=1)
relay_boards.turn_on_all_relays(board_num=4)
relay_boards.turn_on_all_relays(board_num=7)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=1)
relay_boards.turn_off_all_relays(board_num=4)
relay_boards.turn_off_all_relays(board_num=7)
relay_boards.turn_on_all_relays(board_num=2)
relay_boards.turn_on_all_relays(board_num=3)
relay_boards.turn_on_all_relays(board_num=8)
time.sleep(1)

relay_boards.turn_off_all_relays(board_num=2)
relay_boards.turn_off_all_relays(board_num=3)
relay_boards.turn_off_all_relays(board_num=8)
time.sleep(1)



"""
Turn ON/OFF vertically in sequence
"""
for relay_id in range(9):
    relay_boards.turn_on_relay(board_num=0, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=1, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=2, relay_num=relay_id)
    time.sleep(0.2)
relay_boards.turn_off_all_relays(board_num=0)
relay_boards.turn_off_all_relays(board_num=1)
relay_boards.turn_off_all_relays(board_num=2)



for relay_id in range(9):
    relay_boards.turn_on_relay(board_num=3, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=4, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=5, relay_num=relay_id)
    time.sleep(0.2)
relay_boards.turn_off_all_relays(board_num=3)
relay_boards.turn_off_all_relays(board_num=4)
relay_boards.turn_off_all_relays(board_num=5)



for relay_id in range(9):
    relay_boards.turn_on_relay(board_num=6, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=7, relay_num=relay_id)
    relay_boards.turn_on_relay(board_num=8, relay_num=relay_id)
    time.sleep(0.2)
relay_boards.turn_off_all_relays(board_num=6)
relay_boards.turn_off_all_relays(board_num=7)
relay_boards.turn_off_all_relays(board_num=8)




"""
Turn ON/OFF vertically inwards
"""
for _ in range(2):
    for relay_id in range(4):
        relay_id = relay_id + 1
        relay_boards.turn_on_relay(board_num=0, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=5, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=6, relay_num=relay_id)

        relay_id = relay_id + 4
        relay_boards.turn_on_relay(board_num=2, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=3, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=8, relay_num=relay_id)
        time.sleep(0.2)

    for relay_id in range(4):
        relay_id = relay_id + 1
        relay_boards.turn_off_relay(board_num=0, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=5, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=6, relay_num=relay_id)

        relay_id = relay_id + 4
        relay_boards.turn_off_relay(board_num=2, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=3, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=8, relay_num=relay_id)
        time.sleep(0.2)


    for relay_id in range(4):
        relay_id = relay_id + 5
        relay_boards.turn_on_relay(board_num=0, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=5, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=6, relay_num=relay_id)

        relay_id = relay_id - 4
        relay_boards.turn_on_relay(board_num=2, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=3, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=8, relay_num=relay_id)
        time.sleep(0.2)


    for relay_id in range(4):
        relay_id = relay_id + 5
        relay_boards.turn_off_relay(board_num=0, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=5, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=6, relay_num=relay_id)

        relay_id = relay_id - 4
        relay_boards.turn_off_relay(board_num=2, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=3, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=8, relay_num=relay_id)
        time.sleep(0.2)

    for relay_id in range(4):
        relay_id = relay_id + 1
        relay_boards.turn_on_relay(board_num=1, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=4, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=7, relay_num=relay_id)

        relay_id = relay_id + 4
        relay_boards.turn_on_relay(board_num=1, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=4, relay_num=relay_id)
        relay_boards.turn_on_relay(board_num=7, relay_num=relay_id)
        time.sleep(0.2)


    for relay_id in range(4):
        relay_id = relay_id + 1
        relay_boards.turn_off_relay(board_num=1, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=4, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=7, relay_num=relay_id)

        relay_id = relay_id + 4
        relay_boards.turn_off_relay(board_num=1, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=4, relay_num=relay_id)
        relay_boards.turn_off_relay(board_num=7, relay_num=relay_id)
        time.sleep(0.2)




