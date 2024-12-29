from machine import UART, Pin
import time

time.sleep(10)

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
txData = b'hello world\n\r'
time.sleep(10)
uart1.write(txData)
time.sleep(10)
uart1.write(txData)

# rxData = bytes()
# while uart1.any() > 0:
#     rxData += uart1.read(1)
# print(rxData.decode('utf-8'))