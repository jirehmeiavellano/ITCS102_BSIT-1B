# CREATING A LIST

surname1 = 'Avellano'
surname2 = 'Cadiz'
surname3 = 'Delos Santos'

surnames = ['Avellano', 'Cadiz', 'Delos Santos', 'Claro', 'Cos', 'Balmaceda']

print(surnames)
print(surnames[0])
print(surnames[0 : 3])

surnames.append('Plata')
print(surnames)

surnames.append('Moral')
print(surnames)

surnames.insert(3, 'Navaja')
print(surnames)

surnames.pop()
print(surnames)

surnames.remove('Navaja')
print(surnames)

print(len(surnames))

surnames.sort()
print(surnames)

surnames.reverse()
print(surnames)