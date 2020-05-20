import bottle
import model

vislice = model.Vislice()  #objekt razreda Vislice

@bottle.get('/')

def index():
    return bottle.template('views/index.tpl')

#ustvarimo novo igro in jo preusmerimo na svoj naslov
@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('views/igra.tpl', id_igre=id_igre, igra=igra, stanje=stanje)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<slika>')
def pokazi_sliko(slika): 
    return bottle.static_file(slika, root='img') #vrne vsebino te datoteke

bottle.run(reloader=True, debug=True)
