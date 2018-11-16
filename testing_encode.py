from amien_stemmer import encode
from Sastrawi.Stemmer.Filter import TextNormalizer

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

count = 0
for word in read_words('wikipedia_id.txt'):
    # print(word)
    normalizedText = TextNormalizer.normalize_text(word)
    if normalizedText!=encode(word):
        print(normalizedText+ ' = '+ encode(word))
        count+=1
        if count == 300:
            break