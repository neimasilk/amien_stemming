from amien_stemmer import encode
from Sastrawi.Stemmer.Filter import TextNormalizer
import sys

# print(encode('ini adalah percobaan, semoga berhasil, terima kasih'))

def read_words(filename):
    last = ""
    with open(filename) as inp:
        while True:
            buf = inp.read(10240)
            if not buf:
                break
            words = (last+buf).split()
            last = words.pop()
            for word in words:
                yield word
        yield last

def cari(awal,jumlah):
    count = 0
    for word in read_words('wikipedia_id.txt'):
        # print(word)
        normalizedText = TextNormalizer.normalize_text(word)
        kata = encode(word)
        if normalizedText!=kata:
            awalan = kata.split()[0]
            if awalan[-1:]=='~':
                if (awalan[:2]==awal):
                    # print(awalan)
                    print(normalizedText+ ' = '+ kata)
                    count+=1
                    if count == jumlah:
                        break

def cari_semua(jumlah):
    count = 0
    for word in read_words('wikipedia_id.txt'):
        # print(word)
        normalizedText = TextNormalizer.normalize_text(word)
        kata = encode(word)
        if normalizedText!=kata:
            print(normalizedText + ' = ' + kata)
            count += 1
            if count == jumlah:
                break


if __name__ == '__main__':
    if len(sys.argv)==3:
        cari(sys.argv[1],int(sys.argv[2]))
    else:
        cari_semua(10)
