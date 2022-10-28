import json
import stavka
import random
import knjiga
import datetime

def Racun(radnja, adresa, kasir):
    br = random.randint(10000, 99999)
    danas = datetime.datetime.now()

    return {
        'radnja': radnja,
        'adresa': adresa,
        'datum': danas.strftime('%d. %m. %Y.'),
        'kasir': kasir,
        'transakcija': br,
        'stavke': []
    }

def jeValidan(r):
    if type(r) != dict:
        return False
    for kljuc in ['radnja', 'adresa', 'datum', 'kasir', 'transakcija', 'stavke']:
        if kljuc not in r.keys():
            return False
    return True

def dodajStavku(r, s):
    if not jeValidan(r):
        return False
    r['stavke'].append(s)
    return r

def izbrisiStavku(r,s):
    r['stavke'].remove(s)

def ucitajIzDatoteke(imeDatoteke):
    try:
        dat = open(imeDatoteke, 'r')
        content = dat.read()
        if content == '':
            return[]
        lista = json.loads(content)
        dat.close()
        return lista
    except FileNotFoundError:
        return []


def sacuvajUDatoteku(lista, imeDatoteke):
    dat = open(imeDatoteke, 'w')
    json.dump(lista, dat)
    dat.flush()
    dat.close()

def stampaj(r):
    if not jeValidan(r):
        return False
    print('{0:^73s}\n{1:^73s}\n{2:^73s}\n{3:^73s}\n{4:^73s}\n'.format(r['radnja'], r['adresa'], 'Datum: ' + r['datum'], 'Kasir: ' + r['kasir'], 'Br. Transakcije: ' + str(r['transakcija'])))
    print('-'*73)
    ukupnaSuma = 0
    for i in range(len(r['stavke'])):
        stavka.stampaj(r['stavke'][i])
        ukupnaSuma += r['stavke'][i]['kolicina'] * r['stavke'][i]['knjiga']['cena']

    print('-'*73)
    print('{0:<9s}{1:>57.2f} RSD'.format('Ukupno: ', ukupnaSuma))
    print('-'*73)

def prikazRacuna(imeDatoteke):
    racuni = ucitajIzDatoteke(imeDatoteke)
    try:
        redniBroj = int(input('Unesite redni broj racuna: '))

        odgovarajuci = []

        if redniBroj > len(racuni) or redniBroj < 1:
            print('Ne postoji taj racun!')
            return

        racun = racuni[redniBroj - 1]

        stampaj(racun)

    except ValueError:
        print('Niste uneli validan broj')



def prodaja(imeDatoteke, lista):
    r = Racun('Radnja Knjizara', 'Zaplanjska 32', 'Petar Petrovic')
    
    nastavakProdaje = True

    while nastavakProdaje:
        odabranaKnjiga = knjiga.knjigaPoSifri(lista)
        if odabranaKnjiga == None:
            print('Ne postoji knjiga pod izabranom sifrom! ')
        else:
            kolicina = int(input('Koju kolicinu kupujete: '))
            if kolicina > 0 and isinstance(kolicina, int):
                s = stavka.Stavka(odabranaKnjiga, kolicina)
                dodajStavku(r, s)
            else:
                print('Nemoguca kolicina!')

        nastavak = input('Da li zelite da dodate jos jednu knjigu? Y ili N: ')

        nastavakProdaje = nastavak == 'Y'

    stampaj(r)

    def prikazi_opcija():
        print('Opcije:')
        print(' 1 - Brisanje stavke')
        print(' 2 - Cuvanje racuna')
        izabrana_opcija = int(input('Izaberite opciju: '))
        return izabrana_opcija

    izbor = prikazi_opcija()

    if izbor == 1:
        sifra = input('Unesite sifru knjige koju zelite da obrisete: ')
        indeksKnjigeZaBrisanje = None
        for i in range(len(r['stavke'])):
            if r['stavke'][i]['knjiga']['sifra'] == sifra:
                indeksKnjigeZaBrisanje = i
        if indeksKnjigeZaBrisanje == None:
            print('Ne postoji takva knjiga!')
        else:
            del r['stavke'][indeksKnjigeZaBrisanje]
        stampaj(r)
        prikazi_opcija()

    elif izbor == 2:
        racuni = ucitajIzDatoteke(imeDatoteke)
        racuni.append(r)
        sacuvajUDatoteku(racuni, imeDatoteke)

    print('Kraj prodaje!')


