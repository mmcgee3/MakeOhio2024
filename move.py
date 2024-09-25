import serial
import serial.tools.list_ports
import time

ser = serial.Serial("/dev/cu.usbmodem1101", 115200)
command = ""

ser.close()
ser.open()
#Loop to send alternate commands "left" and "right"
'''
for i in range(40):
    if(i % 2 == 0):
        command = "left"
        command = command.encode('utf-8')
        ser.write(command)
        print("Command sent successfully")
        time.sleep(.85)
'''
while True:
    command = input("Enter: ")
    if command == "exit":
        ser.close()
        print("Serial connection closed")
        exit()
    else :
        print("Sending command:", command)
        command = command.encode('utf-8')
        ser.write(command)
        print("Command sent successfully")
    
