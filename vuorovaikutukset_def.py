def maaritys():
    vuorovaik = []
    
    vuorovaik_maara = 29
    for i in range(vuorovaik_maara + 1) :
        vuorovaik.append([])
    
    #suunnat[12].append([6,"sisaan",-1,"Mokin ovi on kiinni."])
    #suunnat[12].append([0,"sisaan",7,"Menet ovesta sisaan mokkiin."])
    #tavarat[0].append(["keppi","oksa"])
    #tavarat[0].append([2])
    #tavarat[0].append([0,True,True,"Keppi on tukeva ja noin puoli metria pitka."])
    
    # eka rivi:mitka verbit sopii, toka rivi, mitka objektit kay, kolmas rivi, missa huoneissa taman voi tehda
    # neljas rivi, mitka objektit pitaa olla missa ja missa moodeissa
    # viides rivi, printattava lause
    # kuudes rivi ja siita etaanpain, seuraukset. Suuntien muutokset alkaa merkilla "S", tavaroiden merkilla "T", suunnat ensin
    vuorovaik[0].append([3])
    vuorovaik[0].append([0])
    vuorovaik[0].append([6,7])
    vuorovaik[0].append([20,6,0])
    vuorovaik[0].append("Aukaiset oven.")
    vuorovaik[0].append(["S",12,1])
    vuorovaik[0].append(["S",13,1])
    vuorovaik[0].append(["S",15,1])
    vuorovaik[0].append(["TM",20,1])
    
    vuorovaik[1].append([4])
    vuorovaik[1].append([0])
    vuorovaik[1].append([6,7])
    vuorovaik[1].append([20,6,1])
    vuorovaik[1].append("Suljet oven.")
    vuorovaik[1].append(["S",12,0])
    vuorovaik[1].append(["S",13,0])
    vuorovaik[1].append(["S",15,0])
    vuorovaik[1].append(["TM",20,0])
    
    vuorovaik[2].append([4])
    vuorovaik[2].append([0])
    vuorovaik[2].append([6,7])
    vuorovaik[2].append([20,6,0])
    vuorovaik[2].append("Ovi on jo kiinni.")
    
    vuorovaik[3].append([3])
    vuorovaik[3].append([0])
    vuorovaik[3].append([6,7])
    vuorovaik[3].append([20,6,1])
    vuorovaik[3].append("Ovi on jo auki.")
    
    vuorovaik[4].append([8,10])
    vuorovaik[4].append([3])
    vuorovaik[4].append([-1])
    vuorovaik[4].append([21,0,0])
    vuorovaik[4].append("Kaadat pilaantuneen mehun maahan pullosta.")
    vuorovaik[4].append(["TM",21,1])
    
    vuorovaik[5].append([8,10])
    vuorovaik[5].append([3])
    vuorovaik[5].append([-1])
    vuorovaik[5].append([21,0,2])
    vuorovaik[5].append("Kaadat likaisen kuraveden pullosta maahan.")
    vuorovaik[5].append(["TM",21,1])
    
    vuorovaik[6].append([8,10])
    vuorovaik[6].append([3])
    vuorovaik[6].append([-1])
    vuorovaik[6].append([21,0,3])
    vuorovaik[6].append("Kaadat vedet maahan pullosta.")
    vuorovaik[6].append(["TM",21,1])
    
    vuorovaik[7].append([8,10])
    vuorovaik[7].append([3])
    vuorovaik[7].append([-1])
    vuorovaik[7].append([21,0,1])
    vuorovaik[7].append("Pullo on jo tyhja.")
    
    vuorovaik[8].append([9])
    vuorovaik[8].append([3])
    vuorovaik[8].append([3,4,5])
    vuorovaik[8].append([21,0,1])
    vuorovaik[8].append("Taytat pullon likaisella kuravedella ojasta.")
    vuorovaik[8].append(["TM",21,2])
    
    vuorovaik[9].append([9])
    vuorovaik[9].append([3])
    vuorovaik[9].append([3,4,5,12])
    vuorovaik[9].append([21,0,0])
    vuorovaik[9].append("Pullo on jo taynna pilaantunutta mehua. Tyhjenna se ensin.")
    
    vuorovaik[10].append([9])
    vuorovaik[10].append([3])
    vuorovaik[10].append([3,4,5,12])
    vuorovaik[10].append([21,0,2])
    vuorovaik[10].append("Pullo on jo taynna kuravetta. Tyhjenna se ensin.")
    
    vuorovaik[11].append([9])
    vuorovaik[11].append([3])
    vuorovaik[11].append([3,4,5,12])
    vuorovaik[11].append([21,0,3])
    vuorovaik[11].append("Pullo on jo taynna vetta. Tyhjenna se ensin.")
    
    vuorovaik[12].append([9])
    vuorovaik[12].append([3])
    vuorovaik[12].append([12])
    vuorovaik[12].append([21,0,1])
    vuorovaik[12].append("Taytat pullon vedella kaivosta.")
    vuorovaik[12].append(["TM",21,3])
    
    vuorovaik[13].append([9])
    vuorovaik[13].append([3])
    vuorovaik[13].append([-1])
    vuorovaik[13].append([21,0,-1])
    vuorovaik[13].append("Et voi tayttaa pulloa taalla.")
    
    vuorovaik[14].append([11])
    vuorovaik[14].append([3])
    vuorovaik[14].append([-1])
    vuorovaik[14].append([21,0,0])
    vuorovaik[14].append("Glug glug..Hik! Pilaantunut mehu oli pahaa... ja sai olosi sekavaksi..")
    vuorovaik[14].append(["TM",21,1])
    
    vuorovaik[15].append([11])
    vuorovaik[15].append([3])
    vuorovaik[15].append([-1])
    vuorovaik[15].append([21,0,1])
    vuorovaik[15].append("Pullo on tyhja, et voi juoda sita.")
    
    vuorovaik[16].append([11])
    vuorovaik[16].append([3])
    vuorovaik[16].append([-1])
    vuorovaik[16].append([21,0,2])
    vuorovaik[16].append("En oikastaan haluaisi juoda tuota likaista kuravetta..")
    
    vuorovaik[17].append([11])
    vuorovaik[17].append([3])
    vuorovaik[17].append([-1])
    vuorovaik[17].append([21,0,3])
    vuorovaik[17].append("Raikas vesi maistui hyvalta.")
    vuorovaik[17].append(["TM",21,1])
    
    vuorovaik[18].append([12])
    vuorovaik[18].append([-1])
    vuorovaik[18].append([17])
    vuorovaik[18].append([000])
    vuorovaik[18].append("Olen kuningas, en tee tuolla mitaan.")
    
    vuorovaik[19].append([12])
    vuorovaik[19].append([3])
    vuorovaik[19].append([22])
    vuorovaik[19].append([21,0,0])
    vuorovaik[19].append("Hik! Broyh! Olisit sentaan voinut tarjota jotain muuta kuin pilaantunutta mehua..")
    vuorovaik[19].append(["TM",21,1])
    
    vuorovaik[20].append([12])
    vuorovaik[20].append([3])
    vuorovaik[20].append([22])
    vuorovaik[20].append([21,0,1])
    vuorovaik[20].append("Oletkin oikea vitsiniekka! Tarjota nyt janoiselle vangille tyhjaa pulloa.")
    
    vuorovaik[21].append([12])
    vuorovaik[21].append([3])
    vuorovaik[21].append([22])
    vuorovaik[21].append([21,0,2])
    vuorovaik[21].append("Yok! Vaikka olenkin janoinen niin en silti koske tuohon kuravelliin!")
    
    vuorovaik[22].append([12])
    vuorovaik[22].append([3])
    vuorovaik[22].append([22])
    vuorovaik[22].append([21,0,3])
    vuorovaik[22].append("Voi kiitos! Tamapa maistui hyvalta.\nHei, jos onnistut loytamaan vanginvartijan piilottaman avaimen niin kerron sinulle lohikaarmeesta.")
    vuorovaik[22].append(["TM",21,1])
    
    vuorovaik[23].append([13,14])
    vuorovaik[23].append([2,4])
    vuorovaik[23].append([4])
    vuorovaik[23].append([2,0,0,3,-1,0])
    vuorovaik[23].append("Tarvitsen vasaran lisaksi jotain muuta..")
    
    vuorovaik[24].append([13,14])
    vuorovaik[24].append([2,4])
    vuorovaik[24].append([4])
    vuorovaik[24].append([2,-1,0,3,0,0])
    vuorovaik[24].append("Tarvitsen jotain milla kiinnittaa nama naulat lautoihin.")

    vuorovaik[25].append([13,14])
    vuorovaik[25].append([2,4])
    vuorovaik[25].append([4])
    vuorovaik[25].append([2,0,0,3,0,0])
    vuorovaik[25].append(["Korjaan siltaa sen verran etta siita paasee luultavasti ylitse."])
    vuorovaik[25].append(["K",4,"Olet viidakossa ojan vieressa. Ojan ylitse kulkee korjaamani silta. Voin menna etelaan ja pohjoiseen siltaa pitkin."])
    vuorovaik[25].append(["S",63,1])

    vuorovaik[26].append([15,16,17])
    vuorovaik[26].append([5])
    vuorovaik[26].append([16])
    vuorovaik[26].append([000])
    vuorovaik[26].append("Oviaukon ylapuolella olevassa kyltissa lukee 'VANKILA, SELLI 1'")
    
    vuorovaik[27].append([15,16,17])
    vuorovaik[27].append([5])
    vuorovaik[27].append([13])
    vuorovaik[27].append([000])
    vuorovaik[27].append("Kierreportaiden vieressa olevassa kyltissa lukee 'VARTIJOIDEN MAJOITUS. PAASY EHDOTTOMASTI KIELLETTY'")

    vuorovaik[28].append([3])
    vuorovaik[28].append([0])
    vuorovaik[28].append([22])
    vuorovaik[28].append([28,0,0])
    vuorovaik[28].append("Klik! vankisellin ovi on nyt auki!\nKiitos kiitos, tama oli todella mukavasti tehty!\nNo niin, seuraa minua niin johdatan sinut yhteen paikkaan..")
    vuorovaik[28].append(["S",70,0])
    vuorovaik[28].append(["S",71,0])
    vuorovaik[28].append(["S",72,0])
    vuorovaik[28].append(["S",65,0])
    vuorovaik[28].append(["TH",28,-999,0])
    vuorovaik[28].append(["HL",3])
    vuorovaik[28].append([22,"O",0,22,22,16,14,10,8,23,-1])
    vuorovaik[28].append(["HP",3,"Kiitos kun vapautit minut! Nopeasti, seuraa nyt minua niin johdatan sinut yhteen paikkaan.."])
    vuorovaik[28].append(["K",22,"Olet vankityrmassa. Vankisellin ymparilla on paksut rautakalterit. Rappuset johtavat huoneesta ylospain."])

    vuorovaik[29].append([16,17,18,19])
    vuorovaik[29].append([6])
    vuorovaik[29].append([21])
    vuorovaik[29].append([28,-1,0])
    vuorovaik[29].append("Loydat eraasta laatikosta avaimen.")
    vuorovaik[29].append(["TH",28,0])

    return vuorovaik