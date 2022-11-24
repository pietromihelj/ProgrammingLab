def sum_csv(nome):
    values = []
    vuoto = True
    my_file = open(nome, 'r')
    for line in my_file:
        elements = line.split(',')
        try:
            if (elements[0] != 'Date' and elements[1] != None):
                vuoto = False
                values.append(float(elements[1]))                
        except ValueError:   
            pass

    my_file.close()
                
    if(vuoto):
        return None
    
    return(sum(values))
