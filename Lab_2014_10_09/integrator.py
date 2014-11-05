import math

class integrator:
  #a=0,
  #b=0,
  #N=0 #poczatek i koniec przedzialu, liczba podprzedziałów
  #__init__(self):
  #  pass
  
  def __init__(self,f,a,b,N):
      self.a = a
      self.b = b
      self.N = int(N)
      self.f = f
      self.integral = 0
      self.interval = (self.b-self.a)/self.N
  
  def integrate(self):  
      pass
  
class RectIntegrator(integrator):
  
  def __init__(self,f,a,b,N):
      integrator.__init__(self,f,a,b,N)
  
  def integrate(self):
      
      x = self.a + self.interval*0.5
      for i in range(self.N):
          self.integral+=self.f(x)*self.interval
          x+=self.interval
      return round(  self.integral,int( math.log(self.N)/math.log(10) )  +3)  #zaokrąglenie do dokładności wyniku

class TrapezoidIntegrator(integrator):
  
  def __init__(self,f,a,b,N):
      integrator.__init__(self,f,a,b,N)
  
  def integrate(self):
      
      x = self.a
      for i in range(self.N):
          self.integral+=self.f(x)*self.interval
          x+=self.interval
      
      self.integral+=(self.f(self.a)+self.f(self.b))/2
      return round(  self.integral,int( math.log(self.N)/math.log(10) )  )  #zaokrąglenie do dokładności wyni

class SimpsonIntegrator(integrator):
  
  def __init__(self,f,a,b,N):
      integrator.__init__(self,f,a,b,N)
  
  def integrate(self):
      s = 0
      x = self.a
      for i in range(1,self.N+1,1):
          x += self.interval
          s += self.f(x-self.interval/2)
          if(i != self.N):
            self.integral += self.f(x)
      self.integral = ( self.interval/6 )*( self.f(self.a) + self.f(self.b) + 2*self.integral + 4*s )
      return round(self.integral,8)

class NetwonCotesIntegrator:
    
  def __init__(self,f,a,b,N):
    integrator.__init__(self,f,a,b,N)
    self.coeff_list = []
    self.divisor = 1
  
  def NewtonCotes(self,degree):
    """
    ustawia współczynniki kwadratury Newtona-Cotesa zadanego rzędu
    degree - degree of quadrature
    """
    if(degree==1):
      self.coeff_list = [1,1]
      self.divisor = 1/2
    if(degree==2):
      self.coeff_list = [1,4,1]
      self.divisor = 1/3
    if(degree==3):
      self.coeff_list = [1,3,3,1]
      self.divisor = 3/8
    if(degree==4):
      self.coeff_list = [7,32,12,32,7]
      self.divisor = 4/90
    if(degree==5):
      self.coeff_list = [19,75,50,50,75,19]
      self.divisor = 5/288
    if(degree==6):
      self.coeff_list = [41,216,27,272,27,216,41]
      self.divisor = 6/840
    self.divisor /= degree
  
  def count(self,function,a,b,coeff_list,factor):
    """
    function - funktion um integrieren zu sien
    a,b - Anfang und Ende des Intervals
    coeff_list - list den Koeffizienten des Newton-Cotes Quadratur
    """
    result = 0.
    for ii,coeff in enumerate(coeff_list):
      x = a + ((ii)*(b-a))/(len(coeff_list)-1) 
      result += coeff*function(x)
      print('{}. x: '.format(ii),x,' coeff: ',coeff,' result: ',result,' factor: ',factor)
      
    result = self.interval*factor*result
    print(result)
    return result
  
  def integrate(self,degree=4):
    self.NewtonCotes(degree)
    print('degree: ',degree)
    print('a: ',self.a)
    print('b: ',self.b)
    print('N: ',self.N)
    print('interval: ',self.interval)
    print('coeff: ',self.coeff_list,len(self.coeff_list))
    print('divisor: ',self.divisor)
    x=self.a
    self.integral=0
    for ii in range(0,self.N):
      self.integral += self.count(self.f,x,x+self.interval,self.coeff_list,self.divisor)
      print (x,self.integral)
      x +=(self.b-self.a)
    return self.integral