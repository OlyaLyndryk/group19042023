user_name = str(input('your nickname is(only letters):'))
password = str(input('your password is:'))
contains_user_name_only_letters = user_name.isalpha()
contains_password_only_digidts_letters = password.isalnum()

if contains_user_name_only_letters and contains_password_only_digidts_letters:

    password == str(input('confirm password:'))
    if password == password:
        print('You are successful login')
        print('The user is disconnected due to the whims teacher')

        user_name_again_login = str(input('your nickname is(only letters):'))
        password_again_login = str(input('your password is:'))
        if password_again_login == password and user_name_again_login == user_name:
            print('You are successful Login')
        else:
            print('')
    else:
        print('password incorrect')
else:
    print('Login or password incorrect')



