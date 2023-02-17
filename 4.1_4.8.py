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

#7
    mac = "AAAA:BBBB:CCCC"
    result = bin(int(''.join(mac.split(':')), 16)).strip('0b')
    print(f'{result}')
#6
'''Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
 ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"'''

#8
'''Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
столбцами
ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами для разделения октетов между собой)
Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001
Ограничение: Все задания надо выполнять используя только пройденные темы.
ip = "192.168.3.1"'''