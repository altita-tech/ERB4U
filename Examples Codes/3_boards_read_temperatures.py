"""
How to run this demo
1) Connect 3 ERB4U boards by custom cable
2) Set each ERB4U address to 0, 1 and 2 respectively 
3) Connect one of the ERB4U boards to the PC via USB type-C cable, and run this demo code 

Demo code explanation:
1) Read board 0, 1 and 2 MCU temperature 
2) Print results and separate by comma 
3) Repeat step 1 and 2 by 10 times
"""

# Add the parent directory to the Python path
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from API.erb4u_api import ERB4U

COM_PORT = 'COM9'
relay_boards = ERB4U(port=COM_PORT)
relay_boards.connect()

for i in range(10):
    temp0 = relay_boards.read_temperature_degree(board_num=0)
    temp1 = relay_boards.read_temperature_degree(board_num=1)
    temp2 = relay_boards.read_temperature_degree(board_num=2)
    print(f"{temp0},{temp1},{temp2}")
    

