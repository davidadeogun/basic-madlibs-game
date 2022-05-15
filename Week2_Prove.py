#Mad libs
#Basic mad libs game

print('Please enter the following: ')
print()
adjective = input('adjective: ')
animal = input('animal: ')
verb = input('verb: ') 
exclamation = input('exclamation: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
print()

print('Your story is: ') 
print()

print('The other day, I was really in trouble. It all started when I saw a very \n' + 
adjective, animal, verb + ' down the hallway."' + exclamation.capitalize() +'!"' + ' I yelled. But all \n'
'I could think to do was to ' + verb1 + ' over and over again. Mircaulously,''\n'
'that caused it to stop, but before it tried to '+ verb2 +'\n'
'right in front of my family.')

print()
first_certificate = input('first certificate: ')
first_course = input('first course: ')
print()
print(f'My first certificate is {first_certificate.title()} and my first course is\n{first_course.title()}.')
