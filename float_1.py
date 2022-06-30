def to_float(a):
  if isinstance(a, (int, float)):
    return float(a)
  else:
    return 'unable to convert'
y = 'y'
while y == 'y':
  num = input('enter number: ', )
  print(to_float(num))
  y = input('restart?(y/n): ', )
print(to_float(1754))
print(to_float(43.2))
print(to_float(False))
print(to_float('gdth'))