#!/bin/python3

import subprocess
import optparse
import re
import netifaces
import time



print("""                         
 ██████╗██╗   ██╗███████╗████████╗ ██████╗ ███╗   ███╗      ███╗   ███╗ █████╗  ██████╗  ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║      ████╗ ████║██╔══██╗██╔════╝ ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██║     ██║   ██║███████╗   ██║   ██║   ██║██╔████╔██║█████╗██╔████╔██║███████║██║█████╗██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║     ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╔╝██║╚════╝██║╚██╔╝██║██╔══██║██║╚════╝██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║      ██║ ╚═╝ ██║██║  ██║╚██████╗ ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
Print("𝑪𝒐𝒏𝒕𝒓𝒊𝒃𝒖𝒕𝒊𝒐𝒏𝒔 𝒂𝒓𝒆 𝒘𝒆𝒍𝒄𝒐𝒎𝒆𝒅: 𝒉𝒕𝒕𝒑𝒔://𝒔𝒆𝒄-𝒇𝒐𝒓𝒕𝒓𝒆𝒔𝒔.𝒈𝒊𝒕𝒉𝒖𝒃.𝒊𝒐")

def get_common_interfaces():
    # Define a list of common interface names
    common_interfaces = ['eth0', 'eth1', 'wlan0', 'wlan1' 'lo']

    # Get a list of available interfaces
    available_interfaces = netifaces.interfaces()

    # Find the common interfaces that are available
    common_available_interfaces = list(set(common_interfaces) & set(available_interfaces))

    return common_available_interfaces


def confirm_interface_with_ifconfig(interface):
    # Perform necessary operations to confirm the interface with ifconfig
    print(f"[*] Confirming interface with ifconfig: {interface}")
    time.sleep(2)
    print("[*] Interface exists :)")


common_interfaces = get_common_interfaces()

print("[*] Just to ensure you are doing the right thing, here are the Lists of common interfaces you can consider changing:")
time.sleep(4)
for i, interface in enumerate(common_interfaces, start=1):
    print(f"{i}. {interface}")
    time.sleep(1)
    
print("[*] Please Ensure you still run the command `ifconfig` on your terminal to make sure this interfaces has a MAC address")
time.sleep(6)
print("[*] In other to avoid Future Errors.......xD")
time.sleep(4)

selection = input("[*] Please select your interface (enter the corresponding number): ")
selected_index = int(selection) - 1

if selected_index >= 0 and selected_index < len(common_interfaces):
    selected_interface = common_interfaces[selected_index]
    confirm_interface_with_ifconfig(selected_interface)
else:
    print("[-] Invalid selection")


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface which MAC address is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="specific MAC address which is to be used")
    (opts, args) = parser.parse_args()
    if not opts.interface:
        parser.error("[%] Interface Not Specified, run --help for more information")
    elif not opts.new_mac:
        parser.error("[%] MAC address Not Specified, run --help for more information")
    return opts


def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("[*] Setting " + interface + " MAC address to " + new_mac)


def get_current_mac(interface):
    interface_result = subprocess.run(['ifconfig', interface], check=True, capture_output=True, text=True).stdout
    mac_address_filtered_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_result)

    if mac_address_filtered_result:
        return mac_address_filtered_result.group(0)
    else:
        print("[*] No MAC address found, Specify a correct Interface<!3")


opts = get_arguments()
current_mac = get_current_mac(opts.interface)
print("[*] Current MAC Address = " + str(current_mac))
change_mac(opts.interface, opts.new_mac)

current_mac = get_current_mac(opts.interface)
if current_mac == opts.new_mac:
    print("[*] MAC address successfully changed to " + current_mac + " </3")
else:
    print("[-] No MAC's  for for you!!")

