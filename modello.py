class Model():
    def fit(self,data):
        raise NotImplementedError('metodo non implementato')
        
    def predict(self,data):
         raise NotImplementedError('metodo non implementato')

    def evaluate(self,data,n):
        diff = []
        for i in range(len(data)-n):
            diff.append(abs(data[n+2]-self.predict(data[i:n+i])))

        return sum(diff)/len(diff)
        

class IncrementModel(Model):
    
    def __media__(self,data):
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
            try:
                float(item)
            except TypeError:
                raise Exception('lo elemento {} non è un numero'.format(item))
            if item < 0:
                raise Exception('Errore, i numeri delle vendite devono essere maggiori o uguali a zero')
            

        #calcolo
        prev_value =  data[-1] + self.__media__(data)
        
        return prev_value
        
    
class FitIncrementModel(IncrementModel):
    def fit(self,data):
         #self.media_tot = self.__media__(data[:-3])
        pass
    def predict(self,data):
        #controlli
        if not isinstance(data,list):        
            raise TypeError
        if len(data) < 3:
            raise Exception('Errore, dati non sufficienti per la predizione')

        for item in data:
            try:
                float(item)
            except TypeError:
                raise Exception('lo elemento {} non è un numero'.format(item))
            if item < 0:
                raise Exception('Errore, i numeri delle vendite devono essere maggiori o uguali a zero')
        self.media_tot = self.__media__(data[:-3])
        media_3_mesi = self.__media__(data[-3:])
        #previsione 
        prev_value =  data[-1] + (media_3_mesi + self.media_tot)/2
    
        return prev_value
        
        

#from class_file.py import NumericalCsvFile

#data = NumericalCsvFile('shampoo_sales.csv')
#data1 = data.getdata()
data1 = [8,19,31,41,50,52,60,67,72,72,67,72,77,81,85]
prova1 = FitIncrementModel()
prova2 = IncrementModel()

fitdata = data1[:6]
evaluedata = data1[6:]

prova1.fit(fitdata)

print(prova1.evaluate(evaluedata,3))
print(prova2.evaluate(evaluedata,3))
