# 3-6 Page 42

guests = ['Mark', 'Katie', 'Lukas']
print(f'Wanna eat, {guests[0]}?')
print(f'Wanna eat, {guests[1]}?')
print(f'Wanna eat, {guests[2]}?')

guests[0] = 'Riley'

print(f'Wanna eat, {guests[0]}?')
print(f'Wanna eat, {guests[1]}?')
print(f'Wanna eat, {guests[2]}?')

print('I found a bigger table')

guests.append('Niamh')
guests.insert(0, 'Mark')
guests.insert(3, 'Cillian')

print(f'Wanna eat, {guests[0]}?')
print(f'Wanna eat, {guests[1]}?')
print(f'Wanna eat, {guests[2]}?')
print(f'Wanna eat, {guests[3]}?')
print(f'Wanna eat, {guests[4]}?')