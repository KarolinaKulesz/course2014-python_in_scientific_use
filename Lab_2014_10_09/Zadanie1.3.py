#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt

ile_liczb=math.ceil(2*math.pi/math.pow(10,-5))
ile_liczb=(round(ile_liczb))
print (type(ile_liczb))
tablica=[]
sinusy=[]
liczba=0
i=0
slownik={0:0}
f=open('slownik.txt', 'w')
while (i<ile_liczb):
  liczba=liczba+math.pow(10,-5)
  tablica.append(liczba)
  sin=math.sin(liczba)
  sinusy.append(sin)
  slownik[liczba]=sin
  #f.write("%s\n" % liczba)
  #print>>f, liczba
  i=i+1
plt.plot(tablica,sinusy)
plt.show()
#f.close()

