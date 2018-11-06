from unittest import TestCase
from amien_stemmer import encode


class TestEncode(TestCase):
    def test_encode_kalimat(self):
        text1='Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan, kami sangat membangga-banggakannya.'
        text_hasil1 = 'per~ ekonomi ~an indonesia sedang dalam per~ tumbuh ~an yang mem~ bangga ~kan, kami sangat mem~ ulg~ bangga ~kannya.'
        self.assertEqual(text_hasil1,encode(text1))

    def test_encode_kata_plural(self):
        text1='kupu-kupu'
        text1_hsl = 'kupu-kupu'
        text2='jalan-jalan'
        text2_hsl = 'ulg~ jalan'
        text3='makan-makan'
        text3_hsl='ulg~ makan'
        text4='memakan'
        text4_hsl='me~ makan'
        text5='memakani'
        text5_hsl='mem~ pakan'
        text6='memakankan'
        text6_hsl='me~ makan ~kan'
        text7='makanan'
        text7_hsl='makan ~an'
        text8='dimakan'
        text8_hsl='di~ makan'
        text9='pemakan'
        text9_hsl='pe~ makan'
        text10='termakan'
        text10_hsl= 'ter~ makan'
        text11='sepemakan'
        text11_hsl='sepe~ makan'
        text12 = 'membebani'
        text12_hsl = 'mem~ beban ~i'

        # Inflection Suffixes (“-lah”, “-kah”, “-ku”, “-mu”, atau “-nya”) dibuang.
        # Jika berupa particles (“-lah”, “-kah”, “-tah” atau “-pun”)
        # maka langkah ini diulangi lagi untuk menghapus Possesive Pronouns (“-ku”, “-mu”, atau “-nya”), jika ada.

        text_lah = 'janganlah'
        text_lah_hsl = 'jangan ~lah'




        self.assertEqual(text1_hsl,encode(text1))
        self.assertEqual(text2_hsl,encode(text2))
        self.assertEqual(text3_hsl,encode(text3))
        self.assertEqual(text4_hsl,encode(text4))
        self.assertEqual(text5_hsl,encode(text5))
        self.assertEqual(text6_hsl,encode(text6))
        self.assertEqual(text7_hsl,encode(text7))
        self.assertEqual(text8_hsl,encode(text8))
        self.assertEqual(text9_hsl,encode(text9))
        self.assertEqual(text10_hsl,encode(text10))
        self.assertEqual(text11_hsl,encode(text11))
        self.assertEqual(text12_hsl,encode(text12))
        self.assertEqual(text_lah_hsl,encode(text_lah))
