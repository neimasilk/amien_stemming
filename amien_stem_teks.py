#!/usr/bin/python

from nltk.tokenize import word_tokenize
from amien_stemmer import encode
from Sastrawi.Stemmer.Filter import TextNormalizer

import sys,getopt

inputfile = ''
outputfile = ''
str(sys.argv)

if len(sys.argv)==3:
    inputfile=sys.argv[1]
    outputfile=sys.argv[2]
else:
    print('parameter salah: contoh amien_stem_teks.py file_input.txt file_output.txt')
    exit(1)



# print(encode('ini adalah percobaan, semoga berhasil, terima kasih'))

with open(inputfile) as f:
    lines = f.readlines()
    f.close()

daftar = []
for line in lines:
    daftar.append(line.strip())

token = []
isi_file_output =[]
for kalimat in daftar:
    for kata in word_tokenize(kalimat):
        token.append(encode(kata) if len(kata)!=1 else kata)
    isi_file_output.append(' '.join(token))
    token =[]

with open(outputfile,'w') as f:
    for isi in isi_file_output:
        f.write("%s\n" % isi)
f.close()

    # for kata in word_tokenize(kalimat):
    #     if len(kata)!=1:
    #         print(encode(kata))
# count = 0
# for word in read_words(inputfile):
#     # print(word)
#     normalizedText = word.lower()
#     if normalizedText!=encode(word):
#         print(normalizedText+ ' = '+ encode(word))
#         count+=1
#         if count == 300:
#             break