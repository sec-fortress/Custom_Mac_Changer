# Custom_Mac_Changer

# Mac Changer Script

A Python script to change the MAC address of a network interface.

## Description

This script allows you to change the MAC address of a network interface on your system. It provides a list of common interfaces and prompts you to select the interface you want to modify. The script also confirms the interface using the `ifconfig` command.

## Requirements

- Python 3.x
- subprocess
- optparse
- re
- netifaces
- time

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/sec-fortress/Custom_Mac_Changer.git

3. Navigate to the Script's Directory:
   
   ```bash
   cd Custom_Mac_Changer

4. Install the required modules:
   
   ```bash
   pip install -r requirements.txt

## Usage

- Open a terminal and navigate to the script's directory.
- Run the script:

  ```bash
  python custom-macchanger.py -i <interface> -m <new_mac_address>

- Make sure to Follow the on-screen prompts, you can also use this command to see the help page:

  ```bash
  python custom-macchanger.py --help

- If none of this works, make sure to run with "sudo":
  
  ```bash
  sudo python custom-macchanger.py --help
  
- Or Switch to "root" and run:
  
  ```bash
      3/>  sudo su -  
      3/>  sudo python custom-macchanger.py -i <interface> -m <new_mac_address>
  ```

## Authors

- [OlaxD](https://sec-fortress.github.io)

## Supported Platforms

The script has been tested and confirmed to work on the following platforms:

- Kali Linux
- Ubuntu

.....And any other thing that runs linux with root priviledges.

