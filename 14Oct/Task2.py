def profil (kwargs):
    return dict
i = 0
while  i < 5:
    name = input('Enter name: ')
    if name == "": continue
    i = i + 1
    surname = input('Enter surname: ')
    if surname == "": continue
    i = i + 1
    age = input('Enter year: ')
    if age == "": continue
    i = i + 1
    city = input('Enter City of birth: ')
    if city == "": continue
    i = i + 1
    phone = input('Enter Phone: ')
    if phone == "": continue
    i = i + 1
    email = input('Enter Email: ')
    if email == "": continue
    dict = {'Username': name, 'Surname': surname, 'Year of birth': age, 'City': city, 'Phone': phone,
           'Email': email}
print(profil(dict))

