# 3-7 Page 42

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

print('Nevermind, only two can come...')

guest_popped = guests.pop()
print(f"{guest_popped} you're cut")
guest_popped = guests.pop()
print(f"{guest_popped} you're cut")
guest_popped = guests.pop()
print(f"{guest_popped} you're cut")
guest_popped = guests.pop(0)
print(f"{guest_popped} you're cut")

print(guests)

del guests[0]
del guests[-1]

print(guests)