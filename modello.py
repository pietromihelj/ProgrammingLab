class Model():
    def fit(self,data):
        raise NotImplementedError('metodo non implementato')

    def predict(self,data):
         raise NotImplementedError('metodo non implementato')

class IncrementModel(Model):


    def media(self,data):
        somma_incrementi = 0
        prev_element = None
        
        for element in data:
            
            if prev_element is not None:
                somma_incrementi += element-prev_element
                
            prev_element = element
                
        return  somma_incrementi / (len(data)-1)
        

        
    def predict(self,data):
        #errori
        if not isinstance(data,list):        
            raise TypeError
        if len(data) == 1:
            raise Exception('Errore, dati non sufficienti per la predizione')

        for item in data:
            if item < 0:
                raise Exception('Errore, i numeri delle vendite devono essere maggiori o uguali a zero')

        #calcolo
        prev_value =  data[-1] + self.media(data)
        
        return prev_value
        
    
class FitIncrementModel(IncrementModel):
    
    def predict(self,data):
        #controlli
        if not isinstance(data,list):        
            raise TypeError
        if len(data) == 1:
            raise Exception('Errore, dati non sufficienti per la predizione')

        for item in data:
            if item < 0:
                raise Exception('Errore, i numeri delle vendite devono essere maggiori o uguali a zero')

       
        #calcolo media dei mesi precedenti
        data1 = data[:-3]
        self.media_tot = self.media(data1)

        #calcolo media ultimi 3 mesi
        data2 = data[-3:]
        media_3_mesi = self.media(data2)
            
        #previsione 
        prev_value =  data[-1] + (media_3_mesi + self.media_tot)/2      
    
        return prev_value
        

data1 = [50,52,60]
data2 = [8,19,31,41,50,52,60]
prova1 = IncrementModel()
prova2 = FitIncrementModel()


print('test 1')
if prova1.predict(data1) == 65:
    print('passato')
else:
    print('Errore, il risultato predetto è {} e non 65'.format(prova1.predict(data1)))

print('-----------')
    
print('test 2')
if prova2.predict(data2) == 68:
    print('passato')
else:
    print('Errore, il risultato predetto è {} e non 68'.format(prova2.predict(data2)))
