# Isim: Muhammed Maksut Cakmaktas
# Numara: 20217170016

class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str="" # plaka numarası
    nereden:str="" # yolculuk nereden başladığını soyluyor
    nereye:str="" # yolculugun nerede bitecegini gosteriyor
    _koltuk_sayisi:int=0 # otobuste kac koltuk oldugunu gosteriyor
    otobusler:list
    satislar:int=0 
    iadeler:int=0
    
    def __init__(self,plaka,nereden,nereye,koltuk):
        """constructor method

        Args:
            plaka (_type_): plaka numarası
            nereden (_type_): yolculuk nereden başladığını soyluyor
            nereye (_type_): yolculugun nerede bitecegini gosteriyor
            koltuk (_type_): otobuste kac koltuk oldugunu gosteriyor
            
        """
    
        self.plaka=plaka
        self.nereden=nereden
        self.nereye=nereye
        self._koltuk_sayisi=koltuk
       
        
    
    

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        kac_bilet_satildi= self.satislar
        return kac_bilet_satildi
        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        kac_bilet_iade= self.iadeler
        return kac_bilet_iade
    
    def dolu(self):
        "dolu koltuk sayısını göstericek"
        dolu_koltuk_sayisi= self.satislar
        return dolu_koltuk_sayisi
    
    def bos(self):
        "bos koltuk sayısını gosterıcek."
        bos_koltuk_Sayisi=self._koltuk_sayisi - self.bilet_sat + self.bilet_iade
        return bos_koltuk_Sayisi
    

    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{},{},{},{},{}".format(self.nereden,self.nereye,self.plaka,self.bos,self.dolu))

