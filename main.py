# This file is executed on every boot (including wake-boot from deepsleep)
# EA1HET @ 2018-12-26

import sys
from ntptime import settime
from utime import localtime

gc.collect()

try:
    settime() 
    tup = localtime()
    lcldate = '{}-{}-{}'.format(tup[0],tup[1],tup[2])  
except:
    lcldate = 'Date not set' 
    pass

print('\n[Main]')
print('Running Micropython on WEMOS.CC LoLin32 v1.0 Rev.1')

if not wlan_client.isconnected():
    print('Error: Wi-Fi not connected')
else:
    print('hostname :', name)
    print('Python   : %s' % sys.version)
    print() 
    print('IP addr  :', ip)
    print('Netmask  :', netmask)
    print('Gateway  :', gateway)
    print('DNS Srv  :', dns)
    print('WiFi MAC :', macaddress) 
    print('Lcl Date :', lcldate) 
    print('Free MEM : %s bytes' % gc.mem_free())

print('\nEntering REPL...\n') 
gc.collect()

# Here comes your code....