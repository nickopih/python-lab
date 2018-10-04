# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

=====================================================================================

In [13]: ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [72]: c = ospf_route.replace(',','').split()

In [73]: c
Out[73]: 
['O',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3',
 '3d18h',
 'FastEthernet0/0']

In [74]: c.remove('O')

In [78]:  c.insert(0, 'OSPF')

In [79]: c
Out[79]: 
['OSPF',
 '10.0.24.0/24',
 '[110/41]',
 'via',
 '10.0.13.3',
 '3d18h',
 'FastEthernet0/0']

In [82]: protocol, prefix, metric_ad, nh, last_update, oi = c[0], c[1], c[2], c[4], c[5], c[6]

In [93]: show_route = '''
    ...: Protocol:              {}
    ...: Prefix:                {}
    ...: AD/Metric:             {}
    ...: Next-Hop:              {}
    ...: Last update:           {}
    ...: Outbound Interface:    {}
    ...: '''


In [95]: print(show_route.format(protocol, prefix, metric_ad, nh, last_update, oi))

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             [110/41]
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0


