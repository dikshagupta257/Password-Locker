#! python3.9
#password_locker.py - password locker program


import sys,pyperclip
passwords = {'google':'abc','facebook':'def','instagram':'ghi','hackerrank':'jkl','nesoacademy':'klm','amazon':'xyz'}

if len(sys.argv) < 2:
    print('enter account name please in the format "<filename accountname>" in command prompt')
    sys.exit()

account = sys.argv[1]
if account.lower() in passwords:
    pyperclip.copy(passwords[account.lower()])
    print('The password of ',account,'is copied on clipboard')
else:
    print('Account name not stored')
