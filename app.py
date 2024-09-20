"""
print('Patient\'s data')
name=input('Name: ')
age=int(input('Age: '))
print('New patient named', name,'is', age,'years old')
"""

"""
print('Someone\'s favorite color')
name=input('Enter your name: ')
color=input('Enter your favorite color: ')
print(name, 'likes', color)
"""

'''
birth_year=int(input('Birth year: '))
age=2024-birth_year
print('You are', age, 'years old')
'''

'''
print('Weight Converter lbs to kgs')
weight_lbs=int(input('Insert your weight in lbs: '))
weight_kgs=int(weight_lbs*2.20462)
print('You weigh', weight_kgs, 'kgs')
'''

'''
course='Python for Beginners'
print(course.upper())
print(course.lower())
print(course==course.title())
print(course.find('o'))
print(course.replace('Beginners', 'Absolute Newbie'))
'''
'''
#augmented operator
x=10
x=x+3
print(x)
x-=3
print(x)
'''

'''
#operator precedence
x=10+3*2
print(x)
'''

'''
import math

x=2.9
print(math.ceil(x))
print(math.floor(x)) 
print(round(x))
print(abs(-x))
'''

'''
is_hot=True
is_cold=False

if is_hot:
    print('It\'s a hot day')
    print('Drink plenty of water')
elif is_cold:
    print('It\'s a cold day')
    print('Wear warm clothes')
else:
    print('It\'s a lovely day')
print('Enjoy your day')
'''

goodcredit=True
price=1000000
if goodcredit:
    percent=10
    dp=int(0.1*price)
else:
    percent=20
    dp=int(0.2*price)
print(f'You need to put down {percent}% of ${price} = ${dp}')