class Iteratore:
    def __init__(self,n):
        self.n = n
        self.contatore = 1
        self.numero_primo = 1
       
        
    def __iter__(self):
        return self

    def primo(self,n):
        primo = True
        for i in range(2,n):
            if n%i == 0:
                primo = False
        return primo
        
    def primo_succ(self,n):
        num = n
        while not self.primo(num):
            num += 1
            
        return num
            
        
    def __next__(self):
        if self.contatore > self.n:
            raise StopIteration
        if self.numero_primo == 1:
            x = self.numero_primo
            self.numero_primo += 1
            self.contatore = self.contatore + 1
            return x
          
        x = self.numero_primo
        self.numero_primo = self.primo_succ(self.numero_primo+1)
        self.contatore = self.contatore + 1
        return x

for i in Iteratore(5):
    print(i)