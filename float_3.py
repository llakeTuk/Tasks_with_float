from math import pi
y = 'y'
while y == 'y':
  volume = float(input('enter volume of sphere: '))
  radius = ((3 * volume) / (4 * pi)) ** (1/3)
  print('radius of sphere: ', radius)
  y = input('restart?(y/n): ')