'''File Generator Module'''

# modify PATH variable according to the filepath you want generate files in
PATH = "./textfiles/input/input"

file_no = int(input('Enter Number of Files : '))
msg = input('Enter text : ')
print('Length of text is {}'.format(len(msg)))


def generate_files(num):
    '''Function for generating files'''
    while num:
        with open(PATH + str(num) + '.txt', 'w', encoding='utf-8') as fptr:
            fptr.write(msg)
        num -= 1
    print('Done! {} Files were created with "{}" written in each of them!'.format(file_no, msg))


ask = input('Are you sure to generate {} files? (y/N): '.format(file_no))
if ask in ('y', 'Y'): generate_files(file_no)
else: print('You chose not to generate any files!')
