def maaritys():
    matriisi = []
    suunnat = []
    
    suunnat_max = 79
    huoneet_max = 24
    for i in range(huoneet_max +1) :        # huoneiden maksimimaara (eli suurin indeksi +1)
        matriisi.append([])
    
    for i in range(suunnat_max+1):         # tavaroiden maksimimaara (eli suurin indeksi +1)
        suunnat.append([])
        
    matriisi[0].append("Olet kuollut")
    suunnat[0].append([0,"p",0])
    
    matriisi[1].append("Olet kuusimetsassa. Voit menna taalta polkua pitkin pohjoiseen P ja lanteen L seka etelaan E")
    suunnat[1].append([1,"pohjoiseen",3])
    suunnat[2].append([1,"etelaan",6])
    suunnat[3].append([1,"lanteen",2])
    
    matriisi[2].append("Olet aavikolla. Hiekkadyynia jatkuvat silmankantamattomiin enka uskalla lahtea niita ylittamaan.\Voit menna vain itaan (I).")
    suunnat[4].append([2,"itaan",1])
    suunnat[62].append([2,"lanteen",-1,"Aavikko jatkuu silmankantamattomiin, en uskalla lahtea harhailemaan sinne."])
    suunnat[64].append([2,"pohjoiseen",-1,"Aavikko jatkuu silmankantamattomiin, en uskalla lahtea harhailemaan sinne."])
    suunnat[14].append([2,"etelaan",-1,"Aavikko jatkuu silmankantamattomiin, en uskalla lahtea harhailemaan sinne."])
    
    matriisi[3].append("Olet viidakossa. Kulkemasi polun katkaisee oja, jossa on krokotiili. Voit menna pohjoiseen (P) krokotiilin ohi tai etelaan (E)")
    suunnat[5].append([3,"pohjoiseen",0])
    suunnat[6].append([3,"etelaan",1])
    
    matriisi[4].append("Olet viidakossa ojan vieressa. Ojan ylitse menee rikkinainen silta, joka estaa kulkusi pohjoiseen. Voit menna nyt vain etelaan (E)")
    suunnat[7].append([4,"etelaan",5])
    suunnat[63].append([4,"pohjoiseen",-1,"En uskalla ylittaa siltaa, se on riski. Ehka voisin korjata sen oikeilla tyokaluilla.."])
    suunnat[63].append([0,"pohjoiseen",8,"Kuljen varovaisesti korjaamani siltaa pitkin pohjoiseen."])
    
    matriisi[5].append("Olet viidakossa. Kulkemasi polun katkaisee oja, jossa on krokotiili. Krokotiilin suussa on keppi poikittain. Voit menna pohjoiseen (P) krokotiilin ohi tai etelaan (E)")
    suunnat[8].append([5,"pohjoiseen",4])
    suunnat[9].append([5,"etelaan",1])
    
    matriisi[6].append("Olet saapunut metsanlaitaan. Lahella metsaa on pieni ransistynyt mokki. Voit menna pohjoiseen (P) seka mokkiin sisalle (S)")
    suunnat[10].append([6,"pohjoiseen",1])
    suunnat[12].append([6,"sisaan",-1,"Mokin ovi on kiinni."])
    suunnat[12].append([0,"sisaan",7,"Menet ovesta sisaan mokkiin."])
    suunnat[13].append([6,"mokki",-1,"Mokin ovi on kiinni."])
    suunnat[13].append([0,"mokki",-1,"Menet ovesta sisaan mokkiin."])
    
    matriisi[7].append("Olet ransistyneen mokin sisalla. Taalla on hamahakinseitteja ja taloa ei ole ilmeisesti kaytetty todella pitkaan aikaan. Voit menna vain ulos (U)")
    suunnat[15].append([7,"ulos",-1,"Ovi on kiinni."])
    suunnat[15].append([0,"ulos",6,"Menit ulos ovesta."])
    
    matriisi[8].append(("Olet saapunut suuren linnan edustalle. Linnassa on korkea muuri seka 4 korkeaa tornia. Keskella linnaa on suuri portti ja linnaa kiertaa vallihauta.\nVoit menna sisaan seka etelaan tai lanteen"))
    suunnat[16].append([8,"lanteen",9])
    suunnat[18].append([8,"sisaan",10,"Menet portista linnaan sisalle."])
    suunnat[19].append([8,"linna",10,"Menet portista linnaan sisalle."])
    suunnat[20].append([8,"linnaan",10,"Menet portista linnaan sisalle."])
    suunnat[21].append([8,"etelaan",11])
    suunnat[74].append([8,"piilopolkua",23])
    suunnat[75].append([8,"piilopolku",23])
    
    matriisi[9].append("Olet vuoristossa. Korkeat vuoret nousevat pilviin asti. Taalla on erikoisen nakoinen pieni mokki. Mokin ylapuolella kiertelee erikoisen nakoisia korppikotkia.\nVoit menna vain itaan (I).")
    suunnat[22].append([9,"itaan",8])
    suunnat[60].append([9,"sisaan",-1,"Mokin ovi on kiinni. Ovi nayttaa suljetun jonkinlaisella taialla."])
    suunnat[61].append([9,"mokki",-1,"Mokin ovi on kiinni. Ovi nayttaa suljetun jonkinlaisella taialla."])
    
    matriisi[10].append("Olet linnan aulassa. Eteisen seinilla palaa useita kirkkaita soihtuja. Voit menna ulos linnasta, lanteen tai itaan kaytavaa pitkin tai pohjoiseen pihalle.") 
    suunnat[23].append([10,"ulos",8])
    suunnat[24].append([10,"pohjoiseen",12])
    suunnat[25].append([10,"lanteen",13])
    suunnat[26].append([10,"itaan",14])
    
    matriisi[11].append("Olet viidakossa ojan vieressa. Ojan ylitse menee korjaamasi silta. Silta on hutera, mutta luulet voivasi ylitta joen turvallisesti..Voit menna sillan ylitse pohjoiseen (P) tai etelaan (E)")
    suunnat[27].append([11,"pohjoiseen",8])
    suunnat[28].append([11,"etelaan",5])
    
    matriisi[12].append("Olet linnan pihamaalla. Pihalta on ovet pohjoiseen, etelaan, lanteen ja etelaan.\nPihan koilliskulmassa on kaivo.")
    suunnat[29].append([12,"pohjoiseen",17])
    suunnat[30].append([12,"etelaan",10])
    suunnat[31].append([12,"lanteen",15])
    suunnat[32].append([12,"itaan",16])
    
    matriisi[13].append("Olet linnan lounaiskulmassa. Taalta nousee kierrerappuset torniin. Kaytavat jatkuvat pohjoiseen ja itaan.")
    suunnat[33].append([13,"pohjoiseen",15])
    suunnat[34].append([13,"itaan",10])
    suunnat[35].append([13,"ylospain",21])
    suunnat[36].append([13,"portaat",21])
    suunnat[37].append([13,"kierreportaat",21])
    
    matriisi[14].append("Olet linnan kaakkoiskulmassa. Taalta nousee kierrerappuset torniin. Kaytavat jatkuvat pohjoiseen ja lanteen.")
    suunnat[38].append([14,"pohjoiseen",16])
    suunnat[39].append([14,"lanteen",10])
    suunnat[40].append([14,"ylospain",18])
    suunnat[41].append([14,"portaat",18])
    suunnat[42].append([14,"kierreportaat",18])
    
    matriisi[15].append("Olet linnan kaytavassa. Pimea kaytava jatkuu pohjoiseen ja etelaan. Oviaukko avautuu itaan linnanpihalle.")
    suunnat[43].append([15,"pohjoiseen",19])
    suunnat[44].append([15,"etelaan",13])
    suunnat[45].append([15,"itaan",12])
    
    matriisi[16].append("Olet linnan kaytavassa. Pimea kaytava jatkuu pohjoiseen ja etelaan. Oviaukko avautuu lanteen linnan pihalle.\nHuoneen koilliskulmassa on oviaukko, josta kierrerapppuset johtavat alaspain. Oviaukon ylapuolella on kyltti.")
    suunnat[46].append([16,"pohjoiseen",20])
    suunnat[47].append([16,"etelaan",14])
    suunnat[48].append([16,"lanteen",12])
    suunnat[66].append([16,"alaspain",22])
    suunnat[67].append([16,"rappuset",22])
    suunnat[68].append([16,"portaat",22])
    suunnat[69].append([16,"raput",22])
    
    matriisi[17].append("Olet linnan valtaistuinsalissa. Kuningas istuu istuimella. Huoneesta avautuu kaytavat lanteen ja itaan.\nOvesta avautuu nakyma linnanpihalle.\nOnneksi olkoon, olet ratkaisuut ensimmaisen haasteen, loysit kuninkaan.")
    suunnat[49].append([17,"lanteen",19])
    suunnat[50].append([17,"itaan",20])
    suunnat[51].append([17,"etelaan",12])
    
    matriisi[18].append("Olet korkeassa tornissa. Etelassa naet laajan matsan ja muualla korkeat, ylitsepaasemattomat vuoret ymparoivat linnaa.\nvoit menna vain alas.")
    suunnat[52].append([18,"alaspain",14])
    suunnat[11].append([20,"ylospain",-1,"Et voi kiiveta torniin. Porraskaytava on muurattu umpeen."])
    
    matriisi[19].append("Olet linnan luoteiskulmassa. Torniin nousevat kierreportaat on muurattu umpeen. Kaytavat jatkuvat etelaan ja itaan.")
    suunnat[53].append([19,"itaan",17])
    suunnat[54].append([19,"etelaan",15])
    suunnat[59].append([19,"ylospain",-1,"Et voi kiiveta torniin. Porraskaytava on muurattu umpeen."])
    
    matriisi[20].append("Olet linnan koilliskulmassa. Torniin nousevat kierreportaat on muurattu umpeen. Kaytavat jatkuvat etelaan ja lanteen.")
    suunnat[55].append([20,"lanteen",17])
    suunnat[56].append([20,"etelaan",16])
    suunnat[58].append([20,"ylospain",-1,"Et voi kiiveta torniin. Porraskaytava on muurattu umpeen."])
    
    matriisi[21].append("Olet korkeassa tornissa. Huoneessa on 4 ikkunaa ja ikkunoiden edessa on nelja sankya ja sankyjen vieressa on pienet laatikostot.")
    suunnat[57].append([21,"alaspain",13])
    suunnat[17].append([21,"ylospain",-1,"Kierreportaat eivat jatku enaa ylospain. Olet jo ylatasolla."])
    suunnat[73].append([20,"ylospain",-1,"Et voi kiiveta torniin. Porraskaytava on muurattu umpeen."])
    
    matriisi[22].append("Olet vankityrmassa. Paksujen rautakaltereiden takana naet voivottelevan miehen. Rappuset johtavat huoneesta ylospain.")
    suunnat[65].append([22,"ylospain",16,"Kiipeat rappuja ylospain"])
    suunnat[65].append([0,"ylospain",-1,"Olet kaltereiden takana ja ovi on lukossa."])
    suunnat[71].append([22,"rappuset",16,"Kiipeat rappuja ylospain"])
    suunnat[71].append([0,"rappuset",-1,"Olet kaltereiden takana ja ovi on lukossa."])
    suunnat[72].append([22,"raput",16,"Kiipeat rappuja ylospain"])
    suunnat[72].append([0,"raput",-1,"Olet kaltereiden takana ja ovi on lukossa."])
    suunnat[70].append([22,"portaat",16,"Kiipeat rappuja ylospain"])
    suunnat[70].append([0,"portaat",-1,"Olet kaltereiden takana ja ovi on lukossa."])

    matriisi[23].append("Olet vuorten valissa kulkevalla piilopolulla. Hyvin kapea polku jatkuu lanteen alas laaksoon seka edelleen itaanpain.")
    suunnat[76].append([23,"lanteen",8])
    suunnat[77].append([23,"itaan",24,"Tasta eteenpain pelia ei ole tehty viela. Olet paassyt maaliin, onneksi olkoon!"])
    suunnat[78].append([23,"vuorta pitkin",-1,"En uskalla kiiveta noin jyrkkaa rinnetta pitkin."])
    
    matriisi[24].append("Olet korkean vuoren rinteella. Taalta paaset vain lanteen polulle.")
    suunnat[79].append([24,"lanteen",23,"Laskeudut vuorelta alas polkua pitkin."])
    
    return (matriisi, suunnat)