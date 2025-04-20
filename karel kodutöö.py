while True:
    hapukapsas = input("Kas teil on hapukapsast? (jah/ei): ")
    if hapukapsas == "ei":
        print("Saad hautist.")

    pott = input("Kas teil on pott? (jah/ei): ")
    if pott == "ei":
        print("Suppi teha ei saa.")

    vesi = input("Kas teil on vett? (jah/ei): ")
    if vesi == "ei":
        print("Saad mulgikapsaid teha.")

    kartul = input("Kas teil on kartulit? (jah/ei): ")
    puljongit = input("Kas teil on puljongit? (jah/ei): ")

    midagimuud = input("Kas teil on midagi muud kapis? (jah/ei): ")

    if midagimuud == "ei":
        if hapukapsas == "jah" and pott == "jah" and vesi == "jah":
            print("Saab teha kapsasuppi.")
        elif hapukapsas == "ei" and pott == "jah":
            print("Saad hautist.")
        elif vesi == "ei":
            print("Saab teha mulgikapsaid.")
        else:
            print("Midagi ikka saab teha!")
    else:
        if hapukapsas == "jah" and kartul == "jah" and puljongit == "jah":
            print("Saate teha ühepajatoitu.")
        else:
            print("Võib-olla ei saa päris ühepajatoitu, aga midagi ikka!")
    
    uuesti = input("Kas soovite uuesti kokandada?  (jah/ei): ")
    if uuesti != "jah":
        break
