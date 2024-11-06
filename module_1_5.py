immutable_var = 1, 2, 3, "string", False
print(immutable_var)
#immutable_var[4] = True
#print(immutable_var)
#В данном случае нельзя изменить значения элементов, потому что в кортеже содержатся неизменяемые данные
mutable_list = ['red', 'blue', 'black', 1, True]
print(mutable_list)
mutable_list[3] = 24
mutable_list[0] = 'yellow'
print(mutable_list)