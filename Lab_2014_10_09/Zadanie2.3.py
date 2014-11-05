#!/usr/bin/env python3
import math

def furier(furier_arg, points, f=math.sin):
    """
        Funkcja ewaluuję wartość funkcji przekazanej jako składowe
        rozbicia na szereg furiera.

        furier_arg to lista floatów które definiują współczynniki rozkładu pewnej funkcji F
        na współczynniki furiera (dla ustalenia uwagi są to współczynniki przy sinusach)
        points to list punktow dla których wartości funkcji F będą zwrócone
    """
    values=[]
    for point in points:
      value=0
      for ii,arg in enumerate(furier_arg):
        if(ii == 0):
          arg *= 0.5
        value+=arg*f(point*ii)
        
      values.append(value)
    return values


f1=furier([1,1],[0,math.pi/2])
print('Fourier z sinusami: \n',f1)
f2=furier([0,0.5],[0,math.pi/2],f=math.cos)
print('Fourier z cosinusami: \n',f2)
    