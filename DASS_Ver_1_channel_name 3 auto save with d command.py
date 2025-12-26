# Improved version of the DASS_Ver_1_channel_name 3 auto save with d command.py
# Last updated by 'faturahman634' on 2025-12-26 02:17:08

"""
This script is a part of the DASS Modbus Serial Acquisition project. It has been improved for better code quality,
readability, comments, and modularity. The goal is to facilitate easier code maintenance and understanding.
"""

import time
import serial  # Import pyserial for serial device communication

# Constants
SERIAL_PORT = "COM3"  # Update to your serial port
BAUD_RATE = 9600  # Communication baud rate
READ_TIMEOUT = 1.0  # Serial read timeout in seconds

# Function Definitions
def setup_serial_connection():
    """
    Create and return a configured serial connection.
    
    Returns:
        serial.Serial: A configured and opened serial port.
    """
    try:
        print(f"Setting up serial connection on {SERIAL_PORT} at {BAUD_RATE} baud.")
        connection = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=READ_TIMEOUT)
        return connection
    except serial.SerialException as e:
        print(f"Error setting up serial connection: {e}")
        raise

def read_from_serial(connection):
    """
    Read a line of data from the serial connection.

    Args:
        connection (serial.Serial): The opened serial connection.

    Returns:
        str: The data line read.
    """
    try:
        if connection.in_waiting:
            data = connection.readline().decode('utf-8').strip()
            print(f"Serial data received: {data}")
            return data
        else:
            print("No data waiting on serial port.")
            return None
    except Exception as e:
        print(f"Error during serial read: {e}")
        return None

def process_serial_data(data):
    """
    Process the data captured from the serial connection for analysis or further logic.

    Args:
        data (str): The raw data string received.

    Returns:
        None: Functionality to process will be customized based on application.
    """
    if not data:
        return

    # Example processing (to be customized as needed)
    print(f"Processing data: {data}")

def main():
    """
    Main control loop for the serial data acquisition system.
    """
    try:
        with setup_serial_connection() as connection:
            print("Serial connection established. Entering main data acquisition loop.")

            while True:
                data = read_from_serial(connection)
                if data:
                    process_serial_data(data)

                time.sleep(0.5)  # Delay to avoid excessive polling

    except KeyboardInterrupt:
        print("Data acquisition halted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Serial connection closed.")

if __name__ == "__main__":
    main()