import re

phoneNumRegex = re.compile(r'\((\d\d\d)\)-\((\d\d\d-\d\d\d\d)\)') # phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') Caso o codigo de área não tenha que estar entre parenteses
mo = phoneNumRegex.search('My number is (415)-(555-4242).')
codArea, mainNum = mo.groups() # dando nome as partes do numero de telefone
if(type(mo) == re.Match):
    print(f'Fisrt: {codArea}')  # print(f'Fisrt: {mo.group(1)}')
    print(f'Second: {mainNum}')  # print(f'Second: {mo.group(2)}')
    print(f'Phone: {mo.group(0)}') # print(f'Phone: {mo.group(0)}')
else:
    print("Nao tem")

######### Existem formas melhores do que essa ##############

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
#
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print(f'Phone number found: {chunk}')
# print('Done')