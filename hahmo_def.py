'''

"S" stationary
"L" looppaava
"R" randomi
"O" one time polku

hahmo[x].append([22,"F")]
hahmo[4].append([26,"L",0,17,18,19,18])
hahmo[4].append([-1,"Minulla ei ole aikaa jutustella, olen kiireinen. Muista pysya poissa vartijoiden tiloista tai heitan sinut tyrmaan!"])
'''
def maaritys():
    hahmo = []
    hahmo_maara = 5
    for i in range(hahmo_maara + 1) :
        hahmo.append([])
    
    hahmo[0].append([17,"L",0,17,17,17,17,17,12])
    hahmo[0].append(["Tervehdys, muukalainen. Olen kuningas, nimeltani Toni\nOlen surullinen koska ilkea lohikaarme uhkaa valtakuntaani. Mistahan loytyisi sankari pelastamaan kansani..?\nHaluatko sina auttaa valtakuntaamme? Jos onnistut lyomaan lohikaarmeen, teen sinusta kunniaritarin!"])
    hahmo[1].append([18,"S"])
    hahmo[1].append(["Olen velho ja tiedan kaikennakoista loitsuista.\nVoin auttaa sinua taikuuden kanssa jos tuot minulle joitakin asioita ensin."])
    hahmo[2].append([19,"S"])
    hahmo[2].append(["Ilkea lohikaarme saapui valtakuntaamme ja kaikki pelkaavat sita.\nLohikaarmeella on kuitenkin heikko kohtansa, mutta mina en tieda sita..\nPuhu vangille lohikaarmeesta, han tietaa siita enemman."])
    hahmo[3].append([22,"S"])
    hahmo[3].append(["Hei, olen syyton. Minut on vangittu syyttomana, ihan oikeasti..\nJos vain tarjoat minulle juotavaa niin voin auttaa sinua."])
    hahmo[4].append([26,"L",0,21,13,15,13])
    hahmo[4].append(["Minulla ei ole aikaa jutustella, olen kiireinen. Muista pysya poissa vartijoiden tiloista tai heitan sinut tyrmaan!"])
    hahmo[5].append([30,"F"])
    hahmo[5].append(["Vuh vuh!"])

    return hahmo
