class Mashina:

    def __init__(self, modeli, rusumi):
        self.modeli = modeli
        self.rusumi = rusumi

    def Malumot(self, tezligi, ot_kuchi, narxi,
                rangi, ishlab_chiqarilgan_yili):

        print("""Modeli:{}\nRusumi:{}\nTezligi:{}
                \nOt-kuchi:{}\nNarxi:{}
                \nIshlab chiqarilgan yili:{}
                """.format(self.modeli,
                           self.rusumi, tezligi, ot_kuchi, rangi,   ishlab_chiqarilgan_yili))


class Narx_boyicha_saralash(Mashina):

