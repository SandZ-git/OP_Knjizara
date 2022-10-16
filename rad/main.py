import knjiga
import racun
import stavka
import art

knjiga = knjiga

bazaKnjiga = 'data/bazaKnjiga.json'
bazaRacuna = 'data/bazaRacuna.json'

lista = knjiga.ucitajListuKnjiga(bazaKnjiga)

print(art.logo)

while True:
    print("")
    print("Opcije")
    print(" 1 - Dodavanje knjiga")
    print(" 2 - Pretraga knjiga")
    print(" 3 - Prikaz svih knjiga")
    print(" 4 - Izmena knjiga")
    print(" 5 - Brisanje knjiga")
    print(" 6 - Nova prodaja")
    print(" 7 - Prikazi racun")
    print(" 0 - Izlaz")
    opcija = int(input("Unesite izbor: "))

    if opcija == 0:
        knjiga.sacuvajListuKnjiga(lista, bazaKnjiga)
        exit()
    elif opcija == 1:
        k = knjiga.inputKnjiga()
        knjiga.dodajUListu(lista, k)
        knjiga.sacuvajListuKnjiga(lista, bazaKnjiga)
    elif opcija == 2:
        pojam = input('Unesite pojam za pretragu: ')
        knjiga.nadjiKnjigu(lista, pojam)
    elif opcija == 3:
        for k in lista:
            knjiga.prikaziKnjigu(k)
    elif opcija == 4:
        sifra = input('Unesite sifru knjige: ')
        indeksKnjigeZaIzmenu = None
        for i in range(len(lista)):
            if lista[i]['sifra'] == sifra:
                indeksKnjigeZaIzmenu = i
        if indeksKnjigeZaIzmenu == None:
            print('Ne postoji takva knjiga!')
        else:
            izmenjenaKnjiga = knjiga.izmeniKnjigu(lista[indeksKnjigeZaIzmenu])
            lista[indeksKnjigeZaIzmenu] = izmenjenaKnjiga
            knjiga.sacuvajListuKnjiga(lista, bazaKnjiga)
    elif opcija == 5:
        sifra = input('Unesite sifru knjige: ')
        indeksKnjigeZaBrisanje = None
        for i in range(len(lista)):
            if lista[i]['sifra'] == sifra:
                indeksKnjigeZaBrisanje = i
        if indeksKnjigeZaBrisanje == None:
            print('Ne postoji takva knjiga!')
        else:
            del lista[indeksKnjigeZaBrisanje]
            knjiga.sacuvajListuKnjiga(lista, bazaKnjiga)
    elif opcija == 6:
        racun.prodaja(bazaRacuna, lista)
    elif opcija == 7:
        racun.prikazRacuna(bazaRacuna)
    else:
        print('Nepoznata opcija')





        
