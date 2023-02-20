if __name__ == '__main__':

#1
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    print(f"{nat.replace('FastEthernet', 'GigabitEthernet')}")

#2
    mac = "AAAA:BBBB:CCCC"
    print(f"{mac.replace(':','.')}")

#3
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    print(f"{config.split()[-1].split(',')}")

#4
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    print(f"{sorted(vlans)}")

#5
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"

    command1 = set(command1.split()[-1].split(','))
    command2 = set(command2.split()[-1].split(','))
    result = sorted(list(command1.intersection(command2)))
    print(f"{result}")
#6
    ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
    list1 = ospf_route.replace(",", "").replace("via", "").split()
    list2 = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]
    for list1, list2 in zip(list1, list2):
        print('{:20}{:20}'.format(list2, list1))

#7
    mac = "AAAA:BBBB:CCCC"
    result = bin(int(''.join(mac.split(':')), 16)).strip('0b')
    print(f'{result}')

#8
    ip = "192.168.3.1"
    oct1, oct2, oct3, oct4 = ip.split('.')
    print(f'{int(oct1):1} {int(oct2):8} {int(oct3):6} {int(oct4):8}')
    print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')