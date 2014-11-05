# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
   # print(x<stop)
    x=start_stop
    if step==None:
	    step=1
    if stop=="None":
	    while True:
		    x=x+step
		    print (x)
		    yield x
    else:
	    while x<stop:
		    x=x+step
		    yield x
	    
	    
print(list(xrange(2,15,2)))#przez print nie tworzy sie referencja;
print(list(xrange(2,15,)))

