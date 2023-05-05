user_age = int(input('Enter your age (int value) >>> '))

true = True
false = False

print(bool(user_age))
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('user_age'))


if user_age < 1:
    print('incorrect input')
elif user_age == 10:
    print('You are in 4-th grade')

elif user_age >= 18:
    print('You can bay alcohol')
else:
    print('I do not know what to do')


print(user_age)


user_name = input('Enter your name >> ')

if user_name == 'John':
    print(f"Hello, {user_name}")
else:
    print('Go away')



my_string = '5555555'
print(my_string.isdigit())
number = int(my_string)
print(number)


true = True
one = 1

if true == one:
    print(888888888)


my_string = '5555555.'
if my_string.isdigit():
    number = int(my_string)
    print(number, end=' ***** ')
else:
    print('not for int')
    print(int(my_string.isdigit()))
