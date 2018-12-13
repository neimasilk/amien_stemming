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

def cari_awalan(awal,jumlah):
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

def cari_awalan_dan_hrf_awal(awal,hrf_awal,jumlah):
    count = 0
    for word in read_words('wikipedia_id.txt'):
        # print(word)
        normalizedText = TextNormalizer.normalize_text(word)
        kata = encode(word)
        if normalizedText!=kata:
            awalan = kata.split()[0]
            hrf_awalan = kata.split()[1][:len(hrf_awal)]
            if awalan[-1:]=='~':
                if (awalan[:2]==awal and hrf_awalan==hrf_awal):
                    # print(awalan)
                    print(normalizedText+ ' = '+ kata)
                    count+=1
                    if count == jumlah:
                        break

if __name__ == '__main__':
    if len(sys.argv)==3:
        cari_awalan(sys.argv[1],int(sys.argv[2]))
    elif (len(sys.argv) == 4):
        cari_awalan_dan_hrf_awal(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    elif (len(sys.argv) == 2):
        cari_semua(int(sys.argv[2]))
    else:
        cari_semua(20)
