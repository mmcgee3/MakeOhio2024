import serial
import serial.tools.list_ports

ser = serial.Serial("/dev/cu.usbmodem101", 9600)
command = ""

ser.close()
ser.open()
#Loop to send alternate commands "left" and "right"
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
        print(command)
