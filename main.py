print('Welcome to your phone book.')

while True:
  print('-'*20)
  print('[1] Add contacts')
  print('[2] View list of registered contacts')
  print('[3] Edit contact')
  print('[4] Mark/unmark contact as favorite')
  print('[5] View list of favorite contacts')
  print('[6] Delete contacts')
  print('[7] Exit')

  option = int(input('> '))
  print('-'*20)

  if option == 7:
    print('Thanks for using.')
    break