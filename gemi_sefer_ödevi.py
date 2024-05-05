import sqlite3 as sql
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

#gemiler sınıfı tablo oluştur/ ekle/ güncelle/ silme metodları

class Gemiler:
    def __init__(self, seri_no, ad, agirlik, yapim_yili):
        self.seri_no = seri_no
        self.ad = ad
        self.agirlik = agirlik
        self.yapim_yili = yapim_yili

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS gemiler (
                        seri_no TEXT PRIMARY KEY,
                        ad TEXT,
                        agirlik REAL,
                        yapim_yili INTEGER)''')

        baglanti.commit()
        baglanti.close()

    def gemi_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO gemiler VALUES (?, ?, ?, ?)",
                      (self.seri_no, self.ad, self.agirlik, self.yapim_yili))

        baglanti.commit()
        baglanti.close()

    def gemi_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE gemiler SET ad=?, agirlik=?, yapim_yili=? WHERE seri_no=?",
                      (self.ad, self.agirlik, self.yapim_yili, self.seri_no))

        baglanti.commit()
        baglanti.close()

    def gemi_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM gemiler WHERE seri_no=?", (self.seri_no,))

        baglanti.commit()
        baglanti.close()

#yolcu gemisi sınıfı tablo oluştur/ ekle/ güncelle/ silme metodları gemiler sınıfından miras alır

class YolcuGemisi(Gemiler):
    def __init__(self, seri_no, ad, agirlik, yapim_yili, yolcu_kapasitesi):
        super().__init__(seri_no, ad, agirlik, yapim_yili)
        self.yolcu_kapasitesi = yolcu_kapasitesi

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS yolcu_gemileri (
                        seri_no TEXT PRIMARY KEY,
                        ad TEXT,
                        agirlik REAL,
                        yapim_yili INTEGER,
                        yolcu_kapasitesi INTEGER)''')

        baglanti.commit()
        baglanti.close()

    def gemi_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO yolcu_gemileri VALUES (?, ?, ?, ?, ?)",
                      (self.seri_no, self.ad, self.agirlik, self.yapim_yili, self.yolcu_kapasitesi))

        baglanti.commit()
        baglanti.close()

    def gemi_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE yolcu_gemileri SET ad=?, agirlik=?, yapim_yili=?, yolcu_kapasitesi=? WHERE seri_no=?",
                      (self.ad, self.agirlik, self.yapim_yili, self.yolcu_kapasitesi, self.seri_no))

        baglanti.commit()
        baglanti.close()

    def gemi_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM yolcu_gemileri WHERE seri_no=?", (self.seri_no,))

        baglanti.commit()
        baglanti.close()

#petrol gemisi sınıfı tablo oluştur/ ekle/ güncelle/ silme metodları gemiler sınıfından miras alır
class PetrolTankeri(Gemiler):
    def __init__(self, seri_no, ad, agirlik, yapim_yili, petrol_kapasitesi):
        super().__init__(seri_no, ad, agirlik, yapim_yili)
        self.petrol_kapasitesi = petrol_kapasitesi

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS petrol_tankerleri (
                        seri_no TEXT PRIMARY KEY,
                        ad TEXT,
                        agirlik REAL,
                        yapim_yili INTEGER,
                        petrol_kapasitesi INTEGER)''')

        baglanti.commit()
        baglanti.close()

    def gemi_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO petrol_tankerleri VALUES (?, ?, ?, ?, ?)",
                      (self.seri_no, self.ad, self.agirlik, self.yapim_yili, self.petrol_kapasitesi))

        baglanti.commit()
        baglanti.close()

    def gemi_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE petrol_tankerleri SET ad=?, agirlik=?, yapim_yili=?, petrol_kapasitesi=? WHERE seri_no=?",
                      (self.ad, self.agirlik, self.yapim_yili, self.petrol_kapasitesi, self.seri_no))

        baglanti.commit()
        baglanti.close()

    def gemi_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM petrol_tankerleri WHERE seri_no=?", (self.seri_no,))

        baglanti.commit()
        baglanti.close()

#konteyner gemisi sınıfı tablo oluştur/ ekle/ güncelle/ silme metodları gemiler sınıfından miras alır
class KonteynerGemisi(Gemiler):
    def __init__(self, seri_no, ad, agirlik, yapim_yili, konteyner_sayisi, maks_agirlik):
        super().__init__(seri_no, ad, agirlik, yapim_yili)
        self.konteyner_sayisi = konteyner_sayisi
        self.maks_agirlik = maks_agirlik

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS konteyner_gemileri (
                        seri_no TEXT PRIMARY KEY,
                        ad TEXT,
                        agirlik REAL,
                        yapim_yili INTEGER,
                        konteyner_sayisi INTEGER,
                        maks_agirlik REAL)''')

        baglanti.commit()
        baglanti.close()

    def gemi_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO konteyner_gemileri VALUES (?, ?, ?, ?, ?, ?)",
                      (self.seri_no, self.ad, self.agirlik, self.yapim_yili, self.konteyner_sayisi, self.maks_agirlik))

        baglanti.commit()
        baglanti.close()

    def gemi_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE konteyner_gemileri SET ad=?, agirlik=?, yapim_yili=?, konteyner_sayisi=?, maks_agirlik=? WHERE seri_no=?",
                      (self.ad, self.agirlik, self.yapim_yili, self.konteyner_sayisi, self.maks_agirlik, self.seri_no))

        baglanti.commit()
        baglanti.close()

    def gemi_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM konteyner_gemileri WHERE seri_no=?", (self.seri_no,))

        baglanti.commit()
        baglanti.close()

#kaptan sınıfı tablo oluştur/ ekle/ güncelle/ sil metodlarıyla beraber
class Kaptan:
    def __init__(self, ID, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisanslar):
        self.ID = ID
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.lisanslar = lisanslar

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS kaptanlar (
                        ID INTEGER PRIMARY KEY,
                        ad TEXT,
                        soyad TEXT,
                        adres TEXT,
                        vatandaslik TEXT,
                        dogum_tarihi TEXT,
                        ise_giris_tarihi TEXT,
                        lisanslar TEXT)''')

        baglanti.commit()
        baglanti.close()

    def kaptan_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO kaptanlar VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      (self.ID, self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.lisanslar))

        baglanti.commit()
        baglanti.close()

    def kaptan_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE kaptanlar SET ad=?, soyad=?, adres=?, vatandaslik=?, dogum_tarihi=?, ise_giris_tarihi=?, lisanslar=? WHERE ID=?",
                      (self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.lisanslar, self.ID))

        baglanti.commit()
        baglanti.close()

    def kaptan_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM kaptanlar WHERE ID=?", (self.ID,))

        baglanti.commit()
        baglanti.close()


#murettabat sınıfı tablo oluştur/ ekle/ güncelle/ sil metodlarıyla beraber
class Murettabat:
    def __init__(self, ID, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, gorev):
        self.ID = ID
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.gorev = gorev

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS murettabat (
                        ID INTEGER PRIMARY KEY,
                        ad TEXT,
                        soyad TEXT,
                        adres TEXT,
                        vatandaslik TEXT,
                        dogum_tarihi TEXT,
                        ise_giris_tarihi TEXT,
                        gorev TEXT)''')

        baglanti.commit()
        baglanti.close()

    def murettabat_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO murettabat VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      (self.ID, self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.gorev))

        baglanti.commit()
        baglanti.close()

    def murettabat_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE murettabat SET ad=?, soyad=?, adres=?, vatandaslik=?, dogum_tarihi=?, ise_giris_tarihi=?, gorev=? WHERE ID=?",
                      (self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.gorev, self.ID))

        baglanti.commit()
        baglanti.close()

    def murettabat_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM murettabat WHERE ID=?", (self.ID,))

        baglanti.commit()
        baglanti.close()


#seferler sınıfı tablo oluştur/ ekle/ güncelle/ sil metodlarıyla beraber
class Seferler:
    def __init__(self, db_file):
        self.conn = sql.connect(db_file)
        self.cursor = self.conn.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sefer (
                                ID INTEGER PRIMARY KEY,
                                gemi_tipi TEXT,
                                gemi_seri_no TEXT,
                                yola_cikis_tarihi TEXT,
                                donus_tarihi TEXT,
                                yola_cikis_limani TEXT,
                                kaptan1_id INTEGER,
                                kaptan2_id INTEGER,
                                kaptan3_id INTEGER,
                                murettabat1_id INTEGER,
                                murettabat2_id INTEGER,
                                murettabat3_id INTEGER
                                )''')
        self.conn.commit()


    def sefer_ekle(self, sefer_id, gemi_tipi, gemi_seri_no, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, kaptan1_id, kaptan2_id, kaptan3_id, murettabat1_id, murettabat2_id, murettabat3_id):
        self.cursor.execute('''INSERT INTO sefer (ID, gemi_tipi, gemi_seri_no, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, kaptan1_id, kaptan2_id, kaptan3_id, murettabat1_id, murettabat2_id, murettabat3_id)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (sefer_id, gemi_tipi, gemi_seri_no, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, kaptan1_id, kaptan2_id, kaptan3_id, murettabat1_id, murettabat2_id, murettabat3_id))
        self.conn.commit()

    def seferleri_goruntule(self):
        self.cursor.execute('''SELECT * FROM sefer''')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def sefer_guncelle(self, sefer_id, gemi_tipi=None, gemi_seri_no=None, yola_cikis_tarihi=None, donus_tarihi=None,
                       yola_cikis_limani=None, kaptan1_id=None, kaptan2_id=None, kaptan3_id=None, murettabat1_id=None,
                       murettabat2_id=None, murettabat3_id=None):
        update_query = '''UPDATE sefer SET'''
        update_values = []

        if gemi_tipi:
            update_query += ''' gemi_tipi=?, '''
            update_values.append(gemi_tipi)
        if gemi_seri_no:
            update_query += ''' gemi_seri_no=?, '''
            update_values.append(gemi_seri_no)
        if yola_cikis_tarihi:
            update_query += ''' yola_cikis_tarihi=?, '''
            update_values.append(yola_cikis_tarihi)
        if donus_tarihi:
            update_query += ''' donus_tarihi=?, '''
            update_values.append(donus_tarihi)
        if yola_cikis_limani:
            update_query += ''' yola_cikis_limani=?, '''
            update_values.append(yola_cikis_limani)
        if kaptan1_id:
            update_query += ''' kaptan1_id=?, '''
            update_values.append(kaptan1_id)
        if kaptan2_id:
            update_query += ''' kaptan2_id=?, '''
            update_values.append(kaptan2_id)
        if kaptan3_id:
            update_query += ''' kaptan3_id=?, '''
            update_values.append(kaptan3_id)
        if murettabat1_id:
            update_query += ''' murettabat1_id=?, '''
            update_values.append(murettabat1_id)
        if murettabat2_id:
            update_query += ''' murettabat2_id=?, '''
            update_values.append(murettabat2_id)
        if murettabat3_id:
            update_query += ''' murettabat3_id=?, '''
            update_values.append(murettabat3_id)

        # Son virgülü kaldır ve WHERE kısmını ekle
        update_query = update_query.rstrip(', ') + ''' WHERE ID=?'''
        update_values.append(sefer_id)

        # Güncelleme sorgusunu çalıştır
        self.cursor.execute(update_query, update_values)
        self.conn.commit()


    def sefer_sil(self, sefer_id):
        self.cursor.execute('''DELETE FROM sefer WHERE ID=?''', (sefer_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()




#liman sınıfı tablo oluştur/ ekle/ güncelle/ sil metodlarıyla beraber
class Liman:
    def __init__(self, liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti):
        self.liman_adi = liman_adi
        self.ulke = ulke
        self.nufus = nufus
        self.pasaport_gerekli = pasaport_gerekli
        self.demirleme_ucreti = demirleme_ucreti

    def tablo_olustur(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute('''CREATE TABLE IF NOT EXISTS limanlar (
                        liman_adi TEXT,
                        ulke TEXT,
                        nufus INTEGER,
                        pasaport_gerekli TEXT,
                        demirleme_ucreti REAL,
                        PRIMARY KEY (liman_adi, ulke))''')

        baglanti.commit()
        baglanti.close()

    def liman_ekle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("INSERT INTO limanlar VALUES (?, ?, ?, ?, ?)",
                      (self.liman_adi, self.ulke, self.nufus, self.pasaport_gerekli, self.demirleme_ucreti))

        baglanti.commit()
        baglanti.close()

    def liman_guncelle(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("UPDATE limanlar SET ulke=?, nufus=?, pasaport_gerekli=?, demirleme_ucreti=? WHERE liman_adi=?",
                      (self.ulke, self.nufus, self.pasaport_gerekli, self.demirleme_ucreti, self.liman_adi))

        baglanti.commit()
        baglanti.close()

    def liman_sil(self):
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        imlec.execute("DELETE FROM limanlar WHERE liman_adi=?", (self.liman_adi,))

        baglanti.commit()
        baglanti.close()


window = Tk()

window.geometry("800x830")
window.iconbitmap("logo.ico")
window.title("GEMİ SEFERLER YÖNETİMİ")
window.configure(bg="#000080")


# pencerede kaptan ekle butonuna gelen fonsiyon
def kaptan_ekle():
    # Yeni pencere oluştur
    new_window = Toplevel(window)
    new_window.geometry("600x720")
    new_window.title("Kaptan bilgilerini giriniz..")

    #kaptan bilgileri giriş kutucukları
    label = Label(new_window, text="KAPTAN ID:")
    label.place(x=150,y=25)
    kaptan_id = Entry(new_window, width=15, font=("none", 18))
    kaptan_id.place(x=150,y=50)

    label = Label(new_window, text="KAPTAN AD:")
    label.place(x=150,y=90)
    kaptan_ad = Entry(new_window, width=15, font=("none", 18))
    kaptan_ad.place(x=150,y=115)

    label = Label(new_window, text="KAPTAN SOYAD:")
    label.place(x=150,y=155)
    kaptan_soyad = Entry(new_window, width=15, font=("none", 18))
    kaptan_soyad.place(x=150,y=180)

    label = Label(new_window, text="KAPTAN ADRES:")
    label.place(x=150,y=220)
    kaptan_adres = Entry(new_window, width=15, font=("none", 18))
    kaptan_adres.place(x=150,y=245)

    label = Label(new_window, text="KAPTAN Doğum TARİHİ :")
    label.place(x=150,y=285)
    kaptan_dogum_tarihi = Entry(new_window, width=15, font=("none", 18))
    kaptan_dogum_tarihi.place(x=150,y=310)

    label = Label(new_window, text="KAPTAN İŞE GİRİŞ TARİHİ :")
    label.place(x=150,y=350)
    kaptan_ise_giris_tarihi = Entry(new_window, width=15, font=("none", 18))
    kaptan_ise_giris_tarihi.place(x=150,y=375)

    label = Label(new_window, text="KAPTAN LİSANSLAR :")
    label.place(x=150, y=415)
    kaptan_lisanslar = Entry(new_window, width=15, font=("none", 18))
    kaptan_lisanslar.place(x=150, y=440)

    label = Label(new_window, text="KAPTAN VATANDAŞLIK :")
    label.place(x=150, y=480)
    kaptan_vatandaslik = Entry(new_window, width=15, font=("none", 18))
    kaptan_vatandaslik.place(x=150, y=505)

    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla tablo oluşturup ekleme
    def tabloya_kaptan_ekle():
        kaptan_id_metni = kaptan_id.get()
        kaptan_ad_metni = kaptan_ad.get()
        kaptan_soyad_metni = kaptan_soyad.get()
        kaptan_adres_metni = kaptan_adres.get()
        kaptan_dogum_tarihi_metni = kaptan_dogum_tarihi.get()
        kaptan_ise_giris_tarihi_metni = kaptan_ise_giris_tarihi.get()
        kaptan_lisanslar_metni = kaptan_lisanslar.get()
        kaptan_vatandaslik_metni = kaptan_vatandaslik.get()
        # Kaptan sınıfından bir nesne oluştur
        yeni_kaptan = Kaptan(ID=kaptan_id_metni, ad=kaptan_ad_metni, soyad=kaptan_soyad_metni, adres=kaptan_adres_metni, vatandaslik=kaptan_vatandaslik_metni,
                             dogum_tarihi=kaptan_dogum_tarihi_metni, ise_giris_tarihi=kaptan_ise_giris_tarihi_metni, lisanslar=kaptan_lisanslar_metni)
        yeni_kaptan.tablo_olustur()
        # Kaptanı veritabanına ekle
        yeni_kaptan.kaptan_ekle()

    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla güncelleme
    def kaptan_gucnelle():
        kaptan_id_metni = kaptan_id.get()
        kaptan_ad_metni = kaptan_ad.get()
        kaptan_soyad_metni = kaptan_soyad.get()
        kaptan_adres_metni = kaptan_adres.get()
        kaptan_dogum_tarihi_metni = kaptan_dogum_tarihi.get()
        kaptan_ise_giris_tarihi_metni = kaptan_ise_giris_tarihi.get()
        kaptan_lisanslar_metni = kaptan_lisanslar.get()
        kaptan_vatandaslik_metni = kaptan_vatandaslik.get()
        guncel_kaptan = Kaptan(ID=kaptan_id_metni, ad=kaptan_ad_metni, soyad=kaptan_soyad_metni, adres=kaptan_adres_metni,
                             vatandaslik=kaptan_vatandaslik_metni,
                             dogum_tarihi=kaptan_dogum_tarihi_metni, ise_giris_tarihi=kaptan_ise_giris_tarihi_metni,
                             lisanslar=kaptan_lisanslar_metni)
        guncel_kaptan.kaptan_guncelle()

#fonksiyonları çağıracak olan butonlar
    kaydet_butonu = Button(new_window,text="~ Bilgileri Kaydet ~",bg="black",fg="white",font=("Arial", 12, "bold italic"),width=15,height=1,command=tabloya_kaptan_ekle)
    kaydet_butonu.place(x=100,y=670)
    guncelle_butonu = Button(new_window, text="~ Bilgileri güncelle ~", bg="black", fg="white", font=("Arial", 12, "bold italic"), width=15, height=1, command=kaptan_gucnelle)
    guncelle_butonu.place(x=300, y=670)

########################################################
#tablo gösterici fonksiyon hangi tablo ve sütun adlarıyla beraber gelirse ona tablo oluşturur pencerede
def tabloyu_goster(tablo_adi, sutun_adlari):
    def verileri_al():
        # Veritabanı bağlantısını oluştur
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        # Veritabanındaki tabloyu seç
        imlec.execute(f"SELECT * FROM {tablo_adi}")
        rows = imlec.fetchall()

        # Tabloyu temizle (önceki görünümü temizle)
        for row in tree.get_children():
            tree.delete(row)

        # Tabloyu doldur
        for row in rows:
            tree.insert('', 'end', values=row)

        # Bağlantıyı kapat
        baglanti.close()

    #tabloda seçili veriyi silme metodu
    def veriyi_sil():
        # Seçili satırın ID'sini al
        selected_item = tree.selection()
        row_id = tree.item(selected_item, 'values')[0]

        # Veritabanı bağlantısını oluştur
        baglanti = sql.connect("tershane.db")
        imlec = baglanti.cursor()

        # Seçili satırı veritabanından sil
        imlec.execute(f"DELETE FROM {tablo_adi} WHERE {sutun_adlari[0]}=?", (row_id,))

        # Değişiklikleri kaydet ve bağlantıyı kapat
        baglanti.commit()
        baglanti.close()

        # Tabloyu güncelle
        verileri_al()

    # tablo pencersi
    root = Tk()
    root.title("Tablo Görüntüleme")

    # Treeview oluştur
    tree = Treeview(root, columns=sutun_adlari, show="headings")
    for i, sutun in enumerate(sutun_adlari, start=1):
        tree.heading(f"#{i}", text=sutun)
    tree.pack()

    # Verileri görüntüleme butonu
    goster_buton = Button(root, text="Tabloyu Görüntüle", command=verileri_al)
    goster_buton.pack()

    # Seçili veriyi silme butonu
    sil_buton = Button(root, text="Seçili Veriyi Sil", command=veriyi_sil)
    sil_buton.pack()

    # Pencereyi göster
    root.mainloop()
#tablosunu görünteyeceğimiz tablolar ve onları tuşa atamamız için fonksiyonlar
def kaptan_tablo():
    sutun_adlari = ["ID", "Ad", "Soyad", "Adres", "Vatandaşlık", "Doğum Tarihi", "İşe Giriş Tarihi", "Lisans"]
    tabloyu_goster("kaptanlar", sutun_adlari)  # "kaptanlar" tablosunu görüntüle
def murattabat_tablo():
    sutun_adlari = ["ID", "Ad", "Soyad", "Adres", "Vatandaşlık", "Doğum Tarihi", "İşe Giriş Tarihi", "görev"]
    tabloyu_goster("murettabat", sutun_adlari)  # "murettabatlar" tablosunu görüntüle
def gemiler_tablo_goster():
    new_window = Toplevel(window)
    new_window.geometry("400x300")
    new_window.title("Hangi gemi tablosunu görüntüleyeceksiniz ?")

    def yolcu_gemisi_tablo():
        sutun_adlari = ["seri_no", "ad", "agirlik", "yapim_yili", "yolcu_kapasitesi"]
        tabloyu_goster("yolcu_gemileri", sutun_adlari)

    def petrol_gemisi_tablo():
        sutun_adlari = ["seri_no", "ad", "agirlik", "yapim_yili", "petrol_kapasitesi"]
        tabloyu_goster("petrol_tankerleri", sutun_adlari)

    def konteyner_gemisi_tablo():
        sutun_adlari = ["seri_no", "ad", "agirlik", "yapim_yili", "konteyner_sayisi", "maks_agirlik"]
        tabloyu_goster("konteyner_gemileri", sutun_adlari)

    yolcu_gemisi_tablo_buton = Button(new_window, text="~  yolcu gemisi tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2, command=yolcu_gemisi_tablo)
    yolcu_gemisi_tablo_buton.place(x=50, y=50)

    petrol_gemisi_tablo_buton = Button(new_window, text="~ petrol gemisi tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2, command=petrol_gemisi_tablo)
    petrol_gemisi_tablo_buton.place(x=50, y=125)

    konteyner_gemisi_tablo_buton = Button(new_window, text="~ konteyner gemisi tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2, command=konteyner_gemisi_tablo)
    konteyner_gemisi_tablo_buton.place(x=50, y=200)

def limanlar_tablo():
    sutun_adlari = ["liman_adi", "ulke","nufus", "pasaport_gerekli", "demirleme_ucreti"]
    tabloyu_goster("limanlar", sutun_adlari)

def seferler_tablo():
    sutun_adlari = ["ID","gemi_tipi","gemi_seri_no","yola_cikis_tarihi","donus_tarihi","yola_cikis_limani","kapta1_id","kapta2_id","kapta3_id","murettabat1_id","murettabat2_id","murettabat3_id"]
    tabloyu_goster("sefer",sutun_adlari)
##################################################################

def murettabat_ekle():
    # Yeni pencere oluştur
    new_window = Toplevel(window)
    new_window.geometry("600x720")
    new_window.title("Mürettabat bilgilerini giriniz")

    #kaptan bilgileri giriş kutucukları
    label = Label(new_window, text="ID:")
    label.place(x=150,y=25)
    murettabat_id = Entry(new_window, width=15, font=("none", 18))
    murettabat_id.place(x=150,y=50)

    label = Label(new_window, text="Ad:")
    label.place(x=150,y=90)
    murettabat_ad = Entry(new_window, width=15, font=("none", 18))
    murettabat_ad.place(x=150,y=115)

    label = Label(new_window, text="Soyad:")
    label.place(x=150,y=155)
    murettabat_soyad = Entry(new_window, width=15, font=("none", 18))
    murettabat_soyad.place(x=150,y=180)

    label = Label(new_window, text="Adres :")
    label.place(x=150,y=220)
    murettabat_adres = Entry(new_window, width=15, font=("none", 18))
    murettabat_adres.place(x=150,y=245)

    label = Label(new_window, text="Doğum Tarihi :")
    label.place(x=150,y=285)
    murettabat_dogum_tarihi = Entry(new_window, width=15, font=("none", 18))
    murettabat_dogum_tarihi.place(x=150,y=310)

    label = Label(new_window, text="İşe Giriş Tarihi :")
    label.place(x=150,y=350)
    murettabat_ise_giris_tarihi = Entry(new_window, width=15, font=("none", 18))
    murettabat_ise_giris_tarihi.place(x=150,y=375)

    label = Label(new_window, text="Hangi görevde :")
    label.place(x=150, y=415)
    murettabat_gorev = Entry(new_window, width=15, font=("none", 18))
    murettabat_gorev.place(x=150, y=440)

    label = Label(new_window, text="Vatandaşlık :")
    label.place(x=150, y=480)
    murettabat_vatandaslik = Entry(new_window, width=15, font=("none", 18))
    murettabat_vatandaslik.place(x=150, y=505)

    def tabloya_murettabat_ekle():
        murettabat_id_metni = murettabat_id.get()
        murettabat_ad_metni = murettabat_ad.get()
        murettabat_soyad_metni = murettabat_soyad.get()
        murettabat_adres_metni = murettabat_adres.get()
        murettabat_dogum_tarihi_metni = murettabat_dogum_tarihi.get()
        murettabat_ise_giris_tarihi_metni = murettabat_ise_giris_tarihi.get()
        murettabat_gorev_metni = murettabat_gorev.get()
        murettabat_vatandaslik_metni = murettabat_vatandaslik.get()
        # Kaptan sınıfından bir nesne oluştur
        yeni_murettabat = Murettabat(ID=murettabat_id_metni, ad=murettabat_ad_metni, soyad=murettabat_soyad_metni, adres=murettabat_adres_metni, vatandaslik=murettabat_vatandaslik_metni,
                             dogum_tarihi=murettabat_dogum_tarihi_metni, ise_giris_tarihi=murettabat_ise_giris_tarihi_metni, gorev=murettabat_gorev_metni)
        yeni_murettabat.tablo_olustur()
        # Kaptanı veritabanına ekle
        yeni_murettabat.murettabat_ekle()


    def murettabat_gucnelle():
        murettabat_id_metni = murettabat_id.get()
        murettabat_ad_metni = murettabat_ad.get()
        murettabat_soyad_metni = murettabat_soyad.get()
        murettabat_adres_metni = murettabat_adres.get()
        murettabat_dogum_tarihi_metni = murettabat_dogum_tarihi.get()
        murettabat_ise_giris_tarihi_metni = murettabat_ise_giris_tarihi.get()
        murettabat_gorev_metni = murettabat_gorev.get()
        murettabat_vatandaslik_metni = murettabat_vatandaslik.get()
        # Kaptan sınıfından bir nesne oluştur
        yeni_murettabat = Murettabat(ID=murettabat_id_metni, ad=murettabat_ad_metni, soyad=murettabat_soyad_metni,adres=murettabat_adres_metni, vatandaslik=murettabat_vatandaslik_metni,dogum_tarihi=murettabat_dogum_tarihi_metni,ise_giris_tarihi=murettabat_ise_giris_tarihi_metni, gorev=murettabat_gorev_metni)
        yeni_murettabat.murettabat_guncelle()

    kaydet_butonu = Button(new_window,text="~ Bilgileri Kaydet ~",bg="black",fg="white",font=("Arial", 12, "bold italic"),width=15,height=1,command=tabloya_murettabat_ekle)
    kaydet_butonu.place(x=100,y=670)
    guncelle_butonu = Button(new_window, text="~ Bilgileri güncelle ~", bg="black", fg="white", font=("Arial", 12, "bold italic"), width=15, height=1, command=murettabat_gucnelle)
    guncelle_butonu.place(x=300, y=670)

def gemiler():
    new_window = Toplevel(window)
    new_window.geometry("1000x600")
    new_window.title("gemi bilgilerini giriniz")

    label = Label(new_window, text="seri no:")
    label.place(x=50,y=25)
    yolcu_gemisi_seri_no = Entry(new_window, width=15, font=("none", 18))
    yolcu_gemisi_seri_no.place(x=50,y=50)

    label = Label(new_window, text="Gemi Adı:")
    label.place(x=50,y=90)
    yolcu_gemisi_ad = Entry(new_window, width=15, font=("none", 18))
    yolcu_gemisi_ad.place(x=50,y=115)

    label = Label(new_window, text="Ağırlığı:")
    label.place(x=50,y=155)
    yolcu_gemisi_agirlik = Entry(new_window, width=15, font=("none", 18))
    yolcu_gemisi_agirlik.place(x=50,y=180)

    label = Label(new_window, text="Yapım yılı :")
    label.place(x=50,y=220)
    yolcu_gemisi_yapim_yili = Entry(new_window, width=15, font=("none", 18))
    yolcu_gemisi_yapim_yili.place(x=50,y=245)

    label = Label(new_window, text="Yolcu Kapasitesi :")
    label.place(x=50,y=285)
    yolcu_gemisi_yolcu_kapasitesi = Entry(new_window, width=15, font=("none", 18))
    yolcu_gemisi_yolcu_kapasitesi.place(x=50,y=310)
################# petrol tankeri #########
    label = Label(new_window, text="seri no:")
    label.place(x=350, y=25)
    petrol_gemisi_seri_no = Entry(new_window, width=15, font=("none", 18))
    petrol_gemisi_seri_no.place(x=350, y=50)

    label = Label(new_window, text="Gemi Adı:")
    label.place(x=350, y=90)
    petrol_gemisi_ad = Entry(new_window, width=15, font=("none", 18))
    petrol_gemisi_ad.place(x=350, y=115)

    label = Label(new_window, text="Ağırlığı:")
    label.place(x=350, y=155)
    petrol_gemisi_agirlik = Entry(new_window, width=15, font=("none", 18))
    petrol_gemisi_agirlik.place(x=350, y=180)

    label = Label(new_window, text="Yapım yılı :")
    label.place(x=350, y=220)
    petrol_gemisi_yapim_yili = Entry(new_window, width=15, font=("none", 18))
    petrol_gemisi_yapim_yili.place(x=350, y=245)

    label = Label(new_window, text="Petrol Kapasitesi :")
    label.place(x=350, y=285)
    petrol_gemisi_petrol_kapasitesi = Entry(new_window, width=15, font=("none", 18))
    petrol_gemisi_petrol_kapasitesi.place(x=350, y=310)
############## konteyner gemisi #############
    label = Label(new_window, text="seri no:")
    label.place(x=650, y=25)
    konteyner_gemisi_seri_no = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_seri_no.place(x=650, y=50)

    label = Label(new_window, text="Gemi Adı:")
    label.place(x=650, y=90)
    konteyner_gemisi_ad = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_ad.place(x=650, y=115)

    label = Label(new_window, text="Ağırlığı:")
    label.place(x=650, y=155)
    konteyner_gemisi_agirlik = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_agirlik.place(x=650, y=180)

    label = Label(new_window, text="Yapım yılı :")
    label.place(x=650, y=220)
    konteyner_gemisi_yapim_yili = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_yapim_yili.place(x=650, y=245)

    label = Label(new_window, text="konteyner Kapasitesi :")
    label.place(x=650, y=285)
    konteyner_gemisi_konteyner_kapasitesi = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_konteyner_kapasitesi.place(x=650, y=310)

    label = Label(new_window, text="maksimum ağırlık :")
    label.place(x=650, y=350)
    konteyner_gemisi_max_kapasitesi = Entry(new_window, width=15, font=("none", 18))
    konteyner_gemisi_max_kapasitesi.place(x=650, y=375)

    def yolcu_gemisi_ekle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        yolcu_gemi = YolcuGemisi(yolcu_gemisi_seri_no.get(), yolcu_gemisi_ad.get(), yolcu_gemisi_agirlik.get(),yolcu_gemisi_yapim_yili.get(),yolcu_gemisi_yolcu_kapasitesi.get())
        # Tabloyu oluşturun
        yolcu_gemi.tablo_olustur()
        # Yolcu gemisini tabloya ekleyin
        yolcu_gemi.gemi_ekle()

    def yolcu_gemisi_guncelle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        yolcu_gemi = YolcuGemisi(yolcu_gemisi_seri_no.get(), yolcu_gemisi_ad.get(), yolcu_gemisi_agirlik.get(),yolcu_gemisi_yapim_yili.get(), yolcu_gemisi_yolcu_kapasitesi.get())
        # Yolcu gemisi tablosunu güncellemek için seri no'ya göre güncelleme yap
        yolcu_gemi.gemi_guncelle()

    def petrol_gemisi_ekle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        petrol_gemi = PetrolTankeri(petrol_gemisi_seri_no.get(), petrol_gemisi_ad.get(), petrol_gemisi_agirlik.get(),petrol_gemisi_yapim_yili.get(),petrol_gemisi_petrol_kapasitesi.get())
        # Tabloyu oluşturun
        petrol_gemi.tablo_olustur()
        # Yolcu gemisini tabloya ekleyin
        petrol_gemi.gemi_ekle()

    def petrol_gemisi_guncelle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        petrol_gemi = PetrolTankeri(petrol_gemisi_seri_no.get(), petrol_gemisi_ad.get(), petrol_gemisi_agirlik.get(),petrol_gemisi_yapim_yili.get(),petrol_gemisi_petrol_kapasitesi.get())
        # Yolcu gemisi tablosunu güncellemek için seri no'ya göre güncelleme yap
        petrol_gemi.gemi_guncelle()

    def konteyner_gemisi_ekle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        konteyner_gemi = KonteynerGemisi(konteyner_gemisi_seri_no.get(), konteyner_gemisi_ad.get(), konteyner_gemisi_agirlik.get(),konteyner_gemisi_yapim_yili.get(),konteyner_gemisi_konteyner_kapasitesi.get(),konteyner_gemisi_max_kapasitesi.get())
        # Tabloyu oluşturun
        konteyner_gemi.tablo_olustur()
        # Yolcu gemisini tabloya ekleyin
        konteyner_gemi.gemi_ekle()

    def konteyner_gemisi_guncelle():
        # Öncelikle yolcu gemisi nesnesini oluşturun
        konteyner_gemi = KonteynerGemisi(konteyner_gemisi_seri_no.get(), konteyner_gemisi_ad.get(), konteyner_gemisi_agirlik.get(),konteyner_gemisi_yapim_yili.get(),konteyner_gemisi_konteyner_kapasitesi.get(),konteyner_gemisi_max_kapasitesi.get())
        # Yolcu gemisi tablosunu güncellemek için seri no'ya göre güncelleme yap
        konteyner_gemi.gemi_guncelle()

    yolcu_gemisi_kaydet_buton = Button(new_window, text="~ yolcu gemisi\nEkle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=yolcu_gemisi_ekle)
    yolcu_gemisi_kaydet_buton.place(x=50,y=370)
    yolcu_gemisi_guncelle_buton = Button(new_window, text="~ yolcu gemisi\nGüncelle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=yolcu_gemisi_guncelle)
    yolcu_gemisi_guncelle_buton.place(x=50,y=425)

    petrol_gemisi_kaydet_buton = Button(new_window, text="~ petrol gemisi\nEkle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=petrol_gemisi_ekle)
    petrol_gemisi_kaydet_buton.place(x=350,y=370)
    petrol_gemisi_guncelle_buton = Button(new_window, text="~ petrol gemisi\nGüncelle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=petrol_gemisi_guncelle)
    petrol_gemisi_guncelle_buton.place(x=350,y=425)

    konteyner_gemisi_kaydet_buton = Button(new_window, text="~ konteyner gemisi\nEkle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=konteyner_gemisi_ekle)
    konteyner_gemisi_kaydet_buton.place(x=650,y=400)
    konteyner_gemisi_guncelle_buton = Button(new_window, text="~ konteyner gemisi\nGüncelle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 8, "bold italic"), width=25, height=2,command=konteyner_gemisi_guncelle)
    konteyner_gemisi_guncelle_buton.place(x=650,y=475)


def liman():
    new_window = Toplevel(window)
    new_window.geometry("500x600")
    new_window.title("gemi bilgilerini giriniz")
#liman bilgileri giriş kutucukaları
    label = Label(new_window, text="Liman adı:")
    label.place(x=50, y=25)
    liman_adi = Entry(new_window, width=15, font=("none", 18))
    liman_adi.place(x=50, y=50)

    label = Label(new_window, text="Ülkesi :")
    label.place(x=50, y=90)
    liman_ulkesi = Entry(new_window, width=15, font=("none", 18))
    liman_ulkesi.place(x=50, y=115)

    label = Label(new_window, text="Nüfusu:")
    label.place(x=50, y=155)
    nufus = Entry(new_window, width=15, font=("none", 18))
    nufus.place(x=50, y=180)

    label = Label(new_window, text="pasaport istiyorsa (evet) istemiyorsa (hayır) :")
    label.place(x=50, y=220)
    pasaport = Entry(new_window, width=15, font=("none", 18))
    pasaport.place(x=50, y=245)

    label = Label(new_window, text="Demirleme ücreti :")
    label.place(x=50, y=285)
    demirleme_ucreti = Entry(new_window, width=15, font=("none", 18))
    demirleme_ucreti.place(x=50, y=310)

    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla tablo oluşturup ekleme
    def liman_kaydet():
        yeni_liman = Liman(liman_adi.get(),liman_ulkesi.get(),nufus.get(),pasaport.get(),demirleme_ucreti.get())
        yeni_liman.tablo_olustur()
        yeni_liman.liman_ekle()
    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla güncelleme
    def liman_guncelle():
        yeni_liman = Liman(liman_adi.get(),liman_ulkesi.get(),nufus.get(),pasaport.get(),demirleme_ucreti.get())
        yeni_liman.liman_guncelle()
    #yukarıdak foksiyonları penceredeyken çağıran butonlar
    liman_kaydet_buton = Button(new_window, text="~ yolcu gemisi\nEkle ~", bg="#a6172d", fg="#FFFFFF",font=("Arial", 8, "bold italic"), width=25, height=2, command=liman_kaydet)
    liman_kaydet_buton.place(x=50, y=370)
    liman_guncelle_buton = Button(new_window, text="~ yolcu gemisi\nGüncelle ~", bg="#a6172d", fg="#FFFFFF",font=("Arial", 8, "bold italic"), width=25, height=2,command=liman_guncelle)
    liman_guncelle_buton.place(x=50, y=425)




def sefer_ekle():
    new_window = Toplevel(window)
    new_window.geometry("800x500")
    new_window.title("Sefer Bilgileri Giriniz")
#sefer bilgileri giriş kutucuklar9
    label = Label(new_window, text="Sefer ID:")
    label.place(x=50, y=25)
    sefer_id = Entry(new_window, width=15, font=("none", 18))
    sefer_id.place(x=50, y=50)

    label = Label(new_window, text="Gemi Tipi (Yolcu Gemisi/Konteyner Gemisi/Petrol Tankeri):")
    label.place(x=350, y=25)
    gemi_tipi = Entry(new_window, width=15, font=("none", 18))
    gemi_tipi.place(x=350, y=50)

    label = Label(new_window, text="Gemi Seri No:")
    label.place(x=50, y=90)
    gemi_seri_no = Entry(new_window, width=15, font=("none", 18))
    gemi_seri_no.place(x=50, y=115)

    label = Label(new_window, text="Yola Çıkış Tarihi:")
    label.place(x=350, y=90)
    yola_cikis_tarihi = Entry(new_window, width=15, font=("none", 18))
    yola_cikis_tarihi.place(x=350, y=115)

    label = Label(new_window, text="Dönüş Tarihi:")
    label.place(x=50, y=155)
    donus_tarihi = Entry(new_window, width=15, font=("none", 18))
    donus_tarihi.place(x=50, y=180)

    label = Label(new_window, text=" yola çıkış limanı:")
    label.place(x=350, y=155)
    yola_cikis_limani = Entry(new_window, width=15, font=("none", 18))
    yola_cikis_limani.place(x=350, y=180)

    label = Label(new_window, text="Kaptan 1 Tablodaki Index No:")
    label.place(x=50, y=220)
    kaptan1_index = Entry(new_window, width=15, font=("none", 18))
    kaptan1_index.place(x=50, y=245)

    label = Label(new_window, text="Kaptan 2 Tablodaki Index No:")
    label.place(x=350, y=220)
    kaptan2_index = Entry(new_window, width=15, font=("none", 18))
    kaptan2_index.place(x=350, y=245)

    label = Label(new_window, text="Kaptan 3 Tablodaki Index No:")
    label.place(x=50, y=285)
    kaptan3_index = Entry(new_window, width=15, font=("none", 18))
    kaptan3_index.place(x=50, y=310)

    label = Label(new_window, text="Mürettbat 1 Tablodaki Index No:")
    label.place(x=350, y=285)
    murettabat1_index = Entry(new_window, width=15, font=("none", 18))
    murettabat1_index.place(x=350, y=310)

    label = Label(new_window, text="Mürettbat 2 Tablodaki Index No:")
    label.place(x=50, y=350)
    murettabat2_index = Entry(new_window, width=15, font=("none", 18))
    murettabat2_index.place(x=50, y=375)

    label = Label(new_window, text="Mürettbat 3 Tablodaki Index No:")
    label.place(x=350, y=350)
    murettabat3_index = Entry(new_window, width=15, font=("none", 18))
    murettabat3_index.place(x=350, y=375)

    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla tablo oluşturup ekleme
    def sefer_kaydet():
        sefer_id_metni = sefer_id.get()
        gemi_tipi_metni = gemi_tipi.get()
        gemi_seri_no_metni = gemi_seri_no.get()
        yola_cikis_tarihi_metni = yola_cikis_tarihi.get()
        donus_tarihi_metni = donus_tarihi.get()
        kaptan1_index_metni = kaptan1_index.get()
        kaptan2_index_metni = kaptan2_index.get()
        kaptan3_index_metni = kaptan3_index.get()
        murettabat1_index_metni = murettabat1_index.get()
        murettabat2_index_metni = murettabat2_index.get()
        murettabat3_index_metni = murettabat3_index.get()
        yola_cikis_limani_metni = yola_cikis_limani.get()

        # Kaptanlar ve mürettebatların varlığını kontrol et
        if not kaptan1_index_metni or not kaptan2_index_metni or not murettabat1_index_metni:
            messagebox.showerror("Hata", "En az iki kaptan ve bir mürettebat girmelisiniz.")


        # else:
        #     seferler_veritabani = Seferler('tershane.db')
        #     seferler_veritabani.tablo_olustur()
        #     seferler_veritabani.sefer_ekle(sefer_id_metni, gemi_tipi_metni, gemi_seri_no_metni, yola_cikis_tarihi_metni,
        #                                    donus_tarihi_metni, yola_cikis_limani_metni, kaptan1_index_metni,
        #                                    kaptan2_index_metni, kaptan3_index_metni, murettabat1_index_metni,
        #                                    murettabat2_index_metni, murettabat3_index_metni)

        conn = sql.connect('tershane.db')
        cursor = conn.cursor()

        # Sorguyu hazırla ve çalıştır
        sorgu = "SELECT EXISTS(SELECT 1 FROM sefer WHERE kaptan1_id = ? OR kaptan2_id = ? OR kaptan3_id = ?)"
        cursor.execute(sorgu, (kaptan1_index_metni, kaptan2_index_metni, kaptan3_index_metni))
        result = cursor.fetchone()[0]
        def ekle():
            seferler_veritabani = Seferler('tershane.db')
            seferler_veritabani.tablo_olustur()
            seferler_veritabani.sefer_ekle(sefer_id_metni, gemi_tipi_metni, gemi_seri_no_metni, yola_cikis_tarihi_metni,
                                           donus_tarihi_metni, yola_cikis_limani_metni, kaptan1_index_metni,
                                           kaptan2_index_metni, kaptan3_index_metni, murettabat1_index_metni,
                                           murettabat2_index_metni, murettabat3_index_metni)


        # Sonucu kontrol et
        if result == 1:
            a_window = Toplevel(new_window)
            a_window.geometry("700x300")
            a_window.title("DİKKAT!!!!")
            label = Label(a_window, text="GİRDİĞİNİZ KAPTAN SEFER TABLOSUNDA YER ALMAKTADIR\nLÜTFEN KAPTANIN SEFER TARİHLERİNİ KONTROL EDİNİZ!!!" , bg="blue", font=("Arial", 12, "bold"))
            label.place(x=50, y=50)
            buton1 = Button(a_window, text="~ YİNEDE Ekle ~", bg="#a6172d", fg="#FFFFFF",
                            font=("Arial", 12, "bold italic"), width=25, height=2, command=ekle)
            buton1.place(x=125, y=130)

        else:
            seferler_veritabani = Seferler('tershane.db')
            seferler_veritabani.tablo_olustur()
            seferler_veritabani.sefer_ekle(sefer_id_metni, gemi_tipi_metni, gemi_seri_no_metni, yola_cikis_tarihi_metni,
                                           donus_tarihi_metni, yola_cikis_limani_metni, kaptan1_index_metni,
                                           kaptan2_index_metni, kaptan3_index_metni, murettabat1_index_metni,
                                           murettabat2_index_metni, murettabat3_index_metni)
        # Bağlantıyı kapat
        conn.close()

    #giriş kutucuklarından gelen bilgileri oluşturduğumuz sınıftaki metodlarla güncelleme
    def sefer_guncelle():
        sefer_id_metni = sefer_id.get()
        gemi_tipi_metni = gemi_tipi.get()
        gemi_seri_no_metni = gemi_seri_no.get()
        yola_cikis_tarihi_metni = yola_cikis_tarihi.get()
        donus_tarihi_metni = donus_tarihi.get()
        kaptan1_index_metni = kaptan1_index.get()
        kaptan2_index_metni = kaptan2_index.get()
        kaptan3_index_metni = kaptan3_index.get()
        murettabat1_index_metni = murettabat1_index.get()
        murettabat2_index_metni = murettabat2_index.get()
        murettabat3_index_metni = murettabat3_index.get()
        yola_cikis_limani_metni =yola_cikis_limani.get()
        seferler_veritabani = Seferler('tershane.db')
        seferler_veritabani.sefer_guncelle(sefer_id_metni,gemi_tipi=gemi_tipi_metni,gemi_seri_no=gemi_seri_no_metni, yola_cikis_tarihi=yola_cikis_tarihi_metni,
                                           donus_tarihi=donus_tarihi_metni, yola_cikis_limani=yola_cikis_limani_metni,
                                           kaptan1_id=kaptan1_index_metni, kaptan2_id=kaptan2_index_metni,
                                           kaptan3_id=kaptan3_index_metni, murettabat1_id=murettabat1_index_metni,
                                           murettabat2_id=murettabat2_index_metni,
                                           murettabat3_id=murettabat3_index_metni)

    #yukarıdaki fonksiyonları pencerede çağıran butonlar
    sefer_kaydet_buton = Button(new_window, text="~ Kaydet ~", bg="#a6172d", fg="#FFFFFF",font=("Arial", 8, "bold italic"), width=25, height=2, command=sefer_kaydet)
    sefer_kaydet_buton.place(x=50, y=425)
    sefer_guncelle_buton = Button(new_window, text="~ Güncelle ~", bg="#a6172d", fg="#FFFFFF",font=("Arial", 8, "bold italic"), width=25, height=2, command=sefer_guncelle)
    sefer_guncelle_buton.place(x=350, y=425)



## ana penceredeki yukarıdaki ana fonksiyonları çağıran butonlar

    ############################
   #~~~TABLO OLUŞTURMA ~~~~~~~#
  #~~~EKLEME VE GÜNCELLEME~~~#
 ############################

buton1 = Button(window, text="~ Kaptan Ekle ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 12, "bold italic"), width=25, height=2,command=kaptan_ekle)
buton1.place(x=100, y=25)

buton2 = Button(window, text="~ Mürettabat kişi Ekle ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=murettabat_ekle)
buton2.place(x=100, y=100)

buton3 = Button(window, text="~ Gemi Ekle ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=gemiler)
buton3.place(x=100,y=175)

buton4 = Button(window, text="~ Liman Ekle ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=liman)
buton4.place(x=100, y=250)

buton5 = Button(window, text="~ Sefer Ekle ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=sefer_ekle)
buton5.place(x=100, y=325)

    ##########################
   # TABLO GÖSTERME VE SİLME #
  ###########################
buton6 = Button(window, text="~ Kaptan Tablo ~", bg="#a6172d", fg="#FFFFFF", font=("Arial", 12, "bold italic"), width=25, height=2,command=kaptan_tablo)
buton6.place(x=450, y=25)

buton7 = Button(window, text="~ Mürettabat Tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=murattabat_tablo)
buton7.place(x=450, y=100)

buton8 = Button(window, text="~ Gemi Tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=gemiler_tablo_goster)
buton8.place(x=450,y=175)

buton9 = Button(window, text="~ Liman Tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=limanlar_tablo)
buton9.place(x=450, y=250)

buton10 = Button(window, text="~ Sefer Tablo ~", bg="#a6172d", fg="white", font=("Arial", 12, "bold italic"), width=25, height=2,command=seferler_tablo)
buton10.place(x=450, y=325)





window.mainloop()
