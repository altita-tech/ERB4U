import serial
import time


class ERB4U:
    def __init__(self, port):
        self.port = port

        self.DONT_CARE_BYTE = 0xFF
        self.TIME_DELAY = 0.005
        
        self.ser = serial.Serial(self.port, 115200)
        self.ser.close()
        time.sleep(self.TIME_DELAY)

    def connect(self):
        self.ser.close()
        time.sleep(self.TIME_DELAY)
        self.ser.open()
        time.sleep(self.TIME_DELAY)
        print("connected")

    def disconnect(self):
        self.ser.close()
        time.sleep(self.TIME_DELAY)
        print("disconnected")

    def read_serial_data(self):
        data = self.ser.readline().decode('utf-8', errors='ignore').strip()
        if data:
            return data
        else:
            print("No available data")
            return None

    # Read commands ================================
    def read_relay_state(self, board_num: int, relay_num: int) -> int:
        cmd = bytes([board_num, 0x00, relay_num, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        relay_state = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return int(relay_state)

    def read_all_relays_states(self, board_num: int) -> str:
        cmd = bytes([board_num, 0x00, 0xA0, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        all_relays_states = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return all_relays_states

    def read_num_of_relay(self, board_num: int) -> int:
        cmd = bytes([board_num, 0x00, 0xA1, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        num_of_relay = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return int(num_of_relay)

    def read_temperature_degree(self, board_num: int) -> float:
        cmd = bytes([board_num, 0x00, 0xA2, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        temperature_degree = float(self.read_serial_data())
        time.sleep(self.TIME_DELAY)
        return temperature_degree
    
    def read_ldo_vdda(self, board_num: int) -> float:
        cmd = bytes([board_num, 0x00, 0xA3, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        temperature_degree = float(self.read_serial_data())
        time.sleep(self.TIME_DELAY)
        return temperature_degree

    def read_pn(self, board_num: int) -> str:
        cmd = bytes([board_num, 0x00, 0xF0, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        pn = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return pn
    
    def read_sn(self, board_num: int) -> str:
        cmd = bytes([board_num, 0x00, 0xF1, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        sn = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return sn

    def read_hardware_rev(self, board_num: int) -> str:
        cmd = bytes([board_num, 0x00, 0xF2, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        hardware_rev = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return hardware_rev

    def read_firmware_rev(self, board_num: int) -> str:
        cmd = bytes([board_num, 0x00, 0xF3, self.DONT_CARE_BYTE])
        self.ser.write(cmd)
        firmware_rev = self.read_serial_data()
        time.sleep(self.TIME_DELAY)
        return firmware_rev


    # Write commands ================================
    def turn_off_relay(self, board_num: int, relay_num: int) -> None:
        cmd = bytes([board_num, 0x01, relay_num, 0x00])
        self.ser.write(cmd)
        time.sleep(self.TIME_DELAY)
        
    def turn_on_relay(self, board_num: int, relay_num: int) -> None:
        cmd = bytes([board_num, 0x01, relay_num, 0x01])
        self.ser.write(cmd)
        time.sleep(self.TIME_DELAY)

    def turn_off_all_relays(self, board_num: int) -> None:
        cmd = bytes([board_num, 0x01, 0xA0, 0x00])
        self.ser.write(cmd)
        time.sleep(self.TIME_DELAY)

    def turn_on_all_relays(self, board_num: int) -> None:
        cmd = bytes([board_num, 0x01, 0xA1, 0x01])
        self.ser.write(cmd)
        time.sleep(self.TIME_DELAY)

