import math 
class Figura():
    def area():
        pass
    def perimetro():
        pass
class Triangolo(Figura):

    def __init__(self,a,b,c):
        self.lato1 = a
        self.lato2 = b
        self.lato3 = c
        

    def classificazione(self):
        if self.lato1 == self.lato2 and self.lato2 == self.lato3:
            print('IL triangolo dato dai lati {}, {}, {} è equilatero'.format(self.lato1,self.lato2,self.lato3))
        if self.lato1 == self.lato2 or self.lato1 == self.lato3 or self.lato2 == self.lato3:
            print('IL triangolo dato dai lati {}, {}, {} è isoscele'.format(self.lato1,self.lato2,self.lato3))
        else:
            print('IL triangolo dato dai lati {}, {}, {} è scaleno'.format(self.lato1,self.lato2,self.lato3))

    def perimetro(self):
        return(self.lato1+self.lato2+self.lato3)

    def area(self):
        p = (self.lato1 + self.lato2 + self.lato3)/2
   
        return math.sqrt(p*(p-self.lato1)*(p-self.lato2)*(p-self.lato3))

class Rettangolo(Figura):
    def __init__(self,a,b):
        self.lato1 = a
        self.lato2 = b

    def classificazione(self):
        if self.lato1 == self.lato2:
            print('è un quadrato')
        else:
            print('non è un quadrato')

    def perimetro(self):
        return 2*self.lato1 + 2*self.lato2

    def area(self):
        return self.lato1*self.lato2


class Cerchio(Figura):
    def __init__(self,r):
        self.r = r

    def perimetro(self):
        return 2* math.pi *self.r

    def area(self):
        return math.pi * (self.r*self.r)


def area_tot(self, *args):
    return sum([item.area() for item in args])


prova = Cerchio(7)
prova1 = Triangolo(6,6,6)
prova2 = Rettangolo(3,5)

print(area_tot(prova,prova1,prova2))