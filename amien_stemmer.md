buat encode(kata):
encode adalah memecah kata yang memiliki imbuhan menjadi kata dasar dan imbuhannya untuk dipisah.
contoh:
encode('bermain') :
mengembalikan nilai : 'ber~ main'

encode('melemparkan'):
mengembalikan nilai : 'me~ lempar ~kan'

decode('me~ lempar ~kan'):
mengembalikan nilai : 'melemparkan'
decode('ber~ main'):
mengembalikan nilai : 'bermain'

