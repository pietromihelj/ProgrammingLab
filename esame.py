class ExamException(Exception):
     pass

class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name = name
        if type(self.name) != str:
            raise ExamException('Errore, lo argomento "{}" non è una stringa'.format(
                self.name))

    def get_data(self):
        #controllo apurtura file
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except:
            raise ExamException('Errore, file inesistente o illegibile')
        #estrazione dei dati e trasformazione del file in una lista di liste dove ogni sottolista rappresenta una riga del file
        row_data = []
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()

            if elements[0] != 'epoch':
                row_data.append(elements)
        #creazione della lista di liste composta solo da epoch e temperature   
        numerical_data = [] 
        last_epoch = None
        for item in row_data:
            numerical_element = []
            for i in range(len(item)):
                #controllo se l'elemento è un numero
                isnumber = True
                try:
                    if item[i] is True:
                        isnumber = False
                    if item[i] is False:
                        isnumber = False
                    item[i] = float(item[i])
                except:
                    isnumber = False
                if isnumber:
                    #controllo se l'elemento è un epoch o una temperatura
                    if item[i] > 100:
                        #controllo dell'ordine degli epoch o di duplicati
                        if last_epoch is None:
                            last_epoch = item[i]
                        else:
                            if last_epoch >= item[i]:
                                raise ExamException('Errore, lista non ordinata o con duplicati')
                            else:
                                #aggiunta dell'epoch alla sottolista
                                numerical_element.append(int(item[i]))
                                last_epoch = item[i]
                    #aggiunta della temperatura alla sottolista
                    else:
                        
                        numerical_element.append(item[i])
                else:
                    pass
            #controllo che la sottolista abbia 2 valori e nel caso la aggiungo alla lista
            if len(numerical_element) == 2:
                numerical_data.append(numerical_element)
            #se non li ha suppongo ci siano stati errori e salto la riga in questione
            else:
                pass

        return numerical_data    
                
                    
            
        
    
    



def compute_daily_max_difference(dataset):
    diff_temp = []
    tmax = None
    tmin = None
    day_start = None
    tmp_count = 1
    day_count = 1
    
    #controllo che la lista dataci sia corretta
    controll_dataset = dataset
    for item in controll_dataset:
        #controllo che la lista sia riempita con sottoliste corrette
        if len(item) != 2:
            raise ExamException('Errore, la lista inserita non è corretta')
        else:
            for i in range(len(item)):
                isnumber = True
                try:
                    if item[i] is True:
                        isnumber = False
                    if item[i] is False:
                        isnumber = False
                    item[i] = float(item[i])
                except:
                    isnumber = False
            if not isnumber:
                raise ExamException('Errore, valori non numerici nella lista')
    
    for item in dataset:
        #se è la prima temperatutra inizializzo la prima temperatura del primo giorno
        if day_start == None:
            day_start = int(item[0] / 86400)
            tmin = item[1]
            tmax = item[1]
            
        else:
            #controllo se la temperatura appartiene al giorno corrente
            if int(item[0] / 86400) == day_start:
                
                #se è cosi controllo se questa possa essere la minima o la massima e nel caso sostituisco
                if item[1] < tmin:
                    tmin = item[1]
                if item[1] > tmax:
                    tmax = item[1]
                #aumento di 1 il numero di temperature prese nella giornata
                tmp_count = tmp_count + 1
            else: 
                #se la temperatura non appartiene al giorno corrente aggiorno il giorno
                day_start = int(item[0] / 86400)
                day_count = day_count + 1
                #controllo quanti rilevamenti ci sono stati, se è 1 solo aggiungo None alla lista delle differenze di temperatura se sono più di uno aggiungo la differenza massima
                if tmp_count == 1:
                    diff_temp.append(None)
                else:
                    diff_temp.append(tmax-tmin)
                #aggiorno il contatore e le temperatura massime e minime della giornata
                tmp_count = 1
                tmax = item[1]
                tmin = item[1]
    
    if day_count == 1:
        diff_temp.append(tmax-tmin)
    return diff_temp

