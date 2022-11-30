class CSVFile():
    def __init__(self,name):
        self.name = name
        try: 
            open(self.name,'r')
        except:
            print('Errore')

    def get_data(self):
        data = []
        row = 0
        vuoto = True
        my_file = open(self.name, 'r')
        
        for line in my_file:
            elements = line.split(',')
            if row != 0:
                data.append(elements)
                vuoto = False
            else:
                pass

            row = row + 1

        if vuoto:
            return data
            

        return data

class NumericalCSVFile(CSVFile):

    def get_data(self):
        data_list = super().get_data()
        numerical_data = []
        tutto_ok = True
       
        
        for item in data_list:
            numerical_row = []
            
            for i in range(len(item)):
                
                if i==0:
                   numerical_row.append(item[i])
                else:
                    try:
                        numerical_row.append(float(item[i]))
                    except Exception as e:
                        print('Errore, il valore"{}", ha creato un errore di tipo:"{}"'.format(item[i],e))
                        tutto_ok = False
                        

            if tutto_ok:
                numerical_data.append(numerical_row)
                        
        return numerical_data
                    
        



                


        
        
        

        
        
    
    