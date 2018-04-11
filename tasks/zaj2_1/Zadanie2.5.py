#!/usr/bin/env python3
from integrator import *

f = math.sin
#f = lambda x : x ** 2
a = 0
b = 1
print('Kolejne rzędy , przedział{}{}'.format(a,b))
for ii in range(1,7):
  intg = NetwonCotesIntegrator(f,0,math.pi,1)
  print('wartość: ',intg.integrate(ii),'\n')