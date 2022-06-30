def average_number(num_list):
  return round(sum(num_list) / len(num_list), 5)
y = 'y'
while y == 'y':
  entered_list = input('enter list of numbers, using comma: ').split(',')
  num_list = list(map(int, entered_list))
  print('sum of elements: ', sum(num_list))
  print('amount of elements: ', len(num_list))
  print('average number: ', average_number(num_list))
  y = input('restart?(y/n): ')