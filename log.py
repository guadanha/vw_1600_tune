import serial
import time
import csv

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
print(ser.name)         # check which port was really used

with open('eggs.csv', 'w', newline='') as csv_file:
    spamwriter = csv.writer(csv_file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for _ in range(5):
        time.sleep(1)
        ser.write(b'A')     # write a string
        received = ser.read(127)
        print('receive available' + received.hex(':'))
        print('AV v: ' + str(int.from_bytes(received[4:5], 'big')))
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        spamwriter.writerow([str(int.from_bytes(received[4:5], 'big')), int.from_bytes(received[4:5], 'big')])

ser.close()             # close port
