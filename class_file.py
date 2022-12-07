class Errore(Exception):
    pass


class CSVFile():

    def __init__(self, name):
        self.name = name
        if type(self.name) != str:
            raise Errore('Errore, lo argomento "{}" non è una stringa'.format(
                self.name))
        try:
            open(self.name, 'r')
        except Exception as e:
            print('Errore, lo argomento "{}" da un errore di tipo"{}""'.format(
                name, e))

    def get_data(self, start=None, end=None):
        data = []
        tutto_ok = True
        my_file = open(self.name, 'r')

        my_file = my_file.readlines()
        lunghezza_file = len(my_file)
       

        if start is None:
              start = 1

        if end is None:
            end = lunghezza_file

        try:
            controllo_start = float(start)
            controllo_end = float(end)
            start = int(start)
            end = int(end)
            if start == controllo_start and end == controllo_end:
                
                if start > end:
                    raise Errore('Errore, i dati start:"{}" e end:"{}" non vanno bene. end deve essere maggiore di start'.format(start,end))

                if start < 0:
                    raise Errore('Errore, il dato start:"{}" o il dato end:"{}" non va bene perche minore di 0'.format(start,end))

                if end > lunghezza_file:
                     raise Errore('Errore, il dato start:"{}" o il dato end "{}" sono fuori dalla lunghezza della lista'.format(start,end))

        except Exception as e:
            print('Errore, il parametro start:"{}" o il parametro end:"{}" creano un errore di tipo: "{}"'.format(start,end,e))
            tutto_ok = False

        if tutto_ok:
            row = 0
            for row, line in enumerate(my_file):
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if row >= start-1 and row-1 <= end and row:
                    data.append(elements)

        return data


class NumericalCSVFile(CSVFile):

    def get_data(self, *args, **kwargs):
        data_list = super().get_data(*args,**kwargs)
        numerical_data = []
        tutto_ok = True

        for item in data_list:
            numerical_row = []

            for i in range(len(item)):

                if i == 0:
                    numerical_row.append(item[i])
                else:
                    try:
                        numerical_row.append(float(item[i]))
                    except Exception as e:
                        print(
                            'Errore, il valore"{}", ha creato un errore di tipo:"{}"'
                            .format(item[i], e))
                        tutto_ok = False

            if tutto_ok:
                numerical_data.append(numerical_row)

        return numerical_data
