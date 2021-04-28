import model

PONOVNI_ZAGON = "p"
IZHOD = "i"

def izpis_igre(igra):
    tekst = f"""###############################\n
    {igra.pravilni_del_gesla()}\n
    Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()} \n
    Nepravilne črke: {igra.nepravilni_ugibi()}
    ######################################\n"""
    return tekst


def izpis_zmage(igra):
    tekst= f"""###############################\n
    Bravo! Zmagali ste! \n
    Uganili ste geslso: {igra.pravilni_del_gesla()}\n
    ###############################\n """
    return tekst


def izpis_poraza(igra):
    tekst= f"""###############################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo}\n
    ###############################\n """
    return tekst

def zahtevaj_vnos():
    return input("Vnesite črko: ")

def zahtevaj_moznost():
    return input("Vnesite moznost: ")
    
     
def ponudi_moznosti():
    tekst = f""" Vpišite črko za izbor naslednjih možnosti: \n
    {PONOVNI_ZAGON} : ponovni zagon igre \n
    {IZHOD} : izdod\n
    """
    return tekst

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            print(ponudi_moznosti())
            moznost = zahtevaj_moznost().strip.lower()
            if moznost == PONOVNI_ZAGON:
                igra = model.nova_igra()
                print(izpis_igre(igra))
            else:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            print(ponudi_moznosti())
            moznost = zahtevaj_moznost().strip.lower()
            if moznost == PONOVNI_ZAGON:
                igra = model.nova_igra()
                print(izpis_igre(igra))
            else:
                break
        else:
            print(izpis_igre(igra))


pozeni_vmesnik()