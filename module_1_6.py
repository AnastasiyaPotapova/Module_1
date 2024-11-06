my_dict = {'Asia':1991, 'Alex':1992, 'Kate':1995}
print(my_dict)
print(my_dict['Alex'])
my_dict['Anna'] = 1985
print(my_dict)
print(my_dict['Anna'])
my_dict.update({'Jake':1987, 'Stan':1983})
print(my_dict)
del my_dict['Asia']
print(my_dict)
my_set = {1, 2, 3, 1, 4, 'string', 3, 'string'}
print(my_set)
my_set.add(5)
my_set.add('red')
print(my_set)
my_set.discard(3)
print(my_set)