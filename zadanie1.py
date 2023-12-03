"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        self.eps=1e-10
        self.n=100
        self.norma=1
        self.alfa=0.3

        
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        ukl1=uklad.Uklad(10)
        ukl2=uklad.Uklad(140)

        ukl1.losuj_uklad_symetryczny_dodatnio_okreslony()
        ukl2.losuj_uklad_symetryczny_dodatnio_okreslony()

        test1=iteracjaprosta.IteracjaProsta(ukl1)
        test2=iteracjaprosta.IteracjaProsta(ukl2)

        ukl1.wypisz_normy_macierzy()
        
        test1.przygotuj()
        test2.przygotuj()

        test1.iteruj_roznica(norma=1, eps=self.eps)

        
        seria1 = test1.normy.copy()
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)

        test2.iteruj_roznica(norma=1,eps=self.eps)

        seria2 = test2.normy.copy()
        niedokl2 = test2.sprawdz_rozwiazanie(self.norma)


        wykres_test = wykresy.Wykresy()
        wykres_test.badaj_zbieznosc(
            tytul="Zbieznosc metod iteracyjnych",
            opis_OY="Normy przyblizeń",
            dane1=seria1,
            opis1="Iteracja Prosta przy mniejszym n",
            dane2=seria2,
            opis2="Iteracja Prosta przy wiekszym n"
        )
        
    def badaj_zbieznosc(self):
            """Badam zbieznosc metody iteracyjnej"""
           #miejsce na realizacje eksperymentu - drugiej czesci zadania 1
            param = [10,20,30,40,50,60,70,80,90,100,110,120,130,140]
           #param = [10,20,30,40,50,60,70,80,90,100,110,120]
           # param = [1e-13,1e-12, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2,1e-1, 1e-0, 1e1, 1e2, 1e3]
            sr_liczba_iteracji = []
            sr_norma_macierzy = []
            sr_niedokladnosc = []
            for n in param :
                u1 = uklad.Uklad(wymiar=self.n)
                norma_macierzy = 0.0
                liczba_iteracji=0.0
                niedokladnosc = 0.0
                iteracje = 0
                while iteracje < self.k:
                    u1.losuj_uklad_symetryczny_dodatnio_okreslony()
                    test1 = iteracjaprosta.IteracjaProsta(ukl=u1)
                    test1.przygotuj()
                    norma_D = u1.norma_macierzy(
                        typ=self.norma,
                        macierz=test1.D
                    )
                    iter=test1.iteruj_roznica(
                        norma = self.norma,
                        eps= self.eps
                    )
                    niedokl = test1.sprawdz_rozwiazanie(norma=self.norma)
                    if iter == 0:
                    # jezeli nie mozna bylo wykonac iteracji
                    # nalezy powtorzyc pomiar
                        continue
                    else:
                    # jezeli eksperyment udalo sie przeprowadzic
                    # agregujemy charakterystyki
                        norma_macierzy += norma_D
                        niedokladnosc += niedokl
                        liczba_iteracji += iter
                        iteracje += 1

                sr_liczba_iteracji.append(liczba_iteracji/self.k)
                sr_norma_macierzy.append(norma_macierzy / self.k)
                sr_niedokladnosc.append(niedokl / self.k)
            print("Wielkosc \nmacierzy \t \t ||D|| \t Iteracje \t   Niedokladnosc")
            print("-------" * 9)
            for i in range(len(param)):
                wyniki = f"{param[i]} \t\t\t"
                wyniki += f"{sr_norma_macierzy[i]:.6f} \t\t"
                wyniki += f"{sr_liczba_iteracji[i]:.2f} \t"
                wyniki += f"{sr_niedokladnosc[i]:.6e} \n"
                print(wyniki)
