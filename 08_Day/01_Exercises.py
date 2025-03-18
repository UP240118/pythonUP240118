#1, 2, 3
dog = {}

dog = {'name':'Pelusa',
    'color':'Black',
    'breed':'House cat',
    'legs':4,
    'age':11}

student = {
    'complete_name':'Perla RUbi',
    'last_name':'Rodriguez',
    'gender':'Female',
    'age':19,
    'marital_status':'In a relationship',
    'skills':['Drawing','Teaching','Playing VD','Sing','Optimism'],
    'country':'Mexico',
    'city':'Guanajuato',
    'addres':{
        'street':'Baker Street',
        'zipcode':'NW1 6XE',
    }
}
#4, 5
print(f'La longitud es - {len(student)}')
print(f'Los datos son - {type(student["skills"])}')

#6, 7
student['skills'].append('PHP')
print(student['skills'])

keyList = list(student.keys())
print(keyList)

#8, 9
valList = list(student.values())
print(valList)

studentTuple = student.items()
print(studentTuple)

#10, 11
student.pop('gender')
print(student)

del dog, student