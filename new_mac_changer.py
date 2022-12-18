#!/usr/bin/env python

import subprocess

interface = input("Type the interface here >")
mac_address = input("Enter the new macc address to assign >")

print("Changing the " + interface + " mac address to " +mac_address)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface, "hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])