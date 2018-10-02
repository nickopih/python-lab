# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

===========================================================

In [12]: CONFIG = 'switchport trunk allowed vlan         1,3,10,20,30,100'

In [13]: CONFIG.split()
Out[15]: ['switchport', 'trunk', 'allowed', 'vlan', '1,3,10,20,30,100']

In [16]: list1 = CONFIG.split()

In [17]: print(list1)
['switchport', 'trunk', 'allowed', 'vlan', '1,3,10,20,30,100']

In [18]: list1[-1]
Out[18]: '1,3,10,20,30,100'

In [19]: list1[-1].split(',')
Out[19]: ['1', '3', '10', '20', '30', '100']

ИЛИ все все задание в одну строку:

In [21]: CONFIG = 'switchport trunk allowed vlan         1,3,10,20,30,100'

In [22]: CONFIG.split()[-1].split(',')
Out[22]: ['1', '3', '10', '20', '30', '100']


