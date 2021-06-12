import os
import sys

OFFSET = 292
ar = os.listdir()
arr=[]

for file in ar:
    if 'PGTA' in file:
        arr.append(file)

def convert(name):
    with open(name, 'rb') as in_file:
        with open(name + '.jpg', 'wb') as out_file:
            out_file.write(in_file.read()[OFFSET:])


def main():
    for name in arr:
        if os.path.isfile(name):
            convert(name)
        else:
            print('WARNING: {} is not a file'.format(name), file=sys.stderr)


if __name__ == '__main__':
    main()