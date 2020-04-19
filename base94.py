#!/usr/bin/env python3

from sys import argv
from math import ceil

base = 42 
abc = '''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''

def to_base(fn_src, fn_dst, base=base):
    out_data = []

    # represent a file as a big decimal number
    with open(fn_src, 'rb') as f:
        in_data = int.from_bytes(f.read(), 'big')
    
    # convert a big decimal number to a baseN
    d, r = in_data % base, in_data // base
    out_data.append(abc[d])
    while r: 
        d, r = r % base, r // base
        out_data.append(abc[d])

    # write a result as a string to a file
    with open(fn_dst, 'wb') as f:
        f.write(''.join(out_data).encode())

def from_base(fn_src, fn_dst, base=base):
    out_data = 0

    # read one long string at once to memory
    with open(fn_src, 'rb') as f:
        in_data = f.read().decode()

    # convert a big baseN number to decimal
    for i, ch in enumerate(in_data):
        out_data = abc.index(ch)*(base**i) + out_data

    # write a big decimal number to a file as a sequence of bytes
    with open(fn_dst, 'wb') as f:
        f.write(out_data.to_bytes(ceil(out_data.bit_length()/8), 'big'))

def usage():
    print(f'usage: {argv[0]} <-e|-d> src dst [base={base}]')
    raise SystemExit(1)

def main():
    if len(argv) == 5:
        base = int(argv[4])
    elif len(argv) < 4:
        usage()

    if argv[1] not in ('-e', '-d'):
        usage()
    elif argv[1] == '-e':
        to_base(argv[2], argv[3], base)
    elif argv[1] == '-d':
        from_base(argv[2], argv[3], base)
    else:
        usage()

if __name__ == '__main__':
    main()
