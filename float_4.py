y = 'y'
while y == 'y':
  number = float(input('enter float number: '))
  if number >= 0:
    sign = 1
  else:
    sign = -1
  print(sign * int(abs(number) + 0.5))
  y = input('restart?(y/n): ')