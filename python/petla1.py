#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma_parzystych():
    wynik = 0
    for i in range(0, 101, 2):
        wynik = wynik + i
    
    print(wynik)
    
def suma_nieparzystych():
    wynik = 0
    for i in range(1, 100, 2):
        wynik = wynik + i
    
    print(wynik)

def sumuj_wprowadzone():
    ile = int(input('Ile wprowadzisz liczb?: '))
    wynik = 0
    for i in range(ile):
        liczba = int(input('Podaj liczbę: '))
        wynik = wynik + liczba
        
    print(wynik)

def main(args):
    # [0, 1, 2, 3, 4]
    suma_nieparzystych()
    suma_parzystych()
    sumuj_wprowadzone()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
