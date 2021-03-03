# SEGITIGA
import geometri.segitiga as st
from datetime import datetime

now = datetime.now()

current_time = now.strftime('%H:%M:%S')
print(f'Current Time = {current_time}\n')

alas = 4
tinggi = 6
luas = alas * tinggi / 2
print(f'luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}')

print("-"*15)

print(st.hitung_luas_segitiga(4, 6))
print(st.generate_prettyprint_luas_segitiga(4, 6))
st.tampilkan_luas_segitiga(4, 6)
