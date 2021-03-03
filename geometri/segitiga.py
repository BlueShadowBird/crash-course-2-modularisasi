def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

def generate_prettyprint_luas_segitiga(alas, tinggi):
    return f'luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {hitung_luas_segitiga(alas, tinggi)}'

def tampilkan_luas_segitiga(alas, tinggi):
    print(generate_prettyprint_luas_segitiga(alas, tinggi))