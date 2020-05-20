import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

ZACETEK = 'S'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        #return set(self.geslo) == set(self.pravilne_crke())
        #return all(crka in self.crke for crka in self.geslo)
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            s += crka + ' ' if crka in self.crke else '_ '
        return s

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(ugibana_crka)
            if ugibana_crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []
for beseda in open('besede.txt', encoding='utf-8'):
    bazen_besed.append(beseda.strip().upper())

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)

class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0  #nekje pač mora začet, vseeno kaj bi dali
        else:
            return max(self.igre.keys()) + 1  #število večje od vseh prejšnjih se še zagotovo ni pojavilo

    def nova_igra(self):
        id_igre = self.prost_id_igre()
    #če bi tukaj klicali self.nova_igra, bi klicali metodo v tem razredu
        igra = nova_igra()  #kličemo torej funkcijo
        self.igre[id_igre] = (igra, ZACETEK)  #nova igra v začetnem stanju
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]    # s podčrtajem ponavadi označujemo spremenljivke, ki jih ne potrebujemo
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)