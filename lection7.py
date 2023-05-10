# try_exept.py
# number_1 = 1
# number_2 = '5'
#
# # if number_2 != 0:
# #     division_result = number_1 / number_2
# # else:
# #     division_result = 0
# # print(division_result)
#
#
# # try:
# #     division_result = number_1 / number_2
# #     int('10.0')
# #
# # except ZeroDivisionError:
# #     print('division on zero')
# # except (TypeError, ValueError):
# #     print('type error or value error')
# #     # raise ArithmeticError
# # else: ###work if there were no errors
# #     print('All right')
# # finally: ####work veery time try run
# #     division_result = 55555
# #     print('close file')
# #
# # print(division_result)
#
#
#
#
# #####set_theme.py
# set1 = set()
# print(set1)
#
# set2 = {5, 6, 6, 6, 'jj', 'k', 5.5, 7., True}
# # print(set2)
# # print(len(set2))
# #
# #
# # cities = ['Kyiv' 'Kyiv' 'London']
# # unique_cities = set(cities)
# # print(unique_cities)
# #
# # unique_letters = set('London 1')
# # print(unique_letters)
# #
# # letters = list
#
# cities = ['Kyiv' 'Kyiv' 'London']
# unique_cities = set(cities)
# print(unique_cities)
# ...
# unique_cities.add('Paris')
# unique_cities.add('Paris')
# print(unique_cities)
# unique_cities.update('abc')
# print(unique_cities)
# unique_cities.remove('a')     ###raise error if no element
# print(unique_cities)
# # data = unique_cities.pop()
# # print(data, unique_cities)
# unique_cities.discard('a')     ###doesen't raise error if no element
# print(unique_cities)

######common elements
# set1 = {1, 2, 3}
# set2 = {4, 2, 3}
# new_set_common = set1.intersection(set2)
# print(new_set_common)
# new_set_common_3_10_and_high  = set1 & set2
# print(new_set_common_3_10_and_high)
# print(new_set_common == new_set_common_3_10_and_high)


# words = input('enter your text >>>> ')
# print(words)
# words = set(input('enter your text >>>> '))
# print(words)
# words = set(input('enter your text >>>> ')).upper().raplace('(', ' '
#             ).replace(',', ' ')
# print(words)

#######union elements
# set1 = {1, 2, 3}
# set2 = {4, 2, 3}
# new_set_union = set1.union(set2)
# print(new_set_union)
# new_set_union_3_10_and_high  = set1 | set2
# print(new_set_union_3_10_and_high)
#
# ######difference elements
# set1 = {1, 2, 3}
# set2 = {4, 2, 3}
# new_set_dif = set1 - set2
# print(new_set_dif)
# new_set_dif_3_10_and_high  = set1 & set2
# print(new_set_dif = set1 ^ ..............................





###########dict
# person = {}
# person = dict {}
# person = {
#      'name': 'John',
#      'hobbies': [
#          'tennis',
#          'darts',
#      ],
#      'age': 12,
# }
#
# person = dict(name='John', hobbies=['tennis', 'darts'], age=12)
# pass


# ###keys
wish1_list = ['name', 'hobbies', 'age']
wish2_list = ['name', 'IBAN', 'age', 'address']

wish1 = set(wish1_list)
wish2 = set(wish2_list)

person = dict.fromkeys(wish1 | wish2, None)


hobbies = [
         'tennis',
         'darts',
],

name = 'John1'
person['name'] = 'John'
person['age'] = 12
person['hobbies'] = 'hobbies'
person['adresse'] = 'Baker Street'
person['name'] = 'jack'


print(person['name'].title())
person(person['hobbies'][:2])
print(person.get('surname', '').title())
