import json

def Knjiga(sifra, naziv, autor, izdavac, zanr, ocena, cena):
    return {
        'sifra': sifra,
        'naziv': naziv,
        'autor': autor,
        'izdavac': izdavac,
        'zanr': zanr,
        'ocena': ocena,
        'cena': cena,
    }


def jeValidan(k):
    if type(k) != dict:
        return False
    for kljuc in ['sifra', 'naziv', 'autor', 'izdavac', 'zanr', 'ocena', 'cena']:
        if kljuc not in k.keys():
            return False
    return True

def inputKnjiga():
    sifra = str(input('Unesite sifru nove knjige: '))
    naziv = str(input('Unesite naziv nove knjige: '))
    autor = str(input('Unesite autora nove knjige: '))
    izdavac = str(input('Unesite izdavaca nove knjige: '))
    zanr = str(input('Unesite zanr nove knjige: '))
    ocena = provera_float('Unesite ocenu nove knjige (1 do 5): ')
    cena = provera_float('Unesite cenu nove knjige: ')
    return Knjiga(sifra, naziv, autor, izdavac, zanr, ocena, cena)

def provera_float(unos):
    nastavi = True
    while nastavi:
        x = input(unos)
        try:
            x = float(x)
            nastavi = False
            return x
        except ValueError:
            print("Uneli ste nedozvoljenu vrednost!")

def dodajUListu(lista, k):
    if not jeValidan(k):
        return False
    lista.append(k)

def prikaziKnjigu(k):
    if not jeValidan(k):
        return False
    print("{0:>8s} {1:39s} {2:32s} {3:32s} {4:32s} {5:1.2f} {6:10.2f}  RSD".format(k['sifra'],  k['naziv'], k['autor'], k['izdavac'], k['zanr'], k['ocena'], k['cena']))

def nadjiKnjigu(lista, kljucnaRec):
    n = 0
    for k in lista:
        if kljucnaRec.lower() in k['sifra'].lower() or kljucnaRec.lower() in k['naziv'].lower() or kljucnaRec.lower() in k['autor'].lower() or kljucnaRec.lower() in k['izdavac'].lower() or kljucnaRec.lower() in k['zanr'].lower():
            prikaziKnjigu(k)
            n += 1
    if n == 0:
        print("Nema pronadjenih knjiga...")

def obrisiIzListe(lista, k):
    lista.remove(k)

def izmeniKnjigu(k):
    naziv = input('Unesite novi naziv knjige ['+ k['naziv'] + ']: ')
    if naziv != '':
        k['naziv'] = naziv

    autor = input('Unesite novog autora knjige ['+ k['autor'] + ']: ')
    if autor != '':
        k['autor'] = autor

    izdavac = input('Unesite novog izdavaca knjige ['+ k['izdavac'] + ']: ')
    if izdavac != '':
        k['izdavac'] = izdavac

    zanr = input('Unesite novi zanr knjige ['+ k['zanr'] + ']: ')
    if zanr != '':
        k['zanr'] = zanr

    ocena = input('Unesite novu ocenu knjige ['+ ("{0:1.2f}".format(k['ocena'])) + ']: ')
    if ocena != '':
        k['ocena'] = float(ocena)

    cena = input('Unesite novu cenu knjige ['+ ("{0:10.2f}".format(k['cena'])) + ' RSD]: ')
    if cena != '':
        k['cena'] = float(cena)

    return k

def sacuvajListuKnjiga(lista, imeDatoteke):
    dat = open(imeDatoteke, 'w')
    json.dump(lista, dat)
    dat.flush()
    dat.close()
    print("Promene su sacuvane!")

def ucitajListuKnjiga(imeDatoteke):
    try:
        dat= open(imeDatoteke, 'r')
        content = dat.read()
        if content == '':
            return[]
        lista = json.loads(content)
        dat.close()
        return lista
    except FileNotFoundError:
        return []

def knjigaPoSifri(lista):
    sifra = input('Unesite sifru knjige: ')
    for knjiga in lista:
        if knjiga['sifra'] == sifra:
            return knjiga

