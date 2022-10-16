

def Stavka(knjiga, kolicina):
    return {
        'knjiga': knjiga,
        'kolicina': kolicina,
    }

def jeValidan(s):
    if type(s) != dict:
        return False
    for kljuc in ['knjiga', 'kolicina']:
        if kljuc not in s.keys():
            return False
    return True

def stampaj(s):
    if not jeValidan(s):
        return False
    sirina = 50
    if len(s['knjiga']['naziv']) > sirina - 10:
        ime = s['knjiga']['naziv'][0:sirina - 13] + '...'
    else:
        ime = s['knjiga']['naziv']

    print(('{0:6s}{1:' + str(sirina - 10) + 's}{2:9d}x {3:9.2f} RSD').format(s['knjiga']['sifra'], ime, s['kolicina'], s['knjiga']['cena']))

