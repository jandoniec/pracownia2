import pagerank, potegowa, iteracjaprosta
import uklad, wykresy
import iteracjaseidela
import numpy as np

class z2:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        self.norma=0
        self.n=30
        self.eps=1e-10



    def testy(self):
            rank = pagerank.PageRank(self.n)
            rank.losuj(0.01)
            print(f"Srednia liczba linkow: {rank.srednia_liczba_linkow()}")
            print("\nIteracja Seidela")
            rank.przygotuj_do_iteracji()
            test1 = iteracjaseidela.IteracjaSeidela(ukl=rank.v)
            test1.przygotuj()
            iter1 = test1.iteruj_roznica(eps=self.eps,
                                        wyswietlaj=0,
                                        norma=self.norma)
            test1.wypisz_rozwiazanie(iter1)
            rank.ranking_po_iteracji(test1.X)
            niedokladnosc1 = test1.sprawdz_rozwiazanie(norma=self.norma)
            
            print("Liczba iteracji: ",iter1)
        
            print("Niedokladnosc: ", niedokladnosc1)


            print("\nMetoda Potegowa")
            uklad.Uklad.wypisz_normy_macierzy(rank.u)
            test2=potegowa.Potegowa(ukl=rank.u)
            iter2=test2.iteruj_roznica(eps=self.eps,wyswietlaj=0)
            test2.wypisz_rozwiazanie(iter2)
            
            rank.ranking(test2.y)
            print("Liczba iteracji:",iter2)
            test2.sprawdz_rozwiazanie(norma=self.norma)


    def badaj_zbieznosc(self):
        gammy=[0.01,0.1,0.2,0.25,0.3,0.4,0.5,0.55,0.6,0.7,0.8,0.9,0.95,0.99]
        
        u1 = uklad.Uklad(wymiar = self.n)

        sr_gamma1 = []
        sr_niedokladnosc1 = []
        sr_liczba_iteracji1 = []
        sr_norma_macierzy1 = []
        sr_liczba_iteracji2 = []
        sr_norma_macierzy2 = []
        sr_gamma2 = []
        sr_niedokladnosc2 = []

        for gamma in gammy:
            norma_macierzy1 = 0.0
            niedokladnosc1 = 0.0
            iteracje1 = 0
            liczba_iteracji1 = 0.0
            gamma1 = 0.0
            norma_macierzy2 = 0.0
            liczba_iteracji2 = 0.0
            gamma2 = 0.0
            niedokladnosc2 = 0.0
            
            while iteracje1 < self.k:
                pgr = pagerank.PageRank(nn=30)
                pgr.losuj(gamma)
                pgr.srednia_liczba_linkow()
                print("Metoda potegowa")
                
                test1 = potegowa.Potegowa(ukl=pgr.u)       
                
                iter1 = test1.iteruj_roznica(
                    eps = self.eps
                    )
                test1.wypisz_rozwiazanie(iter1)
                pgr.ranking(test1.y)
                niedokl1 = test1.sprawdz_rozwiazanie(self.norma)
                if iter1 == 0:
                        continue
                else:
                    norma_macierzy1 += uklad.Uklad.norma_macierzy(pgr.u,typ=self.norma)
                    gamma1 += gamma
                    niedokladnosc1 += niedokl1
                    liczba_iteracji1 += iter1
                    iteracje1 += 1
                print("Metoda Seidela")
    
                pgr.przygotuj_do_iteracji()
                test2 = iteracjaseidela.IteracjaSeidela(ukl=pgr.v)
                test2.przygotuj()        
                iter2 = test2.iteruj_roznica(
                    eps = self.eps,
                    norma = self.norma
                    )
                test2.wypisz_rozwiazanie(iter2)
                pgr.ranking_po_iteracji(test2.X)
                niedokl2 = test2.sprawdz_rozwiazanie(self.norma)
                if iter2 == 0:
                    continue
                else:
                    norma_macierzy2 += uklad.Uklad.norma_macierzy(pgr.u,typ=self.norma)
                    gamma2 += gamma
                    niedokladnosc2 += niedokl2
                    liczba_iteracji2 += iter2
            sr_norma_macierzy1.append(norma_macierzy1/self.k)
            sr_gamma1.append(gamma1/self.k)
            sr_liczba_iteracji1.append(liczba_iteracji1/self.k)
            sr_niedokladnosc1.append(niedokladnosc1/self.k)
            sr_norma_macierzy2.append(norma_macierzy2/self.k)
            sr_gamma2.append(gamma2/self.k)
            sr_liczba_iteracji2.append(liczba_iteracji2/self.k)
            sr_niedokladnosc2.append(niedokladnosc2/self.k)

        print("Metoda Potegowa")
        print("Gamma \t \t ||D|| \t     Iteracje   Niedokladnosc")
        print("------"*9)
        for i in range(len(gammy)):
            wyniki = f"{sr_gamma1[i]} \t"
            wyniki += f"{sr_norma_macierzy1[i]:.6f} \t"
            wyniki += f"{sr_liczba_iteracji1[i]:.2f} \t"
            wyniki += f"{sr_niedokladnosc1[i]:.6e} \n"
            print(wyniki)
            
        print("Metoda Seidela")
        print("Gamma \t \t ||D|| \t     Iteracje   Niedokladnosc")
        print("------"*9)
        for i in range(len(gammy)):
            wyniki = f"{sr_gamma2[i]} \t"
            wyniki += f"{sr_norma_macierzy2[i]:.6f} \t"
            wyniki += f"{sr_liczba_iteracji2[i]:.2f} \t"
            wyniki += f"{sr_niedokladnosc2[i]:.6e} \n"
            print(wyniki)