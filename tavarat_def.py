def maaritys():
    tavarat = []
    tav_maara = 30
    for i in range(tav_maara + 1) :
        tavarat.append([])

    tavarat[0].append(["keppi","oksa"])
    tavarat[0].append([2])
    tavarat[0].append([0,True,True,"Keppi on tukeva ja noin puoli metria pitka."])

    tavarat[1].append(["vakoilukamera"])
    tavarat[1].append([1])
    tavarat[1].append([0,False,True,"Vakoilukamera on kiinnitetty tiukasta puuhun."])
    
    tavarat[2].append(["vasara"])
    tavarat[2].append([7])
    tavarat[2].append([0,True,True,"Vasara on vanha ja hieman ruostunen mutta silti vahvanoloinen."])

    tavarat[3].append(["naulat"])
    tavarat[3].append([6])
    tavarat[3].append([0,True,True,"Naulakasassa on satoja nauloja."])

    tavarat[4].append(["krokotiili"])
    tavarat[4].append([3])
    tavarat[4].append([0,False,False,"Krotokotiili on pelottavan nakoinen ja iso."])

    tavarat[5].append(["mokki"])
    tavarat[5].append([6])
    tavarat[5].append([0,False,False,"Aukiolla on vanha mokki, jossa on ovi."])
    tavarat[6].append(["silta"])
    tavarat[6].append([4])
    tavarat[6].append([0,False,False,"Joen ylittava vanha silta on rikki. Silta on ehka korjattavissa, silla sen osat lojuvat tukirakenteiden vieressa."])
    tavarat[7].append(["silta"])
    tavarat[7].append([11])
    tavarat[7].append([0,False,False,"Joen ylittava vanha silta on nyt korjattu. Luulen etta sen voi ylittaa turvallisesti."])

    tavarat[8].append(["linna"])
    tavarat[8].append([8])
    tavarat[8].append([0,False,False,"Vanha ja jykeva linna nousee edessani. Linnaa kiertaa korkea muuri ja sen keskella on tukeva portti."])

    tavarat[9].append(["vuoret","vuoria"])
    tavarat[9].append([8,9,18,21])
    tavarat[9].append([0,False,False,"Vuoret nousevat niin korkealle etta niita en voi ylittaa."])
    tavarat[10].append(["mokki","rakennus"])
    tavarat[10].append([9])
    tavarat[10].append([0,False,False,"Tama mokki on eriskummallisen nakoinen. Kaikenlaisia ihmeellisia laitteita ja esineita on pihalla."])

    tavarat[11].append(["metsa"])
    tavarat[11].append([1,66])
    tavarat[11].append([0,False,False,"Metsa on sekametsa, kuusi,manty- ja koivupuita."])

    tavarat[12].append(["portti"])
    tavarat[12].append([8])
    tavarat[12].append([0,False,False,"Massiivinen portti on auki talla hetkella. Siita paasee linnaan sisaan."])

    tavarat[13].append(["patsas","patsaat","patsaita"])
    tavarat[13].append([10])
    tavarat[13].append([0,False,False,"Aulan molemmilla puolilla on 3 haarniskapatsasta. Eraan haarniskan miekka on loysasti kiinni.."])

    tavarat[14].append(["miekka"])
    tavarat[14].append([10])
    tavarat[14].append([0,False,False,"Eras miekka on kiinni patsaassa loysasti. Sen voi ehka irroittaa."])

    tavarat[15].append(["soihtu", "soihdut", "soihtuja"])
    tavarat[15].append([10])
    tavarat[15].append([0,False,False,"Suuret ja kirkkaat soihdut luovat muuten pimeaan aulaan valoa."])

    tavarat[16].append(["istuin","valtaistuin", "tuoli"])
    tavarat[16].append([17])
    tavarat[16].append([0,False,False,"Hieno ja kallis valtaistuin hallitsee huonetta. Kuningas istuu siina."])

    tavarat[17].append(["kuningas","mies","ihminen"])
    tavarat[17].append([17])
    tavarat[17].append([0,False,True,"Naet vanhan ja viisaan, mutta huolestuneen nakoisen kuninkaan valtaistuimellaan. Han on mietteliaan nakoinen."])

    tavarat[18].append(["velho", "mies", "ihminen"])
    tavarat[18].append([9])
    tavarat[18].append([0,False,True,"Naet hieman hajamielisen nakoisen velhon, jolla on pitka harmaa parta ja harmaa maahan asti ulkottuva viitta."])

    tavarat[19].append(["tiedemies","mies","ihminen"])
    tavarat[19].append([18])
    tavarat[19].append([0,False,True,"Tiedemies kiertelee kehaa linnantornissa. Hanella on kasissaan outoja mittalaitteita."])

    tavarat[20].append(["ovi"])
    tavarat[20].append([6,7])
    tavarat[20].append([0,False,False,"Ovi on kiinni.", "Ovi on auki."])

    tavarat[21].append(["pullo"])
    tavarat[21].append([7])
    tavarat[21].append([0,True,True,"Ruskeassa lasipullossa on pilaantunutta punaista mehua.", "Ruskea lasipullo on tyhja.","Ruskeassa lasipulossa on likaista vetta ojasta", "Ruskeassa lasipuloss on kirkasta vetta akaivosta."])

    tavarat[22].append(["vanki","mies","ihminen"])
    tavarat[22].append([22])
    tavarat[22].append([0,False,True,"Partainen vanki on risoissa vaatteissa ja teljettyna vankityrmaan."])

    tavarat[23].append(["kyltti"])
    tavarat[23].append([16])
    tavarat[23].append([0,False,True,"Oviaukon ylapuolella olevassa kyltissa lukee 'VANKILA'"])

    tavarat[24].append(["kaivo"])
    tavarat[24].append([12])
    tavarat[24].append([0,False,True,"Kaivossa on kierrettava mekanismi veden nostamiseksi. Vesi nayttaa kirkkaalta."])

    tavarat[25].append(["kyltti"])
    tavarat[25].append([13])
    tavarat[25].append([0,False,True,"Kierreportaiden vieressa olevassa kyltissa lukee 'VARTIJOIDEN MAJOITUS. PAASY EHDOTTOMASTI KIELLETTY'"])

    tavarat[26].append(["vartija"])
    tavarat[26].append([13])
    tavarat[26].append([0,False,True,"Vartija on raskaasti aseistautunut ja pelottavan nakoinen."])

    tavarat[27].append(["kello","kaappikello"])
    tavarat[27].append([17])
    tavarat[27].append([0,False,True,"Antiikkinen painava kaappikello on arvokkaan nakoinen."])

    tavarat[28].append(["avain"])
    tavarat[28].append([-999])
    tavarat[28].append([0,True,True,"Vartijan laatikosta loytamasi avain on hieman ruosteessa ja siina lukee 'SELLI 1'."])

    tavarat[29].append(["laatikko","laatikot","laatikosto","laatikostot"])
    tavarat[29].append([21])
    tavarat[29].append([0,False,False,"Kunkin sankyn vieressa on pieni laatikko."])

    tavarat[30].append(["koira"])
    tavarat[30].append([24])
    tavarat[30].append([0,False,True,"Leikkisa koiranpentu seuraa sinua."])

    return tavarat
