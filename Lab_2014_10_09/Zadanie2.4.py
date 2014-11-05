#!/usr/bin/env python3
from integrator import *

f = math.sin
print('10^N Rectangle\t\t\t\t Trapezium\t\t\t\t Simpson')
for ii in range(7):
  intg1 = RectIntegrator(f,0,math.pi,math.pow(10,ii))
  intg2 = TrapezoidIntegrator(f,0,math.pi,math.pow(10,ii))
  intg3 = SimpsonIntegrator(f,0,math.pi,math.pow(10,ii))
  print('{}.  '.format(ii),intg1.integrate(),'\t\t\t\t',intg2.integrate(),'\t\t\t\t',intg3.integrate())