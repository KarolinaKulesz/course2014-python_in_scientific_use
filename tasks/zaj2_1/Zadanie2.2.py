#!/usr/bin/env python3
def newRange(x0, xN, n):
  cus=(xN-x0)/(float)(n-1)#krok oraz rzutowanie na 'float' dzielnika- wystarczy sam dzielnik
  lista=[]
  for l in range(n):
    liczba=x0+cus*l
    lista.append(liczba)
  return lista

lista = newRange(1,10,5)
print(lista)
