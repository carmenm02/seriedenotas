import pandas as pd
import matplotlib.pyplot as plt

class Notas():

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica


    def calculoMediaAritmetica(self):

        n = self.caracteristica.count()
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica

    def calculoMediana(self):
        mediana = 0
        caracteristica = self.caracteristica.sort_values()
        caracteristica = caracteristica.reset_index(drop=True)
        n = self.caracteristica.count()
        par = False;
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2);
            print("RANGO = "+str(rango))
            rangoPython = rango-1
            valor1 = caracteristica[rangoPython]
            valor2 = caracteristica[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = caracteristica[rangoPython]

        return [mediana, rango]
        
    def calculoModa(self):
        moda = Counter(self.caracteristica)
        return moda
