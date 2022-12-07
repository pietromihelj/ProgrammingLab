class Model():
    def fit(self,data):
        raise NotImplementedError('metodo non implementato')

    def predict(self,data):
         raise NotImplementedError('metodo non implementato')

class IncrementModel(Model):

    def predict(self,data):

        if not isinstance(data,list):
            raise TypeError
        if len(data) == 1:
            raise Exception('Errore, dati non sufficienti per la predizione')

        for item in data:
            if item < 0:
                raise Exception('Errore, i numeri delle vendite devono essere maggiori o uguali a zero')
        
        prev_value = data[-1]
        incremento = data[-1] - data[0]
        incremento_medio = incremento/(len(data)-1)
        prev_value = prev_value + incremento_medio
       
        return prev_value
        
    

# data1 = [50]

# file = IncrementModel()
# file.predict(data1)
# #     raise Exception('test non passato')
            