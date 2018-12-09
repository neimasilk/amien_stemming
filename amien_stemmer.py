
import sys
sys.path.insert(0, './pysastrawi/src')
from pysastrawi.src.Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Stemmer.Filter import TextNormalizer
import re
from string_alignment import encode_word


factory = StemmerFactory()
stemku = factory.create_stemmer()




def encode(text):
    normalizedText =  TextNormalizer.normalize_text(text)

    words = normalizedText.split(' ')
    stems = []

    for word in words:
        hasil_stem = encode_word(word)
        stems.append(hasil_stem)
    return ' '.join(stems)





if __name__ == '__main__':

    # stemming process
    # sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan, kami sangat membangga-banggakannya.'
    sentence1 ='Benarkah semua korban gempa Aceh sudah terjamin kebutuhan pokoknya?'
    sentence2 ='Jokowi mengatakan bahwa konsep Indo-Pasifik ini akan memberikan arah baru bagi kerjasama ASEAN dengan negara-negara mitranya sekaligus membuat sentralitas ASEAN di kawasan tetap terjaga. Artikel ini telah tayang di Kompas dengan judul "Jokowi Ungkap Pentingnya Indo-Pasific bagi ASEAN"'
    sentence3 = '''Apalagi, kondisi itu diprediksi akan diperparah dengan tarik menarik konstelasi kekuatan dunia. Oleh sebab itu, Presiden Jokowi meminta ASEAN yang berada di tengah-tengah kawasan Indo- Pasific mampu menjadi poros maritim.

Artikel ini telah tayang di Kompas.com dengan judul "Jokowi Ungkap Pentingnya Indo-Pasific bagi ASEAN", https://nasional.kompas.com/read/2018/11/14/09281661/jokowi-ungkap-pentingnya-indo-pasific-bagi-asean. 
Penulis : Fabian Januarius Kuwado
Editor : Krisiandi'''
    print(sentence1)
    print(encode(sentence1))

    word = 'temaniku'
    word = 'makananku'
    word = 'putuskanlah'
    word = 'pertanggung-jawaban'
    # word= ''
    print(encode_word(word))
    # print(TextNormalizer.normalize_text(sentence))



    #
    # print(output)
    # # ekonomi indonesia sedang dalam tumbuh yang bangga
    #
    # print(stem_amien('Mereka meniru-nirukannya'))
    # # mereka tiru
    #



    # asli: perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan.
    # peran~ ekonomi indonesia sedang dalam peran~ tumbuh yang memkan~ bangga.

     # asli: mereka meniru-nirukannya.
     # mereka mekan~ nya~ dobel~ tiru


