y = 'y'
while y == 'y':
  a, b = float(input('enter number: '), ), float(input('enter number: '))
  summ = float(input('enter sum of numbers: '))
  e = float(input('enter deviation: '))
  deviation = (e / 100) * max(abs(a), abs(b))
  if abs((a + b) - summ) <= deviation:
    print(True)
  else:
    print(False)
  y = input('restart?(y/n): ')