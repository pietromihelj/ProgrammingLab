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
            if row != 0 and elements[0] != None and elements[1] != None:
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
        data_list = []
        numerical_data = []
        data_list = super().get_data()
        for item in data_list:
            try:
                numerical_data.append(float(item[1]))

            except ValueError:
                print('Errore')
            except TypeError:
                print('Errore')
        return numerical_data
                    
        

file = NumericalCSVFile('shampoo_sales.csv')
print(file.get_data())


                


        
        
        

        
        
    
    