
import sys
sys.path.insert(0, './pysastrawi/src')
from pysastrawi.src.Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Stemmer.Filter import TextNormalizer
import re
from string_alignment import encode_word


factory = StemmerFactory()
stemku = factory.create_stemmer()




def encode(text):
    normalizedText = text.lower() # TextNormalizer.normalize_text(text)

    words = normalizedText.split(' ')
    stems = []

    for word in words:
        hasil_stem = stemku.stem(word)
        if hasil_stem!=word:
            hasil_stem=(encode_word(word))
        stems.append(hasil_stem)
    return ' '.join(stems)


if __name__ == '__main__':

    # stemming process
    sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan, kami sangat membangga-banggakannya.'

    print(sentence)
    # print(encode(sentence))

    word = 'temaniku'
    word = 'makananku'
    word = 'putuskanlah'
    word = 'seperjuangan'
    word= 'menyupir'
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


