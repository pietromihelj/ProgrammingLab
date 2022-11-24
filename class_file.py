class CSVFile():
    def __init__(self,name):
        self.name = name

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
            

                


        
        
        

        
        
    
    