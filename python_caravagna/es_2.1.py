from math import e,pi
class Funzione():
    def eval(self,x):
        pass

    def calcolo_integrale(self,a,b,M):
        h = (b-a)/M
        return h * sum([self.eval(a+i*h) for i in range(M)])
        
class Parabola(Funzione):
    def eval(self,x):
        return (x**2) - (2*x)

class Esponenziale(Funzione):
    def eval(self,x):
        return e**(2*x)

class Rapporto(Funzione):
    def eval(self,x):
        return x/(1+(x*x))




prova = Parabola()
prova1 = Esponenziale()
prova2 = Rapporto()

print(prova.calcolo_integrale(0,1,10000))
print(prova1.calcolo_integrale(-pi/2,pi,10000))
print(prova2.calcolo_integrale(-2,2,10000))






    
