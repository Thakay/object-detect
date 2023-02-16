from pyembedded.raspberry_pi_tools.raspberrypi import PI
import csv

pi = PI()
pi.get_ram_info()

pi.get_cpu_usage()
pi.get_cpu_temp()

with open('usage.csv', 'w', newline='') as file:
     writer = csv.writer(file)

     writer.writerow(["ram", "cpu", "temp"])
     writer.writerow([pi.get_ram_info(), pi.get_cpu_usage(), pi.get_cpu_temp()])