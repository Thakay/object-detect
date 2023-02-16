from pyembedded.raspberry_pi_tools.raspberrypi import PI

pi = PI()
print(pi.get_ram_info())

print(pi.get_cpu_usage())

print(pi.get_cpu_temp())

