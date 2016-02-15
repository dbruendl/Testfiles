__author__ = 'Daniel Bruendl'
import csv

class csv_rw(object):

    def __init__(self, file):
        self.file = file
        self.liste = []

    """
    Die Funktion readf oeffnet ein .csv file
    und liest dann jede einzelne Reihe aus die in diesem csv File steckt

    Die verschiedensten Dialekte koennen hier eingelesen werden von , bis tabulator ; leertaste : und |
    """
    def readf(self,filename):
        with open(filename, 'r') as csvf:
            try:
                dialect = csv.Sniffer().sniff(csvf.read(), [',', '\t', ';', ' ', ':', '|'])
            except:
                dialect = None

            csvf.seek(0)
            gelesen = csv.reader(csvf, dialect)

            for n in gelesen:
                self.liste.append(n)

        return self.liste

    """
    Die Funktion writef oeffnet ein File und gibt dem User durch den zweiten Parameter w schreibrechte.
    Kann auch benutzt werden um zeilen hinzuzufuegen
    Erstellt ausserdem ein neues File wenn es noch nicht existiert

    Die verschiedensten Dialekte koennen hier eingelesen werden
    """
    def writef(self,filename):
        with open(filename, 'w') as csvf:
            schreib = csv.writer(csvf)
            schreib.writerows(self.liste)







csvfile = csv_rw("ergebnisse.csv")
csvfile.readf("ergebnisse.csv")
csvfile.writef("test.csv")
csvfile.readf("test.csv")
csvfile.writef("test.csv")

