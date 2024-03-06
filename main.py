from functions import *

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
  elif option == 1:
    add_contacts()
  elif option == 2:
    show_contacts()
  elif option == 3:
    edit_contacts()
  elif option == 4:
    favorite_contacts()
  elif option == 5:
    delete_contacts()