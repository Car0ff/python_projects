import sys

with open('Switches_Conf_files.txt', 'w') as f:
    sys.stdout = f

    #General Settings
    name=['IT_Network', 'MGMT_network', 'ACCT_network', 'USER_network']
    ram=['512MB','512MB','512MB', '512MB']
    vCPU=[1,1,1,1]
    qemu=['/usr/bin/qemu-system-x86_64(v4.2.1)', '/usr/bin/qemu-system-x86_64(v4.2.1)', '/usr/bin/qemu-system-x86_64(v4.2.1)', '/usr/bin/qemu-system-x86_64(v4.2.1)']
    boot_priority=['CD/DVD-ROM or HDD', 'CD/DVD-ROM or HDD', 'CD/DVD-ROM or HDD', 'CD/DVD-ROM or HDD']
    cons_type=['telnet','telnet','telnet','telnet']
    on_close=['power off the VM', 'power off the VM', 'power off the VM', 'power off the VM']
    adapters=[13,13,13,13]
    mac=['0c:1c:b2:85:00:00', '0c:cc:78:5d:00:00','0c:40:34:07:00:00','0c:e0:f2:0b:00:00']
    type_=['Realtek 8139 Ethernet(rtl8139)','Realtek 8139 Ethernet(rtl8139)', 'Realtek 8139 Ethernet(rtl8139)', 'Realtek 8139 Ethernet(rtl8139)']
    rep_net_con=[True, True, True, True]

    print('#Switches\n')

    print('\n#General Settings\n')

    for i in range(len(name)):
        print('Name: ', name[i])
        print('Ram: ', ram[i])
        print('vCPU: ', vCPU[i])
        print('Console type: ', cons_type[i])
        print('On close: ', on_close[i])
        print(' \n')   

    print('#Network Settings\n')

    for i in range(len(name)):
        print('name: ', name[i])
        print('Adapters: ', adapters[i])
        print('Base MAC: ', mac[i])
        print('Type: ', type_[i])
        print('Replicate network connection states in QEMU: ', rep_net_con[i])
        print(' \n') 

sys.stdout= sys.__stdout__