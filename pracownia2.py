"""Zbieznosc metod iteracyjnych"""

import przyklad0, zadanie, iteracyjne, zadanie1,zadanie2, nastia, z2

def testy(typ):
    if typ == 1:    
        # porownanie metod iteruj_roznica oraz iteruj_twierdzenie
        test1 = przyklad0.Przyklad0(wymiar = 100)
        test1.porownaj(1)
    elif typ == 2:
        # porownanie metod iteracji prostej i Seidela
        test2 = przyklad0.Przyklad0(wymiar = 100)
        test2.porownaj(2)
    elif typ == 3:
        # zbieznosc/rozbieznosc metod iteracyjnych
        test3 = przyklad0.Przyklad0(wymiar = 3)
        test3.badaj_zbieznosc(typ = 1, iteracje = 100)
    elif typ == 4:
        # realizacja przykladowego zadania - sprawdzamy wplyw skali wektora
        # poczatkowego na zbieznosc metody iteracji prostej
        # wykonujemy najpierw test - wybieramy 2 przykladowe wart. parametru
        test4 = zadanie.Zadanie()
        test4.testy()
        test4.badaj_zbieznosc()
    elif typ == 5:
        # realizacja przykladowego zadania - sprawdzamy wplyw skali wektora
        # poczatkowego na zbieznosc metody iteracji prostej
        # przeprowadzamy eksperyment
        test5 = zadanie.Zadanie()
        test5.badaj_zbieznosc(epsilon = 1e-10)
    elif typ == 6:
        # przyklad zastosowania metody potegowej
        test6 = iteracyjne.Iteracyjne(50)
        test6.wartosc_wlasna()
    elif typ == 7:
        # przyklad zastosowania iteracji Seidela do znalezienia rankingu
        test7 = iteracyjne.Iteracyjne(10)
        test7.page_rank_iteracja()
    elif typ == 8:
        # tutaj mozna zrealizowac zadania
        test8 = nastia.Zadanie2()
        test8.testy()
        #test8.badaj_zbieznosc()
    elif typ==9:
        test9=zadanie2.Zadanie2()
        test9.testy()
    elif typ==10:
        test10=zadanie1.Zadanie1()
        test10.testy()
        test10.badaj_zbieznosc();
    elif typ == 11:
        test11=z2.z2()
        test11.testy()
        test11.badaj_zbieznosc()
    
if __name__ == '__main__':
    testy(11)