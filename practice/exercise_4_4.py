# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

=========================================================================

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

In [28]: a = command1.split()[-1].split(',')
In [29]: b = command2.split()[-1].split(',')

In [34]: print(a)
['1', '3', '10', '20', '30', '100']

In [35]: print(b)
['1', '3', '100', '200', '300']

In [36]: set(a)
Out[36]: {'1', '10', '100', '20', '3', '30'}

In [37]: set(b)
Out[37]: {'1', '100', '200', '3', '300'}

In [38]: g = list(set(a).intersection(set(b)))

In [39]: print(g)
['100', '3', '1']

In [43]: type(g)
Out[43]: list

In [44]: g.sort()
In [47]: print(g)
['1', '100', '3']
