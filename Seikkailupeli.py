import hahmo_def
import verbi_def
import tavarat_def
import vuorovaikutukset_def
import objekti_def
import huoneet_def
import a_ohjeet

# eka rivi:mitka verbit sopii, toka rivi, mitka objektit kay, kolmas rivi, missa huoneissa taman voi tehda
# neljas rivi, mitka objektit pitaa olla missa ja missa moodeissa
# viides rivi, printattava lause
# kuudes rivi ja siita etaanpain, seuraukset. Suuntien muutokset alkaa merkilla "S", tavaroiden merkilla "T", suunnat ensin
#verbi[3].append(["avaa","avata"])
#objekti[0].append(["ovi"])
#vuorovaik[12].append([9])
#vuorovaik[12].append([3])
#vuorovaik[12].append([-1])
#vuorovaik[12].append([21,0,-1])
#vuorovaik[12].append("Et voi tayttaa pulloa taalla.")
#suunnat[12].append([6,"sisaan",-1,"Mokin ovi on kiinni."])
#suunnat[12].append([0,"sisaan",7,"Menet ovesta sisaan mokkiin."])
#tavarat[0].append(["keppi","oksa"])
#tavarat[0].append([2])
#tavarat[0].append([0,True,True,"Keppi on tukeva ja noin puoli metria pitka."])

def paikanna_sana(tavarat, huone, etsittava_sana):
#palauttaa 1 jos itsella, 2 jos huoneessa, 3 jos validi sana, 4 muutoin
#tavarat[9].append(["vuoret","vuoria"])
#tavarat[9].append([8,9,18,21])
#tavarat[9].append([0,False,False,"Vuoret nousevat niin korkealle etta niita en voi ylittaa."])
# returns (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi)
    (tav_indeksi, san_indeksi, pai_indeksi, koodi) = (0,0,0,4)
    for i in range(len(tavarat)):
        for j in range(len(tavarat[i][0])) :
            if etsittava_sana == tavarat[i][0][j]:  # loytyi vastaava sana
                for k in range(len(tavarat[i][1])) : # onko joku taman esineen huoneista tama huone
                    if tavarat[i][1][k] == 0:   # loytyi esine joka on itsella
                        (tav_indeksi, san_indeksi, pai_indeksi, koodi) = (i,j,k,1) # sana itsella
                    elif tavarat[i][1][k] == huone:
                        if koodi > 1:
                            (tav_indeksi, san_indeksi, pai_indeksi, koodi) = (i,j,k,2) # sana huoneessa
                    if koodi > 3: # eli kohdetta ei ole loydetty viela mistaan
                        (tav_indeksi, san_indeksi, pai_indeksi, koodi) = (i,j,k,3) # sana olemasssa kuitenkin
    return (tav_indeksi, san_indeksi, pai_indeksi, koodi)

def perus(peli_moodi, sanat, tavarat, suunnat, matriisi, huone, vuorovaik, verbi, objekti):
    onnistuiko = False
    for i in range(len(vuorovaik)):
        if peli_moodi ==2:
            print("Kaydaan lapi vuorovaikutusta",i)
        for j in range(len(vuorovaik[i][0])):
            if sanat[0] == verbi[vuorovaik[i][0][j]][0][0] :
                objektiok = False
                if peli_moodi == 2:
                    print("verbi on",verbi[vuorovaik[i][0][j]][0][0])
                    
                for k in range(len(vuorovaik[i][1])) :
                    if peli_moodi == 2:
                        print ("objekti sana on",vuorovaik[i][1][k])
                    if vuorovaik[i][1][k] == -1:		# eli objekti on mika tahansa sana joka on itsella
                        (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi) = paikanna_sana(tavarat, huone, sanat[1])
                        if koodi == 1:
                            objektiok = True
                    elif sanat[1] == objekti[vuorovaik[i][1][k]][0][0]: # objekti tasmasi
                        objektiok = True 
                    if objektiok == True:
                        if peli_moodi == 2:
                            if vuorovaik[i][1][k] == -1:
                                print("objekti on -1")
                            else:
                                print("objekti on",objekti[vuorovaik[i][1][k]][0][0])

                        for l in range(len(vuorovaik[i][2])):
                            if huone == vuorovaik[i][2][l] or vuorovaik[i][2][l] == -1 :        # oikeassa huoneessa
                                if peli_moodi == 2:
                                    print("Huone tasmasi")
                                onnistuiko = True			# jos ei olekaan yhtaan tavaraehtoa
                                for m in range(int(len(vuorovaik[i][3])/3)):
                                    tutkittavan_tavaran_indeksi = vuorovaik[i][3][m*3]
                                    
                                    if peli_moodi == 2:
                                        print("Tarkistetaan tavaraehto",m)
                                        print ("tutkittava tavara:",tutkittavan_tavaran_indeksi,"ja sen huone on:",tavarat[tutkittavan_tavaran_indeksi][1][0])
                                    sijainti=False
                                    moodi=False

                                    if (tavarat[tutkittavan_tavaran_indeksi][1][0] == vuorovaik[i][3][1+3*m]):
                                        sijainti=True
                                    if (vuorovaik[i][3][1+m*3] == -1 and tavarat[tutkittavan_tavaran_indeksi][1][0] != 0):
                                        sijainti=True
                                    if (tavarat[tutkittavan_tavaran_indeksi][2][0] == vuorovaik[i][3][2+3*m] or vuorovaik[i][3][2+m*3] == -1):
                                        moodi=True
                                    if moodi != True or sijainti != True:
                                        onnistuiko = False

                                if onnistuiko == True:
                                    if peli_moodi ==2:
                                        print("Jokaisen ehdon kaikki ehdot ok")
                                    print (vuorovaik[i][4])
                                    for n in range (len(vuorovaik[i])-5):
                                        if peli_moodi ==2:
                                            print ("toteutetaan seurausta nro:",n)
                                        if vuorovaik[i][5+n][0] == "S":
                                            suunnat[vuorovaik[i][5+n][1]][1][0]=vuorovaik[i][5+n][2]
                                            if peli_moodi ==2:
                                                print("Suunta",vuorovaik[i][5+n][1],"muutettu arvoon",vuorovaik[i][5+n][2])
                                        elif vuorovaik[i][5+n][0] == "TM":
                                            if peli_moodi ==2:
                                                print("Tavara",vuorovaik[i][5+n][1],"muutettu arvoon",vuorovaik[i][5+n][2])
 
                                            tavarat[vuorovaik[i][5+n][1]][2][0]=vuorovaik[i][5+n][2]
                                        elif vuorovaik[i][5+n][0] == "TH":
                                            if peli_moodi ==2:
                                                print("Tavaran",vuorovaik[i][5+n][1],"huone muutettu arvoon",vuorovaik[i][5+n][2])
                                            tavarat[vuorovaik[i][5+n][1]][1][0]=vuorovaik[i][5+n][2]
                                        elif vuorovaik[i][5+n][0] == "HL":
                                            muutettava_hahmo = vuorovaik[i][5+n][1]
                                            hahmo[muutettava_hahmo][0]=vuorovaik[i][6+n]
                                        elif vuorovaik[i][5+n][0] == "HP":
                                            muutettava_hahmo = vuorovaik[i][5+n][1]
                                            hahmo[muutettava_hahmo][1][0]=vuorovaik[i][5+n][2]
                                        elif vuorovaik[i][5+n][0] == "K":
                                            if peli_moodi ==2:
                                                print("Huoneen",vuorovaik[i][5+n][1],"kuvaus muutettu seuraavaksi:\n",vuorovaik[i][5+n][2])
                                            matriisi[vuorovaik[i][5+n][1]][0] = vuorovaik[i][5+n][2]
                                        else:
                                            if peli_moodi == 2:
                                                print("tata rivia ei prosessoida")
                                    return (onnistuiko, tavarat, suunnat, matriisi, huone, vuorovaik)

    return (onnistuiko, tavarat, suunnat, matriisi, huone, vuorovaik)

def nayta_tavarat(tavarat):
#tavarat[9].append(["vuoret","vuoria"])
#tavarat[9].append([8,9,18,21])
#tavarat[9].append([0,False,False,"Vuoret nousevat niin korkealle etta niita en voi ylittaa."])
    tavarat_taalla = 0
    for i in range (len(tavarat)) :
        for j in range (len(tavarat[i][1])):
            if tavarat[i][1][j] == huone and tavarat[i][2][2]:
                if tavarat_taalla == 0:
                    print("Taalla on:")
                    print (tavarat[i][0][0])
                    tavarat_taalla = 1
                else :
                    print (tavarat[i][0][0])
    
def parseri():
    lause=input("Mita haluat tehda?\n")
    sanat=lause.split(" ")
    if (sanat[0] == "p" or sanat[0] == "pohjoiseen" or sanat[0] == "pohjoinen") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("pohjoiseen")
    if (sanat[0] == "e" or sanat[0] == "etelaan" or sanat[0] == "etela") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("etelaan")
    if (sanat[0] == "l" or sanat[0] == "lanteen" or sanat[0] == "lansi") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("lanteen")
    if (sanat[0] == "i" or sanat[0] == "itaan" or sanat[0] == "itaan") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("itaan")
    if (sanat[0] == "y" or sanat[0] == "ylos" or sanat[0] == "ylospain") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("ylospain")
    if (sanat[0] == "a" or sanat[0] == "alas" or sanat[0] == "alaspain") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("alaspain")
    if (sanat[0] == "s" or sanat[0] == "sisaan" or sanat[0] == "sisalle") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("sisaan")
    if (sanat[0] == "u" or sanat[0] == "ulos") and len(sanat) ==1:
        sanat[0] ="mene"
        sanat.append("ulos")
    return sanat

def siirtyminen(huone, sanat, suunnat):
#suunnat[12].append([6,"sisaan",-1,"Mokin ovi on kiinni."])
#suunnat[12].append([0,0,7,"Menet ovesta sisaan mokkiin."])
    for i in range(len(suunnat)):
        if suunnat[i][0][0] == huone and suunnat[i][0][1] == sanat[1] : # loytyi tasmaava merkinta
            suunnan_moodi = 0       # jos ei useita siirtymisvaihtoehtoja

            if len(suunnat[i]) > 1 : # jos eri siirtymisvaihtoehtoja on enemman kuin 1
                suunnan_moodi = suunnat[i][1][0]

            if suunnat[i][suunnan_moodi][2] == -1:
                print(suunnat[i][suunnan_moodi][3])
            else:
                huone = suunnat[i][suunnan_moodi][2]
                if len(suunnat[i][suunnan_moodi]) > 3 :
                    print (suunnat[i][suunnan_moodi][3])
                else:
                    print ("Menit "+suunnat[i][suunnan_moodi][1])
            return huone
    
    print ("Et voi menna taalta "+sanat[1])
    return huone

def ota(huone,sanat, tavarat):
    if len(sanat) == 1:
        print ("Ota mita?")
        return
    (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi) = paikanna_sana(tavarat, huone, sanat[1])
    if koodi == 1:
        print("Sinulla on jo "+sanat[1]+".")
    elif koodi == 2:
        if tavarat[tavaran_indeksi][2][1] == True:
            print("Sinulla on nyt "+tavarat[tavaran_indeksi][0][0]+".")
            tavarat[tavaran_indeksi][1][0] = 0
        else:
            print("Et voi ottaa "+sanat[1]+".")
    elif koodi == 3:
        print("Taalla ei ole "+sanat[1]+".")
    else :
        print("En ymmarra mika "+ sanat[1] +" on.")
    return tavarat

def pudota(huone, sanat, tavarat):
    if len(sanat) == 1:
        print ("Pudota mita?")
        return tavarat
    (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi) = paikanna_sana(tavarat, huone, sanat[1])
    if koodi == 1:
        print("Maassa on nyt "+tavarat[tavaran_indeksi][0][0]+".")
        tavarat[tavaran_indeksi][1][0] = huone
    elif koodi == 2 or koodi == 3:
        print("Et voi pudottaa "+sanat[1]+".")
    else :
        print("En ymmarra mika "+ sanat[1] +" on.")
    return tavarat

def nayta_omat_tavarat(sanat, tavarat):
    tav_maara_itsella = 0
    for i in range(len(tavarat)):
        if tavarat[i][1][0] == 0:
            if tav_maara_itsella == 0:
                print("Sinulla on:")
                tav_maara_itsella = 1
                print(tavarat[i][0][0])
            else:
                print(tavarat[i][0][0])
        
    if tav_maara_itsella == 0:
        print("Sinulla ei ole mitaan.")

def katso(peli_moodi,sanat, tavarat, huone):
    (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi) = paikanna_sana(tavarat, huone, sanat[1])
    if koodi == 1 or koodi == 2:
        tavaran_moodi = tavarat[tavaran_indeksi][2][0]
        if peli_moodi == 2:
            print("tavaran indeksi:",tavaran_indeksi,"tavaran moodi:",tavarat[tavaran_indeksi][2][0])
        print(tavarat[tavaran_indeksi][2][tavaran_moodi + 3])
    elif koodi == 3:
        print ("En nae sita taalla.")
    else:
        print("En ymmarra mika "+ sanat[1] +" on.")
    return

def puhu(hahmo, tavarat, huone, sanat, peli_moodi):
#tavarat[9].append(["vuoria","vuoret"])
#tavarat[9].append([8,9,18,21])
#tavarat[9].append([0,False,False,"Vuoret nousevat niin korkealle etta niita en voi ylittaa."])
#hahmo[4].append([26,"L",0,17,18,19,18])
#hahmo[4].append([0,"Minulla ei ole aikaa jutustella, olen kiireinen. Muista pysya poissa vartijoiden tiloista tai heitan sinut tyrmaan!"])

    (tavaran_indeksi, sana_indeksi, sij_indeksi, koodi) = paikanna_sana(tavarat, huone, sanat[1])

    if koodi == 1 or koodi == 2:    # kohde tassa huoneessa (tai itsella!)
        for i in range(len(hahmo)):
            if peli_moodi == 2:
                print("testataan hahmoa",i)
            if hahmo[i][0][0] == tavaran_indeksi:   # voi puhua objektille
                if peli_moodi == 2:
                    print("hahmo",i,"tasmasi")
                print(hahmo[i][1][0])
                
                return hahmo
        print("En voi puhua '"+sanat[1]+"'.")
        return hahmo
    elif koodi == 3:
        for i in range(len(hahmo)):
            if hahmo[i][0][0] == tavaran_indeksi:   # voi puhua objektille mutta ei ole taalla (koodi=3)
                print("En nae hanta taalla.")
                return hahmo
        print("En voi puhua '"+sanat[1]+"'.")
        return hahmo
    else:
        print("En ymmarra mika "+sanat[1]+" on.")
        return hahmo

def npc_liikkuminen (suunnat, hahmo, tavarat, huone, peli_moodi):
    for i in range (len(hahmo)):
        if peli_moodi == 2:
            print("tarkistetaan hahmo",i)
        if hahmo[i][0][1] == "L" or hahmo[i][0][1] == "O" or hahmo[i][0][1] == "R" or hahmo[i][0][1] == "F":     # tama hahmo liikkuu 
            vanha_huone = tavarat[hahmo[i][0][0]][1][0]
            uusi_huone = vanha_huone
            huoneiden_maara = len(hahmo[i][0])-3
            if peli_moodi == 2:
                print("vanha huone",vanha_huone, "tama hahmo liikkuu ja hanen huoneiden maara on",huoneiden_maara)

            if hahmo[i][0][1] == "L" :                        # liikkuminen ennalta maarattya polkua pitkin loopissa
                hahmo[i][0][2] = hahmo[i][0][2] +1
	            
                if hahmo[i][0][2] == huoneiden_maara:
                    hahmo[i][0][2] = 0
                uusi_huone = hahmo[i][0][hahmo[i][0][2]+3]
                if peli_moodi ==2:
                    print("uusi huone",uusi_huone)
                    print("uusi indeksi hahmolle on", hahmo[i][0][2])
                tavarat[hahmo[i][0][0]][1][0] = uusi_huone
            elif hahmo[i][0][1] == "O":                       # liikkumimen vain kerran maarattya polkua pitkin
                if hahmo[i][0][2] < huoneiden_maara - 1:
                    hahmo[i][0][2] = hahmo[i][0][2] +1
                    uusi_huone = hahmo[i][0][hahmo[i][0][2]+3]
                tavarat[hahmo[i][0][0]][1][0] = uusi_huone
            elif hahmo[i][0][1] == "F":                       # NPC seuraa pelaajaa jos mahdollista
                for j in range(len(suunnat)):
                    for k in range(len(suunnat[i])):
                        if suunnat[j][k][0] == vanha_huone and suunnat[j][k][2] == huone:
                            if peli_moodi == 2:
                                print("hahmo siirtyy luoksesi")
                            tavarat[hahmo[i][0][0]][1][0] = huone 
                            uusi_huone = huone

            if vanha_huone != uusi_huone:                         # kaikkien liikkumismoodien yhteinen silmukka
                hahmon_nimi = tavarat[hahmo[i][0][0]][0][0]
                if vanha_huone == huone:
                    sana = "pois"
                    for j in range(len(suunnat)):
                        if suunnat[j][0][0] == vanha_huone and suunnat[j][0][2] == uusi_huone:
                            if sana == "pois" :
                                sana = suunnat[j][0][1]
                    print(hahmon_nimi[0].upper()+hahmon_nimi[1:]+" siirtyy taalta "+sana+".")

                elif uusi_huone == huone:
                    print(hahmon_nimi[0].upper()+hahmon_nimi[1:]+" saapuu tanne.")

    return (hahmo, tavarat)


peli_moodi = 1                       # onko wiz-moodi paalla (2) vai ei (1) (0=kuollut)
huone = 1                           # aloitushuone
ajastin = 0                          # kello

(matriisi, suunnat) = huoneet_def.maaritys()
hahmo = hahmo_def.maaritys()
verbi = verbi_def.maaritys()
tavarat = tavarat_def.maaritys()
vuorovaik = vuorovaikutukset_def.maaritys()
objekti = objekti_def.maaritys()
a_ohjeet.alkutekstit()

while peli_moodi > 0 :
    ajastin = ajastin + 1
    erikoistoiminto = False
    print("")
    huoneennro = ""
    if peli_moodi == 2 :        # WIZARD MOODI PAALLA
        huoneennro = "["+str(huone)+"]"
    
    
    print(huoneennro+matriisi[huone][0])

    (hahmo,tavarat) = npc_liikkuminen(suunnat, hahmo, tavarat, huone, peli_moodi)

    nayta_tavarat(tavarat)        

    sanat=parseri()

    (erikoistoiminto, tavarat, suunnat, matriisi, huone, vuorovaik) = perus(peli_moodi, sanat, tavarat, suunnat, matriisi, huone, vuorovaik, verbi, objekti)

    if len(sanat) > 2:
        print ("Liian monta sanaa. En ymmarra!")
    if erikoistoiminto == False:
        if(sanat[0] =="wizon"):
            print("Wizard-moodi paalla!")
            peli_moodi = 2
        elif(sanat[0] =="wizoff"):
            peli_moodi = 1
            print("Wizard moodi pois paalta")
        elif (sanat[0] == "wiz" and peli_moodi ==2):
            huone = int(sanat[1])
        # Erikoistilanteet kovakoodattuna:

        elif tavarat[26][1][0] == 21 and huone == 21:
            print("Vartija raivostuu huomatessaan sinut huoneessaan ja hyokkaa kimppuusi. Koetat puolustautua mutta pian olet sidottuna ja vartija raahaa sinut vankityrmaan!")
            huone = 22
            suunnat[70][1][0] = 1          
            suunnat[71][1][0] = 1          
            suunnat[72][1][0] = 1          
            suunnat[65][1][0] = 1          
        elif (sanat[0] == "kayta" or sanat[0] == "aseta" or sanat[0] == "laita") and sanat[1] == "keppi" and huone == 3:
            print("Tunget kepin krokotiilin suuhun pystyyn sen hyokatessa sinua kohti.")
            suunnat[1][0].remove(3)
            suunnat[1][0].insert(2,5)
            huone = 5
            tavarat[0][2].remove(0)
            tavarat[0][2].insert(1,-1)
        elif (sanat[0] == "riko" and sanat[1] == "silta" and huone == 4) or (sanat[0] == "hajota" and sanat[1] == "silta" and huone == 4):
            print("En halua rikkoa siltaa. Luulen etta sen toisella puolella on jotain mielenkiintoista.")
        elif (sanat[0] == "irrota" and sanat[1] == "miekka" and huone == 10) or (sanat[0] == "irroita" and sanat[1] == "miekka" and huone == 10):
            print("Irrotan miekan vanhan haarniskan kadesta. Haarniskasta paasee pelottava kitina, joka kaikuu linnan kaytavissa.\n")
            tavarat[16][0].remove(False)
            tavarat[16][0].remove(False)
            tavarat[16][0].insert(2,True)
            tavarat[16][0].insert(3,True)
            tavarat[16][0].remove("Eras miekka on kiinni patsaassa loysasti. Sen voi ehka irroittaa.")
            tavarat[16][0].insert(4,"Patsaalta irrottamasi miekka on vanha koristemiekka, mutta silti terava.")
        elif sanat[0] == "katso" and sanat[1] == "kello" and huone == 17:
            tunnit = 12 + int(ajastin/60)
            minuutit = ajastin % 60
            mahd_nolla = ""
            if minuutit < 10:
                mahd_nolla = "0"

            print(tavarat[27][2][3]+" Se nayttaa kellonaikaa "+str(tunnit)+":"+mahd_nolla+str(minuutit)+".")

        elif sanat[0] == "puhu" or sanat[0] == "juttele" or sanat[0] == "keskustele" or sanat[0] == "kysy":
            hahmo = puhu(hahmo, tavarat, huone, sanat, peli_moodi)
        elif sanat[0] == "mene" or sanat[0] == "kavele" or sanat[0] == "siirry":
            huone = siirtyminen(huone, sanat, suunnat)
        elif sanat[0] == "ota" :
            tavarat = ota(huone, sanat, tavarat)
        elif sanat[0] == "pudota" :
            tavarat = pudota(huone, sanat, tavarat)
        elif sanat[0] == "tavarat" or sanat[0] == "t" :
            nayta_omat_tavarat(sanat, tavarat)
        elif sanat[0] == "katso":
            if len(sanat) == 1:
                print ("Katselet ymparillesi ja huomaat, etta:")
            else:
                katso(peli_moodi, sanat, tavarat, huone)
        elif sanat[0] == "apua" or sanat[0] =="ohje" or sanat[0] =="ohjeet" :
            a_ohjeet.ohjeet()
        elif sanat[0] =="" or sanat[0] == "odota":
            print("Odotat paikallasi hetken aikaa.")
        else:
            print("En ymmarra tuota.")
        if huone == 0:
            print("Krokotiili hotkaisee sinut suuhunsa.")
            peli_moodi = 0
        
print("Peli paattyi.")

