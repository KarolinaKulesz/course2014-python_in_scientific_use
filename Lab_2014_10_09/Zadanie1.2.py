#!/usr/bin/env python3
import math

integral=0
f=0
for i in range(1000000):
  f=f+2*math.pi*i/1000000
  integral=integral+math.sin(f)/1000000#calkujemy pole pod krzywa, a nie krzywa

print(integral)
print("\n")
