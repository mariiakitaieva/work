if __name__ == '__main__':
#1 Float
    john_salary = 1000.5
    marta_salary = 2000.5
    print(f'john\'s salary is {john_salary}, which is a {type(john_salary)} value and marta\'s salary is {marta_salary}, which is a {type(marta_salary)} value')


#2 Integer
    john_age = 35
    marta_age = 30
    print(f'john\'s age is {john_age},which is a {type(john_age)} value and marta\'s age is {marta_age},which is a {type(marta_age)} value')


#3 String
    john_name = 'John'
    marta_name = 'Marta'
    print(f'john\'s name is {john_name},which is a {type(john_name)} value and marta\'s name is {marta_name},which is a {type(marta_name)} value')


#4 Boolean
    john_gender = False
    marta_gender = True
    print(f'john\'s gender is {john_gender}, which is a {type(john_gender)} value and  marta\'s gender is {marta_gender}, which is a {type(marta_gender)} value')


#5 List
    john_friends = ['Anna', 'Tom', 'Kevin']
    marta_friends = ['John', 'Lena', 'Adam', 'Jerry']
    print(f'{john_friends=} and {marta_friends=}')


#6 Sets
    people_names = ['Lida', 'Tom', 'Anna', 'Lida']
    print(f'{people_names} and type of this object is {type(people_names)}')
    people_names_unique = set(people_names)
    print(f'{people_names_unique} and type of this object is {type(people_names_unique)}')


#7 Tuple
    coordinates = (46.4825, 30.7233)
    print(type(coordinates), f'The latitude is {46.4825} and the longtitude is {30.7233} of the address where we live')


#8 Dictionaries
    john = {'full_name': john_name,'age': john_age, 'salary':john_salary , 'gender': john_gender,'friends': john_friends,'coordinates': coordinates}
    marta = {'full_name': marta_name,'age': marta_age, 'salary': marta_salary , 'gender': marta_gender,'friends': marta_friends,'coordinates': coordinates}
    for key, item in john.items():
        print(f"{key} => {item}")
    for key, item in marta.items():
        print(f"{key} => {item}")

#9
    tom = {'full_name': 'Tom', 'age': 40, 'salary': 3000.5, 'gender': False, 'friends': ["Lora"], 'coordinates': coordinates}
    lena = {'full_name': 'Lena', 'age': 35, 'salary': 4000.5, 'gender': True, 'friends': ["Lui", "Pavel"], 'coordinates': coordinates}

    john_friends = [tom, lena]
    marta_friends = [tom, lena]
    john = {'full_name': john_name, 'age': john_age, 'salary': john_salary, 'gender': john_gender, 'friends': john_friends,
            'coordinates': coordinates}
    marta = {'full_name': marta_name, 'age': marta_age, 'salary': marta_salary, 'gender': marta_gender,
             'friends': marta_friends, 'coordinates': coordinates}
    print(f'{john=}')
    print(f'{marta=}')
