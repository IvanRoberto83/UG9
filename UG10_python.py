def konser(Tiket, Lokasi, TotalWaktu: int):
    if Tiket == 'A':
        hargaTiket = 350000
    elif Tiket == 'B':
        hargaTiket = 270000
    else:
        hargaTiket = 150000
    
    if Lokasi == 'Jakarta':
        hargaTransport = 400000*2
        hargaPenginapan = 0
        if TotalWaktu > 24:
            while TotalWaktu > 24:
                hargaPenginapan += 250000 
                TotalWaktu -= 24
            hargaPenginapan += (TotalWaktu*40000)
        elif TotalWaktu < 24:
            hargaPenginapan += (TotalWaktu*40000)
        else:
            hargaPenginapan += 250000 

    elif Lokasi == 'Bandung': 
        hargaTransport = 390000*2   
        hargaPenginapan = 0
        if TotalWaktu > 24:
            while TotalWaktu > 24:
                hargaPenginapan += 200000 
                TotalWaktu -= 24
            hargaPenginapan += (TotalWaktu*30000)
        elif TotalWaktu < 24:
            hargaPenginapan += (TotalWaktu*30000)
        else:
            hargaPenginapan += 200000 
        
    elif Lokasi == 'Surabaya':
        hargaTransport = 360000*2   
        hargaPenginapan = 0
        if TotalWaktu > 24:
            while TotalWaktu > 24:
                hargaPenginapan += 220000 
                TotalWaktu -= 24
            hargaPenginapan += (TotalWaktu*35000)
        elif TotalWaktu < 24:
            hargaPenginapan += (TotalWaktu*35000)
        else:
            hargaPenginapan += 360000 
        
    elif Lokasi == 'Yogyakarta':
        hargaTransport = 0
        hargaPenginapan = 0

    # return hargaTiket + hargaTransport + hargaPenginapan