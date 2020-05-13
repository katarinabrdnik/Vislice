import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):  #če bi dali za privrezo vrednost crke=[] bi bli problemii
        self.geslo = geslo.upper()
            #self.crke naredi seznam črk v seznam velikih črk s 'pogojnim seznamom'
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

    def napacne_crke(self):
    #    seznam_napacnih_ugibanj = []
    #    for crka in crke:
    #        if crka not in geslo:
    #            NAPACNA_CRKA = crka.upper()
    #            seznam_napacnih_ugibanj += [NAPACNA_CRKA]
    #    return seznam_napacnih_ugibanj
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self, crke):
    #    seznam_pravilnih_ugibanj = []
    #    for crka in crke:
    #        if crka in geslo:
    #            PRAVILNA_CRKA = crka.upper()
    #            seznam_pravilnih_ugibanj += [PRAVILNA_CRKA]
    #    return seznam_pravilnih_ugibanj
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self, crke):
    #    seznam_napacnih_crk = napacne_crke(self, crke)
    #    i = 0
    #    for crka in seznam_napacnih_crk:
    #        i += 1
    #    return i
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

        #lahko tudi return set(self.geslo) == set(self.pravilne_crke())

        #lahko tudi s funkcijo all - preveri, ali so vsi elementi enaki
        #torej return all(crka in self.crke for crka in self.geslo)

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            s += crka if crka in self.crke else '_'
        return s
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.uppeer()
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

#ker for zanka v datoteki bere vrstice je vrstica dejansko beseda
for beseda in open('besede.txt', encoding='utf-8'):
    bazen_besed.append(beseda.strip().upper())
        #s strip se znebimo morebitnih presledkov

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)