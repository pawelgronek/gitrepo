#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input('podaj bok 1: '))
    b = int(input('podaj bok 2: '))
    c = int(input('podaj bok 3: '))
    
    if a + b > c:
        if a + c > b:
            if c + b > a:
                print('boki trojkata sa prawidlowe')
                return 0
            
    print('boki trojkata sa nieprawidlowe')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
