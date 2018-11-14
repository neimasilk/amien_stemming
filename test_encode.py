from unittest import TestCase
from amien_stemmer import encode


class TestEncode(TestCase):
    def test_encode_kalimat(self):
        text1='Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan, kami sangat membangga-banggakannya.'
        text_hasil1 = 'pe~ ekonomi ~an indonesia sedang dalam pe~ tumbuh ~an yang me~ bangga ~kan, kami sangat me~ ulg~ bangga ~kan ~nya.'
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
        text5_hsl='me~ pakan ~i'
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
        text11_hsl='se~ pe~ makan'
        text12 = 'membebani'
        text12_hsl = 'me~ beban ~i'

        word1 = 'biji-bijian'
        word1_hsl = 'ulg~ biji ~an'
        word2 = 'kupu-kupu'
        word2_hsl = 'kupu-kupu'
        word3 = 'jalan-jalan.'
        word3_hsl = 'ulg~ jalan.'
        word = 'menyejahterakan'
        word_hsl = 'me~ sejahtera ~kan'
        word_plural1 = 'meniru-nirukan'
        word_plural1_hsl = 'me~ ulg~ tiru ~kan'
        word_plural2 = 'berbalas-balasan'
        word_plural2_hsl = 'ber~ ulg~ balas ~an'
        # Inflection Suffixes (“-lah”, “-kah”, “-ku”, “-mu”, atau “-nya”) dibuang.
        # Jika berupa particles (“-lah”, “-kah”, “-tah” atau “-pun”)
        # maka langkah ini diulangi lagi untuk menghapus Possesive Pronouns (“-ku”, “-mu”, atau “-nya”), jika ada.

        text_lah = 'janganlah'
        text_lah_hsl = 'jangan ~lah'

        # TESTING PERTAMA
        wword1 = 'biji-bijian'
        wword1_hsl = 'ulg~ biji ~an'
        wword2 = 'kupu-kupu'
        wword2_hsl = 'kupu-kupu'
        wword3 = 'jalan-jalan.'
        wword3_hsl = 'ulg~ jalan.'
        wword4 = 'pemberitahuan'
        wword4_hsl = 'pe~ beritahu ~an'
        wword5 = 'pemilu'
        wword5_hsl = 'pemilu'
        wword6 = 'sebagai'
        wword6_hsl = 'se~ bagai'
        wword7 = 'bagian'
        wword7_hsl = 'bagi ~an'
        wword8 = 'mengecek'
        wword8_hsl = 'me~ cek'
        wword9 = 'mengakomodir'
        wword9_hsl = 'me~ akomodir'

        # print(stemku.stem(word))
        # print(stem_plural_word(word_plural1))

        # # TESTING KEDUA FOKUS DI BER
        # word = 'berkenaan'  # ok
        # word = 'berangan-angan'  # not ok
        # word = 'beraktifitas'  # not ok
        # word = 'beristri'  # ok
        # word = 'berenang'  # ok
        # word = 'belajar'
        # # word = 'bekerja' #ok
        #
        # # TESTING KETIGA FOKUS DI TER
        # word = 'ketersediaan'  # ok
        # word = 'terbaik'  # ok
        # word = 'tercecer-cecer'  # ok

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

        self.assertEqual(word1_hsl,encode(word1))
        self.assertEqual(word2_hsl,encode(word2))
        self.assertEqual(word3_hsl,encode(word3))
        self.assertEqual(word_hsl,encode(word))
        self.assertEqual(word_plural1_hsl,encode(word_plural1))
        self.assertEqual(word_plural2_hsl,encode(word_plural2))


        self.assertEqual(wword1_hsl,encode(wword1))
        self.assertEqual(wword2_hsl,encode(wword2))
        self.assertEqual(wword3_hsl,encode(wword3))
        self.assertEqual(wword4_hsl,encode(wword4))
        self.assertEqual(wword5_hsl,encode(wword5))
        self.assertEqual(wword6_hsl,encode(wword6))
        self.assertEqual(wword7_hsl,encode(wword7))
        self.assertEqual(wword8_hsl,encode(wword8))
        self.assertEqual(wword9_hsl,encode(wword9))
