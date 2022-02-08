# CS175L-50
# Vincent Tuberion
# restaurant.py
# Last Modified 2/7/2022 22:39 EST

vegetarian = ''
vegan = ''
gluten_free = ''


def boolConvert(stringVal):
    if stringVal == 'yes':
        return True
    else:
        return False


print('----WELCOME TO THE RESTAURANT SELECTOR PROGRAM----')
dataValidated = False
while not dataValidated:
    vegetarian = input('Is anyone in your party a vegetarian? (yes/no to answer)\n')
    if vegetarian == 'yes' or vegetarian == 'no':
        dataValidated = True
    else:
        print('UNKNOWN INPUT, PLEASE TRY AGAIN')

dataValidated = False
while not dataValidated:
    vegan = input('Is anyone in your party a vegan? (yes/no to answer)\n')
    if vegan == 'yes' or vegan == 'no':
        dataValidated = True
    else:
        print('UNKNOWN INPUT, PLEASE TRY AGAIN')

dataValidated = False
while not dataValidated:
    gluten_free = input('Is anyone in your party gluten free? (yes/no to answer)\n')
    if gluten_free == 'yes' or gluten_free == 'no':
        dataValidated = True
    else:
        print('UNKNOWN INPUT, PLEASE TRY AGAIN')

vegetarian = boolConvert(vegetarian)
vegan = boolConvert(vegan)
gluten_free = boolConvert(gluten_free)

print('''Here are all the restaurants on your list:
   Joe’s Gourmet Burgers
   Main Street Pizza Company
   Corner Café
   Mama’s Fine Italian
   The Chef's Kitchen\n''')
print('Here are the restaurants you may eat at under the provided conditions:')
if not (vegetarian or vegan or gluten_free):
    print('Joe’s Gourmet Burgers')
if not (vegan):
    print('Main Street Pizza Company')
print('Corner Café')
if not (vegan or gluten_free):
    print('Mama’s Fine Italian')
print('The Chef’s Kitchen')



