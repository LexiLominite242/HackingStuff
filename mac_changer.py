import subprocess
import optparse
import time

def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Please enter the interface name for which you want "
                                                                  "to change the MAC")
    parser.add_option("-m", "--mac", dest="mac_address", help="Enter the MAC Address you want to change to")
    return parser.parse_args()


def change_mac(interface1, mac_address1):
    subprocess.call(["ifconfig", interface1, "down"])
    subprocess.call(["ifconfig", interface1, "hw", "ether", mac_address1])
    subprocess.call(["ifconfig", interface1, "up"])


options, arguements = get_arguements()
if not options.interface:
    print(":( Please Enter the Interface name! using '-i' argument ):")
    time.sleep(1)
    print("Press --help for more info")
    time.sleep(0.5)
    print("<---------------Copyright 2020-2100 LexiLominite242----------------->")

else:
    if not options.mac_address:
        print("!!!!!! Since you did not mention your MacAddress changing your mac address to default once !!!!!")
        time.sleep(1)
        mac_address = "00:16:74:76:53:43"

        print("[+] Changing the MAC Address of " + str(options.interface) + " to " + mac_address)
    else:
        print("[+] Changing the MAC Address of " + str(options.interface) + " to " + str(options.mac_address))
        mac_address = options.mac_address

    interface = options.interface

    change_mac(interface, mac_address)

    print("<---------------Copyright 2020-2100 LexiLominite242----------------->")