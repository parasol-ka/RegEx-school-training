import re
'''Just a simple examples of how to use regex in python. Helps me to practice for my exams.'''


'------------------------------------------------------------------------'
regex_french_phone = r'0[1-9] \d{2} \d{2} \d{2} \d{2}$' # 01 23 45 67 89
french_phones = ('03 12 34 56 78', '03 12 34 56 7')

for french_phone in french_phones:
    if re.match(regex_french_phone, french_phone):
        print(f'Phone number {french_phone} is valid')
    else:
        print(f'Phone number {french_phone} is not valid\n')
'------------------------------------------------------------------------'


'------------------------------------------------------------------------'
regex_email = r'\w+@\w+\.\w+$' # exemple@exemple.com
emails = ('parasol_ka@gmail.com', 'parasol_ka@gmail')

for email in emails:
    if re.match(regex_email, email):
        print(f'E-mail {email} is valid')
    else:
        print(f'E-mail {email} is not valid\n')
'------------------------------------------------------------------------'


'------------------------------------------------------------------------'
regex_date = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$' # dd/mm/yyyy - high level of protection
regex_date2 = r'^\d{2}/\d{2}/\d{4}$' # dd/mm/yyyy - low level of protection

dates = ('30/01/2024', '30/13/2024')

print('High level of protection: \n')
for date in dates:
    if re.match(regex_date, date):
        print(f'Date {date} is valid')
    else:
        print(f'Date {date} is not valid\n')

print('Low level of protection: \n')
for date in dates:
    if re.match(regex_date2, date):
        print(f'Date {date} is valid')
    else:
        print(f'Date {date} is not valid')
'------------------------------------------------------------------------'


'------------------------------------------------------------------------'
regex_iban_be = r'^BE\d{2} \d{4} \d{4} \d{4}$' # BE00 0000 0000 0000
ibans = ('BE00 0000 0000 0000', 'BE04d 00000000 00000')

for iban in ibans:
    if re.match(regex_iban_be, iban):
        print(f'\nIBAN {iban} is valid')
    else:
        print(f'IBAN {iban} is not valid\n')
'------------------------------------------------------------------------'


'------------------------------------------------------------------------'
regex_password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{10,}$' # at least 10 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character
passwords = ('Pssword', 'Pssw0rdPssw0rd', 'P@ssw0rdP@ssw0rd')

for password in passwords:
    if re.match(regex_password, password):
        print(f'Password {password} is valid')
    else:    
        print(f'Password {password} is not valid')
'------------------------------------------------------------------------'