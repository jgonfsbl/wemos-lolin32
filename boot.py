# This file is executed on every boot (including wake-boot from deepsleep)
# EA1HET @ 2018-12-27

import gc
import config
import network
import ubinascii as binascii


print('\n[Booting] ')

print('\nShutting down self-run AP')
wlan_ap = network.WLAN(network.AP_IF)
wlan_ap.active(False)    

print('\nConnecting to IoT network')
wlan_client = network.WLAN(network.STA_IF)

if not wlan_client.isconnected():
    wlan_client.active(True)
    wlan_client.connect(config.essid, config.passphrase)

    while not wlan_client.isconnected():
        pass

print('Connected to network')

(ip, netmask, gateway, dns) = wlan_client.ifconfig()
name = config.hostname + "-esp-%s" % binascii.hexlify(wlan_client.config("mac")[-3:]).decode("ascii")
macaddress = binascii.hexlify(wlan_client.config('mac'),':').decode('utf-8') 

gc.collect()


