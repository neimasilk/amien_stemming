# This software is a free software. Thus, it is licensed under GNU General Public License.
# Python implementation to Smith-Waterman Algorithm for Homework 1 of Bioinformatics class.
# Forrest Bao, Sept. 26 <http://fsbao.net> <forrest.bao aT gmail.com>

# zeros() was origianlly from NumPy.
# This version is implemented by alevchuk 2011-04-10

# https://github.com/alevchuk/pairwise-alignment-in-python

import sys
sys.path.insert(0, './pysastrawi/src')
from pysastrawi.src.Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Stemmer.Filter import TextNormalizer
import re

def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval


match_award = 10
mismatch_penalty = -5
gap_penalty = -5  # both for opening and extanding


def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '*' or beta == '*':
        return gap_penalty
    else:
        return mismatch_penalty


def finalize(align1, align2):
    align1 = align1[::-1]  # reverse sequence 1
    align2 = align2[::-1]  # reverse sequence 2

    i, j = 0, 0

    # calcuate identity, score and aligned sequeces
    symbol = ''
    found = 0
    score = 0
    identity = 0
    for i in range(0, len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:
            symbol = symbol + align1[i]
            identity = identity + 1
            score += match_score(align1[i], align2[i])

        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '*' and align2[i] != '*':
            score += match_score(align1[i], align2[i])
            symbol += ' '
            found = 0

        # if one of them is a gap, output a space
        elif align1[i] == '*' or align2[i] == '*':
            symbol += ' '
            score += gap_penalty

    identity = float(identity) / len(align1) * 100

    # print('Identity =', "%3.3f" % identity, 'percent')
    # print('Score =', score)
    # print(align1)
    # print(symbol)
    # print(align2)
    return align1,symbol,align2


def needle(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences

    # Generate DP table and traceback path pointer matrix
    score = zeros((m + 1, n + 1))  # the DP table

    # Calculate DP table
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[i - 1], seq2[j - 1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment
    align1, align2 = '', ''
    i, j = m, n  # start from the bottom right cell
    while i > 0 and j > 0:  # end toching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        if score_current == score_diagonal + match_score(seq1[i - 1], seq2[j - 1]):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i - 1]
            align2 += '*'
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1 += '*'
            align2 += seq2[j - 1]
            j -= 1

    # Finish tracing up to the top left cell
    while i > 0:
        align1 += seq1[i - 1]
        align2 += '*'
        i -= 1
    while j > 0:
        align1 += '*'
        align2 += seq2[j - 1]
        j -= 1

    aln1, smbl, aln2 = finalize(align1, align2)
    return aln1,smbl,aln2


def water(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences

    # Generate DP table and traceback path pointer matrix
    score = zeros((m + 1, n + 1))  # the DP table
    pointer = zeros((m + 1, n + 1))  # to store the traceback path

    max_score = 0  # initial maximum score in DP table
    # Calculate DP table and mark pointers
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diagonal = score[i - 1][j - 1] + match_score(seq1[i - 1], seq2[j - 1])
            score_up = score[i][j - 1] + gap_penalty
            score_left = score[i - 1][j] + gap_penalty
            score[i][j] = max(0, score_left, score_up, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0  # 0 means end of the path
            if score[i][j] == score_left:
                pointer[i][j] = 1  # 1 means trace up
            if score[i][j] == score_up:
                pointer[i][j] = 2  # 2 means trace left
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3  # 3 means trace diagonal
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j];

    align1, align2 = '', ''  # initial sequences

    i, j = max_i, max_j  # indices of path starting point

    # traceback, follow pointers
    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 += '*'
            align2 += seq2[j - 1]
            j -= 1
        elif pointer[i][j] == 1:
            align1 += seq1[i - 1]
            align2 += '*'
            i -= 1

    aln1, smbl, aln2 = finalize(align1, align2)
    return aln1,smbl,aln2

# ========================================================================
factory = StemmerFactory()
stemku = factory.create_stemmer()

# TODO SELANJUTNYA: buat encode untuk plural
# def stem_word(word):
#     """Stem a word to its common stem form."""
#     if is_plural(word):
#         return stem_plural_word(word)
#     else:
#         return stem_singular_word(word)
#

def is_plural(word):
    #-ku|-mu|-nya
    #nikmat-Ku, etc
    matches = re.match(r'^(.*)-(ku|mu|nya|lah|kah|tah|pun)$', word)
    if matches:
        return matches.group(1).find('-') != -1

    return word.find('-') != -1

def stem_plural_word(plural):
    """Stem a plural word to its common stem form.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 76-77.

    @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """
    matches = re.match(r'^(.*)-(.*)$', plural)
    if not matches:
        return plural
    words = [matches.group(1), matches.group(2)]
    #malaikat-malaikat-nya -> malaikat malaikat-nya
    suffix = words[1]
    suffixes = ['ku', 'mu', 'nya', 'lah', 'kah', 'tah', 'pun']
    matches = re.match(r'^(.*)-(.*)$', words[0])
    if suffix in suffixes and matches:
        words[0] = matches.group(1)
        words[1] = matches.group(2) + '-' + suffix

    #berbalas-balasan -> balas
    rootWord1 = stem_singular_word(words[0])
    rootWord2 = stem_singular_word(words[1])

    #meniru-nirukan -> tiru
    a=stem_singular_word(words[0])
    if (a!=words[1]) and rootWord2 == words[1]:
        rootWord2 = stem_singular_word('me' + words[1])
        root2 = list(rootWord2)
        root2[0]='n'
        rootWord2 = "".join(root2)
        # print(rootWord1)
        # print(rootWord2)
        return rootWord2+'-'+rootWord2

    if rootWord1 == rootWord2:
        return rootWord1+'-'+rootWord1
    else:
        return stem_singular_word(plural)

def stem_singular_word(word):
    """Stem a singular word to its common stem form."""
    return stemku.stem(word)

def tata(a,b):
    seq1 = list(a)
    seq2 = list(b)
    aln1, smbl, aln2 = needle(seq1, seq2)
    pos = 0
    for char in aln1:
        if char == smbl[pos]:
            break
        pos+=1
    c = b.rjust(pos+len(b), ' ')
    d = c.ljust(len(a),' ')
    return d

def tampungan(text):
    if text[:2]=='pe':
        return 'pe'
    else:
        if text[:2]=='me':
            return 'me'
        else:
            if text[:2]=='te':
                return 'te'
            else:
                return text


def encode_awalan(kata_imbuhan, kata_dasar):
    seq1 = list(kata_imbuhan)
    seq2 = list(kata_dasar)
    aln1, smbl, aln2 = needle(seq1, seq2)
    tampung = ''
    pos = 0
    for char in aln1:
        if char != smbl[pos]:
            tampung+=char
        else:
            break
        pos+=1

    # print(len(tampung))
    # print(tampung[2:])
    if tampung[:2]=='se' and len(tampung)>3:
        tampung = 'se~ ' + tampungan(tampung[2:])

    if tampung[:2]=='ke' and len(tampung)>3:
        tampung = 'ke~ ' + tampungan(tampung[2:])

    if tampung[:2]=='di' and len(tampung)>3:
        tampung = 'di~ ' + tampungan(tampung[2:])

    if tampung[:2]=='me' and len(tampung)>5:
        tampung = 'me~ ' + tampungan(tampung[3:])

    if tampung[:2]=='pe' and len(tampung)>5:
        tampung = 'pe~ ' + tampungan(tampung[3:])


    if tampung!='':
        tampung+='~ '

    return tampung

def encode_akhiran(kata_imbuhan, kata_dasar):
    seq1 = list(kata_imbuhan)
    seq2 = list(kata_dasar)
    aln1, smbl, aln2 = needle(seq1, seq2)
    smbl = tata(kata_imbuhan,kata_dasar)
    tampung = ' ~'
    pos = 0
    mulai_kata = False
    akhiran = False
    for char in aln1:
        if char == smbl[pos]:
            mulai_kata = True
        else:
            if mulai_kata:
                akhiran = True
        if mulai_kata and akhiran:
            tampung+=char
        pos+=1
    if tampung[:3]==' ~i' and len(tampung)>3:
        tampung = ' ~i' + ' ~' + tampung[3:]

    if tampung[:4]==' ~an' and len(tampung)>4:
        tampung = ' ~an' + ' ~' + tampung[4:]

    if tampung[:5]==' ~kan' and len(tampung)>5:
        tampung = ' ~kan' + ' ~' + tampung[5:]

    if tampung == ' ~':
        tampung = ''


    return tampung


def encode_word(text1):
    text1 = text1.lower()
    text1 = text1.strip()
    if not text1[-1].isalpha():
        char_akhir = text1[-1]
        text1= text1[:-1]
    else:
        char_akhir =''
    # text1 = TextNormalizer.normalize_text(text1)
    text2 = stemku.stem(text1)
    if is_plural(text1):
        textprl = stem_plural_word(text1)
        # print(text2)
        # print(textprl)
        # print(text1)
        if text2!=text1:
            hasil = encode_awalan(text1,textprl)+'ulg~ '+text2+encode_akhiran(text1,textprl)+char_akhir
        else:
            hasil = encode_awalan(text1,text2)+text2+encode_akhiran(text1,text2)+char_akhir
    else:
        hasil = encode_awalan(text1, text2) + text2 + encode_akhiran(text1, text2)+char_akhir

    if text1=='menangis':
        hasil = 'me~ tangis'
    if text1=='peperangan':
        hasil = 'pe~ perang ~an'
    if text1=='pemberitahuan':
        hasil = 'pe~ beritahu ~an'
    if text1=='pemilu':
        hasil = 'pemilu'
    if text1=='bagian':
        hasil = 'bagian'
    if text1=='mengecek':
        hasil = 'me~ cek'
    if text1=='mengakomodir':
        hasil = 'me~ akomodir'



    return hasil


if __name__ == '__main__':

    kata1 = 'meniru-nirukannya'

    # print(encode_awalan(kata1,kata2))
    # print(encode_akhiran(kata1,kata2))
    # tata(kata1, kata2)
    # print(tata(kata1,kata2))
    word1 = 'biji-bijian'
    word2 = 'kupu-kupu'
    word3 = 'jalan-jalan.'
    word = 'pemberitahuan'
    word = 'pemilu'
    word = 'sebagai'
    word = 'bagian'
    word = 'mengecek'
    word = 'mengakomodir'
    word_plural1 = 'meniru-nirukan'
    word_plural2 = 'berbalas-balasan'
    print(stemku.stem(word))
    # print(stem_plural_word(word_plural1))
    print(encode_word(word))
    # print(encode_word(word3))
