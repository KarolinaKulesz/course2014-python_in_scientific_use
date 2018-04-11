#!/usr/bin/env python3
key_counter = 0
def key(x):
  global key_counter
  key_counter += 1
  return -x

l = list(range(10))
print(l)
l2 = sorted(l,key=key)#sortuj od konca
print(l2)

print('funkcje key() uzyto',key_counter,'razy.')