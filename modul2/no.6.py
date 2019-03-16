from datetime import date

class Manusia(object):

    """Class 'Manusia' dengan inisiasi 'nama'"""

    keadaan = 'sakit'

    

    def __ini__(self, nama):

        self.nama = nama

    def ucapkanSalam(self):

        print('Assalamualaikum, namaku',self.nama)

    def makan(self, s):

        print('Saya baru makan obat', s)

        self.keadaan = 'sehat'

    def olahraga(self, k):

        print('Saya mau melakukan olahraga', k)

        self.keadaan = 'sakit'

    def mengalikanDenganDua(self, n):

        return n*2


class SiswaSMA(Manusia):

    def __init__(self, Nama, Absen, Kelas, umur, Tempat tinggal):

        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""

        self.nama = Nama

        self.absen = Absen


        self.kelas = Kelas

        self.umur = Umur

        self.alamat = Tempat tinggal
        
        

    def __str__(self):

        s = self.nama +', Absen '+str(self.absen)\

            +'. Kelas'+ str(self.kelas) \

 +'. Umur'+ str(self.umur)\

            +'. Tempat tinggal'+ str(self.alamat).'

        return s


    def tahunlahir(self):

        thnskr = date.today().year

        years = thnskr - self.umur

        return years
